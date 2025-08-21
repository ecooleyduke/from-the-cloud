import os
from openai import OpenAI
from dotenv import load_dotenv

SYSTEM_INSTRUCTION = "You are creative and spontaneous. You create interesting responses."

# Load environment variables from .env file
load_dotenv()

# Initialize the OpenAI client
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")  # Pull the API key from environment variables
)

# Call the Chat Completion endpoint
def create_gpt_response(weather_data):
    """This function creates a fun gpt response using weather data"""

    # Extract key info from weather data
    city_name = weather_data["name"]
    temp = weather_data["main"]["temp"]
    description = weather_data["weather"][0]["description"]
    humidity = weather_data["main"]["humidity"]

    prompt = f"Please create a weather data response using the following information. {city_name} is {temp}°C with {humidity}% humidity and described as {description}"

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": SYSTEM_INSTRUCTION},
            {"role": "user",   "content": prompt}
        ]
    )

    # Extract and print the assistant's reply
    reply = response.choices[0].message.content

    return reply

