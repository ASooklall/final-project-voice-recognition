import speech_recognition as sr
import pyaudio, pygame, thorpy
import keyboard
import time, os
from pynput.keyboard import Key, Controller

controller = Controller()

pokemon_list = [
{'name':'pikachu','stats': {'health':3,'attack':1,'defense':1,'speed':1,'current_health':3}, 
 'moves':[{'name':'thundershock','power':1,'type':'electric'},{'name':'quick attack','power':1,'type':'normal'},{'name':'thunderbolt','power':1,'type':'electric'},{'name':'iron tail','power':1,'type':'steel'}],},
{'name':'mewtwo','stats':{'health':3,'attack':1,'defense':1,'speed':1,'current_health':3},
 'moves':[{'name':'psychic','power':1,'type':'psychic'},{'name':'swift','power':1,'type':'normal'},{'name':'recover','power':1,'type':'psychic'},{'name':'psybeam','power':1,'type':'psychic'}],},
{'name':'charizard','stats':{'health':3,'attack':1,'defense':1,'speed':1,'current_health':3},
 'moves':[{'name':'fire blast','power':1,'type':'fire'},{'name':'slash','power':1,'type':'normal'},{'name':'flamethrower','power':1,'type':'fire'},{'name':'steel wing','power':1,'type':'steel'}],},
{'name':'venusaur','stats':{'health':3,'attack':1,'defense':1,'speed':1,'current_health':3},
 'moves':[{'name':'solar beam','power':1,'type':'grass'},{'name':'razor leaf','power':1,'type':'grass'},{'name':'take down','power':1,'type':'normal'},{'name':'earthquake','power':1,'type':'ground'}],},
{'name':'blastoise','stats':{'health':3,'attack':1,'defense':1,'speed':1,'current_health':3},
 'moves':[{'name':'surf','power':1,'type':'water'},{'name':'hydro pump','power':1,'type':'water'},{'name':'strength','power':1,'type':'normal'},{'name':'water gun','power':1,'type':'water'}],},
{'name':'eevee','stats':{'health':3,'attack':1,'defense':1,'speed':1,'current_health':3},
 'moves':[{'name':'quick attack','power':1,'type':'normal'},{'name':'swift','power':1,'type':'normal'},{'name':'take down','power':1,'type':'normal'},{'name':'last resort','power':1,'type':'normal'}],},
{'name':'onyx','stats':{'health':3,'attack':1,'defense':1,'speed':1,'current_health':3},
 'moves':[{'name':'dig','power':1,'type':'ground'},{'name':'iron tail','power':1,'type':'steel'},{'name':'stone edge','power':1,'type':'rock'},{'name':'slam','power':1,'type':'normal'}],},
{'name':'alakazam','stats':{'health':3,'attack':1,'defense':1,'speed':1,'current_health':3},
 'moves':[{'name':'psybeam','power':1,'type':'psychic'},{'name':'recover','power':1,'type':'normal'},{'name':'psychic','power':1,'type':'psychic'},{'name':'night shade','power':1,'type':'ghost'}],},
{'name':'gengar','stats':{'health':3,'attack':1,'defense':1,'speed':2,'current_health':3},
 'moves':[{'name':'shadow ball','power':1,'type':'ghost'},{'name':'dark pulse','power':1,'type':'dark'},{'name':'hypnosis','power':1,'type':'normal'},{'name':'dream eater','power':1,'type':'ghost'}],},
{'name':'nidoqueen','stats':{'health':3,'attack':1,'defense':1,'speed':1,'current_health':3},
 'moves':[{'name':'body slam','power':1,'type':'normal'},{'name':'super power','power':1,'type':'fighting'},{'name':'counter','power':1,'type':'fighting'},{'name':'dragon tail','power':1,'type':'dragon'}],},
{'name':'machamp','stats':{'health':3,'attack':1,'defense':1,'speed':1,'current_health':3},
 'moves':[{'name':'cross chop','power':1,'type':'fighting'},{'name':'dynamic punch','power':1,'type':'fighting'},{'name':'seismic toss','power':1,'type':'fighting'},{'name':'dual chop','power':1,'type':'dragon'}],},
]

def rec():
    try:
        rt = sr.Recognizer()
        mic = sr.Microphone(device_index=0)
        with mic as source:
    #         rt.adjust_for_ambient_noise(source)
            # rt.energy_threshold = 20000
            rt.energy_threshole = 3000
            # rt.dynamic_energy_threshold = True
            rt.adjust_for_ambient_noise(source, duration = 0.6)
            # audio = rt.listen(source, timeout = 0.5)
            audio = rt.listen(source, timeout = 2.0)
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

        
def dict_test2():

    try:
        # Record in '(Pokemon Name) use (move)' format
        audio_play = rec().lower()
        audio_list = audio_play.split(' use')
        
#         print(audio_play)
#         print('---------')

        pokemon_name = audio_list[0].lower()

        move_audio = audio_list[1]

        # check if pokemon_name in pokemon database
        flag = False    #check to see if pokemon_name is found
        for pokemon in pokemon_list:

            if pokemon['name'] == pokemon_name:
                global pkmn1
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
                global mvnm1
                choose_move = mvs
                choose_move_name = mvs['name']
                mvnm1 = choose_move_name #test
                
        print(f'{choose_pokemon_name} used {choose_move_name}! It did 1 damage, just because. \n\n{choose_pokemon}\n\n{choose_move}')
    
    except IndexError:
        print('Please try again, pokemon does not understand you. Say "use [move name here]"')
    except AttributeError:
        print('Please try again, pokemon does not understand you. Say "use [move name here]"')





        
        
