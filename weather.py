import requests
from bs4 import BeautifulSoup
import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def get_weather(city):
    search_query = f"temperature in {city}"
    url = f"https://www.google.com/search?q={search_query}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    
    try:
        temp = soup.find("div", class_="BNeawe iBp4i AP7Wnd").text
        weather_condition = soup.find("div", class_="BNeawe tAd8D AP7Wnd").text.split('\n')[1]

        # Enhanced responses based on weather condition
        if "clear" in weather_condition.lower():
            result = f"Right now in {city}, it's a clear {temp} with sunny skies. Perfect day to enjoy outside!"
        elif "cloudy" in weather_condition.lower():
            result = f"In {city}, it's currently {temp} with cloudy skies. Maybe a cozy indoor day!"
        elif "rain" in weather_condition.lower():
            result = f"Today in {city}, it's {temp} with some rain. Don’t forget your umbrella!"
        elif "snow" in weather_condition.lower():
            result = f"Currently in {city}, it's {temp} with snowflakes falling. Time for some hot cocoa!"
        elif "storm" in weather_condition.lower():
            result = f"In {city}, it's {temp} with a storm brewing. Stay safe and indoors!"
        else:
            result = f"Right now in {city}, the weather is {temp} with {weather_condition}. Have a great day!"

    except AttributeError:
        result = "Sorry, I couldn't fetch the weather data at the moment."
    
    return result