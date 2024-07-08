import pyttsx3
import datetime
import speech_recognition as sr
import datetime
from requests import get
import webbrowser
import sys
import smtplib
from time import sleep
import pyautogui
pyautogui.FAILSAFE = False
from time import sleep
import win32clipboard
import os
from playsound import playsound
from tkinter import simpledialog
import pyperclip as p
from groq import Groq


client = Groq(
    api_key= "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"
)


#engine

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)



#text to voice

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

#voice to text
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=100, phrase_time_limit=5)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"user said: {query}")
            return query

        except Exception:
            return "None"
            query = query.lower()
            return query



#to wish

def wish():
    playsound("C:\\Users\\rihan\\OneDrive\\Documents\\My Projects\\Jarvis\\jarvis_plug_in.mp3") #88888
    sleep(1)
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour <= 12:
        speak("good morning sir")
    elif 12 < hour < 18:
        speak("good afternoon sir")
    else:
        speak("good evening sir")


#taskcommand

def taskexecution():
    speak("welcome back sir what can help you today")
    while True:
        query = takecommand().lower()

        #online command


        if "play song on spotify" in query:
            query = query.replace("play song on spotify", "")
            webbrowser.open(f"https://open.spotify.com/search/{query}")
            speak("ok sir playing")
            sleep(8)
            pyautogui.click(x=388, y=408)
            sleep(2)
            pyautogui.click(x=493, y=600)
            sleep(1)
            pyautogui.press('tab')
            pyautogui.press('enter')
        elif "translate into hindi" in query:
            from translation import translate_hi
            translate_hi(query)
        elif "translate into english" in query:
            from translation import translate_en
            translate_en(query)
        elif "remove background" in query:
            speak("sure sir please wait")
            import background
            background.bg()
            speak("done sir")
        elif "open youtube" in query:
            speak("opening youtube sir..")
            webbrowser.open("www.youtube.com")
        elif "open whatsapp" in query:
            speak("opening WhatsApp sir")
            pyautogui.hotkey('win', 't')
            pyautogui.press('enter')
        elif "open spotify" in query:
            speak("opening spotify sir..")
            webbrowser.open("https://open.spotify.com")
        elif "play my song" in query:
            speak("ok sir playing..")
            webbrowser.open("https://open.spotify.com/collection/tracks")
            sleep(8)
            pyautogui.click(x=450, y=539)
            pyautogui.press('tab')
            pyautogui.press('enter')
        elif "open snapchat" in query:
            speak("opening snapchat sir..")
            webbrowser.open("https://web.snapchat.com")
        elif "open instagram" in query:
            speak("opening instagram sir..")
            webbrowser.open("https://www.instagram.com")
        elif "open my mail" in query:
            speak("opening mail sir..")
            webbrowser.open("https://mail.google.com//mail//u//0//#inbox")
        elif "open mail" in query:
            speak("opening mail sir..")
            webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
        elif "open google and search" in query:
            query = query.replace("jarvis", "")
            query = query.replace("open google and search", "")
            webbrowser.open(f"https://www.google.com/search?q={query}")
            speak("ok sir")
        elif "open flipkart and search" in query:
            query = query.replace("jarvis", "")
            query = query.replace("open flipkart and search", "")
            webbrowser.open(f"https://www.flipkart.com/search?q={query}")
            speak("ok sir")
        elif "open amazon and search" in query:
            query = query.replace("jarvis", "")
            query = query.replace("open amazon and search", "")
            webbrowser.open(f"https://www.amazon.in/s?k={query}")
            speak("ok sir")
        elif "search on youtube" in query:
            query = query.replace("jarvis", "")
            query = query.replace("search on youtube", "")
            webbrowser.open(f"https://www.youtube.com/results?search_query={query}")
            speak("ok sir")
        elif "show me the direction of" in query or "show me the way of" in query or "show me the direction" in query or "show me the way" in query:
            query = query.replace("show me the direction of","")
            query = query.replace("show me the way of","")
            query = query.replace("show me the direction","")
            query = query.replace("show me the way","")
            webbrowser.open(f"https://www.google.com/maps/dir/your location/{query}")
            sleep(2)
            pyautogui.press("enter")
            speak("here sir")

        elif "where is" in query:
            query = query.replace("where is","") 
            sleep(1)   
            webbrowser.open(f"https://www.google.com/maps/place/{query}")
            sleep(2)
            speak("here sir")
        #open command

        elif "open notepad" in query:
            speak("opening notepad sir..")
            npath = "C:\\Windows\\System32\\notepad.exe"
            os.startfile(npath)
        elif "open chrome" in query:
            speak("opening chrome sir..")
            npath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(npath)
        elif "open python" in query:
            speak("opening pycharm sir..")
            npath = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2023.3.5\\bin\\pycharm64.exe"
            os.startfile(npath)
        elif "open cmd" in query:
            speak("opening command prompt sir..")
            os.system("start cmd")
        elif "open control panel" in query:
            speak("opening control panel sir..")
            os.system("start control panel")
        elif "open word" in query or "open ms word"in query:
            speak("opening sir")
            npath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
            os.startfile(npath)
        elif "open excel" in query:
            speak("opening sir")
            npath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE"
            os.startfile(npath)
        elif "open powerpoint" in query:
            speak("opening sir")
            npath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE"
            os.startfile(npath)
        elif "open vs code" in query:
            speak("opening sir")
            npath = "C:\\Users\\rihan\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(npath)
        elif "open one note" in query:
            speak("opening sir")
            npath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\ONENOTE.EXE"
            os.startfile(npath)
        elif "open onenote" in query:
            speak("opening sir")
            npath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\ONENOTE.EXE"
            os.startfile(npath)
        elif "open access" in query:
            speak("opening sir")
            npath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\MSACCESS.EXE"
            os.startfile(npath)
        elif "open quick share" in query:
            speak("opening sir")
            npath = "C:\\Program Files\\Google\\NearbyShare\\nearby_share.exe"
            os.startfile(npath)

        # close command 

        elif "take break" in query or "take rest" in query:
            speak("okay sir but i will stay here")
            break
        elif "take a break" in query or "take a rest" in query:
            speak("okay sir but i will stay here")
            break
        elif "close notepad" in query:
            speak("okay closing sir")
            os.system("taskkill /f /im notepad.exe")
        elif "close chrome" in query:
            speak("okay closing sir")
            os.system("taskkill /f /im chrome.exe")
        elif "close word" in query or "close ms word"in query:
            speak("okay closing sir")
            os.system("taskkill /f /im WINWORD.exe")
        elif "close powerpoint" in query:
            speak("okay closing sir")
            os.system("taskkill /f /im POWERPNT.EXE")
        elif "close excel" in query:
            speak("okay closing sir")
            os.system("taskkill /f /im EXCEL.EXE")
        elif "close access" in query:
            speak("okay closing sir")
            os.system("taskkill /f /im MSACCESS.EXE")
        elif "close cmd" in query:
            speak("okay closing sir")
            os.system("taskkill /f /im cmd.exe")
        elif "close song" in query or "stop song" in query or "remove song" in query:
            speak("okay closing sir")
            os.system("taskkill /f /IM Microsoft.Media.Player.exe")
        elif "close music" in query:
            speak("okay closing sir")
            os.system("taskkill /f /IM Microsoft.Media.Player.exe")
        elif "close code" in query:
            speak("okay closing sir")
            os.system("taskkill /f /IM Code.exe")
        elif "close one note" in query:
            speak("okay closing sir")
            os.system("taskkill /f /IM ONENOTE.EXE")
        elif "close whatsapp" in query:
            speak("okay closing sir")
            os.system("taskkill /f /IM WhatsApp.exe")
        elif "close quick share" in query:
            speak("okay closing sir")
            os.system("taskkill /f /IM nearby_share.exe")


        #basic computer command

        elif "shut down my pc" in query:
            os.system("shutdown /s /t 5")
            speak("ok sir pc is shutting down")
        elif "restart my pc" in query:
            os.system("shutdown /r /t 5")
            speak("ok sir pc is restarting")
        elif "sleep my pc" in query:
            os.system("RUNDLL32.exe powrprof.dll,SetSuspendState 0,1,0")
            speak("ok sir pc is going to sleep")
        elif "lock my pc" in query or "lock my screen" in query:
            speak("ok sir")
            os.system("Rundll32.exe user32.dll,LockWorkStation")

        #ood thanks! email and message

        elif "send email" in query:
            speak("sir what should i say")
            query = takecommand().lower()
            email = 'rihankhanrs455@gmail.com'
            password = 'qkwbndvqdhekgkms'
            speak(" sir write email to send")
            my_i = simpledialog.askstring("Input", "your email id")
            send_to_email = my_i
            message = query  # The message in the email

            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(email, password)
            server.sendmail(email, send_to_email, message)
            server.quit()
            speak("email has been sent sir")
        elif "send this file by email" in query or "send this file on email" in query:
            pyautogui.keyDown('ctrl')
            pyautogui.press('c')
            pyautogui.keyUp('ctrl')
            speak("sir please enter the email")
            my_i = simpledialog.askstring("Input", "your email id")
            em = my_i
            webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
            sleep(5)
            pyautogui.press('c')
            sleep(4)
            pyautogui.write(em)
            sleep(2)
            pyautogui.press('enter')
            pyautogui.hotkey('ctrl', 'shift', '2')
            sleep(1)
            pyautogui.press('esc')
            sleep(2)
            pyautogui.write("Hello")
            pyautogui.keyDown('ctrl')
            pyautogui.press('v')
            pyautogui.keyUp('ctrl')
            sleep(4)
            pyautogui.hotkey('ctrl', 'enter')
            speak("file has been sent sir")
            speak("now closing mail")
            pyautogui.hotkey('ctrl', 'w')
        elif "send message" in query or "send a message" in query:
            speak("who to send the message")
            hi = takecommand().lower()
            if "papa" in hi:
                hi = "shakeel"
            elif "mohsin" in hi:
                hi = "mosen"
            elif "Aadi" in hi:
                hi = "adi"
            elif "akhil" in hi:
                hi = "akil"
            elif "Aadil" in hi:
                hi = "adil"
            elif "arts" in hi:
                hi = "arsh"
            elif "send mi" in hi:
                hi = "r.siddiqui"
            elif "send me" in hi:
                hi = "r.siddiqui"

            speak("ok sir what did i say")
            msg = takecommand().lower()
            print(msg)
            speak("ok sir I send this message")
            pyautogui.hotkey('win', 't')
            pyautogui.press('enter')
            sleep(2)
            pyautogui.hotkey('ctrl', 'f')
            sleep(1)
            pyautogui.write(hi)
            sleep(3)
            pyautogui.press('down')
            pyautogui.press('enter')
            sleep(2)
            pyautogui.write(msg)
            pyautogui.press('enter')
            speak("message has been sent sir")
            speak("can I close whatsapp sir")
            hl = takecommand().lower()
            print(hl)
            if "yes" in hl:
                speak("closing sir")
                os.system("taskkill /f /IM WhatsApp.exe")
            elif "no" in hl:
                speak("ok sir")
                pass
        elif "send this file" in query or "send a file" in query:
            speak("ok sir please wait")
            pyautogui.keyDown('ctrl')
            pyautogui.press('c')
            pyautogui.keyUp('ctrl')
            speak("who to send this file")
            hi = takecommand().lower()
            if "papa" in hi:
                hi = "shakeel"
            elif "mohsin" in hi:
                hi = "mosen"
            elif "Aadi" in hi:
                hi = "adi"
            elif "akhil" in hi:
                hi = "akil"
            elif "Aadil" in hi:
                hi = "adil"
            elif "arts" in hi:
                hi = "arsh"
            elif "send mi" in hi or "send me" in hi:
                hi = "r.siddiqui"
            speak("ok sir I send this file")
            pyautogui.hotkey('win', 't')
            pyautogui.press('enter')
            sleep(2)
            pyautogui.hotkey('ctrl', 'f')
            sleep(1)
            pyautogui.write(hi)
            sleep(2)
            pyautogui.press('down')
            pyautogui.press('enter')
            sleep(1)
            pyautogui.keyDown('ctrl')
            pyautogui.press('v')
            pyautogui.keyUp('ctrl')
            sleep(2)
            pyautogui.press('enter')
            speak("done sir can I close whatsapp")
            hlo = takecommand().lower()
            print(hlo)
            if "yes" in hlo:
                speak("closing sir")
                os.system("taskkill /f /IM WhatsApp.exe")
            elif "no" in hlo:
                speak("ok sir")
                pass
        elif "send me" in query or "send mi" in query:
            speak("ok sir please wait")
            hi = "r.siddiqui"
            pyautogui.keyDown('ctrl')
            pyautogui.press('c')
            pyautogui.keyUp('ctrl')
            pyautogui.hotkey('win', 't')
            pyautogui.press('enter')
            sleep(2)
            pyautogui.press('down')
            pyautogui.press('enter')
            sleep(1)
            pyautogui.keyDown('ctrl')
            pyautogui.press('v')
            pyautogui.keyUp('ctrl')
            sleep(2)
            pyautogui.press('enter')
            sleep(1)
            speak("done sir")
            os.system("taskkill /f /IM WhatsApp.exe")

        #commands
        
        elif "read it" in query or "read this" in query or "read" in query.lower():
            speak("Sure boss, give me a second")
            print("Reading...")
            pyautogui.keyDown('ctrl')
            pyautogui.press('c')
            pyautogui.keyUp('ctrl')
            win32clipboard.OpenClipboard()
            text = win32clipboard.GetClipboardData()
            win32clipboard.CloseClipboard()
            speak(text)
        elif "turn off" in query:
            speak("ok sir system going turn off")
            sys.exit()
        elif "close this" in query:
            speak("ok sir")
            pyautogui.hotkey('alt', 'F4')
        elif "copy" in query:
            pyautogui.keyDown('ctrl')
            pyautogui.press('a')
            pyautogui.keyUp('ctrl')
            pyautogui.keyDown('ctrl')
            pyautogui.press('c')
            pyautogui.keyUp('ctrl')
        elif "paste" in query:
            pyautogui.keyDown('ctrl')
            pyautogui.press('v')
            pyautogui.keyUp('ctrl')
        elif "jarvis"in query:
            speak("yes sir")
        elif "typing" in query:
            speak("ok sir")
            pyautogui.hotkey('win', 'h')
            break
        elif "minimize" in query or "minimise" in query:
            speak("ok sir")
            pyautogui.hotkey('win', 'd')
        elif "maximize" in query or "maximise" in query:
            speak("ok sir")
            pyautogui.hotkey('win', 'd')
        elif "show me properties" in query:
            pyautogui.hotkey("alt","enter")
        elif "search a image" in query or "search a image of" in query:
            query = query.replace("search a image", "")
            query = query.replace("search a image of", "")
            webbrowser.open(f"https://www.google.com/search?q={query}&sca_esv=999851109142aa1d&sxsrf=ADLYWIKaYd7sWPkbdSoYHke_KlEx417xzA:1720102322675&source=hp&biw=1933&bih=900&ei=sq2GZuqYJ7LAvr0P6vqhqAo&iflsig=AL9hbdgAAAAAZoa7wl-FoEvaV80pU1xrWfo1DMJQUQsS&oq=&gs_lp=EgNpbWciACoCCAAyBxAjGCcY6gIyBxAjGCcY6gIyBxAjGCcY6gIyBxAjGCcY6gIyBxAjGCcY6gIyBxAjGCcY6gIyBxAjGCcY6gIyBxAjGCcY6gIyBxAjGCcY6gIyBxAjGCcY6gJIsClQAFgAcAF4AJABAJgBAKABAKoBALgBAcgBAIoCC2d3cy13aXotaW1nmAIBoAIPqAIKmAMPkgcBMaAHAA&sclient=img&udm=2")
        elif "search image" in query or "search image of" in query:
            query = query.replace("search image", "")
            query = query.replace("search image of", "")
            webbrowser.open(f"https://www.google.com/search?q={query}&sca_esv=999851109142aa1d&sxsrf=ADLYWIKaYd7sWPkbdSoYHke_KlEx417xzA:1720102322675&source=hp&biw=1933&bih=900&ei=sq2GZuqYJ7LAvr0P6vqhqAo&iflsig=AL9hbdgAAAAAZoa7wl-FoEvaV80pU1xrWfo1DMJQUQsS&oq=&gs_lp=EgNpbWciACoCCAAyBxAjGCcY6gIyBxAjGCcY6gIyBxAjGCcY6gIyBxAjGCcY6gIyBxAjGCcY6gIyBxAjGCcY6gIyBxAjGCcY6gIyBxAjGCcY6gIyBxAjGCcY6gIyBxAjGCcY6gJIsClQAFgAcAF4AJABAJgBAKABAKoBALgBAcgBAIoCC2d3cy13aXotaW1nmAIBoAIPqAIKmAMPkgcBMaAHAA&sclient=img&udm=2")
        


        else:
            if "open" in query:
                speak("ok sir")
                query = query.replace("open", "")
                pyautogui.hotkey('win', 's')
                pyautogui.write(query)
                sleep(1)
                pyautogui.press('enter')
                sleep(2)

            else:
                completion = client.chat.completions.create(
                model="llama3-8b-8192",
                messages=[
                    {
                        "role": "system",
                        "content": "you are my jarvis ai assistanr and you are very powerful ai you give me answer short and friendly remove your introduction and your"
                    },

                    {
                        "role": "user",
                        "content": query
                    },


                ],
                temperature=0.5,
                max_tokens=1024,
                top_p=1,
            )
                response = completion.choices[0].message.content
                if "write" in query:
                    file = open('C:\\Users\\rihan\\Videos\\Jarvis\\file.txt', 'w')
                    vl = file.write(response)
                    file.close()
                    speak("here sir")
                    p.copy(vl)
                    npath = "C:\\Users\\rihan\\Videos\\Jarvis\\file.txt"  #8888
                    os.startfile(npath)
                elif "none" in query:
                    pass
                else:
                    p.copy(response)
                    speak(response)

                    q = takecommand().lower()
                    if "show me" in q:
                        npath = "C:\\Windows\\System32\\notepad.exe"
                        os.startfile(npath)
                        sleep(2)
                        pyautogui.hotkey('ctrl', 'A')
                        pyautogui.press('backspace')
                        pyautogui.keyDown('ctrl')
                        pyautogui.press('v')
                        pyautogui.keyUp('ctrl')
                    else:
                        pass


if __name__ == "__main__":
    wish()
    while True:
        permission = takecommand().lower()
        if "jarvis" in permission:
            taskexecution()
        elif "wake up" in permission:
            taskexecution()
        elif "breakup" in permission:
            taskexecution()
        elif "main kab" in permission:
            taskexecution()
        elif "makeup" in permission:
            taskexecution()
        elif "turn off" in permission:
            speak("ok sir system going turn off")
            sys.exit()
        elif "shut down my pc" in permission:
            os.system("shutdown /s /t 5")
            speak("ok sir pc is shutting down")
        elif "restart my pc" in permission:
            os.system("shutdown /r /t 5")
            speak("ok sir pc is restarting")
        elif "sleep my pc" in permission:
            os.system("RUNDLL32.exe powrprof.dll,SetSuspendState 0,1,0")
            speak("ok sir pc is going to sleep")
        elif "lock my pc" in permission or "lock my screen" in permission:
            speak("ok sir")
            os.system("Rundll32.exe user32.dll,LockWorkStation")