def battle_init():
    global p1_pokemon, p1_choice, p1_name_check, p1speed, p1atk, p1def, p1move1, p1move2, p1move3, p1move4, p1maxhp, p1curhp, p1_hpbarsize
    global p2_pokemon, p2_choice, p2_name_check, p2speed, p2atk, p2def, p2move1, p2move2, p2move3, p2move4, p2maxhp, p2curhp, p2_hpbarsize

    p1_name_check = False
    p2_name_check = False

    p_name_list = []
    for pokemon in pokemon_list:
        p_name_list.append(pokemon['name'])
        
    checker = True
    
    while checker == True:
        if p1_name_check == False:
            prompt_1 = 'Player 1 Choose Your Pokemon'
            print(prompt_1)
            tb_h = thorpy.Element(text=('Player 1'))
            tb_h.set_font_size(24)
            tb_h.set_size((750, 50))
            tb_h.set_center((720, 375))
            tb_h.blit()
            tb_h.update()
            
            tb = thorpy.Element(text=(prompt_1))
            tb.set_font_size(20)
            tb.set_size((750,150))
            tb.stick_to(tb_h, target_side="bottom", self_side="top")
            tb.blit()
            tb.update()
            
            try: 
                audio_play = rec().lower()
            except:
                try: 
                    prompt_1 = 'Please say your pokemon choice clearly after 1 second.'
                    print(prompt_1)
                    tb = thorpy.Element(text=(prompt_1))
                    tb.set_font_size(20)
                    tb.set_size((750,150))
                    tb.stick_to(tb_h, target_side="bottom", self_side="top")
                    tb.blit()
                    tb.update()
                    time.sleep(1)
                    audio_play = rec().lower()
                except:
                    prompt_1 = 'Cannot hear a voice command, choosing default pokemon of pikachu.'
                    print(prompt_1)
                    tb = thorpy.Element(text=(prompt_1))
                    tb.set_font_size(20)
                    tb.set_size((750,150))
                    tb.stick_to(tb_h, target_side="bottom", self_side="top")
                    tb.blit()
                    tb.update()
                    audio_play = 'pikachu'
            audio_list = audio_play.split(' ')
            for word in audio_list:
                if word in p_name_list:
                     p1_choice = word
                else:
                    prompt_1 = 'You did not choose an appropriate pokemon, default is pikachu.'
                    print(prompt_1)
                    tb = thorpy.Element(text=(prompt_1))
                    tb.set_font_size(20)
                    tb.set_size((750,150))
                    tb.stick_to(tb_h, target_side="bottom", self_side="top")
                    tb.blit()
                    tb.update()
                    p1_choice = 'pikachu'
            for pokemon in pokemon_list:
                if p1_choice == pokemon['name']:
                    p1_pokemon = pokemon
                    p1move1 = pokemon['moves'][0]['name']
                    p1move2 = pokemon['moves'][1]['name']
                    p1move3 = pokemon['moves'][2]['name']
                    p1move4 = pokemon['moves'][3]['name']
                    p1speed = pokemon['stats']['speed']
                    p1atk = pokemon['stats']['attack']
                    p1def = pokemon['stats']['defense']
                    p1maxhp = pokemon['stats']['health']
                    p1curhp = p1maxhp
                    p1_hpbarsize = 200 * (p1curhp/p1maxhp)
                    
                    p1_p_h = thorpy.Element(text=('Player 1 Pokemon'))
                    p1_p_h.set_font_size(30)
                    p1_p_h.set_font_color((0,0,255))
                    p1_p_h.set_size((500,50))
                    p1_p_h.set_topleft((25,25))
                    p1_p_h.blit()
                    p1_p_h.update()

                    p1_p = thorpy.Element(text=(p1_choice))
                    p1_p.set_font_size(35)
                    p1_p.set_font_color((0,0,0))
                    p1_p.set_size((500,100))
                    p1_p.stick_to(p1_p_h, target_side="bottom", self_side="top")
                    p1_p.blit()
                    p1_p.update()

                    p1_m = thorpy.Element(text=('P1 Movelist'))
                    p1_m.set_font_size(20)
                    p1_m.set_font_color((0,0,255))
                    p1_m.set_size((250,100))
                    p1_m.set_center((150, 250))
                    p1_m.blit()
                    p1_m.update()

                    p1_m1 = thorpy.Element(text=(p1move1))
                    p1_m1.set_font_size(20)
                    p1_m1.set_size((250,100))
                    p1_m1.stick_to(p1_m, target_side="bottom", self_side="top")
                    p1_m1.blit()
                    p1_m1.update()

                    p1_m2 = thorpy.Element(text=(p1move2))
                    p1_m2.set_font_size(20)
                    p1_m2.set_size((250,100))
                    p1_m2.stick_to(p1_m1, target_side="bottom", self_side="top")
                    p1_m2.blit()
                    p1_m2.update()

                    p1_m3 = thorpy.Element(text=(p1move3))
                    p1_m3.set_font_size(20)
                    p1_m3.set_size((250,100))
                    p1_m3.stick_to(p1_m2, target_side="bottom", self_side="top")
                    p1_m3.blit()
                    p1_m3.update()

                    p1_m4 = thorpy.Element(text=(p1move4))
                    p1_m4.set_font_size(20)
                    p1_m4.set_size((250,100))
                    p1_m4.stick_to(p1_m3, target_side="bottom", self_side="top")
                    p1_m4.blit()
                    p1_m4.update()

                    p1_mhp_bar = thorpy.Element(text=('P1 Health Bar'))
                    p1_mhp_bar.set_font_size(12)
                    p1_mhp_bar.set_font_color((0,0,255))
                    p1_mhp_bar.set_size((210,30))
                    p1_mhp_bar.set_topleft((45, 815))
                    p1_mhp_bar.blit()
                    p1_mhp_bar.update()
                    
                    p1_hp_box = thorpy.Element(text=(f'HP: {p1curhp}/{p1maxhp}'))
                    p1_hp_box.set_font_size(16)
                    p1_hp_box.set_font_color((0,0,0))
                    p1_hp_box.set_size((100,35))
                    p1_hp_box.stick_to(p1_mhp_bar, target_side="top", self_side="bottom")
                    p1_hp_box.blit()
                    p1_hp_box.update()

                    p1_chp_bar = pygame.draw.rect(screen, (0, 255, 0), (50, 820, p1_hpbarsize, 20), 0)

                    time.sleep(0.1)
                    p1_i = pygame.image.load(os.path.join("images",str(p1_choice)+"_back.png")).convert()
                    p1_i = pygame.transform.scale(p1_i, (300,300))
                    # Bound image to rectangle and move rectangle to place image
                    p1_i_r = p1_i.get_rect()
                    p1_i_r = p1_i_r.move((300,575))
                    screen.blit(p1_i, p1_i_r)
                
            prompt_1 = f'P1 Chooses: {p1_choice}'
            print(prompt_1)
            tb = thorpy.Element(text=(prompt_1))
            tb.set_font_size(20)
            tb.set_size((750,150))
            tb.stick_to(tb_h, target_side="bottom", self_side="top")
            tb.blit()
            tb.update()

            print(p1move1,p1move2,p1move3,p1move4)
            p1_name_check = True
            time.sleep(0.5)

        elif (p1_name_check == True) and (p2_name_check == False):
            prompt_2 = 'Player 2 Choose Your Pokemon'
            print(prompt_2)
            tb_h = thorpy.Element(text=('Player 2'))
            tb_h.set_font_size(24)
            tb_h.set_size((750, 50))
            tb_h.set_center((720, 375))
            tb_h.blit()
            tb_h.update()
            
            tb = thorpy.Element(text=(prompt_2))
            tb.set_font_size(20)
            tb.set_size((750,150))
            tb.stick_to(tb_h, target_side="bottom", self_side="top")
            tb.blit()
            tb.update()
            try: 
                audio_play = rec().lower()
            except:
                try: 
                    prompt_2 = 'Please say your pokemon choice clearly after 1 second.'
                    print(prompt_2)
                    tb = thorpy.Element(text=(prompt_2))
                    tb.set_font_size(20)
                    tb.set_size((750,150))
                    tb.stick_to(tb_h, target_side="bottom", self_side="top")
                    tb.blit()
                    tb.update()
                    time.sleep(1)
                    audio_play = rec().lower()
                except:
                    prompt_2 = 'Cannot hear a voice command, choosing default pokemon of pikachu.'
                    print(prompt_2)
                    tb = thorpy.Element(text=(prompt_2))
                    tb.set_font_size(20)
                    tb.set_size((750,150))
                    tb.stick_to(tb_h, target_side="bottom", self_side="top")
                    tb.blit()
                    tb.update()
                    audio_play = 'pikachu'
            audio_list = audio_play.split(' ')
            for word in audio_list:
                if word in p_name_list:
                     p2_choice = word
                else:
                    prompt_2 = 'You did not choose an appropriate pokemon, default is pikachu.'
                    print(prompt_2)
                    tb = thorpy.Element(text=(prompt_2))
                    tb.set_font_size(20)
                    tb.set_size((750,150))
                    tb.stick_to(tb_h, target_side="bottom", self_side="top")
                    tb.blit()
                    tb.update()
                    p2_choice = 'pikachu'
            for pokemon in pokemon_list:
                if p2_choice == pokemon['name']:
                    p2_pokemon = pokemon
                    p2move1 = pokemon['moves'][0]['name']
                    p2move2 = pokemon['moves'][1]['name']
                    p2move3 = pokemon['moves'][2]['name']
                    p2move4 = pokemon['moves'][3]['name']
                    p2speed = pokemon['stats']['speed']
                    p2atk = pokemon['stats']['attack']
                    p2def = pokemon['stats']['defense']
                    p2maxhp = pokemon['stats']['health']
                    p2curhp = p2maxhp
                    p2_hpbarsize = 200 * (p2curhp/p2maxhp)
                    
                    p2_p_h = thorpy.Element(text=('Player 2 Pokemon'))
                    p2_p_h.set_font_size(30)
                    p2_p_h.set_font_color((255,0,0))
                    p2_p_h.set_size((500,50))
                    p2_p_h.set_topleft((915,725))
                    p2_p_h.blit()
                    p2_p_h.update()

                    p2_m = thorpy.Element(text=('P2 Movelist'))
                    p2_m.set_font_size(20)
                    p2_m.set_font_color((255,0,0))
                    p2_m.set_size((250,100))
                    p2_m.set_center((1290, 250))
                    p2_m.blit()
                    p2_m.update()

                    p2_p = thorpy.Element(text=(p2_choice))
                    p2_p.set_font_size(35)
                    p2_p.set_font_color((0,0,0))
                    p2_p.set_size((500,100))
                    p2_p.stick_to(p2_p_h, target_side="bottom", self_side="top")
                    p2_p.blit()
                    p2_p.update()

                    p2_m1 = thorpy.Element(text=(p2move1))
                    p2_m1.set_font_size(20)
                    p2_m1.set_size((250,100))
                    p2_m1.stick_to(p2_m, target_side="bottom", self_side="top")
                    p2_m1.blit()
                    p2_m1.update()
                    
                    p2_m2 = thorpy.Element(text=(p2move2))
                    p2_m2.set_font_size(20)
                    p2_m2.set_size((250,100))
                    p2_m2.stick_to(p2_m1, target_side="bottom", self_side="top")
                    p2_m2.blit()
                    p2_m2.update()
                    
                    p2_m3 = thorpy.Element(text=(p2move3))
                    p2_m3.set_font_size(20)
                    p2_m3.set_size((250,100))
                    p2_m3.stick_to(p2_m2, target_side="bottom", self_side="top")
                    p2_m3.blit()
                    p2_m3.update()
                    
                    p2_m4 = thorpy.Element(text=(p2move4))
                    p2_m4.set_font_size(20)
                    p2_m4.set_size((250,100))
                    p2_m4.stick_to(p2_m3, target_side="bottom", self_side="top")
                    p2_m4.blit()
                    p2_m4.update()


                    p2_mhp_bar = thorpy.Element(text=('P2 Health Bar'))
                    p2_mhp_bar.set_font_size(12)
                    p2_mhp_bar.set_font_color((0,0,255))
                    p2_mhp_bar.set_size((210,30))
                    p2_mhp_bar.set_topleft((1185, 85))
                    p2_mhp_bar.blit()
                    p2_mhp_bar.update()

                    p2_hp_box = thorpy.Element(text=(f'HP: {p2curhp}/{p2maxhp}'))
                    p2_hp_box.set_font_size(16)
                    p2_hp_box.set_font_color((0,0,0))
                    p2_hp_box.set_size((100,35))
                    p2_hp_box.stick_to(p2_mhp_bar, target_side="top", self_side="bottom")
                    p2_hp_box.blit()
                    p2_hp_box.update()

                    p2_chp_bar = pygame.draw.rect(screen, (0, 255, 0), (1190, 90, p2_hpbarsize, 20), 0)

                    time.sleep(0.1)

                    p2_i = pygame.image.load(os.path.join("images",str(p2_choice)+"_front.png")).convert()
                    p2_i = pygame.transform.scale(p2_i, (300,300))
                    # Place image in bounding rectangle and select rectangle location
                    p2_i_r = p2_i.get_rect()
                    p2_i_r = p2_i_r.move((840,25))
                    screen.blit(p2_i, p2_i_r)
                    
                    
            prompt_2 = f'P2 Chooses: {p2_choice}'
            print(prompt_2)
            tb = thorpy.Element(text=(prompt_2))
            tb.set_font_size(20)
            tb.set_size((750,150))
            tb.stick_to(tb_h, target_side="bottom", self_side="top")
            tb.blit()
            tb.update()

            
            print(p2move1,p2move2,p2move3,p2move4)
            p2_name_check = True
            time.sleep(0.5)

        else:
            checker = False

    print('\n-----\n')
    choice_prompt = f'Player 1 is using {p1_choice} and Player 2 is using {p2_choice}'
    print(choice_prompt)

    tb_h = thorpy.Element(text=('Annoucements:'))
    tb_h.set_font_size(24)
    tb_h.set_size((750, 50))
    tb_h.set_center((720, 375))
    tb_h.blit()
    tb_h.update()

    tb = thorpy.Element(text=(choice_prompt))
    tb.set_font_size(20)
    tb.set_size((750,150))
    tb.stick_to(tb_h, target_side="bottom", self_side="top")
    tb.blit()
    tb.update()


