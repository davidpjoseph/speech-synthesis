import io
import os
from gtts import gTTS
from playsound import playsound

fp = io.open("file.txt",mode="r",encoding="utf-8")
file_content = fp.read()
ob = gTTS(file_content,lang="ml")
ob.save("file.mp3")
playsound("file.mp3")
os.remove("file.mp3")

     
