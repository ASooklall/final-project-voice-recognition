import speech_recognition as sr
import pyaudio
import keyboard


r = sr.Recognizer()
mic = sr.Microphone()
mic = sr.Microphone(device_index=0)

with mic as source:
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)

def rec_z():
    try:
        rt = sr.Recognizer()
        mic = sr.Microphone(device_index=0)
        with mic as source:
            rt.energy_threshold = 3000
            rt.dynamic_energy_threshold = True
            rt.adjust_for_ambient_noise(source, duration = 0.6)
            audio = rt.listen(source, timeout = 2)
            try: 
                audio_play = rt.recognize_google(audio) 
                print("you said: " + audio_play)
                return audio_play
            except sr.UnknownValueError: 
                print("Google Speech Recognition could not understand audio") 

            except sr.RequestError as e: 
                print("Could not request results from Google Speech Recognition service; {0}".format(e))

    except sr.WaitTimeoutError:
        print('Please issue a voice command.')


print('press t or y')
while True:
    if keyboard.read_key() == "t":
        print('t was pressed')
        rec_z()
    elif keyboard.read_key() == 'y':
        print('y was pressed')
    else:
        break