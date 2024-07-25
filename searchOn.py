import speech_recognition as sr
import pyttsx3 
import pywhatkit
import wikipedia 
import webbrowser

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice" , voices[0].id)
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
        audio = r.listen(source,0,4)   

    try:
        print("Understanding.......")
        query = r.recognize_google(audio,language = "en-in")
        print(f"You said : {query}\n")
    except Exception as e:
        print("Say Again.........")
        return "None"
    return query

query = takeCommand().lower()

def searchGoogle(query):
    if "google" in query:
        import wikipedia as googleScrap 
        query = query.replace("jarvis","")
        query = query.replace("google search","")
        query = query.replace("google","")
        speak("This is what I found on GOogle")

        try:
            pywhatkit.search(query)
            result = googleScrap.summary(query,1)
            speak(result)
        except:
            speak("No speakable output available")

def searchYoutube(query):
    if "youtube" in query:
        speak("This is what I found on Youtube!")
        query = query.replace("jarvis","")
        query = query.replace("youtube search","")
        query = query.replace("youtube","")
        query = query.replace("search","")
        query = query.replace("play on youtube","")
        query = query.replace("on youtube","")
        query = query.replace("play","")
        web = "https://www.youtube.com/results?search_query=" + query
        webbrowser.open(web)
        pywhatkit.playonyt(query)
        speak("Done, Boss")

def searchWikipedia(query):
    if "wikipedia" in query:
        speak("Searching from Wikipedia.....")
        query = query.replace("jarvis","")
        query = query.replace("wikipedia search","")
        query = query.replace("wikipedia","")
        results = wikipedia.summary(query,sentences = 2)
        speak("According to wikipedia...")
        print(results)
        speak(results)
 