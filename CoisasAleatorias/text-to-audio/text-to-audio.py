from gtts import gTTS
from playsound import playsound

input_text = input('Digite um texto: ')

audio = 'speech.mp3'
language = 'pt'
sp = gTTS(text=input_text, lang=language, slow=False)
sp.save(audio)
playsound(audio)