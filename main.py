import time
time.sleep(5)
from google import genai

from datetime import datetime

import speech_recognition as sr      #kind of a typedef from C/c++ (now we dont have to write 'speechrecognition' for calling its methods--'sr' will be enough)
import webbrowser  #built in module
import pyttsx3
#import musicLibrary
import os
import requests

music = {
    "got" : "https://www.youtube.com/watch?v=TZE9gVF1QbA" ,     #game of thrones theme
    "friends" : "https://www.youtube.com/watch?v=s2TyVQGoCYo",  #friends theme
    "tahm" : "https://www.youtube.com/watch?v=bl5q4AIGGZQ",      #two and a half man theme
    "himym" : "https://www.youtube.com/watch?v=elZBsxX6SEs",     #how i met your mother theme 
    "pubg" : "https://www.youtube.com/watch?v=7asP7Xw9emQ&list=RDQMktE_DUfgId0&start_radio=1",   #pubg packground score
    "waka" : "https://www.youtube.com/watch?v=pRpeEdMmmQ0"  #wakawaka by shakira
}

news_api_key = "<ENTER YOUR API KEY>"
gemini_api_key = "<ENTER YOUR API KEY>"

#fetching current date and time
now = datetime.now()
# Format date and time
date_str = now.strftime("%d-%m-%y")      # dd-mm-yy
time_str = now.strftime("%H:%M:%S")      # hh:mm:ss (24-hour format)


engine1 = pyttsx3.init()           #initialized pyttsx module

def speak(text: str):
    engine1.say(text)
    engine1.runAndWait()


def aiprocess(command):
    client = genai.Client(api_key=gemini_api_key)
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=command + "(explain it in short)",
    )

    msg = response.text.replace("*"," ") #replacing all * with spaces
    print(msg)
    speak(msg)

def processcommand(command:str):

    if(command=="stop conversation" or command=="stop the chat" or command=="quit conversation" or command=="stop chatting" or command=="exit conversation"):
        pass
    else:
        speak(f".....providing answer to : {command}.... ")
    

    if "open google" in command.lower():
        webbrowser.open("https://www.google.com")
    elif "open facebook" in command.lower():
        webbrowser.open("https://www.facebook.com/")
    elif "open youtube" in command.lower():
        webbrowser.open("https://www.youtube.com/")
    elif "open spotify" in command.lower():
        webbrowser.open("https://open.spotify.com/")
    elif "open whatsapp" in command.lower():
        webbrowser.open("https://web.whatsapp.com/")
    elif "open github" in command.lower():
        webbrowser.open("https://github.com/")  
    elif "image" in command.lower():
        os.startfile("C:\\Users\\jayshree\\Desktop\\kki.jpeg")
    elif command.lower().startswith("play"):
        song = command.lower().split(" ")[1]    #example : play xyz song  --> [0]=play [1]=xyz [2]=song
        link = music.get(song)
        if  link!=None :
            webbrowser.open(link)
        else:
            speak(" can not find the song from the library! ")
    
    elif "your name" in command.lower():
        speak("My name is Jarvis.Your Ginie!")
    elif "your father" in command.lower():
        speak("I have only one family member and her name is jayshree")
    elif "your family" in command.lower():
        speak("I have only one family member and her name is jayshree")
            
    # elif "news" in command.lower():
    #     r=requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={news_api_key}")
    #     if r.status_code==200:
    #         #parse the json response
    #         data = r.json()

    #         #extract the articles
    #         articles = data.get('articles',[])

    #         #print the headlines
    #         for i in articles:
    #             speak(i['title'])
    
    elif "stop conversation" in command.lower():
        speak("...Bye User...This is Jarvis signing off...see you next time!...")
        exit(0)
    elif "stop the chat" in command.lower():
        speak("...Bye User...This is Jarvis signing off...see you next time!...")
        exit(0)
    elif "stop chatting" in command.lower():
        speak("...Bye User...This is Jarvis signing off...see you next time!...")
        exit(0)
    elif "quit conversation" in command.lower():
        speak("...Bye User...This is Jarvis signing off...see you next time!...")
        exit(0)
    elif "exit conversation" in command.lower():
        speak("...Bye User...This is Jarvis signing off...see you next time!...")
        exit(0)       
    else:
        #let Google gemini handle the request
        aiprocess(command)
        






if __name__ == "__main__" :
    print("Running from:", __file__)
    speak("....Initializing Jarvis ....")    
    r = sr.Recognizer()


    while True:
        # obtain audio from the microphone
        with sr.Microphone() as source:
            print("Listening wake word....")

            try:
                audio = r.listen(source,timeout=5,phrase_time_limit=5)
                print("Recognizing wake word...")
                word = r.recognize_google(audio)
                print(f"Recognized word : {word}")
                time.sleep(1)

                if(word.lower()=="jarvis"):
                    speak("....Hey User...")
                    speak("...How can i help you today?....")
                    speak(".........")
                    time.sleep(1)

                    while True:
                        try:
                            #listen for command
                            print("Listening commands....")
                            speak("...listening....")
                            audio = r.listen(source,timeout=10,phrase_time_limit=10)
                            print("Recognizing Command...")

                            command = r.recognize_google(audio)
                            print(f"command : {command}")
                            processcommand(command)
                            time.sleep(1)

                        except sr.UnknownValueError as e1:
                            print("C - did not understand a word!!")
                        except sr.RequestError as e2:
                            print(f"C - Error : {e2}")
                        except sr.WaitTimeoutError as e3:
                            print("C - Speech listening timeout")
                        except Exception as e4:
                            print("C - Exception occured!")

            except sr.UnknownValueError as e:
               print("did not understand a word!!")
            except sr.RequestError as e1:
                print(f"Error : {e1}")
            except sr.WaitTimeoutError as e2:
                print("Speech listening timeout")
            except Exception as e3:
                print("\aException occured!")