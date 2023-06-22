import speech_recognition as sr
import pyttsx3



r = sr.Recognizer()


def SpeakText(command):
    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()


while (1):


    try:

        with sr.Microphone() as source2:

            audio = r.listen(source2)
            print("Whisper thinks you said " + r.recognize_openai.Audio(audio, language="english"))

            SpeakText(r.recognize_whisper(audio, language="english"))

    except sr.UnknownValueError:

        print("Whisper could not understand audio")

    except sr.RequestError as e:

        print("Could not request results from Whisper")
