import streamlit as st
from transformers import pipeline

# Initialize the emotion detection model
emotion_model = pipeline("sentiment-analysis", model="j-hartmann/emotion-english-distilroberta-base")

# Define a function to map emotions to emojis
def emotion_to_emoji(emotion):
    emojis = {
        'anger': '😡',
        'disgust': '🤢',
        'fear': '😨',
        'joy': '😊',
        'neutral': '😐',
        'sadness': '😢',
        'surprise': '😲',
        'love': '❤️'
    }
    return emojis.get(emotion, '🤔')

# Streamlit UI
st.title("Emotion Detector with Emoji")

user_input = st.text_input("Enter your message:")
if user_input:
    # Detect emotion in the input
    result = emotion_model(user_input)[0]
    emotion = result['label'].lower()
    emoji = emotion_to_emoji(emotion)

    # Display the result
    st.write(f"**Detected Emotion:** {emotion.capitalize()} {emoji}")
