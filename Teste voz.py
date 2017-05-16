from gtts import gTTS
import os,pygame,time

def Falagg(fala,tempo):
    tts = gTTS(text=fala, lang='pt')
    tts.save("good.mp3")
    pygame.mixer.init()
    pygame.mixer.music.load("good.mp3")
    pygame.mixer.music.play()
    time.sleep(tempo) 
    pygame.mixer.quit()
    os.remove("good.mp3")
tempo = 11  
fala = "ah tiu,vai tomar no cu"
Falagg(fala,tempo)