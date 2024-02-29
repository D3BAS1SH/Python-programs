from gtts import gTTS
from playsound import playsound

myText='Fuck, Say my name'
text = "यह हिंदी में पाठ है।"  # Hindi text
language = 'en'


# language='en'

myTextSpeech=gTTS(text=myText,lang=language,slow=False)

myTextSpeech.save('TestEngSpeech.mp3')

playsound('TestEngSpeech.mp3')
print('playing sound using  playsound')