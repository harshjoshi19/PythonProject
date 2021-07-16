import pyttsx3 
import  speech_recognition as sr 
import datetime
import webbrowser as web
import os
# import pyaudio
import wikipedia


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.setProperty('rate',185)


def Speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    #It takes microphone from the user ande return string as output
    r = sr.Recognizer()
   
    with sr.Microphone() as source:
        print("Say Something........")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:    
        text = r.recognize_google(audio,language='en-in')
        print("User said :{query}\n")
        return text
    except Exception as e:
        print("Harsh Sir, Learning new things from you when sir you add this function on me Then it work!!!Thank you ")
        return "None"
    return query    
   
def wish():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour<12:
         Speak("Good Morning Sir!")
    elif hour >= 12 and hour <18:
        Speak("Good Afternoon Sir!")
    else:
        Speak("Good Evening Sir!!! ")
    Speak("Please Tell me How may I help You !!! ")    


if __name__ == "__main__":
    wish()
while True:
    
        query = takeCommand().lower()
        if 'wikipedia' in query:
            Speak('Searching Wikipedia....')
            query = query.replace('wikipedia',"")
            result = wikipedia.summary(query,sentences=1)
            Speak("According to wikipedia")
            print(result)
            Speak(result)

        elif "hello Dell" in query:
            Speak("Hello Sir. How are You")
        elif "hey Keera" in query:
            Speak("Hello Sir. How are You") 
        elif "hey Bayby" in query:
            Speak("Hello Sir. How are You") 
        elif "hey jon" in query:
            Speak("Hello Sir. How are You")            
        elif "Open Youtube" in query:
            web.open("www.youtube.com")
        elif "Open Facebook" in query:
            web.open("www.facebook.com")
        # else:
        #     Speak("Harsh Sir, i am Learning new things from you when sir you add this function on me Then it work!!!Thank you ")

   
