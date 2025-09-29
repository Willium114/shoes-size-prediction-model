import streamlit as st
import pickle
import numpy as np
import os

# ==============================
# Load Model & Label Encoder
# ==============================

# Try to load model & encoder (whether in current or parent folder)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "model.pkl")
ENCODER_PATH = os.path.join(BASE_DIR, "label_encoder.pkl")

if not os.path.exists(MODEL_PATH):  # check parent folder if not found
    MODEL_PATH = os.path.join(BASE_DIR, "../model.pkl")

if not os.path.exists(ENCODER_PATH):  # check parent folder if not found
    ENCODER_PATH = os.path.join(BASE_DIR, "../label_encoder.pkl")

with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)

with open(ENCODER_PATH, "rb") as f:
    label_encoder = pickle.load(f)

# ==============================
# Streamlit UI
# ==============================

st.set_page_config(page_title="Shoe Size Predictor", page_icon="👟", layout="centered")

st.title("👟 Shoe Size Predictor")
st.markdown("Enter your details below to predict your shoe size:")

# Input fields
age = st.number_input("Enter Age", min_value=1.0, max_value=100.0, value=25.0)
height = st.number_input("Enter Height (cm)", min_value=50.0, max_value=250.0, value=170.0)
gender = st.selectbox("Select Gender", ["Male", "Female"])

if st.button("Predict Shoe Size"):
    try:
        gender_encoded = label_encoder.transform([gender])[0]
        input_data = np.array([[age, height, gender_encoded]])
        prediction = model.predict(input_data)[0]
        prediction = round(prediction, 2)
        st.success(f"Predicted Shoe Size: **{prediction}**")
    except Exception as e:
        st.error(f"Error while predicting: {e}")

# ==============================
# Footer
# ==============================
st.markdown("---")
st.caption("Built By ❤️ Aqib Javed")