# def choose_move():
#     #record audio
#     #split audio
#     #search split array for match in player's movepement m1/m2/m3/m4 list
#     #if move matches -> return move info as vars for name, priority (0 for now) type, power
#     # save values to player vars
                
    # audio_play = rec().lower()
    # audio_list = audio_play.split(' ')



    # temp_moves = p1_pokemon['moves']
    # for mvs in temp_moves:
    #     if mvs['name'] in audio_list:
    #         p1_movename = mvs['name']
    #         p1_movetype = mvs['type']
    #         p1_movepower = int(mvs['power'])

#             if pokemon['name'] == pokemon_name:
#                 global pkmn1
#                 flag = True
#                 temp_moves = pokemon['moves']   # becomes our movelist
#                 choose_pokemon = pokemon
#                 choose_pokemon_name = pokemon['name']
#                 pkmn1 = choose_pokemon_name #test
        
#         if flag == False:
#             print("Sorry, we couldn't find your pokemon", pokemon_name)
        
# #         print(temp_moves)
# #         print ('-------------- \n')
        
#         for mvs in temp_moves:
#             if mvs['name'] in move_audio:
# #                 print(mvs)
#                 global mvnm1
#                 choose_move = mvs
#                 choose_move_name = mvs['name']
#                 mvnm1 = choose_move_name

