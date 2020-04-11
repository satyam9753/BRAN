import pyttsx3
import datetime
import speech_recognition as s

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[39].id)



def speak(audio):
    
    engine.say(audio)
    engine.runAndWait()

def takeCommandFromUser():

    r = s.Recognizer()

    with s.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("Recognizing.....")
        query = r.recognize_google(audio, language = 'en-in')
        print(f"User said: {query}\n")

    except Exception as exp:
        print("Say that again please......")
        return "None"

def greet():
    
    hour = int(datetime.datetime.now().hour)
    if (hour >= 0 and hour < 12):
        speak("Good Morning Sir!")   
    elif (hour >= 12 and hour <= 17):
        speak("Good Afternoon Sir!")    
    else:
        speak("Good Evening Sir!")
    
    speak("Hi! I'm GOHAN... How may I help you today?")

     

if __name__ == "__main__" :
    greet()
