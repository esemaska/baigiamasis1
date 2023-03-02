from databaze import *
from bs4 import BeautifulSoup
import requests

# nuskaitome visus duomenys is svetaines www.cvbankas.lt
try:
    source = requests.get('https://www.cvbankas.lt/').text
    soup = BeautifulSoup(source, 'html.parser')
    blokas = soup.find_all('div', class_="list_a_wrapper")
except requests.exceptions.RequestException as klaida:
    print("Klaida pasiekiant svetainę: ", klaida)
    print("Prašome patikrinti savo interneto ryšį ir bandyti dar kartą vėliau.")
    exit()

Base.metadata.create_all(bind=engine)

#Isskiriami duomenys pagal profesija, imone, atlyginima, miesta, data,
for blokai in blokas:
    try:
        profesija = blokai.find('h3', class_="list_h3", lang="lt").text.strip()
        imone = blokai.find('span', class_="dib mt5").text.strip()
        atlyginimas = blokai.find('span', class_="salary_amount").text.strip()
        atlyginimo_didis = blokai.find('span', class_="salary_calculation").text.strip()
        miestas = blokai.find('span', class_="list_city").text.strip()
        data = blokai.find('span', class_="txt_list_2").text.strip()

        darbo_skelbimas = DarboSkelbimai(profesija=profesija, imone=imone,
                                         atlyginimas=atlyginimas, atlyginimo_didis=atlyginimo_didis,
                                         miestas=miestas, data=data)
        session.add(darbo_skelbimas)
    except:
        pass
