import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt
from matplotlib import rcParams
import json
from collections import Counter
import streamlit as st

def load_json(js_file):
    with open(js_file, 'r') as f:
        data = json.load(f)
        return data

def print_analyzes():
    hotels = load_json('resources/hotels.json')

    cnt_eco = Counter()
    cnt_eco['oui'] = len([hotel for hotel, infos in hotels.items() if infos['éco-friendly'] == True])
    cnt_eco['non'] = len([hotel for hotel, infos in hotels.items() if infos['éco-friendly'] == False])

    # ----------- table et pie chart par catégorie -------------
    df = pd.DataFrame(list(cnt_eco.items()),columns = ["éco-friendly","nombre"]) 
    st.dataframe(df)

    fig = px.pie(df, values='Nombre', names='éco-friendly', title="Répartition des hôtels éco-friendly et non éco-friendly :")
    st.write(fig)

    fig = plt.figure()
    ax = fig.add_subplot()
    ax.pie(cnt_eco.values(), labels=cnt_eco.keys(), autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax.axis('equal')
    plt.title('Répartition des hôtels éco-friendly et non éco-friendly')
    st.write(ax)
    #plt.savefig("data/graphique.png")
    plt.close()