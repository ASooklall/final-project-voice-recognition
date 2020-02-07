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

print('press "esc" to talk')
if keyboard.read_key() == "esc":
    sentence = rec_z()
    for letter in sentence:
        keyboard.press_and_release(letter)
        time.sleep(0.1)


# print('Sequence [X] or Special [C]')
# while True:
#     if keyboard.read_key() == "x":
#         print('You have chosen Sequence')
#         rec_z()
#     if keyboard.read_key() == 'c':
#         print('You have chosen Special')

