import streamlit as st
from src.data_management import load_house_price_data
import matplotlib.pyplot as plt
import seaborn as sns
import ppscore as pps
sns.set_style("whitegrid")
from feature_engine.discretisation import ArbitraryDiscretiser
import numpy as np
import plotly.express as px


vars_to_study = ['OverallQual', 'GarageArea', 'YearBuilt', 'GarageYrBlt', 'YearRemodAdd', 'GrLivArea', '1stFlrSF', 'TotalBsmtSF', 'KitchenQual']

def page_sales_price_study_body():

    """
    Display correlated features and a checkbox to show
    house price per variable.
    """

    df = load_house_price_data() # load data


    st.write("### Housing Prices Study")

    st.info(
        f"**Business Requirement 1** - The client is interested in discovering how the house attributes correlate with the sale price.\
        Therefore, the client expects data visualisations of the correlated variables against the sale price to show that."
    )

    # inspect data
    if st.checkbox("Inspect House "):
        st.write(
            f"* The dataset has {df.shape[0]} rows and {df.shape[1]} columns, "
            f"find below the first 10 rows.")

        st.write(df.head(10))

    st.write("---")

    # Correlation Study Summary
    st.write(
        f"* A correlation study was conducted in the notebook to better understand how "
        f"the variables are correlated to the price of houses. \n"
        f"The most correlated variable are: **{vars_to_study}**"
    )

    # Text based on "Sales Price Study" notebook - "Conclusions" section
    st.info(
        f"The correlation indications and plots below interpretation converge. We saw that 9 attributes have a high correlation with SalePrice: \n"
        f"* ['OverallQual'], ['GarageArea'], ['YearBuilt'], ['GarageYrBlt'] and ['YearRemodAdd'] have high correlation with SalePrice and a narrow confidence interval bands along the entire regression line. \n"
        f"* ['GrLivArea'], ['1stFlrSF'] and ['TotalBsmtSF'] have high correlation with SalePrice. However the confidence interval bands might be narrow at the start of the regression line, it widden after a SalePrice of 350,000 dollars. We can still consider these features ss we saw on the SalePrice distribution, most of the houses have a Sale Price inferior. The other reason we can consider the ['GrLivArea'], ['1stFlrSF'] and ['TotalBsmtSF'] is that we can see from the data that houses are generaly small. \n"
        f"* ['KitchenQual'] has a high correlation too, even with a missing category (that would be a limit). For the 4 other features, we can see that the quality of the Kitchen corrolate with the SalePrice. \n"
    )

    st.success(
        f"It allow us to confirm: \n"
        f"* A higher Sale price typically has a larger size. \n"
        f"* A higher Sale price typically has a better quality. \n"
        f"* A higher Sale price typically was built recently. \n"
    )

    
    df_eda = df.filter(vars_to_study + ['SalePrice'])
    target_var = 'SalePrice'
    
    st.write("#### Data visualizations")
    
    # Distribution of target variable checkbox
    
    if st.checkbox("Distribution of target variable"):
        plot_target_hist(df_eda, target_var)
    
    # Individual plots per variable checkbox

    if st.checkbox("Sale Price per Variable"):
        sale_price_per_variable(df_eda)

    # Heatmaps checkbox

    if st.checkbox("Heatmaps: Pearson, Spearman and PPS Correlations"):
        df_corr_pearson, df_corr_spearman, pps_matrix = CalculateCorrAndPPS(df)
        DisplayCorrAndPPS(df_corr_pearson = df_corr_pearson,
                  df_corr_spearman = df_corr_spearman, 
                  pps_matrix = pps_matrix,
                  CorrThreshold = 0.4, PPS_Threshold =0.2,
                  figsize=(12,10), font_annot=10)


# Distribution of target variable plot function based on "Sales Price Study" notebook

