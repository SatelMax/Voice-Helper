from gtts import gTTS
import random
import time
from playsound import playsound
import speech_recognition as sr
import pyautogui
import webbrowser
import winsound
import datetime

def listen_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something")
        audio = r.listen(source)

    try:
        our_speech = r.recognize_google(audio)
        print("You said: "+our_speech)
        return our_speech
    except sr.UnknownValueError:
        return "error"
    except sr.RequestError as e:
        return "error"

    # return input("Tell me what do you need: ")

def exec_my_command(message):
    message = message.lower()
    if "hello" in message:
        say_message("Good day, Sergey")
    elif "make a screenshot" in message:
        pyautogui.screenshot("screenshot.png")
        say_message("Screenshot is here")
    elif "open youtube" in message:
        say_message("Opening YouTube.")
        webbrowser.open("http://www.youtube.com")
    elif "what is the time" in message:
        current_time=datetime.datetime.now().strftime("%H:%M:%S")
        say_message(current_time)
    elif "bye" in message:
        say_message("Have a nice day, Sergey")
        exit()
    else:
        say_message("Command is undefined")

def say_message(message):
    voice = gTTS(message, lang="en")
    file_voice_name = "_audio_"+str(time.time())+"_"+str(random.randint(0, 100000))+".mp3"
    voice.save(file_voice_name)
    playsound(file_voice_name)
    print(message)


if __name__ == '__main__':
    while True:
        command = listen_command()
        exec_my_command(command)