# for pokemon in pokemon_list:
#     if pokemon['name'] == p1_choice


#     for word in audio_list:
#         if word == p1_m4:
#             p1_movepriority = 0
#             p1_movetype = str(p1_pokemon['moves'][3]['type'])
#             p1_movepower = int(p1_pokemon['moves'][3]['power'])
#         elif word == p1_m3:
#             p1_movepriority = 0
#             p1_movetype = str(p1_pokemon['moves'][2]['type'])
#             p1_movepower = int(p1_pokemon['moves'][2]['power'])
#         elif word == p1_m2:
#             p1_movepriority = 0
#             p1_movetype = str(p1_pokemon['moves'][1]['type'])
#             p1_movepower = int(p1_pokemon['moves'][1]['power'])
#         else:
#             #default to move1
#             p1_movepriority = 0
#             p1_movetype = str(p1_pokemon['moves'][0]['type'])
#             p1_movepower = int(p1_pokemon['moves'][0]['power'])






def battle_execute():
    global p1_pokemon, p1_choice, p1_movepriority, p1_movetype, p1_movepower, p1_movename, p1curhp, p1atk, p1speed, p1def, p1_m1, p1_m2, p1_m3, p1_m4, p1maxhp, p1_hpbarsize
    global p2_pokemon, p2_choice, p2_movepriority, p2_movetype, p2_movepower, p2_movename, p2curhp, p2atk, p2speed, p2def, p2_m1, p2_m2, p2_m3, p2_m4, p2maxhp, p2_hpbarsize
    global winner, loser, loser_pokemon
    
    print(p1_pokemon, '\n',p2_pokemon)

    while (p1curhp > 0) and (p2curhp > 0):
        tb = thorpy.Element(text=(f'Player 1 Move Choice. Press M when ready to choose move.'))
        tb.set_font_size(20)
        tb.set_size((750,150))
        tb.stick_to(tb_h, target_side="bottom", self_side="top")
        tb.blit()
        tb.update()

        print('press m to talk')
        key = keyboard.read_key()
        print(key)
        if key == "m":
            tb = thorpy.Element(text=(f'Player 1, please say your move now.'))
            tb.set_font_size(20)
            tb.set_size((750,150))
            tb.stick_to(tb_h, target_side="bottom", self_side="top")
            tb.blit()
            tb.update()

            time.sleep(0.2)
            try:
                audio_play = rec().lower()
                # audio_list = audio_play.split(' ')

                temp_moves = p1_pokemon['moves']
                for mvs in temp_moves:
                    if mvs['name'] in audio_play:
                        p1_movename = mvs['name']
                        p1_movetype = mvs['type']
                        p1_movepower = int(mvs['power'])
                        p1_movepriority = 0
                    elif mvs['name'].title() in audio_play:
                        p1_movename = mvs['name']
                        p1_movetype = mvs['type']
                        p1_movepower = int(mvs['power'])
                        p1_movepriority = 0
                    else:
                        p1_movename = temp_moves[0]['name']
                        p1_movetype = temp_moves[0]['type']
                        p1_movepower = int(temp_moves[0]['power'])
                        p1_movepriority = 0
            except AttributeError: 
                try:
                    tb = thorpy.Element(text=(f'{p1_choice} could not understand you. Please try again. '))
                    tb.set_font_size(20)
                    tb.set_size((750,150))
                    tb.stick_to(tb_h, target_side="bottom", self_side="top")
                    tb.blit()
                    tb.update()

                    time.sleep(0.5)

                    audio_play = rec().lower()
                    # audio_list = audio_play.split(' ')

                    temp_moves = p1_pokemon['moves']
                    for mvs in temp_moves:
                        if mvs['name'] in audio_play:
                            p1_movename = mvs['name']
                            p1_movetype = mvs['type']
                            p1_movepower = int(mvs['power'])
                            p1_movepriority = 0
                        elif mvs['name'].title() in audio_play:
                            p1_movename = mvs['name']
                            p1_movetype = mvs['type']
                            p1_movepower = int(mvs['power'])
                            p1_movepriority = 0
                        else:
                            p1_movename = temp_moves[0]['name']
                            p1_movetype = temp_moves[0]['type']
                            p1_movepower = int(temp_moves[0]['power'])
                            p1_movepriority = 0
                except AttributeError:
                    temp_moves = p1_pokemon['moves']
                    p1_movename = temp_moves[0]['name']
                    p1_movetype = temp_moves[0]['type']
                    p1_movepower = int(temp_moves[0]['power'])
                    p1_movepriority = 0


            print(f'test // recognized: {audio_play} \ncompared to {temp_moves} \nchosen: {p1_movename}')
        print('you used ', p1_movename)
        tb = thorpy.Element(text=(f'Player 1 chose {p1_movename}.'))
        tb.set_font_size(20)
        tb.set_size((750,150))
        tb.stick_to(tb_h, target_side="bottom", self_side="top")
        tb.blit()
        tb.update()

        time.sleep(3)

        tb = thorpy.Element(text=(f'Player 2 Move Choice. Press M when ready to choose move.'))
        tb.set_font_size(20)
        tb.set_size((750,150))
        tb.stick_to(tb_h, target_side="bottom", self_side="top")
        tb.blit()
        tb.update()

        print('press m to talk')
        key = keyboard.read_key()
        print(key)
        if key == "m":
            tb = thorpy.Element(text=(f'Player 2, please say your move now.'))
            tb.set_font_size(20)
            tb.set_size((750,150))
            tb.stick_to(tb_h, target_side="bottom", self_side="top")
            tb.blit()
            tb.update()

            time.sleep(0.2)

            # audio_play = rec().lower()

            # temp_moves = p2_pokemon['moves']
            # for mvs in temp_moves:
            #     if mvs['name'] in audio_play:
                    # p2_movename = mvs['name']
                    # p2_movetype = mvs['type']
                    # p2_movepower = int(mvs['power'])
                    # p2_movepriority = 0
            #     elif mvs['name'].title() in audio_play:
            #         p2_movename = mvs['name']
            #         p2_movetype = mvs['type']
            #         p2_movepower = int(mvs['power'])
            #         p2_movepriority = 0
            #     else:
            #         p2_movename = temp_moves[0]['name']
            #         p2_movetype = temp_moves[0]['type']
            #         p2_movepower = int(temp_moves[0]['power'])
            #         p2_movepriority = 0

            try:
                audio_play = rec().lower()
                # audio_list = audio_play.split(' ')

                temp_moves = p2_pokemon['moves']
                for mvs in temp_moves:
                    if mvs['name'] in audio_play:
                        p2_movename = mvs['name']
                        p2_movetype = mvs['type']
                        p2_movepower = int(mvs['power'])
                        p2_movepriority = 0
                    elif mvs['name'].title() in audio_play:
                        p2_movename = mvs['name']
                        p2_movetype = mvs['type']
                        p2_movepower = int(mvs['power'])
                        p2_movepriority = 0
                    else:
                        p2_movename = mvs['name']
                        p2_movetype = mvs['type']
                        p2_movepower = int(mvs['power'])
                        p2_movepriority = 0
            except AttributeError: 
                try:
                    tb = thorpy.Element(text=(f'{p2_choice} could not understand you. Please try again. '))
                    tb.set_font_size(20)
                    tb.set_size((750,150))
                    tb.stick_to(tb_h, target_side="bottom", self_side="top")
                    tb.blit()
                    tb.update()

                    time.sleep(0.5)

                    audio_play = rec().lower()
                    # audio_list = audio_play.split(' ')

                    temp_moves = p2_pokemon['moves']
                    for mvs in temp_moves:
                        if mvs['name'] in audio_play:
                            p2_movename = mvs['name']
                            p2_movetype = mvs['type']
                            p2_movepower = int(mvs['power'])
                            p2_movepriority = 0
                        elif mvs['name'].title() in audio_play:
                            p2_movename = mvs['name']
                            p2_movetype = mvs['type']
                            p2_movepower = int(mvs['power'])
                            p2_movepriority = 0
                        else:
                            p2_movename = mvs['name']
                            p2_movetype = mvs['type']
                            p2_movepower = int(mvs['power'])
                            p2_movepriority = 0
                except AttributeError:
                    temp_moves = p2_pokemon['moves']
                    p2_movename = mvs['name']
                    p2_movetype = mvs['type']
                    p2_movepower = int(mvs['power'])
                    p2_movepriority = 0
            


            print(f'test // recognized: {audio_play} \ncompared to {temp_moves} \nchosen: {p2_movename}')
        print('you used ', p2_movename)
        tb = thorpy.Element(text=(f'Player 2 chose {p2_movename}.'))
        tb.set_font_size(20)
        tb.set_size((750,150))
        tb.stick_to(tb_h, target_side="bottom", self_side="top")
        tb.blit()
        tb.update()

        time.sleep(2)



        p1_turnspeed = int(p1speed) + (int(p1_movepriority)*1000)
        p2_turnspeed = int(p2speed) + (int(p2_movepriority)*1000)

        if p1_turnspeed > p2_turnspeed:
            print('p1fast gofirst')
            tb = thorpy.Element(text=(f'{p1_choice} used {p1_movename}! It did {int(p1_movepower * (p1atk/p2def))} damage to {p2_choice}'))
            tb.set_font_size(20)
            tb.set_size((750,150))
            tb.stick_to(tb_h, target_side="bottom", self_side="top")
            tb.blit()
            tb.update()

            p2curhp = p2curhp - int((p1_movepower * (p1atk / p2def)))
            p2_hpbarsize = 200 * (p2curhp/p2maxhp)
            p2_hpbarsize = round(p2_hpbarsize, 0)

            p2_mhp_bar = thorpy.Element(text=(' '))
            p2_mhp_bar.set_font_size(12)
            p2_mhp_bar.set_font_color((0,0,255))
            p2_mhp_bar.set_size((210,30))
            p2_mhp_bar.set_topleft((1185, 85))
            p2_mhp_bar.blit()
            p2_mhp_bar.update()

            p2_hp_box = thorpy.Element(text=(f'HP: {p2curhp}/{p2maxhp}'))
            p2_hp_box.set_font_size(16)
            p2_hp_box.set_font_color((0,0,0))
            p2_hp_box.set_size((100,35))
            p2_hp_box.stick_to(p2_mhp_bar, target_side="top", self_side="bottom")
            p2_hp_box.blit()
            p2_hp_box.update()

            p2_chp_bar = pygame.draw.rect(screen, (0, 255, 0), (1190, 90, p2_hpbarsize, 20), 0)

            time.sleep(3)

            print('p1atks', p2curhp)
            if p2curhp > 0:
                tb = thorpy.Element(text=(f'{p2_choice} used {p2_movename}! It did {int(p2_movepower * (p2atk/p1def))} damage to {p1_choice}'))
                tb.set_font_size(20)
                tb.set_size((750,150))
                tb.stick_to(tb_h, target_side="bottom", self_side="top")
                tb.blit()
                tb.update()

                p1curhp = p1curhp - int((p2_movepower * (p2atk / p1def)))
                p1_hpbarsize = 200 * (p1curhp/p1maxhp)
                p1_hpbarsize = round(p1_hpbarsize, 0)

                p1_mhp_bar = thorpy.Element(text=(' '))
                p1_mhp_bar.set_font_size(12)
                p1_mhp_bar.set_font_color((0,0,255))
                p1_mhp_bar.set_size((210,30))
                p1_mhp_bar.set_topleft((45, 815))
                p1_mhp_bar.blit()
                p1_mhp_bar.update()
                
                p1_hp_box = thorpy.Element(text=(f'HP: {p1curhp}/{p1maxhp}'))
                p1_hp_box.set_font_size(16)
                p1_hp_box.set_font_color((0,0,0))
                p1_hp_box.set_size((100,35))
                p1_hp_box.stick_to(p1_mhp_bar, target_side="top", self_side="bottom")
                p1_hp_box.blit()
                p1_hp_box.update()

                p1_chp_bar = pygame.draw.rect(screen, (0, 255, 0), (50, 820, p1_hpbarsize, 20), 0)


                print('p2atks', p1curhp)

        elif p2_turnspeed > p1_turnspeed:
            print('p2fast gofirst')
            tb = thorpy.Element(text=(f'{p2_choice} used {p2_movename}! It did {int(p2_movepower * (p2atk/p1def))} damage to {p1_choice}'))
            tb.set_font_size(20)
            tb.set_size((750,150))
            tb.stick_to(tb_h, target_side="bottom", self_side="top")
            tb.blit()
            tb.update()

            p1curhp = p1curhp - int((p2_movepower * (p2atk/p1def)))
            p1_hpbarsize = 200 * (p1curhp/p1maxhp)
            p1_hpbarsize = round(p1_hpbarsize, 0)

            p1_mhp_bar = thorpy.Element(text=(' '))
            p1_mhp_bar.set_font_size(12)
            p1_mhp_bar.set_font_color((0,0,255))
            p1_mhp_bar.set_size((210,30))
            p1_mhp_bar.set_topleft((45, 815))
            p1_mhp_bar.blit()
            p1_mhp_bar.update()
            
            p1_hp_box = thorpy.Element(text=(f'HP: {p1curhp}/{p1maxhp}'))
            p1_hp_box.set_font_size(16)
            p1_hp_box.set_font_color((0,0,0))
            p1_hp_box.set_size((100,35))
            p1_hp_box.stick_to(p1_mhp_bar, target_side="top", self_side="bottom")
            p1_hp_box.blit()
            p1_hp_box.update()

            p1_chp_bar = pygame.draw.rect(screen, (0, 255, 0), (50, 820, p1_hpbarsize, 20), 0)
            print('p2atks', p1curhp)

            time.sleep(3)

            if p1curhp > 0:
                tb = thorpy.Element(text=(f'{p1_choice} used {p1_movename}! It did {int(p1_movepower * (p1atk/p2def))} damage to {p2_choice}'))
                tb.set_font_size(20)
                tb.set_size((750,150))
                tb.stick_to(tb_h, target_side="bottom", self_side="top")
                tb.blit()
                tb.update()

                p2curhp = p2curhp - int((p1_movepower * (p1atk / p2def)))
                p2_hpbarsize = 200 * (p2curhp/p2maxhp)
                p2_hpbarsize = round(p2_hpbarsize, 0)

                p2_mhp_bar = thorpy.Element(text=(' '))
                p2_mhp_bar.set_font_size(12)
                p2_mhp_bar.set_font_color((0,0,255))
                p2_mhp_bar.set_size((210,30))
                p2_mhp_bar.set_topleft((1185, 85))
                p2_mhp_bar.blit()
                p2_mhp_bar.update()

                p2_hp_box = thorpy.Element(text=(f'HP: {p2curhp}/{p2maxhp}'))
                p2_hp_box.set_font_size(16)
                p2_hp_box.set_font_color((0,0,0))
                p2_hp_box.set_size((100,35))
                p2_hp_box.stick_to(p2_mhp_bar, target_side="top", self_side="bottom")
                p2_hp_box.blit()
                p2_hp_box.update()

                p2_chp_bar = pygame.draw.rect(screen, (0, 255, 0), (1190, 90, p2_hpbarsize, 20), 0)
                print('p1atks', p2curhp)
        else:
            print('nobodyfast p1first')
            tb = thorpy.Element(text=(f'{p1_choice} used {p1_movename}! It did {int(p1_movepower * (p1atk/p2def))} damage to {p2_choice}'))
            tb.set_font_size(20)
            tb.set_size((750,150))
            tb.stick_to(tb_h, target_side="bottom", self_side="top")
            tb.blit()
            tb.update()

            p2curhp = p2curhp - int((p1_movepower * (p1atk / p2def)))
            p2_hpbarsize = 200 * (p2curhp/p2maxhp)
            p2_hpbarsize = round(p2_hpbarsize, 0)

            p2_mhp_bar = thorpy.Element(text=(' '))
            p2_mhp_bar.set_font_size(12)
            p2_mhp_bar.set_font_color((0,0,255))
            p2_mhp_bar.set_size((210,30))
            p2_mhp_bar.set_topleft((1185, 85))
            p2_mhp_bar.blit()
            p2_mhp_bar.update()

            p2_hp_box = thorpy.Element(text=(f'HP: {p2curhp}/{p2maxhp}'))
            p2_hp_box.set_font_size(16)
            p2_hp_box.set_font_color((0,0,0))
            p2_hp_box.set_size((100,35))
            p2_hp_box.stick_to(p2_mhp_bar, target_side="top", self_side="bottom")
            p2_hp_box.blit()
            p2_hp_box.update()

            p2_chp_bar = pygame.draw.rect(screen, (0, 255, 0), (1190, 90, p2_hpbarsize, 20), 0)
            print('p1atks', p2curhp)

            time.sleep(3)

            if p2curhp > 0:
                tb = thorpy.Element(text=(f'{p2_choice} used {p2_movename}! It did {int(p2_movepower * (p2atk/p1def))} damage to {p1_choice}'))
                tb.set_font_size(20)
                tb.set_size((750,150))
                tb.stick_to(tb_h, target_side="bottom", self_side="top")
                tb.blit()
                tb.update()

                p1curhp = p1curhp - (int(p2_movepower * (p2atk / p1def)))
                p1_hpbarsize = 200 * (p1curhp/p1maxhp)
                p1_hpbarsize = round(p1_hpbarsize, 0)

                p1_mhp_bar = thorpy.Element(text=(' '))
                p1_mhp_bar.set_font_size(12)
                p1_mhp_bar.set_font_color((0,0,255))
                p1_mhp_bar.set_size((210,30))
                p1_mhp_bar.set_topleft((45, 815))
                p1_mhp_bar.blit()
                p1_mhp_bar.update()
                
                p1_hp_box = thorpy.Element(text=(f'HP: {p1curhp}/{p1maxhp}'))
                p1_hp_box.set_font_size(16)
                p1_hp_box.set_font_color((0,0,0))
                p1_hp_box.set_size((100,35))
                p1_hp_box.stick_to(p1_mhp_bar, target_side="top", self_side="bottom")
                p1_hp_box.blit()
                p1_hp_box.update()

                p1_chp_bar = pygame.draw.rect(screen, (0, 255, 0), (50, 820, p1_hpbarsize, 20), 0)
                print('p2atks', p1curhp)

        time.sleep(3)

        # p1_chp_bar = pygame.draw.rect(screen, (0, 255, 0), (50, 820, p1_hpbarsize, 20), 0)
        # p2_chp_bar = pygame.draw.rect(screen, (0, 255, 0), (1190, 90, p2_hpbarsize, 20), 0)

    if p1curhp <= 0:
        print('p1died')
        loser = "Player 1"
        loser_pokemon = p1_pokemon['name']
        winner = "Player 2"

        tb = thorpy.Element(text=(f'{loser_pokemon} has fainted!'))
        tb.set_font_size(20)
        tb.set_size((750,150))
        tb.stick_to(tb_h, target_side="bottom", self_side="top")
        tb.blit()
        tb.update()
        time.sleep(2)

    elif p2curhp <= 0:
        print('p2died')
        loser = "Player 2"
        loser_pokemon = p2_pokemon['name']
        winner = "Player 1"

        tb = thorpy.Element(text=(f'{loser_pokemon} has fainted!'))
        tb.set_font_size(20)
        tb.set_size((750,150))
        tb.stick_to(tb_h, target_side="bottom", self_side="top")
        tb.blit()
        tb.update()
        time.sleep(2)

