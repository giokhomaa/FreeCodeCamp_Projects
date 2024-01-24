import pyttsx3

text_speech = pyttsx3.init()
while True:
    answer = input("Enter text what you want to convert to speech: ")
    if answer == ".":
        break

    text_speech.say(answer)

    text_speech.runAndWait()

print("The End")
