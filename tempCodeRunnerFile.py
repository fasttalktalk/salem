
import pyttsx3
import time
engine = pyttsx3.init(driverName='nsss')
engine.setProperty('voice', 'com.apple.voice.compact.th-TH.Kanya')
engine.say('สวัสดี')
engine.runAndWait()
def start():
    engine.say('แม่มดหลับตา')
    time.sleep(1)
    for i in range (15):
        engine.say(i)
    
    engine.runAndWait()
start()