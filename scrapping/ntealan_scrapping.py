#!/usr/bin/python3
# coding: utf-8

"""
    TECHNIQUES WEB (Scrapping Project)
    ------------------------------------------
    
    This module creates a json file with the 100 first articles of the Ntealan dictionnary
    
    :copyright: © 2021 by Solveig PODER.
    :license: Creative Commons, see LICENSE for more details.
"""

import time
from selenium import webdriver
import json
import os
from dotenv import load_dotenv
load_dotenv()

def main():
    """Génère un fichier json avec les 100 premiers articles du dictionnaire Ntealan
    Infos données en sortie pour chaque article : entrée (lemme avec ses variantes), catégorie grammaticale, traductions française"""

    driver = './chromedriver.exe'
    browser = webdriver.Chrome(executable_path = driver)

    browser.get("https://ntealan.net/")
    time.sleep(2)

    # Fermeture de la boîte de dialogue sur le Covid
    try :
        annonce_covid = browser.find_element_by_id("dialInfo")
        bouton_close = annonce_covid.find_element_by_tag_name("button")
        bouton_close.click()
    except :
        pass

    time.sleep(2)

    # on se connecte pour ne pas être limité à 10 articles
    login = [elem for elem in browser.find_elements_by_tag_name("span") if elem.get_attribute('title') == "Login"][0].find_element_by_tag_name('i')
    login.click()
    pseudo = [elem for elem in browser.find_elements_by_tag_name("input") if elem.get_attribute('id') == "pseudo"][0]
    mdp = [elem for elem in browser.find_elements_by_tag_name("input") if elem.get_attribute('id') == "password"][0]
    pseudo.send_keys(os.getenv('PSEUDO'))
    mdp.send_keys(os.getenv('PASSWORD'))
    connexion = browser.find_element_by_class_name("modal-footer").find_element_by_tag_name("button")
    connexion.click()

    time.sleep(2)

    articles = {}

    # On clique sur les mots de la barre de gauche, l'un après l'autre, et on récupère les informations : lemme, catégorie grammaticale, traductions en français (on se limite aux 100 premiers)
    words = browser.find_element_by_class_name("listeUL")
    i = 1

    for word in words.find_elements_by_tag_name("li"):
        if len(articles)==100:
            break
            
        word.location_once_scrolled_into_view
        word.click()
        time.sleep(2)
            
        try:
            article = browser.find_element_by_class_name("article")
            lemme = []
            # le lemme peut avoir plusieurs variantes : on les récupère toutes
        
            # chaque variante est un élément de la variante précédente : pour avoir les affixes de chaque variante (sans risquer de récupérer ceux de la variante suivante) il faut donc chercher via leur position
            for variante in [elem for elem in article.find_elements_by_tag_name("span") if elem.get_attribute("class") in ("variant", "groupVariant")]:
                if variante.find_element_by_xpath('span[1]').get_attribute('class') == "aprefix":
                    prefix = variante.find_element_by_xpath('span[1]').text
                else:
                    prefix = ""
                    
                if variante.find_element_by_xpath('span[2]').get_attribute('class') == "suffix":
                    suffix = variante.find_element_by_xpath('span[2]').text
                elif variante.find_element_by_xpath('span[3]').get_attribute('class') == "suffix":
                    suffix = variante.find_element_by_xpath('span[3]').text 
                else:
                    suffix = ""
                    
                lemme.append(prefix + variante.find_element_by_class_name("radical").text+suffix)
        
            if len(lemme) > 1:
                lemme = ", ".join(lemme)
            else:
                lemme = lemme[0]
                
            if lemme in articles.keys():
                lemme = " ".join([lemme, str(i+1)])
                i+=1
            else:
                i = 1
            articles[lemme] = {}

            articles[lemme]["catégorie"] = article.find_element_by_class_name("cat_part").text
            articles[lemme]["traductions"] = []
            for trad in article.find_elements_by_class_name("group_equiv"):
                articles[lemme]["traductions"].append(trad.find_element_by_class_name("equivalent").text)
            time.sleep(2)

        except:
            continue
        
    with open("../data/ntealan.json", "w", encoding="utf8") as f:
        f.write(json.dumps(articles, indent=4, ensure_ascii=False))

if __name__ == "__main__":
    main()