from gtts import gTTS
import os

# Open and read the content of the text file
with open('text_file.txt', 'r') as file:
    mytext = file.read()

language = 'en'
myobj = gTTS(text=mytext, lang=language, slow=False)
myobj.save("speech.mp3")
os.system("open welcome.mp3")