####################################
##### Initialize Pygame Engine #####
####################################
class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location


pygame.init()
pygame.key.set_repeat(300, 30) #set behavior for key repeats (delay,inteval)
screen = pygame.display.set_mode((1440,900))
BackGround1 = Background('images/bg5_rescaled.png', [0,0])
BackGround2 = Background('images/bg6_rescaled.png', [0,0])


pygame.display.set_caption('Pokemon Voice Battle Simulator')

screen.fill((255,255,255))
screen.blit(BackGround1.image, BackGround1.rect)

clock = pygame.time.Clock()
pygame.display.flip()

pkmn1 = ''


################################
##### Battle Announcements #####
################################

tb_h = thorpy.Element(text=('Announcements:'))
tb_h.set_font_size(24)
tb_h.set_size((750, 50))
tb_h.set_center((720, 375))
tb_h.blit()
tb_h.update()

tb = thorpy.Element(text=('\
                Welcome to Pokemon Battle Simulator! \n \
    Use voice commands to choose your pokemon and battle. \n \
                Please read prompts to play the game. \n \
                    To begin a match, press the S.'))
tb.set_font_size(20)
tb.set_size((750,150))
tb.stick_to(tb_h, target_side="bottom", self_side="top")
tb.blit()
tb.update()


##############################
########## Player 1 ##########
##############################

