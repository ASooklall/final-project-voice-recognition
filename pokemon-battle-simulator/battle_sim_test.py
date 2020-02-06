import speech_recognition as sr
import pyaudio
import pygame, thorpy

pokemon_list = [
{'name':'pikachu','stats': {'health':3,'attack':1,'defense':1,'speed':1,'current_health':3}, 
 'moves':[{'name':'thundershock','power':1,'type':'electric'},{'name':'quick attack','power':1,'type':'normal'},{'name':'thunderbolt','power':1,'type':'electric'},{'name':'iron tail','power':1,'type':'steel'}],},
{'name':'mewtwo','stats':{'health':3,'attack':1,'defense':1,'speed':1,'current_health':3},
 'moves':[{'name':'psychic','power':1,'type':'psychic'},{'name':'swift','power':1,'type':'normal'},{'name':'recover','power':1,'type':'psychic'},{'name':'psybeam','power':1,'type':'psychic'}],},
{'name':'charizard','stats':{'health':3,'attack':1,'defense':1,'speed':1,'current_health':3},
 'moves':[{'name':'fire blast','power':1,'type':'fire'},{'name':'slash','power':1,'type':'normal'},{'name':'flamethrower','power':1,'type':'fire'},{'name':'steel wing','power':1,'type':'steel'}],},
{'name':'vensausaur','stats':{'health':3,'attack':1,'defense':1,'speed':1,'current_health':3},
 'moves':[{'name':'solar beam','power':1,'type':'grass'},{'name':'razor leaf','power':1,'type':'grass'},{'name':'take down','power':1,'type':'normal'},{'name':'earthquake','power':1,'type':'ground'}],},
{'name':'blastoise','stats':{'health':3,'attack':1,'defense':1,'speed':1,'current_health':3},
 'moves':[{'name':'surf','power':1,'type':'water'},{'name':'hydro pump','power':1,'type':'water'},{'name':'strength','power':1,'type':'normal'},{'name':'water gun','power':1,'type':'water'}],},
{'name':'eevee','stats':{'health':3,'attack':1,'defense':1,'speed':1,'current_health':3},
 'moves':[{'name':'quick attack','power':1,'type':'normal'},{'name':'swift','power':1,'type':'normal'},{'name':'take down','power':1,'type':'normal'},{'name':'last resort','power':1,'type':'normal'}],},
{'name':'onyx','stats':{'health':3,'attack':1,'defense':1,'speed':1,'current_health':3},
 'moves':[{'name':'dig','power':1,'type':'ground'},{'name':'iron tail','power':1,'type':'steel'},{'name':'stone edge','power':1,'type':'rock'},{'name':'slam','power':1,'type':'normal'}],},
{'name':'alakazam','stats':{'health':3,'attack':1,'defense':1,'speed':1,'current_health':3},
 'moves':[{'name':'psybeam','power':1,'type':'psychic'},{'name':'recover','power':1,'type':'normal'},{'name':'psychic','power':1,'type':'psychic'},{'name':'night shade','power':1,'type':'ghost'}],},
{'name':'gengar','stats':{'health':3,'attack':1,'defense':1,'speed':1,'current_health':3},
 'moves':[{'name':'shadow ball','power':1,'type':'ghost'},{'name':'dark pulse','power':1,'type':'dark'},{'name':'hypnosis','power':1,'type':'normal'},{'name':'dream eater','power':1,'type':'ghost'}],},
{'name':'nidoqueen','stats':{'health':3,'attack':1,'defense':1,'speed':1,'current_health':3},
 'moves':[{'name':'body slam','power':1,'type':'normal'},{'name':'super power','power':1,'type':'fighting'},{'name':'counter','power':1,'type':'fighting'},{'name':'dragon tail','power':1,'type':'dragon'}],},
{'name':'machamp','stats':{'health':3,'attack':1,'defense':1,'speed':1,'current_health':3},
 'moves':[{'name':'cross chop','power':1,'type':'fighting'},{'name':'dynamic punch','power':1,'type':'fighting'},{'name':'seismic toss','power':1,'type':'fighting'},{'name':'dual chop','power':1,'type':'dragon'}],},
]

# assign global test variables
global pkmn1
global pkmn2, mvnm1, mvnm2

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

def dict_test2():

    try:
        # Record in '(Pokemon Name) use (move)' format
        audio_play = rec_z().lower()
        audio_list = audio_play.split(' use')
        
#         print(audio_play)
#         print('---------')

        pokemon_name = audio_list[0].lower()

        move_audio = audio_list[1]

        # check if pokemon_name in pokemon database
        flag = False    #check to see if pokemon_name is found
        for pokemon in pokemon_list:

            if pokemon['name'] == pokemon_name:
                flag = True
                temp_moves = pokemon['moves']   # becomes our movelist
                choose_pokemon = pokemon
                choose_pokemon_name = pokemon['name']
                pkmn1 = choose_pokemon_name #test
        
        if flag == False:
            print("Sorry, we couldn't find your pokemon", pokemon_name)
        
#         print(temp_moves)
#         print ('-------------- \n')
        
        for mvs in temp_moves:
            if mvs['name'] in move_audio:
#                 print(mvs)
                choose_move = mvs
                choose_move_name = mvs['name']
                mvnm1 = choose_move_name #test
                
        print(f'{choose_pokemon_name} used {choose_move_name}! It did 1 damage, just because. \n\n{choose_pokemon}\n\n{choose_move}')
    
    except IndexError:
        print('Please try again, pokemon does not understand you. Say "use [move name here]"')

    

dict_test2()

print (pkmn1)