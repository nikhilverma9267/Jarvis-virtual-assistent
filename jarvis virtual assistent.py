import speech_recognition as sr
import webbrowser
import pyttsx3

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak (text):
    engine.say(text)
    engine.runAndWait()
def processCommand(c):
   if "open google" in c.lower():
      webbrowser.open("https://google.com")
   elif  "open youtube" in c.lower():
      webbrowser.open("https://youtube.com") 
   elif  "open instagram" in c.lower():
      webbrowser.open("https://instagram.com")
   elif  "play hanuman song" in c.lower():
      webbrowser.open("https://www.youtube.com/watch?v=U3Z8gMZPJX8&list=RDU3Z8gMZPJX8&start_radio=1") 
   elif  "play mareeze isq" in c.lower():
      webbrowser.open("https://www.youtube.com/watch?v=WxEmaBaLHVk&list=RDWxEmaBaLHVk&start_radio=1")    



if __name__=="__main__":
    speak("initialising your setup ........")
    while True :
        #listening for the wake word "hey nikhil"
        # obtain audio from microphone
        r = sr.Recognizer()
       
   
        print("recognizing")
        # recognize speech using Sphinx
        try:
           with sr.Microphone() as source:
              print("listening .....!")
              audio = r.listen(source, timeout=8, phrase_time_limit=1)
           word = r.recognize_google(audio)
           if(word.lower() == "jarvis"):
              speak("ha bolo")
              #listen for commond
              with sr.Microphone() as source:
                 print("nikhil active .....!")
                 audio = r.listen(source)
                 command = r.recognize_google(audio)

                 processCommand(command)


                
                 

                 

    
        except Exception as e:
          print("Error;{0}".format(e))
       