def plot_target_hist(df, target_var):
    """
    Function to plot a histogram of the target variable
    """
    fig, axes = plt.subplots(figsize=(12, 6))
    sns.histplot(df['SalePrice'], kde=True)
    plt.axvline(x=df['SalePrice'].mean(), color='g', linewidth=2)
    plt.title(f"Distribution of {target_var}", fontsize=18)
    st.pyplot(fig)

# Individual plots per variable functions based on "Sales Price Study" notebook

def sale_price_per_variable(df_eda):
    target_var = 'SalePrice'
    categorical_var = 'KitchenQual'

    for col in vars_to_study[:-1]: # Only the last vars_to_study is a categorical variable
        plot_numerical(df_eda, col, target_var)
        print("\n\n")
        
    plot_categorical(df_eda, categorical_var, target_var)


def plot_numerical(df, col, target_var):
  fig = plt.figure(figsize=(10, 7))
  sns.regplot(data=df, x=col, y=target_var, line_kws={"color": "green"})
  plt.title(f"{col}", fontsize=20)
  st.pyplot(fig)


def plot_categorical(df, categorical_var, target_var):
  fig = plt.figure(figsize=(10, 7))
  sns.boxplot(data=df, x=categorical_var, y=target_var)  
  plt.title(f"{categorical_var}", fontsize=20)
  st.pyplot(fig)


# Heatmaps plots functions based on "Sales Price Study" notebook

def heatmap_corr(df,threshold, figsize=(20,12), font_annot = 8):
  """
  Function to create heatmap using correlations.
  """
  if len(df.columns) > 1:
    mask = np.zeros_like(df, dtype=np.bool)
    mask[np.triu_indices_from(mask)] = True
    mask[abs(df) < threshold] = True

    fig, axes = plt.subplots(figsize=figsize)
    sns.heatmap(df, annot=True, xticklabels=True, yticklabels=True,
                mask=mask, cmap='viridis', annot_kws={"size": font_annot}, ax=axes,
                linewidth=0.5
                     )
    axes.set_yticklabels(df.columns, rotation = 0)
    plt.ylim(len(df.columns),0)
    st.pyplot(fig)


def heatmap_pps(df,threshold, figsize=(20,12), font_annot = 8):
    """
    Function to create heatmap using pps.
    """
    if len(df.columns) > 1:

      mask = np.zeros_like(df, dtype=np.bool)
      mask[abs(df) < threshold] = True

      fig, ax = plt.subplots(figsize=figsize)
      ax = sns.heatmap(df, annot=True, xticklabels=True,yticklabels=True,
                       mask=mask,cmap='rocket_r', annot_kws={"size": font_annot},
                       linewidth=0.05,linecolor='grey')
      
      plt.ylim(len(df.columns),0)
      st.pyplot(fig)


def CalculateCorrAndPPS(df):
  """
  Function to calculate correlations and pps.
  """
  df_corr_spearman = df.corr(method="spearman")
  df_corr_spearman.name = 'corr_spearman'
  df_corr_pearson = df.corr(method="pearson")
  df_corr_pearson.name = 'corr_pearson'

  pps_matrix_raw = pps.matrix(df)
  pps_matrix = pps_matrix_raw.filter(['x', 'y', 'ppscore']).pivot(columns='x', index='y', values='ppscore')

  pps_score_stats = pps_matrix_raw.query("ppscore < 1").filter(['ppscore']).describe().T
  print(pps_score_stats.round(3))

  return df_corr_pearson, df_corr_spearman, pps_matrix


def DisplayCorrAndPPS(df_corr_pearson, df_corr_spearman, pps_matrix,CorrThreshold,PPS_Threshold,
                      figsize=(20,12), font_annot=8 ):
  """
  Function to display the correlations and pps.
  """

  heatmap_corr(df=df_corr_spearman, threshold=CorrThreshold, figsize=figsize, font_annot=font_annot)

  heatmap_corr(df=df_corr_pearson, threshold=CorrThreshold, figsize=figsize, font_annot=font_annot)

  heatmap_pps(df=pps_matrix,threshold=PPS_Threshold, figsize=figsize, font_annot=font_annot)



