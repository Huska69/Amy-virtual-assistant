import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def say(text):
    engine.say(text)
    engine.runAndWait()


# noinspection PyBroadException
def get_command():
    try:
        with sr.Microphone() as source:
            print('Say something please.')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'amy' in command:
                command = command.replace('amy', '')
                say(command)
    except Exception:
        pass
    return command


def get_amy():
    command = get_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        say('Okay bro Im playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I %M %p')
        print('bro its ' + time)
        say('bro its' + time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        information = wikipedia.summary(person, 2)
        print(information)
        say(information)
    elif 'what is' in command:
        question = command.replace('what is', '')
        information = wikipedia.summary(question, 2)
        print(information)
        say(information)
    elif 'who are you' in command:
        say('Who do you think I am Amy you idiot')
    elif 'I love you' in command:
        say('Sorry Im in relationship with this Nitro five laptop')
    elif 'joke' in command:
        joke = pyjokes.get_joke()
        print(joke)
        say(joke)
    else:
        say('please tell me something again.I dont understand')


while True:
    get_amy()
