import streamlit as st
import os
from google import genai
from google.genai import types
from PIL import Image
from dotenv import load_dotenv

# --- 1. CONFIGURATION ---
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    st.error("⚠️ API Key missing! Check your .env file.")
    st.stop()

# New 2025 Client Setup
client = genai.Client(api_key=api_key)

# --- 2. PROMPT LOGIC ---
def get_chef_prompt(roast_mode):
    if roast_mode:
        return "You are Gordon Ramsay. Roast the user about these ingredients, then give a recipe. Be funny!"
    else:
        return "You are a friendly chef. Identify these ingredients and suggest a delicious recipe."

# --- 3. UI SETUP ---
st.set_page_config(page_title="Fridge-to-Feast", page_icon="🥦")
st.title("🥦 Fridge-to-Feast")

roast_mode = st.toggle("🔥 Gordon Ramsay Mode")
uploaded_file = st.file_uploader("Upload Fridge Photo", type=["jpg", "png", "jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption='Your Fridge', use_column_width=True)
    
    if st.button("Generate Recipe"):
        with st.spinner('Chef is thinking...'):
            try:
                # CONVERT IMAGE FOR API
                # The new API handles images differently (easier)
                prompt = get_chef_prompt(roast_mode)
                
                # CALL THE NEW API (Gemini 2.0)
                response = client.models.generate_content(
                    model="gemini-flash-latest",
                    contents=[prompt, image]
                )
                
                st.success("Recipe Found!")
                st.markdown(response.text)
                
            except Exception as e:
                st.error(f"Error: {e}")