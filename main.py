#meu projeto
import speech_recognition as sr 
#Cria em reconhecedor 
r = sr.Microphone()
# Abrir o microfine  para captura
with sr.Microphone() as source:
    audio = r.listen(source)

    print(r.recongnize_google(audio))