import streamlit as st
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Download VADER lexicon
nltk.download('vader_lexicon')
sia = SentimentIntensityAnalyzer()

def analyze_sentiment(text):
    """Analyze sentiment of input text and return sentiment category."""
    score = sia.polarity_scores(text)
    if score['compound'] >= 0.05:
        return "😊 Positive"
    elif score['compound'] <= -0.05:
        return "☹️ Negative"
    else:
        return "😐 Neutral"

# Streamlit App UI
st.title("📝 NLP Sentiment Analysis App")
st.subheader("Analyze the sentiment of your text in real-time!")

# User input
user_input = st.text_area("Enter text:", "Type here...")

if st.button("Analyze Sentiment"):
    if user_input.strip():
        sentiment = analyze_sentiment(user_input)
        st.write(f"**Sentiment:** {sentiment}")
    else:
        st.warning("Please enter some text to analyze.")
