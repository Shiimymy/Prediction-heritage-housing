import streamlit as st

def page_project_hypothesis_body():
    st.write("### Project Hypothesis and Validation")

    # conclusions taken from "SalesPriceStudy" notebook
    st.success(
        f"We suspect that the size, the quality of the house and the year it was built impact the sale price \
        and that the price correlates strongly with other features: \n"
        f"* **It is correct**: The correlation study the Sales Price Study supports that."
    )
    
    st.info(
        f"**Hypothesis 1:** \n"
        f"* We expect that the size of a house is positively correlated to the sale price.\
        A larger house will tend to have a higher price.\
        The features that confirm it are 'GrLivArea', '1stFlrSF' and 'TotalBsmtSF'. \n"

        f"* Then we can also expect that the better the quality of the house, the higher the price too.\
        It is confirmed thanks to the following features: 'OverallQual' and 'KitchenQual'. \n"

        f"* Finally, we expect that the age of the house impact positively the sale price. \
        It is confimed thanks to the 'YearBuilt' feature."
    )

    st.info(
        f"**Hypothesis 2:** \n"

        f"* When analysing the dataset, we suspect that the price of a house would correlate strongly with other different features: "
        f"We can confirm that the price of a house correlates strongly with other different features: ['GarageYrBlt'], ['GarageArea'] and ['YearRemodAdd']. \
        We can see that the Garage and remodel date are important features in the area of Ames, Iowa."
    )

    st.info(
        f"**Hypothesis 3:** \n"

        f"* We proposed that it is possible to predict a property's sale price with a reasonable model performance of a R2 score of at least 0.75 with the given dataset. "
        f"This hypothesis was confirmed during the evalution of performance of the train and test set in the Modelling & Evaluation notebook. The score is 0.87 and 0.75, respectively."

        f" (*More details on next page.*) "
    )