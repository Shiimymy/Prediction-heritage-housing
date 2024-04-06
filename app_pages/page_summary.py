import streamlit as st


def page_summary_body():
    """
    Displays contents of the project summary page
    """
    st.write("### Quick Project Summary")

    st.info(
        f"**Project Terms & Jargons**\n\n"
        f"* **Sales price** of a house refers to the current market price,\
         in US dollars, of a house with with various attributes.\n"
        f"* **Inherited house** is a house that the client inherited from grandparents.\n"
        f"* **Summed price** is the total of the predicted sales prices\
         of the four inherited houses.\n\n"
        f"**Project Dataset**\n"
        f"* **Sales price** of a house refers to the current market price,\
         in US dollars, of a house with with various attributes.\n"
        f"* **Inherited house** is a house that the client inherited\
         from grandparents.\n"
        f"* **Summed price** is the total of the predicted sales prices\
         of the four inherited houses.\n\n"
    )

    # Link to README file, so the users can have access to
    # full project documentation
    st.write(
        f"* For additional information, please visit and read the "
        f"[Project README file]\
        (https://github.com/Shiimymy/Prediction-heritage-housing).")

    # copied from README file - "Business Requirements" section
    st.success(
        f"**Project Business Requirements**\n\n"

        f"The project has 2 business requirements:\n"
        f"* **- 1 -** The client is interested in discovering how the house\
         attributes correlate with the sale price."
        f" Therefore, the client expects data visualisations of the correlated\
         variables against the sale price to show that.\n\n"
        f"* **- 2 -** The client is interested in predicting the house sale\
         price from her four inherited houses and any other house\
         in Ames, Iowa."
    )