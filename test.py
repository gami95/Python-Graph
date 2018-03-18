import speech_recognition as sr
import sndhdr   
# get audio from the microphone
def audiolisten(s):
	print("hello "+s+"!")                                                                       
r = sr.Recognizer()                                                                                   
with sr.Microphone() as source:                                                                       
    print("Speak:")                                                                                   
    audio = r.listen(source)   
#print(sndhdr.what(audio))
try:
    print("You said " + r.recognize_google(audio))
    s=r.recognize_google(audio)
    #audiolisten(s)
except sr.UnknownValueError:
    print("Could not understand audio")
except sr.RequestError as e:
    print("Could not request results; {0}".format(e))
#def audiolisten(s):
	#print("you said "+s)
