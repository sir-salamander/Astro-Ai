from playsound import playsound
import speech_recognition as sr
import keyboard
import gtts
import datetime
import os

r = sr.Recognizer()

# var
now = datetime.datetime.now()

# greeting
tts1 = gtts.gTTS("What can i do for you today?")
tts1.save("wcidfyt.mp3")
# please try again
tts2 = gtts.gTTS("Please try again")
tts2.save("pta.mp3")
# ok
tts3 = gtts.gTTS("ok")
tts3.save("ok.mp3")
# gLiTCh AcTIvE
tts5053 = gtts.gTTS("Manual Override complete. Welcome Liam Basilone")
tts5053.save("gLiTCh AcTIvE.mp3")
# recording started
tts4 = gtts.gTTS("Recording started")
tts4.save("RS.mp3")
# recording ended
tts5 = gtts.gTTS("Recording ended")
tts5.save("RE.mp3")

# listening loop
while True:
    with sr.Microphone() as source:
        audio = r.listen(source)

        try:

            data = r.recognize_google(audio)
            print(data)
            if data.lower() == "hey astro":
                print("What can i do for you today?")
                playsound("wcidfyt.mp3")
            if data.lower() == "rick roll me":
                playsound("Never Gonna Give You Up Original.mp3")
            if data.lower() == "hey astro rickroll me":
                playsound("Never Gonna Give You Up Original.mp3")
            if data.lower() == "quit":
                break
            if data.lower() == "nevermind":
                print("ok")
                playsound("ok.mp3")
            if data.lower() == "code 505 3":
                playsound("glitch.mp3")
                playsound("gLiTCh AcTIvE.mp3")
            if data.lower() == "code 5053":
                playsound("glitch.mp3")
                playsound("gLiTCh AcTIvE.mp3")
            if data.lower() == "505 3 initiate keylogging":
                print("Recording Started")
                playsound("RS.mp3")
            if data.lower() == "5053 initiate keylogging":
                print("Recording Started")
                playsound("RS.mp3")
                rk = keyboard.record(until='-')
            if data.lower() == "505 3 replay keylogging":
                keyboard.play(rk, speed_factor=5)
                print("Recording Ended")
                print("RE.mp3")
            if data.lower() == "5053 stop keylogging":
                keyboard.play(rk, speed_factor=5)
                print("Recording Ended")
                print("RE.mp3")
            if data.lower() == "what time is it":
                # time
                tts6 = gtts.gTTS(str(now))
                tts6.save("timenow.mp3")
                print(now)
                playsound("timenow.mp3")
            if data == "open YouTube":
                os.system("start \"\" https://youtube.com")
            if data.lower() == "nevermind":
                break
            if data.lower() == "quit":
                break
            if keyboard.is_pressed("-"):
                break
        except:
            print("please try again")
