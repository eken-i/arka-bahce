import speech_recognition as sr
import pyttsx3
import openai

r = sr.Recognizer()
openai.api_key = "TOKEN"


def SpeakText(command):
    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()


def start_call():
    with sr.Microphone() as source3:
        audio1 = r.listen(source3)
        r.adjust_for_ambient_noise(source3, duration=2.0)
        startcall = r.recognize_google(audio1)
        startcall = startcall.lower()
        print(startcall)
        if startcall == "help":
            pergen()


def pergen():
    print("Hello! How can I assist you today?")
    with sr.Microphone() as source2:
        audio = r.listen(source2)
        r.adjust_for_ambient_noise(source2, duration=2.0)
        MyText = r.recognize_google(audio)
        MyText = MyText.lower()
        print(MyText)
        prompt = MyText
        if 'exit' in prompt or 'quit' in prompt:
            quit()
        MODEL = "gpt-3.5-turbo-0301"
        completion = openai.ChatCompletion.create(
            model=MODEL,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=4000,
            n=1, )

        SpeakText(completion.choices[0].message.content)

while 1:

    try:
        start_call()



    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
    except sr.UnknownValueError:
        print("unknown error occurred")
