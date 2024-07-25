import os 
import pyautogui
import webbrowser 
import pyttsx3
from time import sleep
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


apps = {
    "command prompt": "cmd",
    "paint": "mspaint",
    "word": "winword",
    "excel": "excel",
    "chrome": "chrome",
    "vs code": "code",
    "powerpoint": "powerpnt",
    "notepad": "notepad",
    "calculator": "calc",
    "outlook": "outlook",
    "file explorer": "explorer",
    "task manager": "taskmgr",
    "control panel": "control",
    "settings": "start ms-settings:",
    "snipping tool": "snippingtool",
    "windows media player": "wmplayer",
    "internet explorer": "iexplore",
    "system information": "msinfo32",
    "device manager": "devmgmt.msc",
    "event viewer": "eventvwr",
    "disk cleanup": "cleanmgr",
    "disk management": "diskmgmt.msc",
    "registry editor": "regedit",
    "resource monitor": "resmon",
    "this pc": "explorer shell:MyComputerFolder",
    "documents": "explorer shell:DocumentsLibrary",
    "downloads": "explorer shell:Downloads",
    "pictures": "explorer shell:PicturesLibrary",
    "music": "explorer shell:MusicLibrary",
    "videos": "explorer shell:VideosLibrary",
    "recycle bin": "explorer shell:RecycleBinFolder"
}

def openappweb(query):
    speak("Launching, Boss")
    if".com" in query or ".co.in" in query or ".org" in query:
        query = query.replace("open","")
        query = query.replace("jarvis","")
        query = query.replace("launch","")
        query = query.replace(" ","")
        webbrowser.open(f"https://www.{query}")
    else:
        keys = list(apps.keys())
        for app in keys:
            if app in query:
                os.system(f"start {apps[app]}")

def closeappweb(query):
    if "1 tab" in query or "one tab" in query:
        pyautogui.hotkey("ctrl","w")
        speak("Tab closed")
    elif "2 tabs" in query or "2 tab" in query:
        pyautogui.hotkey("ctrl","w")
        sleep(0.3)
        pyautogui.hotkey("ctrl","w")
        speak("Tabs closed")
    elif "3 tab" in query or "3 tabs" in query:
        pyautogui.hotkey("ctrl","w")
        sleep(0.3)
        pyautogui.hotkey("ctrl","w")
        sleep(0.3)
        pyautogui.hotkey("ctrl","w")
        speak("Tabs closed")
    elif "4 tab" in query or "4 tabs" in query:
        pyautogui.hotkey("ctrl","w")
        sleep(0.3)
        pyautogui.hotkey("ctrl","w")
        sleep(0.3)
        pyautogui.hotkey("ctrl","w")
        sleep(0.3)
        pyautogui.hotkey("ctrl","w")
        speak("Tabs closed")
    elif "5 tab" in query or "5 tabs" in query:
        pyautogui.hotkey("ctrl","w")
        sleep(0.3)
        pyautogui.hotkey("ctrl","w")
        sleep(0.3)
        pyautogui.hotkey("ctrl","w")
        sleep(0.3)
        pyautogui.hotkey("ctrl","w")
        sleep(0.3)
        pyautogui.hotkey("ctrl","w")
        sleep(0.3)
        pyautogui.hotkey("ctrl","w")
        speak("All Tabs closed")
    elif "window" in query:
        pyautogui.hotkey("alt","f4") 
    else:
        keys = list(apps.keys())
        for app in keys:
            if app in query:
                os.system(f"taskkill /f /im {apps[app]}.exe")




    