# Player 1 Pokemon Info
p1_p = thorpy.Element(text=('Player 1 Pokemon'))
p1_p.set_font_size(35)
p1_p.set_font_color((0,0,255))
p1_p.set_size((500,150))
p1_p.set_topleft((25,25))
p1_p.blit()
p1_p.update()

# Player 1 Movelist
p1_m = thorpy.Element(text=('P1 Movelist'))
p1_m.set_font_size(20)
p1_m.set_font_color((0,0,255))
p1_m.set_size((250,100))
p1_m.set_center((150, 250))
p1_m.blit()
p1_m.update()

p1_m1 = thorpy.Element(text=('Move 1'))
p1_m1.set_font_size(20)
p1_m1.set_size((250,100))
p1_m1.stick_to(p1_m, target_side="bottom", self_side="top")
p1_m1.blit()
p1_m1.update()

p1_m2 = thorpy.Element(text=('Move 2'))
p1_m2.set_font_size(20)
p1_m2.set_size((250,100))
p1_m2.stick_to(p1_m1, target_side="bottom", self_side="top")
p1_m2.blit()
p1_m2.update()

p1_m3 = thorpy.Element(text=('Move 3'))
p1_m3.set_font_size(20)
p1_m3.set_size((250,100))
p1_m3.stick_to(p1_m2, target_side="bottom", self_side="top")
p1_m3.blit()
p1_m3.update()

