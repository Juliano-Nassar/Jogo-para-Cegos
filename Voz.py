from gtts import gTTS
import os,pygame,time

def Falagg(fala):
    tts = gTTS(text=fala, lang='pt')
    tts.save("good.mp3")
    pygame.mixer.init()
    pygame.mixer.music.load("good.mp3")
    pygame.mixer.music.play() 
    pygame.mixer.quit()
    os.remove("good.mp3")
