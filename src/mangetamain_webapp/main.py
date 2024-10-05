import pandas as pd
import streamlit as st
import plotly.express as px


@st.cache_data
def load_data():
    return pd.read_csv("data/dataset.csv")


def main():
    data = load_data()
    analysis_type = st.sidebar.selectbox(
        "Choisissez une analyse", ["Analyse 1", "Analyse 2"]
    )

    if analysis_type == "Analyse 1":
        st.header("Analyse 1")
        fig = px.histogram(data, x="column_name")
        st.plotly_chart(fig)

    if analysis_type == "Analyse 2":
        st.header("Analyse 2")
        fig = px.scatter(data, x="column_x", y="column_y")
        st.plotly_chart(fig)


if __name__ == "__main__":
    main()
