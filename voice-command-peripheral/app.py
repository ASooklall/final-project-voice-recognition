import speech_recognition as sr
import pyaudio
import keyboard, time
from pynput.keyboard import Key, Controller
from csv import writer

# sentence = "the quick brown fox jumps over the lazy dog"

# keyboard.wait('esc')

# for letter in sentence:
#     keyboard.press_and_release(letter)
#     time.sleep(0.1)

def rec_z():
    try:
        rt = sr.Recognizer()
        mic = sr.Microphone(device_index=0)
        with mic as source:
    #         rt.adjust_for_ambient_noise(source)
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

# print('press "esc" to talk')
# if keyboard.read_key() == "esc":
#     sentence = rec_z()
#     for letter in sentence:
#         keyboard.press_and_release(letter)
#         time.sleep(0.2)

inputter = Controller()

def basic_commands(word):
    if word in ['a', 'yes']:
        inputter.press('j')
        time.sleep(0.2)
        inputter.release('j')
    elif word in ['b', 'no', 'back']:
        inputter.press('k')
        time.sleep(0.2)
        inputter.release('k')
    elif word in ['up']:
        inputter.press('w')
        time.sleep(0.2)
        inputter.release('w')
    elif word in ['left']:
        inputter.press('a')
        time.sleep(0.2)
        inputter.release('a')
    elif word in ['down']:
        inputter.press('s')
        time.sleep(0.2)
        inputter.release('s')
    elif word in ['right']:
        inputter.press('d')
        time.sleep(0.2)
        inputter.release('d')

while True:
    print('Sequence [X] or Special [C]? Press "esc" to escape')
    pressed_key = keyboard.read_key()
    print(pressed_key)
    if pressed_key == "x":
        print('You have chosen Sequence')
        seq = rec_z()
        seq_list = seq.split()
        for c in seq_list:
            basic_commands(c)
            time.sleep(0.2)
    elif pressed_key == 'c':
        print('You have chosen Special')
        spe = rec_z()
        print(spe)
        basic_commands(spe)
        time.sleep(0.2)
    elif pressed_key == 'esc':
        break
    time.sleep(0.2)