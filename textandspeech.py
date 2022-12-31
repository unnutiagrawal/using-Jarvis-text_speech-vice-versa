import speech_recognition as sr
import pyttsx3 as p
r= sr.Recognizer()
engine=p.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

rate = engine.getProperty('rate')   # getting details of current speaking rate
print (rate)                        #printing current voice rate
engine.setProperty('rate', 150)

volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
print (volume)                          #printing current volume level
engine.setProperty('volume',1.0)



engine.say("ae mota bhai!! kem cho?")
engine.runAndWait()

with sr.Microphone() as source:
    text = r.listen(source)
    print(text)

    try:

        recognised_text= r.recognize_google(text)
        print(recognised_text)
    except sr.UnknownValueError:
        print("")
    except sr.RequestError as e:
        print("")
    engine.say("kaise ho mota bhai? how ya doin'")
    engine.runAndWait()
    text1 = r.listen(source)

    try:
        recognised_text1 = r.recognize_google(text1)
        print(recognised_text1)
    except sr.UnknownValueError:
        print("")
    except sr.RequestError as e:
        print("")




