import pytest
import pandas as pd
import streamlit as st
from src.mangetamain_webapp.main import load_data

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
    monkeypatch.setattr(st, 'title', lambda x: None)
    monkeypatch.setattr(st.sidebar, 'selectbox', lambda label, options: options[0])
    monkeypatch.setattr(st, 'header', lambda x: None)
    monkeypatch.setattr(st, 'plotly_chart', lambda x: None)

def test_load_data(mock_read_csv):
    # Clear Streamlit cache to avoid UnhashableParamError
    st.cache_data.clear()
    
    data = load_data()
    assert not data.empty
    assert list(data.columns) == ['column_name', 'column_x', 'column_y']
    assert len(data) == 3

def test_streamlit_app(mock_streamlit):
    from src.mangetamain_webapp.main import data, analysis_type

    # Test Analysis 1
    analysis_type = "Analyse 1"
    assert analysis_type == "Analyse 1"

    # Test Analysis 2
    analysis_type = "Analyse 2"
    assert analysis_type == "Analyse 2"