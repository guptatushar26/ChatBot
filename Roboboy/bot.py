import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import requests
from bs4 import BeautifulSoup

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)
chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        print("Good Morning! My name is roboboy. How may I assist you?")
        speak("Good Morning! My name is robo boy. Please tell me how may I assist you?")

    elif hour>=12 and hour<18:
        print("Good Afternoon! My name is roboboy. How may I assist you?") 
        speak("Good Afternoon! My name is robo boy. Please tell me how may I assist you?")  

    else:
        print("Good Evening! My name is roboboy. How may I assist you?")
        speak("Good Evening! My name is robo boy. Please tell me how may I assist you?")  
      

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query
    
def takeCommand():
    query = input()
    return query

def sendEmail(to, content):
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    #server.ehlo()
    #server.starttls()
    server.login('your email', 'gmail app password')
    server.sendmail('your email',to , content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'tell me about' in query:
            print('searching...')
            speak('Ok Sir... searching...')
            query = query.replace("tell me about", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            print("ok sir opening youtube")
            speak("ok sir opening youtube")
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            print("ok sir opening google")
            speak("ok sir opening google")
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            print("ok sir opening stackoverflow")
            speak("ok sir opening stackoverflow")
            webbrowser.open("stackoverflow.com")   


        elif 'music' in query:
            music_dir = 'D:\SONGS'
            songs = os.listdir(music_dir)
            print(songs)    
            a = int(input())
            os.startfile(os.path.join(music_dir, songs[a-1]))

        elif 'hello' in query or 'hi' in query or 'hola' in query or 'hey there' in query :
            speak("Hey")
            print("What is your name?")
            speak("What is your name")
            name = input("")
            print(f"nice to meet you {name}",)
            speak(f"nice to meet you {name}")

        elif 'who are you' in query or 'tell me about you' in query or 'introduce yourself' in query:
            speak("i am a Robo  boy , a vertual assistance and a self learner .Develop in python ")

        elif 'news' in query:
            webbrowser.get(chrome_path).open("https://news.google.com/topstories?hl=en-IN&gl=IN&ceid=IN:en")

        elif 'ok' in query:
            speak("Ask Me anything")

        elif 'good' in query:
            speak("Thank You sir. Give a spacial thanks Who develop me")
            exit(0);

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")   
            print(f"Sir, the time is {strTime}") 
            speak(f"Sir, the time is {strTime}")
           

        elif 'open code' in query:
            codePath = "C:\\Users\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'email to senders name' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "senders email"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry. I am not able to send this email")

        elif 'cricket' in query or 'cricket live score' in query:
             webbrowser.get(chrome_path).open("https://www.cricbuzz.com/cricket-match/live-scores")
        
        elif 'news' in query or 'latest news' in query:
             webbrowser.get(chrome_path).open("https://news.google.com/topstories?hl=en-IN&gl=IN&ceid=IN:en")

        elif 'dollar' in query or 'dollar price' in query :
           search = "usd+inr"
           url = f"https://www.google.com/search?q={search}"
           r = requests.get(url)
           data = BeautifulSoup(r.text,"html.parser")
           usd = data.find("div",class_="BNeawe").text
           print(f"The Value of 1 dollar is {usd}")
           speak(f"The Value of 1 dollar is {usd}")


        elif 'weather' in query :
           search = "weather"
           url = f"https://www.google.com/search?q={search}"
           r = requests.get(url)
           data = BeautifulSoup(r.text,"html.parser")
           temp = data.find("div",class_="BNeawe").text
           print(f"current {search} is {temp}")
           speak(f"current {search} is {temp}")

        elif 'bitcoin price' in query or 'bitcoin' in query:
           search = "bitcoin"
           url = f"https://www.google.com/search?q={search}"
           r = requests.get(url)
           data = BeautifulSoup(r.text,"html.parser")
           temp = data.find("div",class_="BNeawe").text
           print(f"bitcoin price in india is {search} is {temp}")
           speak(f"bitcoin price in india is {search} is {temp}")
           
        elif 'search ' in query:
           speak('Ok Sir... searching...')
           print('searching...')
           query = query.replace("search", "")
           search = query
           url = f"https://www.google.com/search?q={search}"
           r = requests.get(url)
           data = BeautifulSoup(r.text,"html.parser")
           temp = data.find("div",class_="BNeawe").text
           print(f"{query} is {temp}")
           speak(f"{query} is {temp}")

        elif 'exit' in query or 'goodbye' in query:
            exit(0);
        else:
            print("Sorry say that again")
            

