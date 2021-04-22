# Application Streamlit pour la visualisation de données scrappées

**Projet pour le cours de Techniques Web, M2 TAL IM Inalco**

**Auteur : Solveig PODER**

### Outils utilisés
- Streamlit
- Selenium
- BeautifulSoup

### Sites web scrappés
- NH Hotels
- NTeALan

## Lancement de l'application

Avant de lancer, créez un environnement virtuel et installez les librairies :

```python -m virtualenv venv```

```source venv/bin/activate```

```pip install -r requirements. txt```

Pour lancer l'application, placez-vous à la racine du répertoire et tapez ```streamlit run app.py``` dans le terminal, puis rendez-vous à l'URL qui s'affiche.

L'application est également visible sur Heroku en cliquant [ici](https://streamlit-investment-plan.herokuapp.com/)

Le répertoire *scrapping* contient les scripts ayant servi au scrapping des sites web et à la création des fichiers json dans le dossier *data*. Ces scripts ne sont plus utilisés par l'application mais peuvent être relancés pour mettre à jour les fichiers json. Pour ce faire, il faudra disposer d'un compte sur le site de [NTeALan](ntealan.net) et compléter le fichier *.env* avec vos identifiants.

Pour plus d'information sur cette application, vous référer au manuel utilisateur.