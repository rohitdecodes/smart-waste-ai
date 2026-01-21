# ♻️ Smart Waste Segregation AI

A **hybrid AI-powered web application** that classifies waste items from images and provides guidance for responsible disposal, aligned with **UN Sustainable Development Goal 12 (Responsible Consumption and Production)**.

This project demonstrates how **computer vision + zero-shot AI reasoning** can be combined to solve real-world sustainability problems.

---

## 🌐 Live Demo (Public URL)

👉 **Hugging Face Space (Live Website):**  
https://huggingface.co/spaces/OGrohit/smart-waste-ai

### How to view and use the demo
1. Open the link above  
2. Upload an image of a waste item (for example: bottle, phone, food waste, screen)  
3. Click **Analyze Waste**  
4. View the detected object, waste category, and disposal guidance  

No installation is required to use the demo.

---

## 🧠 Project Overview

The system uses a **Hybrid AI Architecture** that combines visual recognition and semantic reasoning:

- **ResNet50 (CNN)**  
  Used for detecting the object present in the image.

- **CLIP (Vision–Language Model)**  
  Used for **zero-shot waste classification**, allowing the system to classify waste without a manually labeled waste dataset.

- **Explanation Engine**  
  Provides the reason for classification, correct disposal method, and environmental impact.

This hybrid approach allows the system to work even for **previously unseen objects**.

---

## 🧩 System Architecture
<img width="1082" height="560" alt="image" src="https://github.com/user-attachments/assets/5f9616a7-ff6d-4e53-9271-013f2885dbed" />

---

## ♻️ Supported Waste Categories

- **Wet Waste**  
  Organic and biodegradable waste

- **Dry Waste**  
  Recyclable materials such as plastic and paper

- **E-Waste**  
  Electronic and electrical items

- **Hazardous Waste**  
  Harmful or chemical substances

---

## 🖥️ Tech Stack

- Python  
- PyTorch  
- TorchVision  
- Hugging Face Transformers (CLIP)  
- Gradio (Web Interface)  
- Hugging Face Spaces (Deployment)

---

## ▶️ Run Locally (Optional)

If you want to run the project locally on your system:

pip install -r requirements.txt
python app.py

Then open the following URL in your browser: http://127.0.0.1:7860

---

## ⚠️ Limitations

- Uses CPU inference on Hugging Face Spaces, which may be slower than GPU
- Zero-shot classification can be less accurate for ambiguous images
- The model is not fine-tuned on a dedicated waste-specific dataset

These limitations are acknowledged as part of responsible and transparent AI development.

---

## 🔮 Future Improvements

- Fine-tuning CLIP on a waste-specific dataset  
- Adding confidence-based warnings for uncertain predictions  
- Improving mobile responsiveness of the UI  
- Expanding waste categories such as medical waste, glass, and metal  

---

## 👤 Author

**Rohit Patil**  
Information Technology Engineering Student  

---

## 📜 License

This project is licensed under the **MIT License** and is intended for educational and demonstration purposes.





