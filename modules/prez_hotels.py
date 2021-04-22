#!/usr/bin/python3
# coding: utf-8

"""
    TECHNIQUES WEB (Scrapping Project)
    ------------------------------------------
    
    This module analyzes data about eco-friendly hotels on the NH Hotels website
    
    :copyright: © 2021 by Solveig PODER.
    :license: Creative Commons, see LICENSE for more details.
"""

import pandas as pd
import plotly.express as px
import json
from collections import Counter
import streamlit as st

def load_json(js_file):
    """Récupère le contenu d'un fichier json dans un dictionnaire"""
    with open(js_file, 'r') as f:
        data = json.load(f)
        return data

def create_df_eco(hotels):
    """Génère un dataframe Pandas avec la répartition des hôtels éco-friendly et non éco-friendly"""
    cnt_eco = Counter()
    cnt_eco['oui'] = len([hotel for hotel, infos in hotels.items() if infos['éco-friendly'] == True])
    cnt_eco['non'] = len([hotel for hotel, infos in hotels.items() if infos['éco-friendly'] == False])
    df = pd.DataFrame(list(cnt_eco.items()),columns = ["éco-friendly","nombre"])
    return df
    
def create_df_countries(hotels):
    """Génère un dataframe Pandas avec la répartition des hôtels par pays"""
    cnt_country = {}
    for country in set([infos['pays'] for infos in hotels.values()]):
        cnt_country[country] = Counter()
        cnt_country[country]['écolo'] = len([hotel for hotel, infos in hotels.items() if infos['pays'] == country and infos["éco-friendly"] == True])
        cnt_country[country]['non écolo'] = len([hotel for hotel, infos in hotels.items() if infos['pays'] == country and infos["éco-friendly"] == False])
    df = pd.DataFrame.from_dict(cnt_country, orient='index')
    return df
    
def create_df_stars(hotels):
    """Génère un dataframe Pandas avec la répartition des hôtels par nombre d'étoiles"""
    cnt_stars = {}
    for nb in range(6):
        cnt_stars[str(nb)] = Counter()
        cnt_stars[str(nb)]['écolo'] = len([hotel for hotel, infos in hotels.items() if infos['étoiles'] == str(nb) and infos["éco-friendly"] == True])
        cnt_stars[str(nb)]['non écolo'] = len([hotel for hotel, infos in hotels.items() if infos['étoiles'] == str(nb) and infos["éco-friendly"] == False])
    df = pd.DataFrame.from_dict(cnt_stars, orient='index')
    return df

def print_analyzes():
    """Charge le json avec la liste des hôtels NH et produit des graphiques avec des analyses, les affiche sur l'appli Streamlit"""

    hotels = load_json('data/hotels.json')

    st.markdown("## L'accord de Paris et l'hôtellerie")
    st.markdown("Lors de la COP21 à Paris, le 12 décembre 2015, les 196 Parties à la CCNUCC (Convention-cadre des Nations unies sur les changements climatiques) sont parvenues à un accord historique pour lutter contre le changement climatique et pour accélérer et intensifier les actions et les investissements nécessaires à un avenir durable à faible intensité de carbone. L'Accord de Paris, entré en vigueur le 4 novembre 2016, rassemble pour la première fois toutes les nations autour d'une cause commune pour entreprendre des efforts ambitieux afin de combattre le changement climatique et de s'adapter à ses conséquences, avec un soutien accru pour aider les pays en développement à le faire.")
    st.markdown("Dans le domaine de l'hôtellerie, le Partenariat international pour le tourisme (ITP), organisation mondiale regroupant les plus grandes entreprises hôtelières du monde avec 30 000 hôtels membres, a quant à lui adopté l'ambition des objectifs scientifiques qui sont au cœur de l'Accord de Paris. Une étude commandée par l’ITP souligne que l'industrie hôtelière doit réduire ses émissions de carbone de 66% d'ici 2030 et de 90% d'ici 2050 pour rester dans les limites du seuil de 2°C convenu lors de la COP21.")

    df = create_df_eco(hotels)
    st.markdown("## Répartition des hôtels éco-friendly et non éco-friendly")
    fig = px.pie(df, values='nombre', names='éco-friendly')
    st.write(fig)
    st.markdown("Les établissements écologiques sont majoritaires chez NH Hotels. La marque est en effet engagée dans la protection de l'environnement. Depuis 2008, l'empreinte carbone de ses hôtels a été réduite de **70 %**. Elle a également enregistré une réduction de **28 %** des coûts en énergie et de **30 %** des coûts en eau. Ces initiatives ont été reconnues par l'Organisation internationale de normalisation et certains de ses hôtels sont titulaires d'un certificat d'énergie durable (ISO 14001 et ISO 50001).")
    st.write("Plus d'informations sur [cette page](https://www.nh-hotels.fr/environnement/hotels-ecologiques-developpement-durable)")
    
    df = create_df_countries(hotels)
    st.markdown("## Répartition des hôtels par pays")
    fig = px.bar(df, y=['écolo', 'non écolo'])
    st.write(fig)
    st.markdown("**Belgique**, **Allemagne**, **Autriche**, **Pays-Bas** et **Italie** ont une majorité d'hôtels écologiques. L'**Espagne**, où se trouvent le plus grand nombre d'hôtels du groupe, a encore quelques efforts à fournir puisque seulement un tiers de ses hôtels sont signalés comme eco-friendly. Il est difficile de tirer des conclusions pour les autres pays, où le nombre d'hôtels est peu élevé.")

    df = create_df_stars(hotels)
    st.markdown("## Répartition des hôtels par nombre d'étoiles")
    fig = px.bar(df, y=['écolo', 'non écolo'])
    st.write(fig)
    st.write("Le groupe NH Hotels possède une majorité d'hôtels **4 étoiles** dont la plupart sont écologiques. Presque la moitié des hôtels **5 étoiles** sont eco-friendly. On peut facilement en conclure que le respect de l'environnement n'empêche pas un certain standing et que la cible de ce marché ne concerne pas des citoyens aux revenus modestes mais au contraire des personnes aisées.")

