import time
import requests 
import random
from bs4 import BeautifulSoup
from plyer import notification

URL = "https://www.sportscounty.com/interesting-football-facts/"
r = requests.get(URL)

soup = BeautifulSoup(r.content, 'html5lib')
#  print(soup.prettify())

table = soup.findAll('h3')[1:-1]

facts = []

for  i in table:
    facts.append(i.find('span').text)

while True:
    v = random.randint(0, 39)
    notification.notify(title = "Random Football Facts", message=str(facts[v]), app_name="Football Notifier", app_icon="C:\\Users\\ashish\\OneDrive\\Desktop\\ResumeKaProject\\football.ico", timeout=10)
    time.sleep(10)

