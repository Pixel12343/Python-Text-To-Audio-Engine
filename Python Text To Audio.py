# pip install pyttsx3

# Depending on what python version you are using installation may be different for example i am using python3.12
# my installation method is py -m pip install pyttsx3, may alsobe py3 -m pip install pyttsx3.
# i have tested and ensure it works on 3.12 python

import pyttsx3
engine = pyttsx3.init()

text = input("Enter Your Text:")

engine.save_to_file(
    text=text, filename="audio.mp3"
)
engine.runAndWait()

print("Audio Saved Successfuly")

#when using the project the file will be saved in the directory where your python file is located