import streamlit as st
import create_response
from get_weather_from_input import get_weather
from create_response import create_gpt_response


st.title("From the Cloud Weather App")
st.write("This program will take user input for a city and create a fun and interesting response using real-time weather data")

# capture user text input for city
user_input = st.text_input("Please input a city to get weather for:")

if user_input:
    weather_data = get_weather(user_input)
    response = create_gpt_response(weather_data)
    st.markdown(response)
