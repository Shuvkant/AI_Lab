import pandas as pd
import tensorflow as tf
from tensorflow import keras
from sklearn.model_selection import train_test_split
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np
import streamlit as st
import pickle

# Load trained model and tokenizer
model = keras.models.load_model("sentiment_model.h5")
with open("tokenizer.pkl", "rb") as f:
    tokenizer = pickle.load(f)

# Parameters
max_len = 100

# Function to predict sentiment
def predict_sentiment(text):
    sequence = tokenizer.texts_to_sequences([text])
    padded_sequence = pad_sequences(sequence, maxlen=max_len, padding="post")
    prediction = model.predict(padded_sequence)
    sentiment_labels = {2: "😊 Positive", 1: "😐 Neutral", 0: "☹️ Negative"}
    return sentiment_labels[np.argmax(prediction)]

# Streamlit App UI
st.title("📝 NLP Sentiment Analysis App")
st.subheader("Analyze the sentiment of your text in real-time!")

# User input
user_input = st.text_area("Enter text:", "Type here...")

if st.button("Analyze Sentiment"):
    if user_input.strip():
        sentiment = predict_sentiment(user_input)
        st.write(f"**Sentiment:** {sentiment}")
    else:
        st.warning("Please enter some text to analyze.")
