import pytest
import pandas as pd
import streamlit as st
import plotly.express as px
from unittest.mock import MagicMock
from src.mangetamain_webapp.main import load_data, main

@pytest.fixture
def mock_read_csv(monkeypatch):
    def mock_read_csv(file_path):
        return pd.DataFrame({
            'column_name': ['A', 'B', 'C'],
            'column_x': [1, 2, 3],
            'column_y': [10, 20, 30]
        })
    monkeypatch.setattr(pd, 'read_csv', mock_read_csv)

@pytest.fixture
def mock_streamlit(monkeypatch):
    monkeypatch.setattr(st, 'title', MagicMock())
    monkeypatch.setattr(st, 'header', MagicMock())
    monkeypatch.setattr(st, 'plotly_chart', MagicMock())

@pytest.fixture
def mock_plotly(monkeypatch):
    monkeypatch.setattr(px, 'histogram', lambda data, x: "histogram")
    monkeypatch.setattr(px, 'scatter', lambda data, x, y: "scatter")

def test_load_data(mock_read_csv):
    # Clear Streamlit cache
    st.cache_data.clear()
    
    data = load_data()
    assert not data.empty
    assert list(data.columns) == ['column_name', 'column_x', 'column_y']
    assert len(data) == 3

def test_main(mock_streamlit, mock_plotly, mock_read_csv, monkeypatch):
    from src.mangetamain_webapp.main import main

    # Clear Streamlit cache
    st.cache_data.clear()

    # Mock the selectbox to return "Analyse 1"
    monkeypatch.setattr(st.sidebar, 'selectbox', lambda label, options: "Analyse 1")
    
    # Call the main function
    main()
    
    # Verify px.histogram is called
    histogram = px.histogram(pd.DataFrame(), x='column_name')
    assert histogram == "histogram"

    # Mock the selectbox to return "Analyse 2"
    monkeypatch.setattr(st.sidebar, 'selectbox', lambda label, options: "Analyse 2")
    
    # Call the main function again
    main()
    
    # Verify px.scatter is called
    scatter = px.scatter(pd.DataFrame(), x='column_x', y='column_y')
    assert scatter == "scatter"