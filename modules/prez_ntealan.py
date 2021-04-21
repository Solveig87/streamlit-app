#!/usr/bin/python3
# coding: utf-8

"""
    TECHNIQUES WEB (Scrapping Project)
    ------------------------------------------
    
    This module shows a random article of the Ntealan dictionnary and presents NTeALan association
    
    :copyright: © 2021 by Solveig PODER.
    :license: Creative Commons, see LICENSE for more details.
"""

import json
import streamlit as st
import random

def load_json(js_file):
    """Récupère le contenu d'un fichier json dans un dictionnaire"""
    with open(js_file, 'r') as f:
        data = json.load(f)
        return data

def show_article(articles):
    """Prend en entrée un dictionnaire des articles Ntealan et en affiche un hasard"""
    mot, infos = random.choice(list(articles.items()))
    st.subheader(mot)
    st.info(infos["catégorie"])
    for trad in infos["traductions"]:
        st.write(trad)

def ntealan_presentation():
    """Présente le projet Ntealan, charge le json avec les articles de dictionnaires Ntealan et en affiche un au hasard"""

    articles = load_json('data/ntealan.json')

    st.markdown("## NTeALan, qu'est-ce que c'est ?")
    st.markdown("Le projet NTeALan (New Technologies for African Languages) travaille à la mise en œuvre d’outils technologiques intelligents pour la promotion, le développement et l’enseignement des langues nationales africaines.")
    st.markdown("Depuis sa création en 2017, l’association NTeALan n’a cessé d’accroître ses effectifs et ses projets. Ses membres comptent aujourd’hui parmi les grands contributeurs bénévoles pour la sauvegarde de l’héritage linguistique et culturel de l’Afrique.")
    
    st.markdown("## Le dictionnaire collaboratif de NTeALan")
    st.markdown("La plateforme de Dictionnaire Collaboratif de NTeALan permet aux Africains et spécialistes de langues et cultures africaines de partager et échanger sur leurs ressources culturelles et linguistiques.​ C’est un projet open source de par son caractère collaboratif, et du fait de l’importante quantité de ressources à collecter. Cette plateforme facilite la collecte et l’échange des données.")
    
    st.markdown("### Un exemple d'article")
    show_article(articles)


