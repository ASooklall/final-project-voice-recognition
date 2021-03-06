import speech_recognition as sr
import pyaudio, keyboard, time
from datetime import datetime
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
                print("You said: " + audio_play)
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

def append_vcp_log(log_entry):
    with open('../data/logs/vcp_log.csv', 'a+', newline='') as write_obj:
        csv_writer = writer(write_obj)
        csv_writer.writerow(log_entry)


inputter = Controller()

input_sleep = 0.25

def basic_commands(word, mode):
    if word in ['a', 'yes', 'okay', 'confirm', 'accept', 'except', 'talk']:
        inputter.press('j')
        time.sleep(input_sleep)
        inputter.release('j')
        append_vcp_log([datetime.now(),word,mode])
    elif word in ['b', 'no', 'back']:
        inputter.press('k')
        time.sleep(input_sleep)
        inputter.release('k')
        append_vcp_log([datetime.now(),word,mode])
    elif word in ['up']:
        inputter.press('w')
        time.sleep(input_sleep)
        inputter.release('w')
        append_vcp_log([datetime.now(),word,mode])
    elif word in ['left']:
        inputter.press('a')
        time.sleep(input_sleep)
        inputter.release('a')
        append_vcp_log([datetime.now(),word,mode])
    elif word in ['down']:
        inputter.press('s')
        time.sleep(input_sleep)
        inputter.release('s')
        append_vcp_log([datetime.now(),word,mode])
    elif word in ['right', 'write', 'rights']:
        inputter.press('d')
        time.sleep(input_sleep)
        inputter.release('d')
        append_vcp_log([datetime.now(),word,mode])
    elif word in ['start']:
        inputter.press('u')
        time.sleep(input_sleep)
        inputter.release('u')
        append_vcp_log([datetime.now(),word,mode])
    elif word in ['select']:
        inputter.press('i')
        time.sleep(input_sleep)
        inputter.release('i')
        append_vcp_log([datetime.now(),word,mode])
    elif word in ['upright']:
        inputter.press('w')
        time.sleep(input_sleep)
        inputter.release('w')
        inputter.press('d')
        append_vcp_log([datetime.now(),'up',mode])
        time.sleep(input_sleep)
        inputter.release('d')
        append_vcp_log([datetime.now(),'right',mode])
    elif word in ['downright']:
        inputter.press('s')
        time.sleep(input_sleep)
        inputter.release('s')
        append_vcp_log([datetime.now(),'down',mode])
        inputter.press('d')
        time.sleep(input_sleep)
        inputter.release('d')
        append_vcp_log([datetime.now(),'right',mode])
    else:
        append_vcp_log([datetime.now(),word,'incorrect'])

def special_commands(cmnd):
    if cmnd.lower().startswith('go up'):
        print('How many steps? (up to 9)')
        distance = keyboard.read_key()
        for i in range(0, int(distance)):
            inputter.press('w')
            time.sleep(input_sleep)
            inputter.release('w')
            append_vcp_log([datetime.now(),'go up','special'])
    elif cmnd.lower().startswith('go left'):
        print('How many steps? (up to 9)')
        distance = keyboard.read_key()
        for i in range(0, int(distance)):
            inputter.press('a')
            time.sleep(input_sleep)
            inputter.release('a')
            append_vcp_log([datetime.now(),'go left','special'])
    elif cmnd.lower().startswith('go down'):
        print('How many steps? (up to 9)')
        distance = keyboard.read_key()
        for i in range(0, int(distance)):
            inputter.press('s')
            time.sleep(input_sleep)
            inputter.release('s')
            append_vcp_log([datetime.now(),'go down','special'])
    elif cmnd.lower().startswith('go right'):
        print('How many steps? (up to 9)')
        distance = keyboard.read_key()
        for i in range(0, int(distance)):
            inputter.press('d')
            time.sleep(input_sleep)
            inputter.release('d')
            append_vcp_log([datetime.now(),'go right','special'])
    else:
        basic_commands(cmnd, 'special')
        # time.sleep(input_sleep)

while True:
    print('Sequence [X] or Special [C]? (Press [esc] to escape)')
    pressed_key = keyboard.read_key()
    # print(pressed_key)
    if pressed_key == "x":
        print('You have chosen Sequence (multiple basic commands)')
        seq = rec_z()
        try:
            seq_list = seq.split()
            for c in seq_list:
                basic_commands(c, 'sequence')
                time.sleep(0.1)
        except AttributeError:
            pass
    elif pressed_key == 'c':
        print('You have chosen Special (single command; "go [direction]")')
        spe = rec_z()
        # print(spe)
        try:
            special_commands(spe)
        except AttributeError:
            pass
    elif pressed_key == 'esc':
        break
    # time.sleep(input_sleep)
    print('----------------------------------------------------------------------')