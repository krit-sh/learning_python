# Text to audio
import pyttsx3
engine = pyttsx3.init()
engine.say("hmm Hey, I am Reteash")
engine.runAndWait()

#Print the contents of a directory
import os

directory_path = 'E:\learning_python\Chapter 1'

contents = os.listdir(directory_path)

for item in contents:
    print(item)