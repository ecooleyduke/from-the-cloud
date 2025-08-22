from get_weather_from_input import get_weather
from create_response import create_gpt_response
import streamlit as st


"""
This program will take user input for a city and create a fun and interesting response using real-time weather data
"""


def get_user_input():
    city_name = input("Please input a city to get weather for: ").title()

    return city_name


def run():
    city_name = get_user_input()
    weather_data = get_weather(city_name)
    response = create_gpt_response(weather_data)

    print(response)
