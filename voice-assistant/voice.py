import pyttsx3
import datetime
import speech_recognition as sr

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[39].id)



def speak(audio):
    
    engine.say(audio)
    engine.runAndWait()

def takeCommandFromUser():

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening.....")
        r.adjust_for_ambient_noise(source,duration=1)
        r.pause_threshold = 1
        #r.record(source,duration=2)
        audio = r.listen(source)
        print("done")
    
    try:
        print("Recognizing.....")
        query = r.recognize_google(audio, language = 'en-in', show_all=False)
        print(f"User said: {query}\n")

    except Exception:
        #print (exp)
        print("Say that again please......")
        return "None"

    return (query)

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
    takeCommandFromUser()
