import pyttsx3
import datetime
import pygame
import random 

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def welcome():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Boss")
    elif hour >= 12 and hour <= 18:
        speak("Good Afternoon Boss")
    else:
        speak("Good Evening Boss")
    speak("Tell me How can I help you")


def play_audio(file_name):
    pygame.mixer.init()

    pygame.mixer.music.load(file_name)

    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)



def tell_random_joke():
    jokes = [
        "Why don't scientists trust atoms? Because they make up everything!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "Why don’t skeletons fight each other? They don’t have the guts.",
        "What do you get when you cross a snowman and a vampire? Frostbite.",
        "Why don't some couples go to the gym? Because some relationships don't work out.",
        "What do you call fake spaghetti? An impasta!",
        "Why don't programmers like nature? It has too many bugs.",
        "Why do bicycles fall over? Because they are two-tired!",
        "What do you call cheese that isn't yours? Nacho cheese.",
        "Why did the math book look sad? Because it had too many problems."
    ]
    return random.choice(jokes)

def tell_date():
    today = datetime.date.today()
    formatted_date = today.strftime("%B %d, %Y")
    speak(f"Today's date is {formatted_date}")