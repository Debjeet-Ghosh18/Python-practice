# import pyttsx3   # text-to-speech library

# engine = pyttsx3.init()   # initialize text-to-speech engine
# engine.say("if you think you are not ready then start today ")  # convert text to speech
# engine.runAndWait()   # play the speech

import pyttsx3   # text-to-speech library

# initialize text-to-speech engine
engine = pyttsx3.init()

# set speaking rate (optional)
engine.setProperty('rate', 150)  

# set volume (0.0 to 1.0)
engine.setProperty('volume', 1.0)

# set voice (0 for male, 1 for female usually)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# speak the text
engine.say("If you think you are not ready, then start today.")
engine.runAndWait()
