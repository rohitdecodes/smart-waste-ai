import gradio as gr
from classifier import analyze_image

def analyze(image):
    if image is None:
        return "Please upload an image."

    image.save("temp.jpg")
    result = analyze_image("temp.jpg")

    return f"""
🧠 **Detected Object:** {result['detected_object']}  
📊 **Object Confidence:** {result['object_confidence']}

♻️ **Waste Category:** {result['waste_category']}  
📊 **Waste Confidence:** {result['waste_confidence']}

📝 **Reason:**  
{result['reason']}

🚮 **Disposal Method:**  
{result['disposal']}

🌍 **Environmental Impact:**  
{result['environmental_impact']}
"""

with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("""
    # ♻️ Smart Waste AI  
    **Hybrid AI-powered Waste Segregation Advisor**  
    ResNet + CLIP (Zero-shot Vision Reasoning)
    """)

    image = gr.Image(type="pil", label="Upload Waste Image")
    button = gr.Button("Analyze Waste", variant="primary")
    output = gr.Markdown()

    button.click(analyze, image, output)

    gr.Markdown("""
    ---
    🔗 **GitHub:** https://github.com/OGrohit/smart-waste-ai  
    """)
    
demo.launch()
