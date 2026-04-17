import pyttsx3
engine = pyttsx3.init()

name = input("What is your name: ")

massage = f" Hello {name} , I a Jarvis, Your Personal Assistant. How can I help you ?"

print(massage)

engine.say(massage)
engine.runAndWait()



