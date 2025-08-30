import pyttsx3   # text-to-speech library

engine = pyttsx3.init()   # initialize text-to-speech engine
engine.say("if you think you are not ready then start today ")  # convert text to speech
engine.runAndWait()   # play the speech
