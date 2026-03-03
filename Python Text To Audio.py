import pyttsx3
engine = pyttsx3.init()

text = input("Enter Your Text:")

engine.save_to_file(
    text=text, filename="audio.mp3"
)
engine.runAndWait()

print("Audio Saved Successfuly")