p1_m4 = thorpy.Element(text=('Move 4'))
p1_m4.set_font_size(20)
p1_m4.set_size((250,100))
p1_m4.stick_to(p1_m3, target_side="bottom", self_side="top")
p1_m4.blit()
p1_m4.update()

# Player 1 Pokemon Image
# p1_i = thorpy.Element(text=('P1 Image'))
# p1_i.set_font_size(20)
# p1_i.set_font_color((0,0,255))
# p1_i.set_size((300,300))
# p1_i.set_topleft((300,575))
# p1_i.blit()
# p1_i.update()


# p1_i = pygame.image.load(os.path.join("images","blastoise_back.png")).convert()
# p1_i = pygame.transform.scale(p1_i, (300,300))
# # You can then get the bounding rectangle of picture with
# p1_i_r = p1_i.get_rect()
# # and move the picture with
# p1_i_r = p1_i_r.move((300,575))
# screen.blit(p1_i, p1_i_r)


##############################
########## Player 2 ##########
##############################

# Player 2 Pokemon Info
p2_p = thorpy.Element(text=('Player 2 Pokemon'))
p2_p.set_font_size(35)
p2_p.set_font_color((255,0,0))
p2_p.set_size((500,150))
p2_p.set_topleft((915,725))
p2_p.blit()
p2_p.update()

# Player 2 Movelist
p2_m = thorpy.Element(text=('P2 Movelist'))
p2_m.set_font_size(20)
p2_m.set_font_color((255,0,0))
p2_m.set_size((250,100))
p2_m.set_center((1290, 250))
p2_m.blit()
p2_m.update()

p2_m1 = thorpy.Element(text=('Move 1'))
p2_m1.set_font_size(20)
p2_m1.set_size((250,100))
p2_m1.stick_to(p2_m, target_side="bottom", self_side="top")
p2_m1.blit()
p2_m1.update()

