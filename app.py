import streamlit as st
from app_pages.multipage import MultiPage

from app_pages.page_summary import page_summary_body
#from app_pages.page_sales_price_study import page_sales_price_study
#from app_pages.page_predict_price_tool import page_predict_price_tool
#from app_pages.page_project_hypothesis import page_project_hypothesis
#from app_pages.page_ML_predict_price import page_ml_predict_price


app = MultiPage(app_name= "Heritage Housing Prediction") # Create an instance of the app 


# load pages scripts
app.add_page("Quick Project Summary", page_summary_body)
#app.add_page("Housing Sales Price Study", page_Sales_price_study)
#app.add_page("Prediction Sales Tool", page_predict_price_tool)
#app.add_page("Project Hypothesis and Validation", page_project_hypothesis)
#app.add_page("ML: House Price Predictor", page_ml_predict_price)


app.run() # Run the  app