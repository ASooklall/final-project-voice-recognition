# Import Dependencies to web scrape
import pandas as pd
from bs4 import BeautifulSoup
from splinter import Browser


# function to set up chromedriver for scrape
def use_browser():
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    return Browser('chrome', **executable_path, headless=False)

# RUN WEB SCRAPER
def scrape():
    browser = use_browser()

    # List for scraped data
    pokemon_dict = [
    {'pokemon_id':1,'name':'pikachu','type1':'electric','type2':'ptype2','hp':3,'atk':1,'def':1,'spd':1,
     'move1':1,'move2':2,'move3':3,'move4':4},
    {'pokemon_id':2,'name':'mewtwo','type1':'psychic','type2':'ptype2','hp':3,'atk':1,'def':1,'spd':1,
     'move1':5,'move2':6,'move3':7,'move4':8},
    {'pokemon_id':3,'name':'charizard','type1':'fire','type2':'flying','hp':3,'atk':1,'def':1,'spd':1,
     'move1':9,'move2':10,'move3':11,'move4':36},
    {'pokemon_id':4,'name':'venasaur','type1':'grass','type2':'ptype2','hp':3,'atk':1,'def':1,'spd':1,
     'move1':12,'move2':13,'move3':14,'move4':15},
    {'pokemon_id':5,'name':'blastoise','type1':'water','type2':'ptype2','hp':3,'atk':1,'def':1,'spd':1,
     'move1':16,'move2':17,'move3':18,'move4':19},
    {'pokemon_id':6,'name':'eevee','type1':'normal','type2':'ptype2','hp':3,'atk':1,'def':1,'spd':1,
     'move1':2,'move2':6,'move3':14,'move4':20},
    {'pokemon_id':7,'name':'onyx','type1':'rock','type2':'ground','hp':3,'atk':1,'def':1,'spd':1,
     'move1':4,'move2':21,'move3':22,'move4':23},
    {'pokemon_id':8,'name':'alakazam','type1':'psychic','type2':'ptype2','hp':3,'atk':1,'def':1,'spd':1,
     'move1':5,'move2':7,'move3':8,'move4':24},
    {'pokemon_id':9,'name':'gengar','type1':'ghost','type2':'poison','hp':3,'atk':1,'def':1,'spd':1,
     'move1':25,'move2':262,'move3':27,'move4':28},
    {'pokemon_id':10,'name':'nidoqueen','type1':'poison','type2':'ptype2','hp':3,'atk':1,'def':1,'spd':1,
     'move1':29,'move2':30,'move3':31,'move4':32},
    {'pokemon_id':10,'name':'machamp','type1':'fighting','type2':'ptype2','hp':3,'atk':1,'def':1,'spd':1,
     'move1':18,'move2':33,'move3':34,'move4':35}
     ]

    # url of page to be scraped
    pokedex_url = 'https://www.pokemon.com/us/pokedex/'
    browser.visit(pokedex_url)

    # set an html object to be used by BeautifulSoup
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')


    #print(soup)
    # save the pokemon image, name, type info
    #divTag = soup.find('div', class_='container pokedex')
    divTag = soup.find('div', class_='container pokedex')
    #print(divTag)
    pokemon_div = divTag.find_all('h5')
    print(pokemon_div)

    for info in pokemon_div:
        print('--------')
        print(info)

    print('done')

    browser.quit()

# Python program to executable
# main directly
if __name__ == '__main__':
    scrape()
