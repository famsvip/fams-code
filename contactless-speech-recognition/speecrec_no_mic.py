import speech_recognition as sr
r = sr.Recognizer()
file = sr.AudioFile('audio_2.wav')
with file as source:
    r.adjust_for_ambient_noise(source)
    audio = r.record(source)

    text = r.recognize_google(audio)
    """
    f = open("transcription_2.txt", "w")
    words = text.split()
    for word in words:
        f.write(word +"\n")
    f.close()
    """
