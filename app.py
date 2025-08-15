import streamlit as st
import google.generativeai as genai
import openai
import io
from PIL import Image
import requests
from stability_sdk import client
import stability_sdk.interfaces.gooseai.generation.generation_pb2 as generation

# -------------------- UI HEADER --------------------
st.set_page_config(page_title="MultiModal AI Tool", page_icon="🤖", layout="centered")
st.title("🖼️ MultiModal AI Tool")
st.write("Convert Images to Text (Gemini) & Text to Images (DALL·E / Stability AI)")

# -------------------- API KEY INPUTS --------------------
st.sidebar.header("🔑 API Keys")
gemini_api_key = st.sidebar.text_input("Gemini API Key", type="password")
openai_api_key = st.sidebar.text_input("OpenAI API Key (for DALL·E)", type="password")
stability_api_key = st.sidebar.text_input("Stability AI API Key", type="password")

# -------------------- MODE SELECTION --------------------
mode = st.radio("Select Mode", ["Image to Text (Gemini)", "Text to Image (DALL·E)", "Text to Image (Stability AI)"])

# -------------------- GEMINI: IMAGE TO TEXT --------------------
if mode == "Image to Text (Gemini)":
    uploaded_image = st.file_uploader("Upload an Image", type=["jpg", "jpeg", "png"])
    if uploaded_image and gemini_api_key:
        image = Image.open(uploaded_image)
        st.image(image, caption="Uploaded Image", use_column_width=True)

        genai.configure(api_key=gemini_api_key)
        model = genai.GenerativeModel("gemini-1.5-flash")

        if st.button("Generate Description"):
            with st.spinner("Generating description..."):
                response = model.generate_content([image, "Describe this image in detail."])
                st.subheader("Image Description:")
                st.write(response.text)

# -------------------- DALL-E: TEXT TO IMAGE --------------------
elif mode == "Text to Image (DALL·E)":
    prompt = st.text_area("Enter your prompt")
    if prompt and openai_api_key:
        openai.api_key = openai_api_key
        if st.button("Generate Image (DALL·E)"):
            with st.spinner("Generating image..."):
                try:
                    result = openai.images.generate(
                        model="gpt-image-1",
                        prompt=prompt,
                        size="1024x1024"
                    )
                    image_url = result.data[0].url
                    st.image(image_url, caption="Generated Image (DALL·E)", use_column_width=True)
                except Exception as e:
                    st.error(f"Error: {e}")

# -------------------- STABILITY AI: TEXT TO IMAGE --------------------
elif mode == "Text to Image (Stability AI)":
    prompt = st.text_area("Enter your prompt")
    if prompt and stability_api_key:
        stability_api = client.StabilityInference(
            key=stability_api_key,
            verbose=True
        )
        if st.button("Generate Image (Stability AI)"):
            with st.spinner("Generating image..."):
                answers = stability_api.generate(
                    prompt=prompt,
                    steps=30,
                    cfg_scale=8.0,
                    width=512,
                    height=512,
                    samples=1,
                    sampler=generation.SAMPLER_K_DPMPP_2M
                )
                for resp in answers:
                    for artifact in resp.artifacts:
                        if artifact.type == generation.ARTIFACT_IMAGE:
                            img = Image.open(io.BytesIO(artifact.binary))
                            st.image(img, caption="Generated Image (Stability AI)", use_column_width=True)
