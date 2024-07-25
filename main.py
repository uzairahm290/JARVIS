import pyttsx3 
import webbrowser
import speech_recognition as sr
from welcome import welcome
from welcome import play_audio 
from welcome import tell_random_joke
from welcome import tell_date
import requests
from bs4 import BeautifulSoup
import datetime
import os
from time import sleep
import pyautogui
import random
import speedtest
import psutil
from news import get_news

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

def alarm(query):
    timehere = open("alarmtext.txt","a")
    timehere.write(query)
    timehere.close()
    os.startfile("alarm.py")



if __name__ == "__main__":
    play_audio("welcome.mp3")
    while True:
        query = takeCommand().lower()
        if "wake up" in query or "uth ja" in query or "jarvis" in query:
            welcome()  # Call the corrected function
            while True:
                query = takeCommand().lower()
                if "go to sleep" in query:
                    speak("Ok Boss, You can call me anytime")
                    break 
                elif "hello" in query:
                    speak("Hello Boss, how are you ?")
                elif "how are you" in query:
                    speak("I am fine,  What about you ?")
                elif "i am fine" in query:
                    speak("That's Great , Boss")
                elif "thank you" in query or "shukriya" in query or "thanks" in query:
                    speak("You're Welcome!")
                elif "what's your name" in query:
                    speak("I'm Jarvis, your friendly assistant.")
                elif "what do you eat" in query:
                    speak("I consume data, lots of it.")
                elif "what can you do" in query:
                    speak("I can help you with various tasks like searching the web, opening tabs, playing music, telling jokes, and more. Just ask!")
                elif "do you like humans" in query:
                    speak("Of course! Humans are fascinating. You created me, after all.")
                elif "what's your favorite movie" in query:
                    speak("I like The Matrix. It's a classic.")
                elif "joke" in query:
                    joke = tell_random_joke()
                    speak(joke)
                    speak("I hope you like the joke")
                elif "are you real" in query:
                    speak("As real as your imagination, Boss!")
                elif "what's your favorite color" in query:
                    speak("I'd say blue. It's calm and cool, like me.")
                elif "tired" in query:
                    speak("Playing your favourite nasheeds , Boss")
                    a = (1,2,3)
                    b = random.choice(a)
                    if b==1:
                        webbrowser.open("https://www.youtube.com/watch?v=dWBgNHT4ipE")
                    if b==2:
                        webbrowser.open("https://www.youtube.com/watch?v=NrsCej6SVxM")
                    if b==3:
                        webbrowser.open("https://www.youtube.com/watch?v=coInHMUQzCg")
                elif "depressed" in query:
                    speak("Listen this then")
                    webbrowser.open("https://www.youtube.com/watch?v=Mi37IRnW0Ds")
                elif "calculate" in query:
                    from calculate import WolfRamAlpha
                    from calculate import Calc
                    query = query.replace("calculate","")
                    query = query.replace("jarvis","")
                    Calc(query)
                elif "news" in query:
                    api_key = 'edb3ac244ac54543b0c71cb4baa3fedd' 
                    news = get_news(api_key)
                    print(news)
                    speak(news)
                elif 'new tab' in query:
                    pyautogui.hotkey('ctrl', 't')
                    speak("Opening new tab")
                elif 'close tab' in query:
                    pyautogui.hotkey('ctrl', 'w')
                elif 'close window' in query:
                    pyautogui.hotkey('alt', 'f4')
                    speak("Closing current tab")
                elif 'reopen closed tab' in query:
                    pyautogui.hotkey('ctrl', 'shift', 't')
                    speak("Reopening closed tab")
                elif 'next tab' in query:
                    pyautogui.hotkey('ctrl', 'tab')
                    speak("Switching to next tab")
                elif 'previous tab' in query:
                    pyautogui.hotkey('ctrl', 'shift', 'tab')
                    speak("Switching to previous tab")
                elif 'history' in query:
                    pyautogui.hotkey('ctrl', 'h')
                    speak("Opening history")
                elif 'downloads' in query:
                    pyautogui.hotkey('ctrl', 'j')
                    speak("Opening downloads")
                elif 'bookmarks' in query:
                    pyautogui.hotkey('ctrl', 'shift', 'b')
                    speak("Opening bookmarks")
                elif 'refresh' in query:
                    pyautogui.hotkey('ctrl', 'r')
                    speak("Refreshing page")
                elif 'new window' in query:
                    pyautogui.hotkey('ctrl', 'n')
                    speak("Opening new window")
                elif 'incognito mode' in query:
                    pyautogui.hotkey('ctrl', 'shift', 'n')
                    speak("Opening incognito mode")
                elif 'zoom in' in query:
                    pyautogui.hotkey('ctrl', '+')
                    speak("Zooming in")
                elif 'zoom out' in query:
                    pyautogui.hotkey('ctrl', '-')
                    speak("Zooming out")
                elif "pause" in query:
                    pyautogui.press("k")
                    speak("Video paused")
                elif "play next" in query:
                    pyautogui.hotkey("shift" , "n")
                    speak("Next Video Played")
                elif "mute" in query:
                    from keyboard import volumemute
                    speak("Muted")
                    volumemute()
                elif "scroll up" in query:
                    pyautogui.scroll(500)
                elif "scroll down" in query:
                    pyautogui.scroll(-500)
                elif "ummute" in query:
                    from keyboard import volumemute
                    volumemute()
                    speak("Unmuted")                    
                elif "volume up" in query:
                    from keyboard import volumeup
                    speak("Turning volume up, Boss")
                    volumeup()
                elif "volume down" in query:
                    from keyboard import volumedown
                    speak("Turning volume down, Boss")
                    volumedown()
                elif "open" in query:
                    speak("Opening Boss")
                    query = query.replace("jarvis","")
                    query = query.replace("open","")
                    pyautogui.press("super")
                    pyautogui.typewrite(query)
                    pyautogui.sleep(2)
                    pyautogui.press("enter")
                elif "internet speed" in query or "wifi speed" in query:
                    wifi = speedtest.Speedtest()
                    upload_net = round(wifi.upload()/1048576, 2)
                    download_net = round(wifi.download()/1048576, 2)
                    print(f"Wifi Upload Speed is {upload_net} MB")
                    print(f"Wifi Download Speed is {download_net} MB")
                    speak(f"Wifi Upload Speed is {upload_net} MB")
                    speak(f"Wifi Download Speed is {download_net} MB")
                elif "whatsapp" in query:
                    from whatsappchat import sendMessage
                    sendMessage()
                elif "battery" in query:
                    battery = psutil.sensors_battery()
                    percentage = battery.percent  
                    speak(f"Boss our system have {percentage} percent battery")
                    if percentage >= 75:
                        speak("We have enough battery we can continue our work")
                    elif percentage >=30 and percentage <=75:
                        speak("We should connect our system to charging point to charge our battery")
                    elif percentage >=15 and percentage <= 30:
                        speak("We don't have enough power to work, please connect to charging")
                    elif percentage <= 15:
                        speak("We have low power, please connect ot charging otherwise system will shutdown ") 
                elif "shutdown system" in query:
                    speak("Are you sure you want to shutdown your computer? Say yes to confirm or no to cancel.")
                    confirmation = takeCommand().lower()
                            
                    if "none" in confirmation:
                        speak("I didn't catch that. Please say yes to confirm or no to cancel.")
                        continue                        
                    print(f"Confirmation: {confirmation}")
                    if "yes" in confirmation:
                        speak("Shutting down the system.")
                        os.system("shutdown /s /t 1")
                        break
                    elif "no" in confirmation:
                        speak("Shutdown canceled.") 
                    else:
                        speak("I didn't catch that. Please say yes to confirm or no to cancel.")
                elif "restart system" in query:
                    speak("Are you sure you want to restart your computer? Say yes to confirm or no to cancel.")
                    confirmation = takeCommand().lower()
                    if confirmation is None:
                        speak("I didn't catch that. Please say yes to confirm or no to cancel.")
                        continue
                    print(f"Confirmation: {confirmation}")
                    if "yes" in confirmation:
                        speak("Restarting the system.")
                        os.system("shutdown /r /t 1")
                        break
                    elif "no" in confirmation:
                        speak("Restart canceled.")
                    else:
                        speak("I didn't catch that. Please say yes to confirm or no to cancel.")
                elif "open" in query:
                    from apps import openappweb
                    openappweb(query)
                elif "google" in query:
                    from searchOn import searchGoogle
                    searchGoogle(query)
                elif "youtube" in query:
                    from searchOn import searchYoutube
                    searchYoutube(query)
                elif "wikipedia" in query:
                    from searchOn import searchWikipedia
                    searchWikipedia(query)
                elif "temperature in" in query:
                    city = query.split("in")[-1].strip()
                    search = f"temperature in {city}"
                    url = f"https://www.google.com/search?q={query}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div", class_ = "BNeawe").text
                    speak(f"Current {search} is {temp}")
                elif "temperature" in query:
                    search = "temperature in toba tek singh"
                    url = f"https://www.google.com/search?q={query}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div", class_ = "BNeawe").text
                    speak(f"Current {search} is {temp}")
                elif "weather in" in query:
                    from weather import get_weather
                    city = query.split("in")[-1].strip()
                    weather_info = get_weather(city)
                    print(weather_info)
                    speak(weather_info)
                elif "weather" in query:
                    from weather import get_weather
                    city = 'toba tek singh'
                    weather_info = get_weather(city)
                    print(weather_info)
                    speak(weather_info)
                elif "the date" in query:
                    today = tell_date()
                    speak(today)
                elif "the time" in query:
                    strTime = datetime.datetime.now().strftime("%H:%M")
                    speak(f"Boss, the time is {strTime}")
                elif "deactivate" in query:
                    speak("Jarvis Deactivated Successfully ......")
                    exit() 
                elif "set an alarm" in query:
                    print("Input time example:- 10 and 10 and 10")
                    speak("set the time")
                    a = input("Please tell the time :-")
                    alarm(a)
                    speak("Done, Boss")
                elif "remember that" in query:
                    rememberMessage = query.replace("remember that","")
                    rememberMessage = query.replace("jarvis","")
                    rememberMessage = query.replace("that","")
                    rememberMessage = query.replace("remember","")
                    speak("You told me to remember that " + rememberMessage)
                    remember = open("remember.txt","w")
                    remember.write(rememberMessage)
                    remember.close()
                elif "what do you remember" in query:
                    remember = open("remember.txt")
                    speak("You told me to remember that " + remember.read() )

                elif "play" in query:
                    pyautogui.press("k")
                    speak("Video played")
                elif "full screen" in query:
                    pyautogui.press("f")
                    speak("Full screen Mode On")
                elif "search" in query:
                    query = query.replace("search","")
                    speak(f"searching for {query}")
                    pyautogui.press("/")
                    pyautogui.hotkey("ctrl","a")
                    pyautogui.write(query)
                    pyautogui.press("enter")

                elif "typing mode" in query :
                    speak("typing mode on")
                    while True:
                        command = takeCommand.lower()
                        if "jarvis stop" in command:
                            speak("typing mode off")
                            break
                        elif "jarvis wait" in command:
                            speak("I am waiting")
                            sleep(10)
                        elif "jarvis continue" in command:
                            speak("ok boss")
                            pyautogui.write(command)
                        elif command == None:
                            continue
                        else:
                            pyautogui.write(command)
                elif "press enter" in query:
                    pyautogui.press("enter")

                        

