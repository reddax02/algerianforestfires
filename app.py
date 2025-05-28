import streamlit as st
import joblib
import numpy as np

# Load the trained model
model = joblib.load("final_linear_model.pkl")

st.title("🔥 Algerian Forest Fire FWI Predictor")
st.markdown("Enter the following values to predict the Fire Weather Index (FWI):")

# Inputs must match the model's trained features
ISI = st.number_input("🔥 Initial Spread Index (ISI)", min_value=0.0)
BUI = st.number_input("🔥 Build Up Index (BUI)", min_value=0.0)
DC = st.number_input("🔥 Drought Code (DC)", min_value=0.0)
Temperature = st.number_input("🌡️ Temperature (°C)", min_value=0.0, max_value=50.0)
RH = st.number_input("💧 Relative Humidity (%)", min_value=0.0, max_value=100.0)
Rain = st.number_input("🌧️ Rain (mm)", min_value=0.0, max_value=50.0)

if st.button("Predict FWI"):
    features = np.array([[ISI, BUI, DC, Temperature, RH, Rain]])
    prediction = model.predict(features)
    st.success(f"🔥 Predicted Fire Weather Index (FWI): {prediction[0]:.2f}")
