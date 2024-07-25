import pyttsx3 
import speech_recognition as sr
from bs4 import BeautifulSoup
from time import sleep
from datetime import datetime, timedelta
import pywhatkit

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.......")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source, 0, 4)
    try:
        print("Understanding.......")
        query = r.recognize_google(audio, language="en-in")
        print(f"You said : {query}\n")
    except Exception as e:
        print("Say Again.........")
        return "None"
    return query

strTime = int(datetime.now().strftime("%H"))
update = int((datetime.now() + timedelta(minutes=2)).strftime("%M"))

# Dictionary of names and their phone numbers
contacts = {
    "uzair": "+923136874323",
    "husain": "+923136874679",
    "ammi": "+923346286322",
    "abu": "+923336874323",
    "mamu": "+923008793199",
}

def sendMessage():
    speak("Whom do you want to message?")
    name = input("Enter the name of the contact you want to message: ").lower()
    
    if name in contacts:
        speak(f"What's the message for {name}?")
        message = input(f"Enter message for {name}: ")
        
        if not message:
            speak("The message is empty. Please provide a valid message.")
            return
        
        current_time = datetime.now()
        time_hour = current_time.hour
        time_min = (current_time.minute + 1) % 60  # Send in the next minute

        # If minute rolls over, adjust the hour
        if time_min == 0:
            time_hour = (time_hour + 1) % 24
        
        pywhatkit.sendwhatmsg(contacts[name], message, time_hour=time_hour, time_min=time_min, tab_close=True)
        speak(f"Message sent to {name}.")
        
        sleep(20)
    else:
        speak("Sorry, I couldn't find that person in the contacts.")