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
import plotly.graph_objects as go
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
    cnt_country = Counter()
    for country in set([infos['pays'] for infos in hotels.values()):
        cnt_country[country] = len([hotel for hotel, infos in hotels.items() if infos['pays'] == country])
    df = pd.DataFrame(list(cnt_country.items()),columns = ["pays","nombre"])
    return df
    
def create_df_stars(hotels):
    """Génère un dataframe Pandas avec la répartition des hôtels par nombre d'étoiles"""
    pass

def print_analyzes():
    """Charge le json avec la liste des hôtels NH et produit des graphiques avec des analyses, les affiche sur l'appli Streamlit"""

    hotels = load_json('data/hotels.json')

    df = create_df_eco(hotels)
    fig = px.pie(df, values='nombre', names='éco-friendly', title="Répartition des hôtels éco-friendly et non éco-friendly")
    st.write(fig)
    st.write("Les établissements écologiques sont majoritaires chez NH Hotels. La marque est en effet engagée dans la protection de l'environnement.")
    
    # Création de deux colonnes pour comparer les données des hôtels écolo et des autres hôtels
    col1, col2 = st.beta_columns(2)
    
    # On sépare les données en deux : hôtels eco-friendly et non eco-friendly
    eco_hotels = dict((hotel,infos) for hotel, infos in hotels.items() if infos['éco-friendly'] == True)
    neco_hotels = dict((hotel,infos) for hotel, infos in hotels.items() if infos['éco-friendly'] == False)
    
    df = create_df_countries(eco_hotels)
    fig = px.pie(df, values='nombre', names='pays', title="Répartition des hôtels éco-friendly par pays")
    col1.write(fig)
    
    df = create_df_countries(neco_hotels)
    fig = px.pie(df, values='nombre', names='pays', title="Répartition des hôtels non éco-friendly par pays")
    col2.write(fig)
    

