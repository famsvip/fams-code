# must install following libraries:
# install PyAudio
# install SpeechRecognition

import speech_recognition as sr   # importing required modules/libraries

r = sr.Recognizer()    # recognizer = speech to text
mic = sr.Microphone()  # setting up microphone object

while True:  # runs on an endless loop for the sake of testing
    with mic as source:  # setting up our audio source
        try:
            r.adjust_for_ambient_noise(source) # filter for ambient noise
            print("Speak")   # prompt
            audio_text = r.listen(source)   # sets up variable with audio input
            print("Stop")    # prompt
            text = r.recognize_google(audio_text)  # sends to google and returns text from audio
            print(text)  # outputs the audio --> text
        except Exception:  # catches any exceptions -- if an empty audio sample is sent, it'll result in an error
            print("Try Again.")

