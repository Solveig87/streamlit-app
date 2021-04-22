#!/usr/bin/python3
# coding: utf-8

"""
    TECHNIQUES WEB (Scrapping Project)
    ------------------------------------------
    
    This module shows a random article of the NTeAlan dictionnary and presents NTeALan association
    
    :copyright: © 2021 by Solveig PODER.
    :license: Creative Commons, see LICENSE for more details.
"""

import json
import streamlit as st
import random
import pandas as pd

def load_json(js_file):
    """Récupère le contenu d'un fichier json dans un dictionnaire"""
    with open(js_file, 'r') as f:
        data = json.load(f)
        return data

def show_article(articles):
    """Prend en entrée un dictionnaire des articles NTeALan et en affiche un hasard"""
    mot, infos = random.choice(list(articles.items()))
    st.title(mot)
    col1, col2 = st.beta_columns(2)
    col1.markdown("**Catégorie grammaticale**")
    col1.markdown("**Traduction(s) française(s)**")
    col2.write(infos["catégorie"])
    i = 1
    for trad in infos["traductions"]:
        col2.write(". ".join([str(i), trad]))
        i+=1

def ntealan_presentation():
    """Présente le projet NTeAlan, charge le json avec les articles de dictionnaires NTeALan et en affiche un au hasard"""

    articles = load_json('data/ntealan.json')

    st.markdown("## Pourquoi investir dans les langues peu dotées ?")
    st.markdown("Dans de très nombreux pays, on pratique plusieurs langues mais dont le statut est, généralement, différent (langue officielle, langue régionale). Cet état de fait engendre une grande disparité au niveau des outils et des ressources en traitement automatique des langues (TAL). Dans ce domaine, les langues ’mineures/minorées’ sont communément connues sous le nom de « langues peu dotées ». ")
    st.markdown("Il est pourtant important de concevoir des outils et ressources pour ces langues et d'assurer leur apprentissage, afin de les sauvegarder et les pérenniser comme le préconisent les différentes initiatives mises en place par les grandes organisations internationales (Nations-Unies, Conseil de l’Europe, etc.).")
    st.markdown("La nécessité de traiter automatiquement les langues peu dotées découle, à la fois, des besoins scientifiques et humanitaires (santé, éducation, culture, littératie, etc.) mais également des enjeux d’ordre politique (accès à l’information et à l’enseignement).")

    st.markdown("## NTeALan, qu'est-ce que c'est ?")
    st.markdown("Le projet NTeALan (New Technologies for African Languages) travaille à la mise en œuvre d’outils technologiques intelligents pour la promotion, le développement et l’enseignement des langues nationales africaines.")
    st.markdown("Depuis sa création en 2017, l’association NTeALan n’a cessé d’accroître ses effectifs et ses projets. Ses membres comptent aujourd’hui parmi les grands contributeurs bénévoles pour la sauvegarde de l’héritage linguistique et culturel de l’Afrique.")
    
    st.markdown("## Le dictionnaire collaboratif de NTeALan")
    st.markdown("La plateforme de Dictionnaire Collaboratif de NTeALan permet aux Africains et spécialistes de langues et cultures africaines de partager et échanger sur leurs ressources culturelles et linguistiques.​ C’est un projet open source de par son caractère collaboratif, et du fait de l’importante quantité de ressources à collecter. Cette plateforme facilite la collecte et l’échange des données.")
    
    st.markdown("## Un exemple d'article du dictionnaire yemba-français")
    st.markdown("La langue yɛmba est parlée en plein cœur du territoire Bamiléké. Le peuple yɛmba est un groupe culturel qui prend corps dans l’ensemble du département de la Ménoua, dans l’ouest du Cameroun.")
    show_article(articles)


