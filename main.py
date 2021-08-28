from neuralintents import GenericAssistant
import speech_recognition
import pyttsx3 as tts
import sys
import func
import requests



recognizer = speech_recognition.Recognizer()
s = tts.init()

mappings = {
    "hello": func.hello,
    "create_note": func.create_note,
    "create_todo": func.add_todo,
    "show_todos": func.show_todos,
    "age": func.age,
    "name": func.name,
    "time": func.time,
    "date": func.date,
    "calculate": func.calculate,
    "exit": func.quit,
    "roast": func.roast,
    "favsong": func.favsong,
    "favcolor": func.favcolor,
    "favanimal": func.favanimal,
    "favfood": func.favfood
}

assistant = GenericAssistant('intents.json', intent_methods=mappings)

tm = input("Would you like to train the model or use a saved model? \n")

if tm == 't':
    saveas = input("\nSave as: ")
    assistant.train_model()
    assistant.save_model(model_name=saveas)
    runasis = input("\nRun assistant? y/n ")
    if runasis == "n":
        sys.exit(0)
if tm == 's':
    modeln = input("\nModel name: ")
    assistant.load_model(model_name=modeln)

print("\nVoice Assistant is ready!")
func.hello()
while True:
    try:
        with speech_recognition.Microphone() as mic:
            print("Assistant is ready for next command")
            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            audio = recognizer.listen(mic)
            message = recognizer.recognize_google(audio)
            message = message.lower()
            print(message)
        try:
            assistant.request(message)
        except KeyError:
            print("key error lol")
    except speech_recognition.UnknownValueError:
        recognizer = speech_recognition.Recognizer()
        print("Didn't hear you lol")
