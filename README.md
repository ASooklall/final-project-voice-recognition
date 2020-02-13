# Voice Recognition Emulation And Gaming
### Using voice recognition for both accessibility and primary control in gaming.

### Data Science Final Project
* <a href='https://github.com/ASooklall' target='_blank'>Andrew Sooklall</a>
* <a href='https://github.com/Mikey-Esteban' target='_blank'>Mikey Esteban</a>
* <a href='https://github.com/PratikPathak07' target='_blank'>Pratik Pathak</a>
* <a href='https://github.com/zclynchzc' target='_blank'>Zane Christopher Lynch</a>

### Related Links:
* Github Project Repository Share Link:
    * https://github.com/ASooklall/final-project-voice-recognition
* Tableau Story for VCP Analysis:
    * https://public.tableau.com/profile/andrew.sooklall#!/vizhome/final_project_vcp_analysis/VoiceRecognitioninGamingEmulation

### Goal:
* Providing accessibility in gaming and facilitating novel methods for game control that companies can use to improve consumer purchases and demographics.
    * Accessibility in gaming refers to the ability of a user to receive output, provide input, and understand the process or input/output of a game.
        * Deficits in accessbility can be due to sensory impairment, mechanical disability, cognitive impairment, etc.
    * https://en.wikipedia.org/wiki/Game_accessibility
* Collecting data logs to improve the system to create a model or modes of input that improves user experience and utility.
* Designing and creating a python based battle simulation game that utilizes voice recognition as primary method of control.

## Project Breakdown:

### Voice Simulation in Game Emulation:

<img src="/data/resources/vpc_screenshot02122020.png" alt="VPC_Emulation" width="1024" height="720">

#### Purpose:
* To facilitate accessbility for individuals with physical sensory or mechanical disability in gaming by providing a method of control for users that does not require precise or dexterous tactile control. 
* Voice Recognition based gaming that uses oral output to play the game instead of pressing buttons on a control.
#### Requirements:
* Emulator Software (in our case we used mgba)
* Game Rom
* Python
    * Modules/Libraries located in requirements.txt files stored in their respective directories. (pip install requirements.txt)
#### Installation: 
* download and install emulator of choice
* download rom of choice
* Navigate inside the voice-command-peripheral directory
* pip install requirements.txt
* If you have issues utilizing PyAudio:
    * try removing PyAudio with 'pip remove pyaudio'
    * utilize 'pip install pipwin' for the custom package installer for python 3.7
    * use 'pipwin install pyaudio' to install the python 3.7 specific pyaudio package
* If your PyAudio is working:
    * installation complete, follow instructions for use
#### Instructions: 
* Launch your emulator software and load your rom
* Launch app.py in terminal
    * Note: If your software (ex; Visual Studio Code) indicates missing modules after you've successfully pip installed them, this can be due to anaconda not locating the files because they weren't installed through conda (there is no conda package for these files). However, it should run as expected because python has the packages through pip install.
* Follow instructions on terminal for button presses to activate voice command types
    * Commands:
        * D
        * X
* Play the game using your voice commands through the app. You do not have to type the commands into terminal to utilize the app, you may keep the game open.
#### Significance: 
* Designing this voice to control software for emulation proves the feasability and ease of design this concept has.
* As a very manageable alternative or addition to mechanical/physical control using keyboard, controllers, etc. this option allows for users unable to physically press buttons accurately or quickly to still be able to play games and have a reason to purchase gaming products.
* This opens the avenue to marketing to demographics that previously would not consider gaming due to disability by increasing accessibility as a whole.
* As a side-note, this also can be marketed as an alternative way to play for individuals who simply want to use voice commands in their game or for communities like speed runners who might want to use voice as a novel way of inputting specific arrays of commands in sequence without having to worry about accidentally pressing the wrong button.
* The software also logs key prompts in the developmental version which allows for testing which voice options are most used, what key buttons are most frequented, and how often mistakes occur. This can be used for both increasing the accuracy of a speech recognition model geared to emulation as well as providing information for marketing accessory products that could increase comfortability for users who would normally need to press these buttons often.
* Providing insight into the habits and tendencies of gamer time consumption per play session, sessions per day, preferred weekday, etc. all have marketing value and weight when developing new consumer products. This software can log these times, dates, etc. and store them for future use.
#### Analysis: 
* Insert Tableau Link / Screenshots
* As shown in the Tableau comparison:
    * https://public.tableau.com/profile/andrew.sooklall#!/vizhome/final_project_vcp_analysis/VoiceRecognitioninGamingEmulation
