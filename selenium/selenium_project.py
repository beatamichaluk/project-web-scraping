#Libraries
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
import time
import getpass
import datetime
import pandas as pd
import csv

#GeckoDriver path
gecko_path = '/usr/bin/geckodriver'
ser = Service(gecko_path)
#options = webdriver.Firefox.options.Options()
#options.headless = False
driver = webdriver.Firefox(service=ser) #options = options

Limit = True

linki1 = []
imie_nazwisko = []
mecze = []
bramki = []
minuty_rozegrane = []

url = 'http://www.hppn.pl/reprezentacja/pilkarze'

### Here we have actual program ###

driver.get(url)

driver.implicitly_wait(6)

cookies = driver.find_element(By.XPATH, '//*[@id="cookie-consent-banner"]/div/div[2]/div/form/button')
cookies.click()

linki_do_zawodnikow = driver.find_elements(By.CSS_SELECTOR, ("a[href*='/reprezentacja/pilkarze/']"))
for link in linki_do_zawodnikow:
href1 = link.get_attribute("href")
if href1 is not None:
if href1 not in linki1:
linki1.append(href1)

while Limit == True:
print("program will scrap 100 pages")
limit = 0
for links in linki1:
if limit == 100:
break
driver.get(links)
driver.implicitly_wait(3)

#xpaths to players characteristics
players = driver.find_elements(By.XPATH, '//*[@id="player-profile"]/section[1]/div[1]/div[2]')
matches = driver.find_elements(By.XPATH, '//*[@id="player-profile"]/div[3]/div[2]/section[3]/table/tbody/tr[2]/td[2]')
goals = driver.find_elements(By.XPATH, '//*[@id="player-profile"]/div[3]/div[2]/section[3]/table/tbody/tr[4]/td[2]')
minutes = driver.find_elements(By.XPATH, '//*[@id="player-profile"]/div[3]/div[2]/section[3]/table/tbody/tr[1]/td[2]')


for i in range(len(players)):
imie_nazwisko.append(players[i].text)
try:
bramki.append(goals[i].text)
except:
bramki.append(" ")
try:
mecze.append(matches[i].text)
except:
mecze.append(" ")
try:
minuty_rozegrane.append(minutes[i].text)
except:
minuty_rozegrane.append(" ")

limit += 1

df = pd.DataFrame(list(zip(imie_nazwisko,bramki,minuty_rozegrane,mecze)), columns = ['Name_Surname','Goals','Minutes','Matches'])

df.to_csv('Table.csv', sep=';')

driver.quit
break
