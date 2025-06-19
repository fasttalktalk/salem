import tkinter as tk
import pyttsx3
import time
engine = pyttsx3.init(driverName='nsss')
engine.setProperty('voice', 'com.apple.voice.compact.th-TH.Kanya')
# สร้างหน้าต่างหลัก
root = tk.Tk()
root.title("Salem")
root.geometry("300x250")

# ฟังก์ชันเมื่อกดปุ่มเริ่มเกม
def start_game():
    engine.say('ทุกคนหลับตา')
    engine.runAndWait()
    time.sleep(5)
    engine.say('แม่มดลืมตา')
    engine.runAndWait()
    time.sleep(2)
    engine.say('แม่มดเลือกวางแบล็คแค็ท')
    engine.runAndWait()
    time.sleep(1)
    for i in range(15, -1, -1):  
        engine.say(str(i))
        engine.runAndWait()    
        time.sleep(0.5)
    time.sleep(2)
    engine.say('ทุกคนลืมตา')
    engine.runAndWait() 

# ฟังก์ชันเมื่อกดปุ่มเข้ากลางคืน
def enter_night():
    engine.say('ทุกคนหลับตา')
    engine.runAndWait()
    time.sleep(5)
    engine.say("แม่มดลืมตา")
    engine.runAndWait()
    time.sleep(3)
    engine.say("แม่มดเลือกฆ่า")
    engine.runAndWait()
    time.sleep(2)
    for i in range(20, -1, -1):  
        engine.say(str(i))
        engine.runAndWait()    
        time.sleep(0.5)
    time.sleep(2)
    engine.say('แม่มดหลับตา')
    engine.runAndWait()
    time.sleep(5)
    engine.say('คอนลืมตา')
    engine.runAndWait()
    time.sleep(2)
    engine.say('คอนเลือกปกป้อง')
    engine.runAndWait()
    time.sleep(1)
    for i in range(15, -1, -1):  
        engine.say(str(i))
        engine.runAndWait()    
        time.sleep(0.5)
    time.sleep(2)
    engine.say('ทุกคนลืมตา')
    engine.runAndWait()

# ฟังก์ชันเมื่อกดปุ่มกลางคืนคอนตาย
def night_confirm_death():
    engine.say('ทุกคนหลับตา')
    engine.runAndWait()
    time.sleep(5)
    engine.say("แม่มดลืมตา")
    engine.runAndWait()
    time.sleep(3)
    engine.say("แม่มดเลือกฆ่า")
    engine.runAndWait()
    time.sleep(2)
    for i in range(20, -1, -1):  
        engine.say(str(i))
        engine.runAndWait()    
        time.sleep(0.5)
    time.sleep(2)
    engine.say('ทุกคนลืทตา')
    engine.runAndWait()

# สร้างปุ่ม
btn_start = tk.Button(root, text="เริ่มเกม", font=("Tahoma", 14), command=start_game)
btn_night = tk.Button(root, text="เข้ากลางคืน", font=("Tahoma", 14), command=enter_night)
btn_confirm = tk.Button(root, text="กลางคืนคอนตาย", font=("Tahoma", 14), command=night_confirm_death)

# วางปุ่มในหน้าต่าง
btn_start.pack(pady=15)
btn_night.pack(pady=10)
btn_confirm.pack(pady=10)

# เริ่มลูป tkinter
root.mainloop()
