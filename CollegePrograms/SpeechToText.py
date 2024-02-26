import speech_recognition as sr
import pyttsx3

# Initialize recognizer and text-to-speech engine
r = sr.Recognizer()
engine = pyttsx3.init()

import time

# Start time
start_time = time.time()

# Listen for audio
with sr.Microphone() as source:
  audio = r.listen(source)

# Calculate duration
duration = time.time() - start_time

# Check if duration is within your desired limit
if duration <= 1:  # Check for 1 second or less
  # Process the audio
  text = r.recognize_google_cloud(audio)
  print("You said:", text)
else:
  print("Speech exceeded the 1-second limit.")


# Function to speak text
""" def speak(text):
  engine.say(text)
  engine.runAndWait()

# Capture audio from microphone
with sr.Microphone() as source:
  print("Speak for 1 second...")
  audio = r.listen(source,timeout=1)  # Limit duration to 1 second
  print("Listening.")

# Try to recognize speech
try:
  text = r.recognize_google_cloud(audio)
  print("You said: {}".format(text))
  speak(text)
except sr.UnknownValueError:
  print("Sorry, could not understand audio")
except sr.RequestError as e:
  print("Could not request results from Google Speech Recognition service; {0}".format(e))
 """