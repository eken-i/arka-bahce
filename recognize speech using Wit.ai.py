import speech_recognition as sr
import pyttsx3

r = sr.Recognizer()


def SpeakText(command):
    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()


while (1):

    WIT_AI_KEY = "IBXQBK5J2KGWDGZQ5WNS3WVR5DIFTMJ4"  # Wit.ai keys are 32-character uppercase alphanumeric strings
    try:

        with sr.Microphone() as source2:

            audio = r.listen(source2)
            print( r.recognize_wit(audio, key=WIT_AI_KEY))

            SpeakText(r.recognize_wit(audio, key=WIT_AI_KEY))

    except sr.UnknownValueError:
        print("Wit.ai could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Wit.ai service; {0}".format(e))


