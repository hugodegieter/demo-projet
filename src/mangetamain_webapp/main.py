import streamlit as st
import pandas as pd
import plotly.express as px


# Charger les données
@st.cache_data
def load_data():
    data = pd.read_csv("data/dataset.csv")
    return data


data = load_data()

# Titre de l'application
st.title("Mangetamain Webapp d'Analyse de Données")

# Sélectionner une analyse
analysis_type = st.sidebar.selectbox(
    "Choisissez une analyse", ["Analyse 1", "Analyse 2"]
)

if analysis_type == "Analyse 1":
    st.header("Analyse 1")
    fig = px.histogram(data, x="column_name")
    st.plotly_chart(fig)
elif analysis_type == "Analyse 2":
    st.header("Analyse 2")
    fig = px.scatter(data, x="column_x", y="column_y")
    st.plotly_chart(fig)
