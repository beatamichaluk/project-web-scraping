#Libraries
from urllib import request
from bs4 import BeautifulSoup as BS
import re
import pandas as pd

#Limit extracted links to 101 
limit = True

if limit == 1:
    Limit = 101 

#Below is the part of the code that extracts links from the homepage. 
url = 'http://www.hppn.pl/reprezentacja/pilkarze' 
html = request.urlopen(url)
bs = BS(html.read(), 'html.parser')


tags_0 = bs.find_all('a', {'href':re.compile('/reprezentacja/pilkarze/.*')})[::2]
tags = tags_0[1:limit] 
links = ['http://www.hppn.pl' + tag['href'] for tag in tags]

players_links = []
players_links.extend(links)

for link in players_links:
    print(link)
#In this part of the code, the program extracts selected information from each of the previously extracted links.
#At 'name' we have name and surname of the player, at 'matches' the number of played matches,
#at 'bench' matches startes on the bench and at 'minutes' all minutes on football field during all matches. 
d = pd.DataFrame({'name':[], 'matches':[], 'bench':[], 'minutes':[] })

for players_link in players_links:
    print(players_link)

    html = request.urlopen(players_link)
    bs = BS(html.read(), 'html.parser')
    
    try:
        name = bs.find('div', {'class':'desc'}).text
    except:
        name = ''
        
    try:
        matches = bs.find('td', string = 'Mecze »').next_sibling.text
    except:
        matches = ''
        
    try:
        bench = bs.find('td', string = 'Mecze rozpoczęte na ławce »').next_sibling.text
    except:
        bench = ''
        
    try:
        minutes = bs.find('td', string = 'Minuty na boisku »').next_sibling.text
    except:
        minutes = ''    
    
    player = {'name':name, 'matches':int(matches), 'bench': bench, 'minutes':int(minutes)}
    
    d = d.append(player, ignore_index = True)
    print(d)
