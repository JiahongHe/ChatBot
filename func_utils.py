from bot.inference import inference
import speech_recognition as sr
from pygame import mixer
from gtts import gTTS
import numpy as np

def give_response(msg):
    response = inference(msg)
    rand = round(4*np.random.rand())
    message = response['answers'][rand]
    print("the bot responded: "+ message)
    tts = gTTS(text=message, lang='en')
    tts.save("test.mp3")

    mixer.init()
    mixer.music.load('test.mp3')
    mixer.music.play()

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak:")
        audio = r.listen(source)
        msg = r.recognize_google(audio)
        try:
            print("You said: " + msg)
        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
    return msg
