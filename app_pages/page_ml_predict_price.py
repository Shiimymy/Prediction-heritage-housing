import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from src.data_management import load_pkl_file

def page_ml_predict_price_body():
    """
    Displays ML pipeline, feature importance and ML and regression
    performance plots
    """
    # load price pipeline files
    version = 'v1'
    pipeline = load_pkl_file(
        f"outputs/ml_pipeline/predict_price/{version}/regression_pipeline.pkl")
    feature_importance = plt.imread(
        f"outputs/ml_pipeline/predict_price/{version}/best_features.png")
    X_train = pd.read_csv(
        f"outputs/ml_pipeline/predict_price/{version}/X_train.csv")
    X_test = pd.read_csv(
        f"outputs/ml_pipeline/predict_price/{version}/X_test.csv")
    y_train = pd.read_csv(
        f"outputs/ml_pipeline/predict_price/{version}/y_train.csv")
    y_test = pd.read_csv(
        f"outputs/ml_pipeline/predict_price/{version}/y_test.csv")
    
    st.write("### ML Pipeline: Predict House Price")
    # display pipeline training summary conclusions
    st.success(
        f"The pipeline was shaped to have at least 0.75 accuracy in predicting the sales price of a property. "
        f"This was done to answer the **Business Requirement 2**. \n\n"
        f"* The pipeline performance on train and test set is 0.87 and 0.75, respectively."
    )

    st.write("##### Pipeline steps:")

    # show pipeline
    st.write("1. ML pipeline to predict sales prices of houses.")
    st.code(pipeline)

    # show best features
    st.write("2. The features the model was trained and their importance")
    st.write(X_train.columns.to_list())
    st.image(feature_importance)
    st.write("---")
