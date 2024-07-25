import pyttsx3
import datetime
import os
import time as t
from AudioPlay import play_audio

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Read the time from the file
with open("alarmtext.txt", "r") as file:
    time = file.read().strip()

# Clear the file
with open("alarmtext.txt", "w") as file:
    file.write("")

def ring(alarm_time):
    # Clean up the alarm time string
    alarm_time = alarm_time.replace("jarvis", "").replace("set an alarm", "").replace(" and ", ":").strip()
    
    print(f"Alarm set for: {alarm_time}")

    while True:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        
        if current_time == alarm_time:
            speak("Alarm ringing, Boss")
            play_audio("alarm.mp3")
            break
        
        t.sleep(1)

ring(time)
