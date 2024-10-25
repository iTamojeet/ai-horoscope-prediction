import streamlit as st
import google.generativeai as gemini
from datetime import date
from dotenv import load_dotenv,find_dotenv
import os

# Set your Google Gemini API key
load_dotenv(find_dotenv(),override=True)
api_key = os.getenv("GOOGLE_API_KEY")
gemini.configure(api_key=api_key)


model = gemini.GenerativeModel("gemini-1.5-pro")

# Use Streamlit's caching to speed up repeated requests
@st.cache_data
def generate_horoscope(zodiac_sign,input):
    try:
        # Simplified prompt for faster processing
        prompt = (
            f"Please provide a detailed daily horoscope for the zodiac sign {zodiac_sign}. "
            f"Include insights on career prospects, relationship dynamics, and health considerations. "
            f"Ensure the tone is positive and encouraging, while offering practical advice."
            f"Also give lucky number and lucky dates"
            f"Also provide compatibility with other zodiac signs!"
            f"Also provide if any negative aspect in bold letters!!!"
)+input.casefold()

        # Generate a prediction using the Google Gemini API
        # Correctly passing the prompt, check the updated method if needed
        response = model.generate_content(prompt)

        prediction=response.text

    except AttributeError as attr_err:
        prediction = "Error: Unexpected response structure from the API."
        print(f"AttributeError: {attr_err}")

    except Exception as e:
        prediction = "Unable to retrieve your horoscope. Please try again later."
        print(f"General Exception: {e}")  # Log the general exception details

    return prediction


# Streamlit app layout
st.title("Your Daily AI Horoscope Predictor✨")
st.write("Select your zodiac sign to reveal your daily horoscope.")

# Zodiac sign selection
zodiac_sign = st.selectbox("Choose your zodiac sign:", [
    "Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo",
    "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"
])

input=st.text_input("Ask your query here...")

# Generate and display horoscope
if st.button("Get Daily Horoscope"):
    st.subheader(f"Your Horoscope for {date.today()}")
    horoscope = generate_horoscope(zodiac_sign,input)
    st.success(horoscope)
