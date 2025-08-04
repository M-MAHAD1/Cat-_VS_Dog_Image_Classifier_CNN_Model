import streamlit as st
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from PIL import Image

# Load Trained Model
model = load_model("best_model.h5")

# Title
st.title("🐱🐶 Cat or Dog Classifier")
st.write("Upload an image to predict whether it's a **Cat** or a **Dog**.")

# File uploader
uploaded_file = st.file_uploader("Upload an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    img = Image.open(uploaded_file)

    # Reduce both height and width (preserves aspect ratio)
    img.thumbnail((200, 200))  # Set max width and height
    st.image(img, caption='Uploaded Image', use_column_width=False)

    # Predict button
    if st.button("Predict"):
        # Resize for model prediction
        img = img.resize((150, 150))
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        img_array = img_array / 255.0

        # Make prediction
        result = model.predict(img_array)
        prediction = "🐶 Dog" if result[0][0] > 0.5 else "🐱 Cat"

        # Show result
        st.subheader(f"Prediction: {prediction}")
