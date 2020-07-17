from stegano import lsb,lsbset
from stegano.lsbset import generators
import speech_recognition as sr
def getfrommicrophone():
    
    rec= sr.Recognizer()
    with sr.Microphone() as mic:
        print("say the message that u want to send")
        audio=rec.listen(mic)
        print('Message Recorded!')
    return rec.recognize_google(audio)


message=lsb.reveal('ddd.png')

print("the message is :",message)

msg="Hello world"


lsb.hide('epc.png',message=msg).save('dbz9encoded.png')

message=lsb.reveal('dbz9encoded.png')

print("the message is :",message)

message=getfrommicrophone()
lsbset.hide(
'epc1.png',
message,
generators.eratosthenes()


    ).save('epc1encode.png')

msg=lsbset.reveal('epc1encode.png',generators.eratosthenes())
print("you said:", msg)
