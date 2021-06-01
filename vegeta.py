import pyttsx3 as pt
import datetime 
import speech_recognition as sr
import wikipedia
import os
import webbrowser
import pywhatkit
# from googlesearch.googlesearch import GoogleSearch

chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
webbrowser.get(chrome_path).open('http://docs.python.org/')


engine=pt.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)
# print(voices[1].id)

def speak(string):
    engine.say(string)
    engine.runAndWait()
    
def input():
    s=sr.Recognizer()
    with sr.Microphone() as source:
        print('LISTENING...')
        s.pause_threshold=0.8
        s.energy_threshold=250
        string=s.listen(source)
        
    try:
        print('.......')
        query=s.recognize_google(string, language='en-in')
        print(query)
    except Exception as e:
        print(e)
        print('SAY THAT AGAIN PLEASE')
        return 'NONE'
    return query
    
    
    
def intro():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        print('GOOD MORNING! I am VEGETA, HOW MAY I HELP YOU?')
        speak('GOOD MORNING! I am VEGETA, HOW MAY I HELP YOU?')
    if hour>=12 and hour<16:
        print('GOOD AFTERNOON! I am VEGETA, HOW MAY I HELP YOU?')
        speak('GOOD AFTERNOON! I am VEGETA, HOW MAY I HELP YOU?')
    if hour>=16:
        print('GOOD EVENING! I am VEGETA, HOW MAY I HELP YOU?')
        speak('GOOD EVENING! I am VEGETA, HOW MAY I HELP YOU?')
        
    
    
if __name__ == '__main__':
    # string=input('WHAT YOU WANT ME TO SAY?')
    # speak(string)
    intro()
    # list=['spotify','notepad',]
    # input()
    while True:
        audio=input().lower()
        if audio=="who made you" :
            print('MANMEET is my developer!')
            speak('MANMEET is my developer!')
            
        elif audio=='who are you':
            print('I am VEGETA')
            speak('I am VEGETA')
            
        elif audio=='shut up':
            print('OKAY! BYE, HAVE A GREAT DAY')
            speak('OKAY! BYE, HAVE A GREAT DAY')
            exit()
            
        elif any(x in audio for x in['wikipedia','search for on wikepedia','who is'])  :
            print('SEARCHING.....')
            speak('SEARCHING.....')
            audio=audio.replace('wikipedia','')
            audio=audio.replace('search for','')
            audio=audio.replace('on','')
            audio=audio.replace('who','')
            audio=audio.replace('is','')
            
            print(audio)
            print(wikipedia.summary(audio))
            speak(wikipedia.summary(audio, sentences=1))
            
        elif any(x in audio for x in["open"]):
            audio=audio.replace('open','')
            
            print(f'opening {audio}.....')
            speak(f'opening {audio}.....')
            if  any(x in audio for x in['spotify','notepad']):
                os.system(audio)
            else:
                url="https://www.{}.com".format(audio)
                webbrowser.open(url.replace(" ",""))
            
        # elif 'open' in audio:
        #     chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        #     webbrowser.get(chrome_path).open('http://docs.python.org/')
        #     print('opening.....')
        #     speak('opening....')
        #     audio=audio.replace('open','')
        #     print(audio)
        #     url="https://www.{}.com".format(audio)
        #     webbrowser.open(url.replace(" ",""))
            
        elif 'search for' in audio:
            audio=audio.replace('search','')
            audio=audio.replace('for','')
            webbrowser.open(f'https://www.google.com/search?q={audio}')
            
        elif 'weather' in audio:
                audio=audio.replace('weather','')
                audio=audio.replace('what','')
                audio=audio.replace('is','')
                audio=audio.replace('the','')
                audio=audio.replace('in','')
                audio=audio.replace('forecast','')
                webbrowser.open(f'https://www.google.com/search?q={audio}weather')
                
        elif "what's the time" in audio:
            now=datetime.datetime.now().time()
            time = now.strftime("%H:%M:%S")
            print(time)
            speak(time)
        elif "what's the date" in audio:
            now=datetime.date.today()
            d2 = now.strftime("%B %d, %Y")
            print(d2)
            speak(d2)
            
        elif any(x in audio for x in['send','text','message']):
            audio=audio.replace('send','')
            audio=audio.replace('text','')
            audio=audio.replace('message','')
            audio=audio.replace('a','')
            audio=audio.replace('to','')
            print("Tell me the number")
            speak("Tell me the number")
            number=input()
            nmb=f'+91{number}'
            nmb=nmb.replace(' ','')
            print("What's your message?")
            speak("What's your message?")
            info=input()
            hour=int(datetime.datetime.now().hour)
            min=int(datetime.datetime.now().minute)
            sec=int(datetime.datetime.now().second)
            if sec>45:
                min=min+2
            else:
                min=min+1
            pywhatkit.sendwhatmsg(nmb, info, hour, min,10)
            print('sending....')
            speak('sending....') 
        # elif any(x in audio for x in['email']):
        #     pywhatkit.join_discord()
        
            # pywhatkit.send_mail("meetkohli@gmail.com", "Meet@1049", "Test Mail", "This is a test email", "manmeetkohli1049@gmail.com")
        else:
            print('coudnt recognize!')
            speak('coudnt recognize!')
            
            
        