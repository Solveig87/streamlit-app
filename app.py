#!/usr/bin/python3
# coding: utf-8

"""
    TECHNIQUES WEB (Scrapping Project)
    ------------------------------------------
    
    This module runs the Streamlit app
    
    :copyright: © 2021 by Solveig PODER.
    :license: Creative Commons, see LICENSE for more details.
"""

import streamlit as st
import pandas as pd
from modules import *

def main():

    # Page d'accueil du projet
    st.title("Smart Investment")
    st.markdown("*Pour vous permettre d'investir l'avenir*")
    st.markdown("**Logements écologiques et langues peu dotées**")
    st.sidebar.header("Projet - Techniques web")
    st.sidebar.subheader("M2 TAL - Inalco ")
    st.sidebar.info('Auteur : Solveig PODER')

    # Radio selector sur sidebar pour accéder aux différentes pages
    st.sidebar.header("Votre sélection :")
    radio = st.sidebar.radio(label="", options=['Présentation','NH Hotels : chiffres', 'NH Hotels : recherche', 'NTeALan'])

    # Page de présentation du projet
    if radio == "Présentation":
        st.markdown("## Présentation du projet ")
        st.markdown("Cette application conçue avec Streamlit vous permettra de découvrir le domaine des hôtels écologiques et des langues peu dotée et, nous l'espérons, vous donnera envie d'investir dans ces domaines.")

        st.markdown("**NH Hotels : quelques statistiques**")
        st.markdown("Sur cette page, vous trouverez une présentation du domaine des hôtels écologiques et quelques graphiques effectués avec des données issues du site du groupe NH Hotels. L'objectif est de montrer que l'hôtellerie s'intéresse de plus en plus à l'écologie et que l'écologie n'empêche pas le confort !")
        
        st.markdown("**NH Hotels : Recherche d'hôtels écologiques**")
        st.markdown("Cette page vous permettra d'effectuer une recherche des hôtels écologiques du groupe NH Hotels par ville, afin de voir par vous-mêmes les jolies prestations de ces hôtels.")
        st.markdown("Les informations suivantes vous seront données pour chaque hôtel : nom, nombre d'étoiles, une photo, et un lien vers le site de NH Hotels pour plus d'informations.")
        st.markdown("Afin de vous assurer des informations toujours à jour, notre moteur de recherche cherche en temps réel sur le site de NH Hotels, ce qui peut occasionner une certaine lenteur.")

        st.markdown("**NTeALan : dictionnaire de langues africaines**")
        st.markdown("Vous pourrez consulter sur cette page quelques articles du dictionnaire en ligne de langues africaines peu dotées NTeALan.")
        st.markdown("Nous espérons que le travail de qualité effectué par les bénévoles vous donnera envie d'investir !")

    # Page d'analyses des données du site de NH Hotels
    if radio == "NH Hotels : chiffres":
        prez_hotels.print_analyzes()
        
    # Page de recherches d'hôtels écologiques sur le site de NH Hotels
    if radio == "NH Hotels : recherche":
        recherche_hotels.recherche()
        
    # Page de présentation du dictionnaire en ligne de NTeALan
    if radio == "NTeALan":
        prez_ntealan.ntealan_presentation()
    
if __name__ == "__main__":
    main()