p2_m2 = thorpy.Element(text=('Move 2'))
p2_m2.set_font_size(20)
p2_m2.set_size((250,100))
p2_m2.stick_to(p2_m1, target_side="bottom", self_side="top")
p2_m2.blit()
p2_m2.update()

p2_m3 = thorpy.Element(text=('Move 3'))
p2_m3.set_font_size(20)
p2_m3.set_size((250,100))
p2_m3.stick_to(p2_m2, target_side="bottom", self_side="top")
p2_m3.blit()
p2_m3.update()

p2_m4 = thorpy.Element(text=('Move 4'))
p2_m4.set_font_size(20)
p2_m4.set_size((250,100))
p2_m4.stick_to(p2_m3, target_side="bottom", self_side="top")
p2_m4.blit()
p2_m4.update()

# Player 2 Pokemon Image
# p2_i = thorpy.Element(text=('P2 Image'))
# p2_i.set_font_size(20)
# p2_i.set_font_color((255,0,0))
# p2_i.set_size((300,300))
# p2_i.set_topleft((840,25))
# p2_i.blit()
# p2_i.update()

# p2_i = pygame.image.load(os.path.join("images","blastoise_front.png")).convert()
# p2_i = pygame.transform.scale(p2_i, (300,300))
# # You can then get the bounding rectangle of picture with
# p2_i_r = p2_i.get_rect()
# # and move the picture with
# p2_i_r = p2_i_r.move((840,25))
# screen.blit(p2_i, p2_i_r)



################################
##### Launch Pygame Engine #####
################################

# screen = pygame.display.get_surface()
# font = pygame.font.Font(None, 40)

# font_surface = font.render("original", True, (255,255,255), (255,255,255))
# screen.blit(font_surface, (0, 0))


playing_game = True
newgame = True
first_attempt = True
choice_locked = False

while playing_game:

        clock.tick(45)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playing_game = False
                break
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    if first_attempt == True:
                        screen.blit(BackGround2.image, BackGround2.rect)
                        battle_init()

                        time.sleep(2)
                        tb = thorpy.Element(text=(f'Press A to accept choices, Press R to reroll.'))
                        tb.set_font_size(20)
                        tb.set_size((750,150))
                        tb.stick_to(tb_h, target_side="bottom", self_side="top")
                        tb.blit()
                        tb.update()
                        
                        first_attempt = False

                elif event.key == pygame.K_a:
                    if first_attempt == False and choice_locked == False:
                        tb = thorpy.Element(text=(f'Choices Confirmed.'))
                        tb.set_font_size(20)
                        tb.set_size((750,150))
                        tb.stick_to(tb_h, target_side="bottom", self_side="top")
                        tb.blit()
                        tb.update()

                        choice_locked = True
                        time.sleep(0.2)

                        controller.press('z')
                        time.sleep(0.3)
                        controller.release('z')
                    elif choice_locked == True and newgame == False:
                        tb = thorpy.Element(text=(f"Cannot confirm choices after already beginning the game."))
                        tb.set_font_size(20)
                        tb.set_size((750,150))
                        tb.stick_to(tb_h, target_side="bottom", self_side="top")
                        tb.blit()
                        tb.update()
                    elif first_attempt == True:
                        tb = thorpy.Element(text=(f'Press S to start game before confirming choices.'))
                        tb.set_font_size(20)
                        tb.set_size((750,150))
                        tb.stick_to(tb_h, target_side="bottom", self_side="top")
                        tb.blit()
                        tb.update()
                elif event.key == pygame.K_r:
                        if choice_locked == True:
                            tb = thorpy.Element(text=(f"You've already confirmed all choices, can't reroll pokemon choices."))
                            tb.set_font_size(20)
                            tb.set_size((750,150))
                            tb.stick_to(tb_h, target_side="bottom", self_side="top")
                            tb.blit()
                            tb.update()
                        elif first_attempt == True:
                            tb = thorpy.Element(text=(f"Start the game using S. You cannot reroll without starting the game."))
                            tb.set_font_size(20)
                            tb.set_size((750,150))
                            tb.stick_to(tb_h, target_side="bottom", self_side="top")
                            tb.blit()
                            tb.update()
                        else:
                            screen.blit(BackGround2.image, BackGround2.rect)
                            battle_init()
                            time.sleep(2)
                            
                            tb = thorpy.Element(text=(f'Press A to accept choices, Press R to reroll.'))
                            tb.set_font_size(20)
                            tb.set_size((750,150))
                            tb.stick_to(tb_h, target_side="bottom", self_side="top")
                            tb.blit()
                            tb.update()

                elif event.key == pygame.K_z:
                    if choice_locked == True and newgame == True:
                        newgame = False
                        tb = thorpy.Element(text=(f'Begin Game!'))
                        tb.set_font_size(20)
                        tb.set_size((750,150))
                        tb.stick_to(tb_h, target_side="bottom", self_side="top")
                        tb.blit()
                        tb.update()

                        time.sleep(1)
                        # battlecommand here
                        battle_execute()
                        
                        tb = thorpy.Element(text=(f"All of {loser}'s Pokemon have fainted. {winner} is the winner! \n(ESC to close)"))
                        tb.set_font_size(20)
                        tb.set_size((750,150))
                        tb.stick_to(tb_h, target_side="bottom", self_side="top")
                        tb.blit()
                        tb.update()

                    elif choice_locked == True and newgame == False:
                        tb = thorpy.Element(text=(f"Match has already started."))
                        tb.set_font_size(20)
                        tb.set_size((750,150))
                        tb.stick_to(tb_h, target_side="bottom", self_side="top")
                        tb.blit()
                        tb.update()
                    else:
                        tb = thorpy.Element(text=(f'Please start the game with S then confirm choices with A first.'))
                        tb.set_font_size(20)
                        tb.set_size((750,150))
                        tb.stick_to(tb_h, target_side="bottom", self_side="top")
                        tb.blit()
                        tb.update()
                elif event.key == pygame.K_t:
                    dict_test2()
                    try:
                        tb = thorpy.Element(text=(f'{pkmn1} used {mvnm1}! It did 1 damage, just because.'))
                    except NameError:
                        tb = thorpy.Element(text=(f'Please try again, pokemon does not understand you. Say "use [move name here]" test char limit'))
                    tb.set_font_size(20)
                    tb.set_size((750,150))
                    tb.stick_to(tb_h, target_side="bottom", self_side="top")
                    tb.blit()
                    tb.update()
                elif event.key == pygame.K_ESCAPE:

                    playing_game = False


                elif event.key == pygame.K_b:
                    break

            pygame.display.update()
            tb.react(event)


pygame.quit()