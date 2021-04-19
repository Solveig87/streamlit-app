import streamlit as st
import pandas as pd
from scrapping import *

def main():

    # Page d'accueil du projet
    st.title("Smart Investment")
    st.subtitle("Logements écologiques et langues peu dotées")
    st.sidebar.header("Projet pour le cours de Techniques web - M2 TAL, Inalco ")
    st.sidebar.info('Auteur : Solveig PODER')
    st.info("Pour vous permettre d'investir l'avenir")

    # Radio selector sur sidebar pour aller aux pages différentes
    st.sidebar.header("Votre sélection :")
    radio = st.sidebar.radio(label="", options=['Présentation','NH Hotels : chiffres', 'NH Hotels : recherche', 'Ntealan'])

    # Si bouton 'Présentation' sélectionné
    if radio == "Présentation":
        st.markdown("## Présentation du projet ")
        st.markdown("Cette application conçue avec Streamlit vous permettra de découvrir le domaine des hôtels écologiques et des langues peu dotée et, nous l'espérons, vous donnera envie d'investir dans ces domaines.")
        st.markdown("### À gauche dans le sidebar, vous trouverez 4 boutons à sélectionner pour aller à la page correspondante: ")
        df_presentation = pd.DataFrame({'Thème': ['Présentation générale', 'NH Hotel : quelques graphiques','NH Hotel : Recherche d\'hôtels', 'Présentation du dictionnaire en ligne Ntealan'], 'Bouton': ['Présentation','NH Hotels : chiffres', 'NH Hotels : recherche', 'Ntealan']})
        st.dataframe(df_presentation)
        st.markdown("**NH Hotels : présentations**")
        st.markdown("Sur cette page, vous trouverez une présentation du domaine des hôtels écologiques et quelques graphiques effectués avec des données issues du site du groupe NH Hotels. L'objectif est de montrer que l'hôtellerie s'intéresse de plus en plus à l'écologie et que l'écologie n'empêche pas le confort !")
        
        st.markdown("***NH Hotels : Recherche***")
        st.markdown("Cette page vous permettra d'effectuer une recherche des hôtels écologiques du groupe NH Hotels par ville, afin de voir par vous-mêmes les jolies prestations de ces hôtels.")
        st.markdown("Les informations suivantes vous seront données pour chaque hôtel : nom, nombre d'étoiles, une photo, et un lien vers le site de NH Hotels pour plus d'informations.")
        st.markdown("Afin de vous assurer des informations toujours à jour, notre moteur de recherche cherche en temps réel sur le site de NH Hotels, ce qui peut occasionner une certaine lenteur.")

        st.markdown("**Ntealan : dictionnaire de langues africaines**")
        st.markdown("Vous pourrez consulter sur cette page quelques articles du dictionnaire en ligne de langues africaines peu dotées Ntealan.")
        st.markdown("Nous espérons que le travail de qualité effectué par les bénévoles vous donnera envie d'investir !")

        st.write(" <--- Veuillez sélectionner un bouton pour commencer !")
        
    if radio == "NH Hotels : recherche":
        hotels_scraping.recherche()
    
if __name__ == "__main__":
    main()
