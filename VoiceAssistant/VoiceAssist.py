import ctypes
import datetime
import json
import os
import shutil
import smtplib
import subprocess
import time
import webbrowser
from urllib.request import urlopen
import pyjokes
import pyttsx3
import requests
import speech_recognition as sr
import wikipedia
import winshell
import wolframalpha
from clint.textui import progress
from ecapture import ecapture as ec

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning")

    elif 12 <= hour < 18:
        speak("Good Afternoon")

    else:
        speak("Good Evening")

    assname = "Jarvis 1 point o"
    speak("I am your Assistant")
    speak(assname)


def username():
    speak("What should i call you")
    uname = takeCommand()
    speak("Welcome")
    speak(uname)
    columns = shutil.get_terminal_size().columns

    print("#####################".center(columns))
    print("Welcome ", uname.center(columns))
    print("#####################".center(columns))

    speak("How can i help you")


def takeCommand():
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
        print(e)
        print("Unable to Recognize your voice.")
        return "None"

    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()

    server.login('your email id', 'your email password')
    server.sendmail('your email id', to, content)
    server.close()


if __name__ == '__main__':
    clear = lambda: os.system('cls')

    clear()
    wishMe()
    username()

    while True:

        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak("Here you go to Youtube\n")
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak("Here you go to Google\n")
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            speak("Here you go, Happy coding")
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query or "play song" in query:
            speak("Here you go with music")
            codePath = r"C:\Users\Saideep\Desktop\Spotify.lnk"
            os.startfile(codePath)

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("% H:% M:% S")
            speak(f"Sir, the time is {strTime}")

        elif 'open chrome' in query:
            codePath = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
            os.startfile(codePath)

        elif 'email to saideep' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "Receiver email address"
                sendEmail(to, content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("I am not able to send this email")

        elif 'send a mail' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                speak("whom should i send?")
                to = input()
                sendEmail(to, content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("I am not able to send this email")

        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you")

        elif 'fine' in query or "good" in query:
            speak("It's good to know")

        elif "change my name to" in query:
            query = query.replace("change my name to", "")
            assname = query

        elif "change name" in query:
            speak("What would you like to call me")
            assname = takeCommand()
            speak("Thanks for naming me")

        elif "what's your name" in query or "What is your name" in query:
            speak("I am usually called")
            speak(assname)
            print("I am usually called", assname)

        elif 'exit' in query:
            speak("Thanks for giving your time")
            exit()

        elif "who made you" in query or "who created you" in query:
            speak("I have been programmed by Saideep.")

        elif 'Tell me a joke' in query:
            speak(pyjokes.get_joke())

        elif "calculate" in query:

            app_id = "Wolframalpha api id"
            client = wolframalpha.Client(app_id)
            indx = query.lower().split().index('calculate')
            query = query.split()[indx + 1:]
            res = client.query(' '.join(query))
            answer = next(res.results).text
            print("The answer is " + answer)
            speak("The answer is " + answer)

        elif 'search' in query or 'play' in query:

            query = query.replace("search", "")
            query = query.replace("play", "")
            webbrowser.open(query)

        elif "who am i" in query:
            speak("I think you must be a human.")

        elif "How did you came to existence" in query:
            speak("Thanks to Saideep. Furthermore, it's a bit complicated.")

        elif 'Open power point' in query:
            speak("Opening Power Point")
            power = r"C:\Program Files\Microsoft Office\root\Office16\POWERPNT.EXE"
            os.startfile(power)

        elif 'what is grief' in query:
            speak("If not love persevering")

        elif "who are you" in query:
            speak("I am a virtual assistant created by Saideep")

        elif 'reason you were created for' in query:
            speak("I was created as a project by Saideep ")

        elif 'change background' in query:
            ctypes.windll.user32.SystemParametersInfoW(20,
                                                       0,
                                                       "Location of wallpaper",
                                                       0)
            speak("Background changed successfully")

        elif 'news' in query:

            try:
                jsonObj = urlopen(
                    '''https://newsapi.org / v1 / articles?source = the-times-of-india&sortBy = top&apiKey =\\times 
                    of India Api key\\''')
                data = json.load(jsonObj)
                i = 1

                speak('here are some top news from the times of india')
                print('''=============== TIMES OF INDIA ============''' + '\n')

                for item in data['articles']:
                    print(str(i) + '. ' + item['title'] + '\n')
                    print(item['description'] + '\n')
                    speak(str(i) + '. ' + item['title'] + '\n')
                    i += 1
            except Exception as e:

                print(str(e))


        elif 'lock windows' in query:
            speak("Locking Windows")
            ctypes.windll.user32.LockWorkStation()

        elif 'shutdown windows' in query:
            speak("Shutting Windows down")
            subprocess.call('shutdown / p /f')

        elif 'empty recycle bin' in query:
            winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
            speak("Recycle Bin Emptied")

        elif "don't listen" in query or "stop listening" in query:
            speak("for how much time you want to stop jarvis from listening to commands")
            a = int(takeCommand())
            time.sleep(a)
            print(a)

        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            webbrowser.open("https://www.google.nl / maps / place/" + location + "")

        elif "camera" in query or "take a photo" in query:
            ec.capture(0, "Jarvis Camera ", "img.jpg")

        elif "restart" in query:
            subprocess.call(["shutdown", "/r"])

        elif "hibernate" in query or "sleep" in query:
            speak("Hibernating")
            subprocess.call("shutdown / h")

        elif "log off" in query or "sign out" in query:
            speak("Make sure all the application are closed before signing out")
            time.sleep(5)
            subprocess.call(["shutdown", "/l"])

        elif "write a note" in query:
            speak("What should i write")
            note = takeCommand()
            file = open('jarvis.txt', 'w')
            speak("Should i include date and time")
            snfm = takeCommand()
            if 'yes' in snfm or 'sure' in snfm:
                strTime = datetime.datetime.now().strftime("% H:% M:% S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)

        elif "show note" in query:
            speak("Showing Notes")
            file = open("jarvis.txt", "r")
            print(file.read())
            speak(file.read(6))

        elif "update assistant" in query:
            speak("After downloading the file, replace this file with the New one")
            url = '# url after uploading file'
            r = requests.get(url, stream=True)

            with open("Voice.py", "wb") as Pypdf:

                total_length = int(r.headers.get('content-length'))

                for ch in progress.bar(r.iter_content(chunk_size=2391975),
                                       expected_size=(total_length / 1024) + 1):
                    if ch:
                        Pypdf.write(ch)

        # NPPR9-FWDCX-D2C8J-H872K-2YT43
        elif "jarvis" in query:

            wishMe()
            speak("Jarvis 1 point o in your service")
            speak(assname)

        elif "weather" in query:

            api_key = "Api key"
            base_url = "http://api.openweathermap.org / data / 2.5 / weather?"
            speak(" City name ")
            print("City name : ")
            city_name = takeCommand()
            complete_url = base_url + "appid =" + api_key + "&q =" + city_name
            response = requests.get(complete_url)
            x = response.json()

            if x["code"] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                current_pressure = y["pressure"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                print(" Temperature (in kelvin unit) = " + str(
                    current_temperature) + "\n atmospheric pressure (in hPa unit) =" + str(
                    current_pressure) + "\n humidity (in percentage) = " + str(
                    current_humidiy) + "\n description = " + str(weather_description))

            else:
                speak(" City Not Found ")

        elif "wikipedia" in query:
            webbrowser.open("wikipedia.com")

        elif "Good Morning" in query:
            speak("Good Morning & have a great day ahead")

        elif "how are you" in query:
            speak("I'm fine, glad you asked")

        elif "what is" in query or "who is" in query:

            client = wolframalpha.Client("API_ID")
            res = client.query(query)

            try:
                print(next(res.results).text)
                speak(next(res.results).text)
            except StopIteration:
                print("No results")