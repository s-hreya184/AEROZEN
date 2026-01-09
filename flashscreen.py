import streamlit as st
from PIL import Image
from pathlib import Path

st.set_page_config(layout="wide", page_title="Global Travel Network")

st.markdown("""
<style>
.stApp {
    background: linear-gradient(to bottom, #1a3a5c 0%, #5a89b8 100%);
}
.block-container {
    padding-top: 3rem;
}
#MainMenu, footer, header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# Load image safely
img_path = Path.cwd() / "travel_map.png"
image = Image.open(img_path)

# Resize to reduce height
new_height = 500
w, h = image.size
new_width = int(w * (new_height / h))
image = image.resize((new_width, new_height))

# CENTER the image
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image(image)