* It is important to note that while storing the recorded data in a database and cloud-hosting or locally hosting it on hard memory might be best, we chose to simply append a csv for demonstration purposes and ease of access for the scope of the project.
    * As logs from multiple users could become massive, we recommend using a cloud-based hosting service for your database (such as AWS).



### Pokemon Voice Battle Simulator:

<img src="/data/resources/battle_sim_demo1.png" alt="BattleSimDemo" width="1024" height="720">

#### Purpose:
* To demonstrate the feasability of designing a game based around voice recognition outside of the standard sandbox (games without linear development or purpose) or tag-along game (see Pokemon: Let's Go Eevee/Pikachu or N64 Hey You Pikachu!). 
    * Games of this nature solely allow the user to give voice commands to an NPC (non-playable-character) that will then attempt to perform/follow those commands.
    * Our goal instead is to allow users to play other types of games, such as a battle simulation, using primarily or solely their voice which would broaden the genre of games voice recognition could be used in.
* Increase marketing and proliferation of voice recognition in gaming by providing an example that could impact a broader range of consumers that currently existing games or be utilized in more party-like environments.
#### Installation:
* Navigate inside the pokemon-battle-simulator directory
* pip install requirements.txt
* If you have issues utilizing PyAudio:
    * try removing PyAudio with 'pip remove pyaudio'
    * utilize 'pip install pipwin' for the custom package installer for python 3.7
    * use 'pipwin install pyaudio' to install the python 3.7 specific pyaudio package
* If your PyAudio is working:
    * installation complete, follow instructions for use
#### Instructions:
* launch battle_sim.py or demo.py (for demo)
    * Note: If your software (ex; Visual Studio Code) indicates missing modules after you've successfully pip installed them, this can be due to anaconda not locating the files because they weren't installed through conda (there is no conda package for these files). However, it should run as expected because python has the packages through pip install.
* follow instructions on screen for key presses or voice prompts
* use voice to choose pokemon, moves, etc. when prompted
* game is fully playable within the pygame screen, you do not need to use your terminal after launching the .py file
* The main menu looks like:
<img src="/data/resources/battle_sim_home1.png" alt="BattleSimHome" width="900" height="400">
    * In the center Announcement box, relative game text and instructions appear as needed.
    * You can begin the game by pressing the "S" key and after selecting your pokemon with voice input, use the "A" key to choose.
    * A full list of pokemon can be found in the game dictionary but are also below:
        * Pikachu, Mewtwo, Charizard, Venusaur, Blastoise, Eevee, Onyx, Alakazam, Gengar, Nidoqueen, Machamp, Gyarados, Scizor, Snorlax, Dragonite, Dewgong
        * This list is up-to-date as of the demo.py
    * Before confirming with "A" you have the option to reroll/reselect your Pokemon with the "R" key as many times as you'd like.
        * This option will cause both players to reselect.
    * After confirmation, the battle will automatically begin and prompt player 1 to use the "T" key to initiate voice selection of their move, then repeat the process with player 2. Afterwards, the game engine will automatically determine move order based on speed and calculate damage and the battle.
    * This process is repeated until one player wins when their opponent is left with 0 HP or health points.
* A breakdown of stats can be seen as follows:
    * HP / Health : The amount of damage your pokemon can receive before fainting / losing.
    * Atk / Attack : The damage modifier your pokemon multiplies when attacking.
    * Def / Defense : The defensive modifier your pokemon divides by when defending.
    * Spd / Speed : The raw speed integer that determines who goes first. If both pokemon have equal speeds, player 1 goes first as a handicap for choosing their move and pokemon first.
#### Significance:
* A fully designed game engine in python that can utilize speech recognition and allow players to directly interact via voice opens the doors to vast marketing opportunities and design concepts for gaming.
    * demo.py and battle_sim.py are the proof of concept we designed for this.
* Previously, games were very limited in what a user could do with their voice and the responses available. This game simulation shows that user input can have expanded output even within the limited pygame engine and these opportunities can only be expanded when developed in C/C++. 
    * Within the timeframe provided for the project, developing in C/C++ was out of scope as we would have needed to learn syntax and libraries to accurately script and debug our code.
* Being able to market voice recognition as a novel or unique mode of control for a game as well as method of increasing accessibility can increase consumer base and interest.
* Even with the standard google cloud API, the model and engine are extremely accurate. With a specifically trained and weighted model, this number can only increase.
<!-- #### Analysis: -->

### Conclusion:
* The final project turned out much different than the initial proposal. While the main theme of voice recognition and accessibility remain unchanged, and the battle simulator was created, the original concept of using the Nintendo Switch was scrapped due to hardware issues with Nintendo banning the modification of consoles thus rendering this method beyond the scope of the project. In turn, we decided to use an emulator to control handheld games instead. The initial project proposal can be found under 'data/resources' in .docx format.
* Voice Recognition proved a viable method of playing games as both an alternative to normal controllers for those unable to for mechanical reasons, as well as an alternative to traditional controllers to provide a more engaging way of playing niche games such as the Pokemon Battle Simulation.
* The above methods would increase marketing towards users who may not normally engage in video games due to accessibility, but also rekindle interest in gaming for those who aren't interested in the standard controllers or users who want a more engaging experience for environments like parties, etc.
* With control over ambient voice thresholds and dynamic adjusting, the voice recognition models can be easily modified to fit any environment or adjust to multiple environments and room populations.
* However, it is important to remember that while default APIs (ex; Google Voice API) are broad spectrum and excellent resources to utilize, that same nature provides multiple word recognitions that can clash with specific commands you may want to utilize (as in the case with the game emulation) and because of that, creating a specialized voice model for a game or emulation software can drastically improve response accuracy by either removing unnecessary word recognition, or creating a weighted model that has greater weight on the specific words used in the software.
* In the future, it is imperative to test this theory with multiple models and systems, but this project proves that it is very possible and probably to extend accessibility in gaming to those mechanically unable to use a controller as well as broaden consumer reach through voice recognition. A powerful marketing strategy for the future.



## Resources:
* Speech Recognition
    * Speech Recognition Library
        * https://pypi.org/project/SpeechRecognition/
    * PyAudio
        * https://people.csail.mit.edu/hubert/pyaudio/
    * Cloud Speech-to-Text (Google Cloud API)
        * https://cloud.google.com/speech-to-text/docs
* Emulator: mgba
    * Disclaimer: We used emulation software for the development of our program. We do not aim to or condome promotion of using emulation instead of purchasing the retail game and devices. However, the use of emulator software is legal for the purpose of development and research.
    * https://mgba.io/faq.html
* Rom: Pokemon Emerald
    * Disclaimer: See Above. For legal purposes, we cannot and are not providing a link to the rom used. We own a physical copy of the game and the rom was used solely to allow projecting of the game on the PC platform for testing and demonstration purposes.
    * It is legal to own a backup of a game you physically own as a rom. The distribution or sharing of any rom is illegal.
* Databases:
    * Pokemon Stat Makeups: Bulbapedia (Used as a reference for stats. Stat breakdown in the simulation is our custom formula.)
        * https://bulbapedia.bulbagarden.net/wiki/Main_Page
    * Pokemon Images: Kaggle
        * https://github.com/fudgenuggets1/hax_free_pokemon
* Libraries:
    * Python
        * See requirements.txt
    * Pygame, Thorpy
        * Engine and library used to develop the battle simulation.
        * https://www.pygame.org/docs/
        * http://thorpy.org/documentation.html
* Accessory Voice Modeling
    * Teachable Machine
        * Not used in the demonstration or application.
        * Used to provide insight on the accuracy of specifically trained models vs. cloud based and broad trained models.
        * https://teachablemachine.withgoogle.com/faq




