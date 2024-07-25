import requests
import json
import pyttsx3

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def latestnews():
    apidect = {
        "pakistan":"https://gnews.io/api/v4/top-headlines?category=general&lang=en&country=pk&max=1&apikey=bb02698a5230761289a54a655bd5d89a",
        "technology":"https://newsapi.org/v2/top-headlines?country=us&category=technology&apiKey=edb3ac244ac54543b0c71cb4baa3fedd",
        "apple":"https://newsapi.org/v2/everything?q=apple&from=2024-07-19&to=2024-07-19&sortBy=popularity&apiKey=edb3ac244ac54543b0c71cb4baa3fedd",
        "business":"https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=edb3ac244ac54543b0c71cb4baa3fedd",
        "education":"https://newsapi.org/v2/top-headlines?country=us&category=education&apiKey=edb3ac244ac54543b0c71cb4baa3fedd",
        "health":"https://newsapi.org/v2/top-headlines?country=us&category=health&apiKey=edb3ac244ac54543b0c71cb4baa3fedd",
        "science":"https://newsapi.org/v2/top-headlines?country=us&category=science&apiKey=edb3ac244ac54543b0c71cb4baa3fedd",
        "sports":"https://newsapi.org/v2/top-headlines?country=us&category=sports&apiKey=edb3ac244ac54543b0c71cb4baa3fedd",
        "entertainment":"https://newsapi.org/v2/top-headlines?country=us&category=entertainment&apiKey=edb3ac244ac54543b0c71cb4baa3fedd"
    }
