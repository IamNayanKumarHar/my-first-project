import pyttsx3
import speech_recognition as sr
import pyaudio
import webbrowser

# url library 

youtube = "https://www.youtube.com"
google = "https://www.google.com"
spotify = "https://www.spotify.com"
gmail = "https://www.gmail.com"
flipkart = "https://www.flipkart.com"

def play_on_youtube(command):
    sorted = command.split(" ")
    return 



def speak(speech):
    # Initialize the pyttsx3 engine
    engine = pyttsx3.init()

    # # Set properties before adding anything to say
    engine.setProperty('rate', 150)    # Speed of speech
    engine.setProperty('volume', 1.0)  # Volume level (0.0 to 1.0)
    engine.say(speech)
    # # Blocks while processing all the currently queued commands
    engine.runAndWait()

    
while True:

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Please say something")
        audio = r.listen(source)

        # modified
    
        

    print("Recognizing...")
    # recognize speech using Google Speech Recognition
    try:
        wake = r.recognize_google(audio)
        print(wake)
        if "jarvis" in wake.lower():
            speak("Yes how may i help you?")

            with sr.Microphone() as source:
                audio = r.listen(source)
                instructions = r.recognize_google(audio)

                if instructions.lower() == "youtube" or instructions.lower() == "open youtube" :
                    webbrowser.open(youtube)
                elif "google" in instructions.lower():
                    webbrowser.open(google)
                elif "spotify" in instructions.lower():
                    webbrowser.open(spotify)
                elif "gmail" in instructions.lower():
                    webbrowser.open(gmail)
                elif "flipkart" in instructions.lower():
                    webbrowser.open(flipkart)
                elif "on youtube" in instructions.lower():
                    webbrowser.open(f"https://www.youtube.com/results?search_query={instructions}")
                else:
                    webbrowser.open(f"https://www.google.co.in/search?query={instructions}")



        
        
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))









    