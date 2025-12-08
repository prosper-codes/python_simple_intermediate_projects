from gtts import gTTS
import os
text= open('input_text.txt','r').read()

language= 'en'
output=gTTS(text=text,lang=language,slow=False)
output.save('soundoutput.mp3')
os.system("start soundoutput.mp3")