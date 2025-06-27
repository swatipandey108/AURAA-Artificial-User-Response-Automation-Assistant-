import os
import openai
import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
from config import apikey

# Set OpenAI key
openai.api_key = apikey

# Initialize TTS engine
engine = pyttsx3.init()

def say(text):
    engine.say(text)
    engine.runAndWait()

def ai(prompt):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    print("AI Response:", response["choices"][0]["text"].strip())
    say(response["choices"][0]["text"].strip())

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception:
            say("Some error occurred. Sorry Swati ji.")
            return ""

if __name__ == '__main__':
    say("Hello Swati ji, I am Jarvis. How can I help you today?")
    chatStr = ""

    while True:
        print("Waiting for command...")
        query = takeCommand()

        if not query:
            continue

        # Open websites
        sites = [
            ["youtube", "https://www.youtube.com"],
            ["wikipedia", "https://www.wikipedia.com"],
            ["google", "https://www.google.com"]
        ]
        for site in sites:
            if f"open {site[0]}" in query.lower():
                say(f"Opening {site[0]} Swati ji...")
                webbrowser.open(site[1])

        # Play music
        elif "open music" in query.lower():
            musicPath = "C:\\Users\\SWATI PANDEY\\Music\\sample.mp3"  # Update path if needed
            os.startfile(musicPath)

        # Tell time
        elif "the time" in query.lower():
            hour = datetime.datetime.now().strftime("%H")
            minute = datetime.datetime.now().strftime("%M")
            say(f"Swati ji, time is {hour} bajke {minute} minutes.")

        # Open apps (you can customize these paths)
        elif "open notepad" in query.lower():
            os.system("start notepad")

        # AI chat
        elif "using artificial intelligence" in query.lower():
            ai(prompt=query)

        elif "reset chat" in query.lower():
            chatStr = ""
            say("Chat reset successfully.")

        elif "jarvis quit" in query.lower() or "exit" in query.lower():
            say("Goodbye Swati ji!")
            break

        else:
            print("Chatting...")
            ai(prompt=query)
