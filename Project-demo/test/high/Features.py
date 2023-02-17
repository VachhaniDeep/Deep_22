import pywhatkit
import wikipedia
from pywikihow import RandomHowTo, search_wikihow
import os
import speech_recognition as sr
import webbrowser as web
import bs4
import pyttsx3
from time import sleep
import requests
import wolframalpha

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[1].id)

def Speak(audio):
    print(" ")
    print(f": {audio}")
    engine.say(audio)
    engine.runAndWait()
    print(" ")

def TakeCommand():

    r = sr.Recognizer()

    with sr.Microphone() as source:

        print(": Listening....")

        r.pause_threshold = 1

        audio = r.listen(source)


    try:

        print(": Recognizing...")

        query = r.recognize_google(audio,language='en-in')

        print(f": Your Command : {query}\n")

    except:
        return ""

    return query.lower()

def GoogleSearch(term):
    query = term.replace("jarvis","")
    query = query.replace("what is","")
    query = query.replace("how to","")
    query = query.replace("what is","")
    query = query.replace(" ","")
    query = query.replace("what do you mean by","")

    writeab = str(query)

    oooooo = open('C:\\Users\\Deep\\PycharmProjects\\PyProject\\high\\Data.txt','a')
    oooooo.write(writeab)
    oooooo.close()

    Query = str(term)

    pywhatkit.search(Query)

    os.startfile('C:\\Users\\Deep\\PycharmProjects\\PyProject\\high\\DataBase\ExtraPro\start.py')

    if 'how to' in Query:

        max_result = 1

        how_to_func = search_wikihow(query=Query,max_results=max_result)

        assert len(how_to_func) == 1

        how_to_func[0].print()

        Speak(how_to_func[0].summary)

    else:

        search = wikipedia.summary(Query,2)

        Speak(f": According To Your Search : {search}")

def YouTubeSearch(term):
    result = "https://www.youtube.com/results?search_query=" + term
    web.open(result)
    Speak("This Is What I Found For Your Search .")
    pywhatkit.playonyt(term)
    Speak("This May Also Help You Sir .")

def Alarm(query):

    TimeHere=  open('C:\\Users\\Deep\\PycharmProjects\\PyProject\\high\\Data.txt','a')
    TimeHere.write(query)
    TimeHere.close()
    os.startfile("C:\\Users\\Deep\\PycharmProjects\\PyProject\\high\\DataBase\\ExtraPro\\Alarm.py")



def DownloadYouTube():
    from pytube import YouTube
    from pyautogui import click
    from pyautogui import hotkey
    import pyperclip
    from time import sleep

    sleep(2)
    click(x=1202,y=49)
    hotkey('ctrl','c')
    value = pyperclip.paste()
    Link = str(value) # Important 

    def Download(link):


        url = YouTube(link)


        video = url.streams.first()


        video.download('C:\\Users\\Deep\\PycharmProjects\\PyProject\\high\\DataBase\\Youtube\\')


    Download(Link)


    Speak("Done Sir , I Have Downloaded The Video .")

    Speak("You Can Go And Check It Out.")


    os.startfile('C:\\Users\\Deep\\PycharmProjects\\PyProject\\high\\DataBase\\Youtube\\')

def SpeedTest():

    os.startfile("C:\\Users\\Deep\\PycharmProjects\\PyProject\\high\\DataBase\\Gui Programs\\SpeedTestGui.py")

def WolfRam(query):
    
    api_key = "9LA632-X2HPVER5E6"

    requester = wolframalpha.Client(api_key)

    requested = requester.query(query)


    try:
        Answer = next(requested.results).text

        return Answer

    except:
        Speak("Not Data Found.")

def Calculator(query):
    Term = str(query)

    Term = Term.replace("jarvis", "")
    Term = Term.replace("multiply", "*")
    Term = Term.replace("plus", "+")
    Term = Term.replace("minus", "_")
    Term = Term.replace("divied", "/")
    Term = Term.replace("into", "*")

    Final = str(Term)

    try:
        result = WolfRam(Final) 
        Speak(f"{result}")

    except:
        Speak("Not Data Found.")  

def Temp(query):
    
    Term = str(query)

    Term = Term.replace("jarvis ", "")
    Term = Term.replace("in ", "")
    Term = Term.replace("what is ", "")
    Term = Term.replace("temperature", "")

    temp_quwry = str(Term)

    if 'outside' in query:
        
        var1 = "Temperature in rajkot"

        answer = WolfRam(var1)

        Speak(f"{var1} is {answer} .")

    else:
        var2 = "temperature in " + temp_quwry

        answ = WolfRam(var2)

        Speak(f"{var2} is {answ} .")

def DateConverter(Query):

    Date = Query.replace(" and ","-")
    Date = Date.replace(" and ","-")
    Date = Date.replace("and","-")
    Date = Date.replace("and","-")
    Date = Date.replace(" ","")

    return str(Date)

def My_Location():

    op = "https://www.google.com/maps/place/Delhi/@28.6472799,76.8130619,83757m/data=!3m2!1e3!4b1!4m5!3m4!1s0x390cfd5b347eb62d:0x37205b715389640!8m2!3d28.7040592!4d77.1024902"

    Speak("Checking....")

    web.open(op)

    ip_add = requests.get('https://api.ipify.org').text

    url = 'https://get.geojs.io/v1/ip/geo/' + ip_add + '.json'

    geo_q = requests.get(url)

    geo_d = geo_q.json()

    state = geo_d['city']

    country = geo_d['country']

    Speak(f"Sir , You Are Now In {state , country} .")

def CoronaVirus(Country):

    countries = str(Country).replace(" ","")

    url = f"https://www.worldometers.info/coronavirus/country/{countries}/"

    result = requests.get(url)

    soups = bs4.BeautifulSoup(result.text,'lxml')

    corona = soups.find_all('div',class_ = 'maincounter-number')

    Data = []

    for case in corona:

        span = case.find('span')

        Data.append(span.string)

    cases , Death , recovored = Data

    Speak(f"Cases : {cases}")
    Speak(f"Deaths : {Death}")
    Speak(f"Recovered : {recovored}")



