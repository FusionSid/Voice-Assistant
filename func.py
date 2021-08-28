import random
import speech_recognition
import pyttsx3 as tts
import sys
import datetime
import roast_list
import json

# write to json files
def write_json(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f)

recognizer = speech_recognition.Recognizer()
s = tts.init()

import random
import speech_recognition
import pyttsx3 as tts
import sys
import datetime
import roast_list
import json

# write to json files
def write_json(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f)

recognizer = speech_recognition.Recognizer()
s = tts.init()

# Short answer questions

def age():
    s.say("I am 42 years old")
    s.runAndWait()


def name():
    s.say("My name is Rick")
    s.runAndWait()


def favsong():
    s.say("My favourite song is Never gonna give you up")
    s.runAndWait()


def favfood():
    s.say("Pizza, Pizza is my favourite food")
    s.runAndWait()


def favanimal():
    s.say("The duck is my favourite animal")
    s.runAndWait()


def favcolor():
    s.say("My favourite color is blue")
    s.runAndWait()


def roast():
    roast = random.choice(roast_list.roastlist)
    s.say(roast)
    s.runAndWait()


def create_note():
    global recognizer

    s.say("What would you like to write on the note?")
    s.runAndWait()

    done = False

    while not done:
        try:
            with speech_recognition.Microphone() as mic:
                print("\nWhat would you like to write to the note!")
                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)
                note = recognizer.recognize_google(audio)
                note = note.lower()
                print(note)

                s.say("What would you like to call the note")
                s.runAndWait()
                print("What would you like to call the note")
                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)
                filename = recognizer.recognize_google(audio)
                print(filename)
                filename = filename.lower()

            with open(filename, 'w') as f:
                f.write(note)
                done = True
                s.say("Your note has been created")
                s.runAndWait()
        except speech_recognition.UnknownValueError:
            recognizer = speech_recognition.Recognizer()
            print("f")
            s.say("Sorry I didn't understand you, please try again")
            s.runAndWait()


def add_todo():
    global recognizer

    s.say("What would you like to add to you todo list?")
    s.runAndWait()

    filename = 'todo_list.json'
    done = False

    while not done:
        try:
            with speech_recognition.Microphone() as mic:
                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                print("\nWhat would you like to add to your todo list!")
                audio = recognizer.listen(mic)

                item = recognizer.recognize_google(audio)
                item = item.lower()
                print(item)
                filename = 'todo_list.json'

                with open(filename) as json_file:
                    data = json.load(json_file)
                    data.append(item)

                write_json(data, filename)

                done = True
                s.say(f"{item} Has been added to the todo list")
                s.runAndWait()

        except speech_recognition.UnknownValueError:
            recognizer = speech_recognition.Recognizer()
            print("f")
            s.say("Sorry I didn't understand you, please try again")
            s.runAndWait()


def show_todos():
    s.say("The items in your todo list are the following")
    s.runAndWait()

    filename = 'todo_list.json'
    with open(filename) as json_file:
        data = json.load(json_file)

    for item in data:
        s.say(item)
    s.runAndWait()


def date():
    s.say(f"The date today is: {datetime.date.today()}")
    s.runAndWait()


def time():
    now = datetime.datetime.now()
    timern = now.strftime("%I:%M %p")
    s.say(f'The time right now is: {timern}')
    s.runAndWait()


def hello():
    hellores = ["Hello", "Hi there", "Wassup", "Hello there, What can I do for you"]
    s.say(random.choice(hellores))
    s.runAndWait()


def quit():
    quitchoices = ["Goodbye Sir", "Goodbye", "Bye", "See ya later", "See ya later alligator"]
    s.say(random.choice(quitchoices))
    s.runAndWait()
    sys.exit(0)


def calculator(n1, op, n2):
    if op == "+":
        return n1 + n2
    if op == "x":
        return n1 * n2
    if op == "-":
        return n1 - n2
    if op == "/":
        return n1 / n2
    else:
        return "invalid"


def calculate():
    global recognizer
    try:
        with speech_recognition.Microphone() as mic:
            s.say("What would you like to calculate")
            s.runAndWait()
            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            print("\nWhat would you like to calculate")
            audio = recognizer.listen(mic)
            n2calc = recognizer.recognize_google(audio)
            print(n2calc)
            n2calc = n2calc.split()
            n1 = int(n2calc[0])
            op = n2calc[1]
            n2 = int(n2calc[2])
            ans = calculator(n1, op, n2)
            if ans == 'invalid':
                s.say("Invalid input")
                s.runAndWait()
            else:
                s.say(str(ans))
                s.runAndWait()
    except speech_recognition.UnknownValueError:
        recognizer = speech_recognition.Recognizer()

