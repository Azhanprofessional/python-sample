import os
from gtts import gTTS
text=input('Enter the text:')
voice=gTTS(text=text,lang='en',slow=False)
voice.save('Audio.mp3')
os.system('start Audio.mp3')
