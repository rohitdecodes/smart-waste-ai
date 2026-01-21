# ♻️ Smart Waste Segregation AI

A **hybrid AI-powered web application** that classifies waste items from images and provides guidance for responsible disposal, aligned with **UN Sustainable Development Goal 12 (Responsible Consumption and Production)**.

This project demonstrates how **computer vision + zero-shot AI reasoning** can be combined to solve real-world sustainability problems.

---

## 🌐 Live Demo (Public URL)

👉 **Hugging Face Space (Live Website):**  
https://huggingface.co/spaces/YOUR_USERNAME/smart-waste-ai

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


