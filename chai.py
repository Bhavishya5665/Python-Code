# total = 0

# while True:

#     print("\n----- Tea Menu -----")
#     print("1. Small Tea - ₹15 ")
#     print("2. Medium Tea - ₹30")
#     print("3. Larg Tea - ₹45")


# # Enter the choice of cup

#     choice = input("Enter cup size (small/medium/larg): ").lower()
#     # Enter the quanity of cup
#     qty = int(input("Enter quantity: "))

# #  if else statement

#     if choice == "small":
#         price = 15

#     elif choice == "medium":
#         price = 30

#     elif choice == "larg":
#         price = 45

#     else:
#         print("Invalid choice! Try again")
#         continue

#     amount = price * qty
#     total += amount

#     print("Added ₹", amount, "to total bill.")
#     more = input("Do you want to order more? (yes/no): ").lower()
#     if more != "yes":
#         break
# print("\n-------Final Bill-------")
# print("Total Amount to Pay: ₹", total)
# print("Thank you! visit again")



# total = 0

# while True:

#     print("\n----- Tea Menu -----")
#     print("1. Small Tea - ₹15 ")
#     print("2. Medium Tea - ₹30")
#     print("3. Larg Tea - ₹45")


# # Enter the choice of cup

#     choice = input("Enter cup size (small/medium/larg): ").lower()
#     # Enter the quanity of cup
#     qty = int(input("Enter quantity: "))

# #  if else statement

#     if choice == "small":
#         price = 15

#     elif choice == "medium":
#         price = 30

#     elif choice == "larg":
#         price = 45

#     else:
#         print("Invalid choice! Try again")
#         continue

#     amount = price * qty
#     total += amount

#     print("Added ₹", amount, "to total bill.")
#     more = input("Do you want to order more? (yes/no): ").lower()
#     if more != "yes":
#         break
# print("\n-------Final Bill-------")
# print("Total Amount to Pay: ₹", total)

# if total > 1000:
#     x = str(input("Enter your cupan code: ")).lower()
#     if x == "ayush":
#         print(total-total/100*25)

#     else:
#         print("Coupen code is invalide")



# print("Thank you! visit again")

# import speech_recognition as sr
# import pyttsx3
# import sounddevice as sd

# # initialize
# r = sr.Recognizer()
# engine = pyttsx3.init()

# def speak(text):
#     print(text)
#     engine.say(text)
#     engine.runAndWait()

# def listen():
#     with sr.Microphone() as source:
#         speak("Boliyé...")
#         audio = r.listen(source)
#     try:
#         text = r.recognize_google(audio).lower()
#         print("You said:", text)
#         return text
#     except:
#         speak("Samajh nahi aaya, dobara boliyé")
#         return listen()

# total = 0

# while True:
#     speak("Tea menu sun lijiye. Small tea 15 rupay. Medium tea 30 rupay. Large tea 45 rupay.")

#     speak("Cup size boliyé: small, medium ya large")
#     choice = listen()

#     speak("Quantity boliyé")
#     try:
#         qty = int(listen())
#     except:
#         speak("Invalid quantity")
#         continue

#     if "small" in choice:
#         price = 15
#     elif "medium" in choice:
#         price = 30
#     elif "large" in choice:
#         price = 45
#     else:
#         speak("Galat choice, dobara try kijiye")
#         continue

#     amount = price * qty
#     total += amount

#     speak(f"{amount} rupay total me add ho gaye")

#     speak("Aur order karna hai? yes ya no boliyé")
#     more = listen()
#     if "no" in more:
#         break

# speak(f"Aapka total bill hai {total} rupay")

# if total > 1000:
#     speak("Coupon code boliyé")
#     code = listen()

#     if "ayush" in code:
#         discount = total * 0.25
#         total -= discount
#         speak(f"Discount ke baad total {total} rupay")
#     else:
#         speak("Coupon code invalid hai")

# speak("Dhanyavaad! Phir se aaiyega")


import speech_recognition as sr
import pyttsx3
import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav

r = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    print(text)
    engine.say(text)
    engine.runAndWait()

def record_audio(duration=4, fs=44100):
    speak("Boliyé...")
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()
    wav.write("input.wav", fs, audio)
    return "input.wav"

def listen():
    try:
        file = record_audio()
        with sr.AudioFile(file) as source:
            audio = r.record(source)
        text = r.recognize_google(audio).lower()
        print("You said:", text)
        return text
    except:
        speak("Samajh nahi aaya, dobara boliyé")
        return listen()

total = 0

while True:
    speak("Tea menu sun lijiye. Small tea 15 rupay. Medium tea 30 rupay. Large tea 45 rupay.")

    speak("Cup size boliyé: small, medium ya large")
    choice = listen()

    speak("Quantity boliyé")
    try:
        qty = int(listen())
    except:
        speak("Invalid quantity")
        continue

    if "small" in choice:
        price = 15
    elif "medium" in choice:
        price = 30
    elif "large" in choice:
        price = 45
    else:
        speak("Galat choice, dobara try kijiye")
        continue

    amount = price * qty
    total += amount

    speak(f"{amount} rupay total me add ho gaye")

    speak("Aur order karna hai? yes ya no boliyé")
    more = listen()
    if "no" in more:
        break

speak(f"Aapka total bill hai {total} rupay")

if total > 1000:
    speak("Coupon code boliyé")
    code = listen()

    if "ayush" in code:
        discount = total * 0.25
        total -= discount
        speak(f"Discount ke baad total {total} rupay")
    else:
        speak("Coupon code invalid hai")

speak("Dhanyavaad! Phir se aaiyega")