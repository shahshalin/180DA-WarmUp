#!/usr/bin/env python3

# NOTE: this example requires PyAudio because it uses the Microphone class
# built on top of https://github.com/Uberi/speech_recognition
import speech_recognition as sr
import sys
if len(sys.argv) == 2:
    word = sys.argv[1]
elif len(sys.argv) > 2:
    print('Too many arguments inputted.')
    print('USAGE: \n$ python speechrecognition.py \nOR \n$ python speechrecognition.py \'[word or phras to test against]\'')
    exit(1)
else:
    word == 'hello'
# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

# recognize speech using Sphinx
sphinx = ''
try:
    sphinx += r.recognize_sphinx(audio)
    print("Sphinx thinks you said " + sphinx)
except sr.UnknownValueError:
    print("Sphinx could not understand audio")
except sr.RequestError as e:
    print("Sphinx error; {0}".format(e))

# recognize speech using Google Speech Recognition
google = ''
try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
    google += r.recognize_google(audio)
    print("Google Speech Recognition thinks you said " + google)
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))

if sphinx == word:
    print('Sphinx understood you')
else:
    print('Sphinx misunderstood you')
if google == word:
    print('Google understood you')
else:
    print('Google misunderstood you')
