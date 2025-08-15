# 🖼️ Multi-Modal AI App (Image ↔ Text)

A Streamlit web app that allows you to:
- **Image → Text**: Describe any image using Google's Gemini API  
- **Text → Image**: Generate images from text prompts using Stable Diffusion or DALL·E  

---

## 🚀 Features
- Upload an image and get a detailed description (Gemini API)
- Enter a text prompt to generate high-quality AI images (Stable Diffusion / DALL·E)
- Easy API key input directly in the app (No `.secrets.toml` editing required)
- Modern, clean Streamlit interface

---

## 📦 Installation

1. **Clone this repository**
```bash
git clone https://github.com/your-username/multimodal-ai-app.git
cd multimodal-ai-app

2. **Install dependencies**
pip install -r requirements.txt
```

## 🔑 API Keys Required

**This project requires the following API keys:**

# Gemini API Key:

Get it from: https://makersuite.google.com/app/apikey

# OpenAI API Key (for DALL·E):

Get it from: https://platform.openai.com/api-keys

# Stability AI API Key (for Stable Diffusion):

Get it from: https://platform.stability.ai/account/api-keys

You do not need to store keys in files. When you run the app, there will be input boxes in the sidebar where you can paste your keys.

## ▶️ Usage:
**Run the Streamlit app:**
cd (Folder location)
streamlit run app.py
