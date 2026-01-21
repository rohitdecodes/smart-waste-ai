import torch
import numpy as np
from torchvision import models, transforms
from PIL import Image
from transformers import CLIPProcessor, CLIPModel

from waste_logic import get_explanation

# -------------------------
# Device
# -------------------------
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# -------------------------
# Load ResNet50 (object detection)
# -------------------------
resnet = models.resnet50(weights=None)
resnet.load_state_dict(torch.load("resnet50.pth", map_location=device))
resnet.to(device)
resnet.eval()

# ImageNet labels
with open("imagenet_classes.txt") as f:
    imagenet_labels = [line.strip() for line in f.readlines()]

# -------------------------
# Load CLIP (waste classification)
# -------------------------
clip_model = CLIPModel.from_pretrained(
    "openai/clip-vit-base-patch32"
).to(device)
clip_processor = CLIPProcessor.from_pretrained(
    "openai/clip-vit-base-patch32"
)

WASTE_LABELS = [
    "wet waste",
    "dry waste",
    "electronic waste",
    "hazardous waste"
]

# -------------------------
# Image preprocessing
# -------------------------
preprocess = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(
        mean=[0.485, 0.456, 0.406],
        std=[0.229, 0.224, 0.225]
    )
])

# -------------------------
# ResNet object detection
# -------------------------
def detect_object(image):
    tensor = preprocess(image).unsqueeze(0).to(device)

    with torch.no_grad():
        outputs = resnet(tensor)
        probs = torch.softmax(outputs, dim=1)

    confidence, idx = torch.max(probs, 1)
    label = imagenet_labels[idx.item()]

    return label, round(confidence.item(), 3)

# -------------------------
# CLIP waste classification
# -------------------------
def classify_waste_clip(image):
    inputs = clip_processor(
        text=WASTE_LABELS,
        images=image,
        return_tensors="pt",
        padding=True
    ).to(device)

    with torch.no_grad():
        outputs = clip_model(**inputs)
        logits = outputs.logits_per_image
        probs = logits.softmax(dim=1).cpu().numpy()[0]

    idx = np.argmax(probs)
    confidence = probs[idx]

    label_map = {
        "wet waste": "Wet Waste",
        "dry waste": "Dry Waste",
        "electronic waste": "E-Waste",
        "hazardous waste": "Hazardous Waste"
    }

    return label_map[WASTE_LABELS[idx]], round(float(confidence), 3)

# -------------------------
# Final hybrid analysis
# -------------------------
def analyze_image(image_path):
    image = Image.open(image_path).convert("RGB")

    object_label, object_conf = detect_object(image)
    waste_category, waste_conf = classify_waste_clip(image)

    explanation = get_explanation(waste_category)

    return {
        "detected_object": object_label,
        "object_confidence": object_conf,
        "waste_category": waste_category,
        "waste_confidence": waste_conf,
        "reason": explanation["reason"],
        "disposal": explanation["disposal"],
        "environmental_impact": explanation["impact"]
    }
