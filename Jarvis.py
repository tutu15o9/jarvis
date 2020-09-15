import pyttsx3
import datetime
import calendar
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb
import os
import pyautogui
import psutil
import pyjokes
import requests
engine = pyttsx3.init()

ownerName = "Rahul"
sendermail = "rahultuteja1509@gmail.com"
password = "Tutu@1410"
chromePath = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
songsDir = "E:\\songs"
data = ""


# https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def time():
    speak("the current Time is")
    t = datetime.datetime.now().strftime("%H:%M:%S")
    speak(t)
    return t


def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    day = int(datetime.datetime.now().day)
    speak("the current Date is")
    speak(year)
    speak(month)
    speak(day)


def greet():
    speak("Welcome back sir")
    hour = int(datetime.datetime.now().hour)
    print(hour)
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    Time = datetime.datetime.now().strftime("%H:%M:%S")
    print(Time)
    print(date)
    print(calendar.month_name[month])
    print(year)
    speak("the current Time is")
    speak(Time)
    speak("the current Date is")
    speak(str(date) + calendar.month_name[month] + str(year))
    if 6 <= hour < 12:
        speak("Good Morning {}".format(ownerName))

    elif 12 <= hour < 18:
        speak("Good Afternoon {}!".format(ownerName))

    elif 18 <= hour < 24:
        speak("Good Evening {}!".format(ownerName))

    else:
        speak("Good Night {}!".format(ownerName))

    speak("Jarvis at your Service. Please tell me how can I help You ")


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    server.login(sendermail, password)
    server.sendmail(sendermail, to, content)
    server.close()


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        # audio = r.adjust_for_ambient_noise(source)
        audio = r.listen(source, phrase_time_limit=10)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print("{} Said:{}\n".format(ownerName, query))
        # speak("{} Said:{}\n".format(ownerName, query))

    except Exception as e:
        print(e)
        print("Say that again Please...")
        speak("Say that again Please...")
        return "None"
    return query


def screenShot():
    img = pyautogui.screenshot()
    img.save("./ss.png")


def cpu():
    speak("Cpu is at {} percent usage".format(psutil.cpu_percent()))
    speak("Battery is at {}percent.".format(psutil.sensors_battery().percent))


def jokes():
    speak(pyjokes.get_joke())


if __name__ == "__main__":
    # greet()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'email to harry' and 'send email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                speak(content)
                to = sendermail
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend . I am not able to send this email")
        elif 'logout' in query or 'log out' in query:
            os.system("shutdown -l")
        elif 'shutdown' in query:
            os.system("shutdown /s /t 1")
        elif 'restart' in query:
            os.system("shutdown /r /t 1")
        elif 'search in chrome' in query:
            speak("what should i search?")

            r = sr.Recognizer()

            with sr.Microphone() as source:
                print('say something!')
                audio = r.listen(source, phrase_time_limit=5)
                print("done")
            try:
                text = r.recognize_google(audio)
                print('google think you said:\n' + text + '.com')
                wb.get(chromePath).open(text + '.com')
            except Exception as e:
                print(e)
        elif "play songs" in query:
            songs = os.listdir(songsDir)
            print(songs)
            os.startfile(os.path.join(songsDir, songs[0]))
        elif "remember that" in query:
            speak("What should i remember?")

            data = takeCommand()
            speak("you said" + data)
            remember = open('data.txt', 'w')
            remember.write(data)
            remember.close()
        elif "do you know anything" in query:
            remember = open('data.txt', 'r')
            speak("I remeber" + remember.read())
        elif 'take a screenshot' in query:
            screenShot()
            speak("screenshot taken.")
        elif "cpu" in query or 'c p u' in query:
            cpu()
        elif "tell" in query and "joke" in query:
            jokes()
        elif "time" in query:
            time()
        elif "date" in query:
            date()
        elif "close" in query:
            speak("Bye bye {}".format(ownerName))
            quit()
