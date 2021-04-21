#!/usr/bin/python3
# coding: utf-8

"""
    TECHNIQUES WEB (Scrapping Project)
    ------------------------------------------
    
    This module allows to search the eco-friendly hotels of a city on the NH Hotels website
    
    :copyright: © 2021 by Solveig PODER.
    :license: Creative Commons, see LICENSE for more details.
"""

from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import streamlit as st

def hotels_scrap(ville):
    """Génère la liste des hôtels éco-friendly d'une ville (liste de dictionnaires)
    Paramètre d'entrée : nom de la ville
    Infos données en sortie pour chaque hôtel : nom, url, photo, nombre d'étoiles"""

    urlpage = 'https://www.nh-hotels.fr/hotels'
    req = Request(urlpage, headers={'User-Agent': 'Mozilla/5.0'})
    page = urlopen(req).read()
    soup = BeautifulSoup(page, 'html.parser')

    # Récupération des pages affichant la liste des hôtels par pays
    pages_countries = [country.find("a").get("href") for country in soup.find_all('h3', attrs={'class': 'h6'})]

    hotels_url = []

    for urlpage in pages_countries:
        if len(hotels_url) > 0:
            break
        req = Request(urlpage, headers={'User-Agent': 'Mozilla/5.0'})
        page = urlopen(req).read()
        soup = BeautifulSoup(page, 'html.parser')
        
        # recherche de la ville demandée dans la liste des villes du pays ayant un ou plusieurs hôtel(s) et récupération des pages des hôtels si match
        for city in soup.find_all('div', attrs={'class': 'grid-item'}):
            city_name = city.find('h2', attrs={'class': 'h4'}).getText().split()[-1]
            if city_name.lower() == ville.lower() :
                hotels_url = ["https://www.nh-hotels.fr" + hotel_url.find("a").get("href") for hotel_url in city.find_all("li")]
                break

    # la ville n'a pas été trouvée (pas d'hôtel dans cette ville)
    if len(hotels_url) == 0:
        return []

    # la ville a été trouvé, on donne la liste des hôtels
    else:
        hotels = []
        hotel = {}
    
        for url in hotels_url:
            req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            page = urlopen(req).read()
            soup = BeautifulSoup(page, 'html.parser')
            icones = soup.find('ul', attrs={'class': 'group-icons'})
            if "Eco-friendly" in [elem.getText() for elem in icones.find_all('p', attrs={'class': 'color-primary'})]:
                hotel['nom'] = soup.find('div', attrs={'class':'book-now'}).h2.getText()
                hotel['url'] = url
                image = soup.find('section', attrs={'class':'m-gallery box'})
                hotel['image'] = image.find_all('img')[0].get('data-lazy')
                stars = soup.find_all('div', attrs={'class':'stars'})[0]
                hotel['nb_etoiles'] = str(len(stars.find_all('span', attrs={'class':'nh-ic-star'}))) + " étoiles"
                hotels.append(hotel)
            hotel = {}
        return hotels

    
def recherche():
    """Permet à l'utilisateur d'effectuer une recherche d'hôtels sur une application Streamlit et affiche des informations sur cet hôtel"""

    # Affichage de la barre de recherche
    st.header("NH Group : eco-friendly hotels")
    user_input = st.text_input("Dans quel ville souhaitez-vous séjourner ?")

    # L'utilisateur a entré le nom d'une ville, on affiche les résultats
    if user_input :

        hotels = hotels_scrap(user_input)

        nb_result = "**"+ str(len(hotels)) + " résultats**" if len(hotels) > 1 else str(len(hotels))+" résultat**"
        st.markdown(nb_result)
        for hotel in hotels:
            st.subheader(hotel['nom'])
            st.text(hotel['nb_etoiles'])
            st.image(hotel['image'])
            lien = "[Pour plus d'infos]("+hotel['url']+")"
            st.write(lien)
