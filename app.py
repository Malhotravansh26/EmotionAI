
import streamlit as st
import pickle
import os

# Page configuration
st.set_page_config(
    page_title="EmotionAI",
    page_icon="🧠",
    layout="centered"
)

# Load trained model
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_DIR = os.path.join(BASE_DIR, "model")

with open(os.path.join(MODEL_DIR, "emotion_model.pkl"), "rb") as f:
    model = pickle.load(f)

with open(os.path.join(MODEL_DIR, "vectorizer.pkl"), "rb") as f:
    vectorizer = pickle.load(f)

with open(os.path.join(MODEL_DIR, "label_mapping.pkl"), "rb") as f:
    label_mapping = pickle.load(f)

# Reverse label mapping
reverse_mapping = {v: k for k, v in label_mapping.items()}

# UI
st.title("🧠 EmotionAI")
st.subheader("AI Powered Emotion Detection")
st.write("Enter any sentence and discover the emotion behind it.")

user_text = st.text_area(
    "Enter your text:",
    placeholder="Example: I am feeling very happy today..."
)

if st.button("Predict Emotion", use_container_width=True):

    if user_text.strip():

        # Transform text
        text_vector = vectorizer.transform([user_text])

        # Predict
        prediction = model.predict(text_vector)[0]

        emotion = reverse_mapping.get(prediction, str(prediction))

        st.success(f"Detected Emotion: {emotion.upper()}")

        # Prediction probabilities
        if hasattr(model, "predict_proba"):
            probabilities = model.predict_proba(text_vector)[0]

            st.subheader("Emotion Probability")

            for index, probability in enumerate(probabilities):
                label = reverse_mapping.get(
                    model.classes_[index],
                    str(model.classes_[index])
                )

                st.write(f"{label}: {probability*100:.2f}%")
                st.progress(float(probability))

    else:
        st.warning("Please enter some text first.")
