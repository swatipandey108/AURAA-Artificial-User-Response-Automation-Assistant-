import speech_recognition as sr
import os
import webbrowser
import openai
import datetime
import random
import win32com.client
import pyjokes
import psutil
import pywhatkit
from config import apikey

chatStr = ""

def say(text):
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    speaker.Speak(text)

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}")
        return query
    except Exception as e:
        print(f"Speech Recognition Error: {e}")
        return ""

def chat(query):
    global chatStr
    openai.api_key = apikey
    chatStr += f"User: {query}\nJarvis: "
    try:
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=chatStr,
            temperature=0.7,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        reply = response["choices"][0]["text"].strip()
        say(reply)
        chatStr += f"{reply}\n"
        return reply
    except Exception as e:
        say("Sorry, I had trouble responding.")
        print(f"OpenAI Error: {e}")
        return "Error"

def ai(prompt):
    openai.api_key = apikey
    say("Thinking...")
    try:
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            temperature=0.7,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        result = response["choices"][0]["text"].strip()
        say(result)

        if not os.path.exists("Openai"):
            os.mkdir("Openai")

        filename = f"Openai/{datetime.datetime.now().strftime('%Y%m%d-%H%M%S')}.txt"
        with open(filename, "w") as f:
            f.write(f"Prompt: {prompt}\n\nResponse:\n{result}")

    except Exception as e:
        say("There was an error with the AI response.")
        print(f"OpenAI Error: {e}")

# Custom Windows app paths
app_paths = {
    "notepad": "notepad.exe",
    "calculator": "calc.exe",
    "chrome": r"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
}

music_folder = r"C:\\Users\\SWATI PANDEY\\Music"

def tell_joke():
    joke = pyjokes.get_joke()
    say(joke)

def system_status():
    battery = psutil.sensors_battery()
    plugged = "Plugged In" if battery.power_plugged else "Not Plugged In"
    percent = battery.percent
    say(f"Battery is at {percent} percent and it is {plugged}.")

if __name__ == '__main__':
    print("Welcome to Jarvis A.I")
    say("Jarvis activated. Hello Swati!")

    while True:
        query = takeCommand().lower()
        if not query:
            continue

        # Website Shortcuts
        sites = [
            ["youtube", "https://www.youtube.com"],
            ["wikipedia", "https://www.wikipedia.com"],
            ["google", "https://www.google.com"]
        ]

        opened = False
        for site in sites:
            if f"open {site[0]}" in query:
                say(f"Opening {site[0]}...")
                webbrowser.open(site[1])
                opened = True
                break

        if opened:
            continue

        # New Feature: Play Specific YouTube Video
        elif "play" in query and "on youtube" in query:
            video = query.replace("play", "").replace("on youtube", "").strip()
            say(f"Playing {video} on YouTube")
            pywhatkit.playonyt(video)

        # New Feature: Web search
        elif "search" in query:
            search_term = query.replace("search", "").strip()
            if search_term:
                say(f"Searching Google for {search_term}")
                pywhatkit.search(search_term)
            else:
                say("What should I search?")
                search_query = takeCommand().lower()
                if search_query:
                    pywhatkit.search(search_query)
                    say(f"Searching Google for {search_query}")

        elif "open music" in query:
            try:
                songs = [f for f in os.listdir(music_folder) if f.endswith(".mp3")]
                if songs:
                    song = random.choice(songs)
                    os.startfile(os.path.join(music_folder, song))
                    say("Playing music.")
                else:
                    say("No music files found in your music folder.")
            except Exception as e:
                say("Unable to play music.")
                print(f"Music Error: {e}")

        elif "the time" in query:
            now = datetime.datetime.now()
            say(f"The time is {now.strftime('%I:%M %p')}")

        elif "battery status" in query:
            system_status()

        elif "tell me a joke" in query:
            tell_joke()

        elif "open" in query:
            found = False
            for app in app_paths:
                if app in query:
                    os.startfile(app_paths[app])
                    say(f"Opening {app}")
                    found = True
                    break
            if not found:
                say("I don't know how to open that app. Please update my settings.")

        elif "using artificial intelligence" in query:
            ai(prompt=query)

        elif "reset chat" in query:
            chatStr = ""
            say("Chat history reset.")

        elif "jarvis quit" in query or "exit" in query:
            say("Goodbye Swati ji. Have a wonderful day!")
            break

        else:
            print("Chatting...")
            chat(query)
        