# Short answer questions

def age():
    s.say("I am 42 years old")
    s.runAndWait()


def name():
    s.say("My name is Rick")
    s.runAndWait()


def favsong():
    s.say("My favourite song is Never gonna give you up")
    s.runAndWait()


def favfood():
    s.say("Pizza, Pizza is my favourite food")
    s.runAndWait()


def favanimal():
    s.say("The duck is my favourite animal")
    s.runAndWait()


def favcolor():
    s.say("My favourite color is blue")
    s.runAndWait()


def roast():
    roast = random.choice(roast_list.roastlist)
    s.say(roast)
    s.runAndWait()


def create_note():
    global recognizer

    s.say("What would you like to write on the note?")
    s.runAndWait()

    done = False

    while not done:
        try:
            with speech_recognition.Microphone() as mic:
                print("\nWhat would you like to write to the note!")
                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)
                note = recognizer.recognize_google(audio)
                note = note.lower()
                print(note)

                s.say("What would you like to call the note")
                s.runAndWait()
                print("What would you like to call the note")
                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)
                filename = recognizer.recognize_google(audio)
                print(filename)
                filename = filename.lower()

            with open(filename, 'w') as f:
                f.write(note)
                done = True
                s.say("Your note has been created")
                s.runAndWait()
        except speech_recognition.UnknownValueError:
            recognizer = speech_recognition.Recognizer()
            print("f")
            s.say("Sorry I didn't understand you, please try again")
            s.runAndWait()


def add_todo():
    global recognizer

    s.say("What would you like to add to you todo list?")
    s.runAndWait()

    filename = 'todo_list.json'
    done = False

    while not done:
        try:
            with speech_recognition.Microphone() as mic:
                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                print("\nWhat would you like to add to your todo list!")
                audio = recognizer.listen(mic)

                item = recognizer.recognize_google(audio)
                item = item.lower()
                print(item)
                filename = 'todo_list.json'

                with open(filename) as json_file:
                    data = json.load(json_file)
                    data.append(item)

                write_json(data, filename)

                done = True
                s.say(f"{item} Has been added to the todo list")
                s.runAndWait()

        except speech_recognition.UnknownValueError:
            recognizer = speech_recognition.Recognizer()
            print("f")
            s.say("Sorry I didn't understand you, please try again")
            s.runAndWait()


def show_todos():
    s.say("The items in your todo list are the following")
    s.runAndWait()

    filename = 'todo_list.json'
    with open(filename) as json_file:
        data = json.load(json_file)

    for item in data:
        s.say(item)
    s.runAndWait()


def date():
    s.say(f"The date today is: {datetime.date.today()}")
    s.runAndWait()


def time():
    now = datetime.datetime.now()
    timern = now.strftime("%I:%M %p")
    s.say(f'The time right now is: {timern}')
    s.runAndWait()


def hello():
    hellores = ["Hello", "Hi there", "Wassup", "Hello there, What can I do for you"]
    s.say(random.choice(hellores))
    s.runAndWait()


def quit():
    quitchoices = ["Goodbye Sir", "Goodbye", "Bye", "See ya later", "See ya later alligator"]
    s.say(random.choice(quitchoices))
    s.runAndWait()
    sys.exit(0)


def calculator(n1, op, n2):
    if op == "+":
        return n1 + n2
    if op == "x":
        return n1 * n2
    if op == "-":
        return n1 - n2
    if op == "/":
        return n1 / n2
    else:
        return "invalid"


def calculate():
    global recognizer
    try:
        with speech_recognition.Microphone() as mic:
            s.say("What would you like to calculate")
            s.runAndWait()
            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            print("\nWhat would you like to calculate")
            audio = recognizer.listen(mic)
            n2calc = recognizer.recognize_google(audio)
            print(n2calc)
            n2calc = n2calc.split()
            n1 = int(n2calc[0])
            op = n2calc[1]
            n2 = int(n2calc[2])
            ans = calculator(n1, op, n2)
            if ans == 'invalid':
                s.say("Invalid input")
                s.runAndWait()
            else:
                s.say(str(ans))
                s.runAndWait()
    except speech_recognition.UnknownValueError:
        recognizer = speech_recognition.Recognizer()
