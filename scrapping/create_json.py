from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import json

def main():
    """Génère un fichier json répertoriant les hôtels du site de NH Hotels
    Infos données en sortie pour chaque hôtel : nom, pays, nombre d'étoiles, éco-friendly (booléen)"""

    hotels = {}

    urlpage = 'https://www.nh-hotels.fr/hotels'
    req = Request(urlpage, headers={'User-Agent': 'Mozilla/5.0'})
    page = urlopen(req).read()
    soup = BeautifulSoup(page, 'html.parser')
    
    for country in soup.find_all('h3', attrs={'class': 'h6'}):
        country_name = country.find("strong").getText()
        print("Processing hotels in " + country_name)
        page_country = country.find("a").get("href")
        req = Request(page_country, headers={'User-Agent': 'Mozilla/5.0'})
        page = urlopen(req).read()
        soup2 = BeautifulSoup(page, 'html.parser')
        
        for city in soup2.find_all('div', attrs={'class': 'grid-item'}):
            for hotel in city.find_all("li"):
                url = "https://www.nh-hotels.fr" + hotel.find("a").get("href")
                req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
                page = urlopen(req).read()
                soup3 = BeautifulSoup(page, 'html.parser')
                name = soup3.find('div', attrs={'class':'book-now'}).h2.getText()
                hotels[name] = {}
                hotels[name]['pays'] = country_name
                icones = soup3.find('ul', attrs={'class': 'group-icons'})
                if "Eco-friendly" in [elem.getText() for elem in icones.find_all('p', attrs={'class': 'color-primary'})]:
                    hotels[name]['éco-friendly'] = True
                else:
                    hotels[name]['éco-friendly'] = False
                stars = soup3.find_all('div', attrs={'class':'stars'})[0]
                hotels[name]['étoiles'] = str(len(stars.find_all('span', attrs={'class':'nh-ic-star'})))
                #print(name, " : ", hotels[name])

    print("Création du fichier json")
    with open("../resources/hotels.json", "w", encoding="utf8") as f:
        f.write(json.dumps(hotels, indent=4, ensure_ascii=False))

if __name__ == "__main__":
    main()