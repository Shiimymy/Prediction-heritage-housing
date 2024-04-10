import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from src.data_management import load_pkl_file
from src.machine_learning.evaluate_reg import regression_performance, regression_evaluation_plots


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
        f"This was done to answer the **Business Requirement 2**."
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

    st.write("### Pipeline Performance")

    st.write("##### Performance goal of the predictions:\n")
    st.write("* We agreed with the client an R2 score of at least 0.75 on the train set as well as on the test set.")
    regression_performance(X_train=X_train, y_train=y_train,
                        X_test=X_test, y_test=y_test,
                        pipeline=pipeline)
    st.write("We can see that the test set is slightly under the R2 score of 0.75 and the train set is well above.")
    st.write("If we round the scores, we can say that the regressor pipeline reached the expected performance threshold. \n\n")

    st.write("### Regression Performance Plots")
    st.write("* The regression performance plots below indicate that our model,\
         in most part, is able to predict sale prices well. The model looks less effective for houses with high prices though.")
    regression_evaluation_plots(X_train=X_train, y_train=y_train, X_test=X_test, y_test=y_test, pipeline=pipeline)  
