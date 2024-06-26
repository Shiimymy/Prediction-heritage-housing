import streamlit as st
import pandas as pd
import numpy as np
import joblib

@st.cache(suppress_st_warning=True, allow_output_mutation=True)
def load_house_price_data():
    df = pd.read_csv("outputs/datasets/cleaned/clean_pipeline.csv")
    return df

@st.cache(suppress_st_warning=True, allow_output_mutation=True)
def load_heritage_data():
    df_inherited = pd.read_csv("inputs/datasets/raw/house-price-20211124T154130Z-001/house-price/inherited_houses.csv")
    return df_inherited

def load_pkl_file(file_path):
    return joblib.load(filename=file_path) 