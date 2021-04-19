from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import streamlit as st

@st.cache(persist=True)
def nh_scrap():
    """Génère un dictionnaire donnant la liste des pages des hôtels par ville"""

    urlpage = 'https://www.nh-hotels.fr/hotels'
    req = Request(urlpage, headers={'User-Agent': 'Mozilla/5.0'})
    page = urlopen(req).read()
    soup = BeautifulSoup(page, 'html.parser')

    pages_countries = [country.find("a").get("href") for country in soup.find_all('h3', attrs={'class': 'h6'})] 
        
    hotels_url = {}

    for urlpage in pages_countries:
            req = Request(urlpage, headers={'User-Agent': 'Mozilla/5.0'})
            page = urlopen(req).read()
            soup = BeautifulSoup(page, 'html.parser')
            
            for city in soup.find_all('div', attrs={'class': 'grid-item'}):
                city_name = city.find('h2', attrs={'class': 'h4'}).getText().split()[-1]
                hotels_url[city_name.lower()] = ["https://www.nh-hotels.fr" + hotel_url.find("a").get("href") for hotel_url in city.find_all("li")]

    return hotels_url

def hotels_scrap(ville, hotels_url):
    """Génère la liste des hôtels éco-friendly d'une ville (liste de dictionnaires)
    Paramètres d'entrée : nom de la ville en minuscules (string), liste des pages web des hôtels par ville (dictionnaire)
    Infos données en sortie pour chaque hôtel : nom, url, photo, nombre d'étoiles"""

    hotels = []
    hotel = {}
    
    try:
        for url in hotels_url[ville]:
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
        
    except:
        return hotels
    
def main():

    hotels_url = nh_scrap()

    st.title("NH Group : eco-friendly hotels")
    user_input = st.text_input("Dans quel ville souhaitez-vous séjourner ?")

    if user_input :

        hotels = hotels_scrap(user_input.lower(), hotels_url)

        nb_result = str(len(hotels))+" résultats" if len(hotels) > 1 else str(len(hotels))+" résultat"
        st.header(nb_result)
        for hotel in hotels:
            st.subheader(hotel['nom'])
            st.text(hotel['nb_etoiles'])
            st.image(hotel['image'])
            lien = "[Pour plus d'infos]("+hotel['url']+")"
            st.write(lien)

if __name__ == "__main__":
    main()