import speech_recognition as sr
import pyaudio
import keyboard, time

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
#         time.sleep(0.1)

def basic_commands(word):
    if word in ['a', 'yes']:
        keyboard.press_and_release('j')
    elif word in ['b', 'no', 'back']:
        keyboard.press_and_release('k')
    elif word in ['up']:
        keyboard.press_and_release('w')
    elif word in ['left']:
        keyboard.press_and_release('a')
    elif word in ['down']:
        keyboard.press_and_release('s')
    elif word in ['right']:
        keyboard.press_and_release('d')

while True:
    print('Sequence [X] or Special [C]? Press "esc" to escape')
    pressed_key = keyboard.read_key()
    print(pressed_key)
    if pressed_key == "x":
        print('You have chosen Sequence. Pls talk')
        seq = rec_z()
        seq_list = seq.split()
        for c in seq_list:
            basic_commands(c)
            time.sleep(0.1)
    elif pressed_key == 'c':
        print('You have chosen Special. Pls talk')
        spe = rec_z()
        basic_commands(spe)
    elif pressed_key == 'esc':
        break
    time.sleep(0.1)