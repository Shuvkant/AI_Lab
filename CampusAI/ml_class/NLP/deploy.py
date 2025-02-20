import streamlit as st
import joblib

# Load the pre-trained model
model = joblib.load('lr_model.joblib')

# Streamlit UI
st.title('News Categorization')

# Text input for the user
text_input = st.text_area('Enter news text:', height=150)

# Predict button
if st.button('Predict'):
    if text_input:
        # Use the model to predict the category
        prediction = model.predict([text_input])
        st.write(f'Predicted Category: {prediction[0]}')
    else:
        st.warning('Please enter some text to predict the category.')
