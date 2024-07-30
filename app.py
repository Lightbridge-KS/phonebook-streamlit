import pandas as pd
import streamlit as st

# Load the data
phonebook_raw = pd.read_csv("data/TelephoneDepartment.csv")
phonebook = phonebook_raw[["CodeName", "Description", "Telephone"]].fillna("")

def query_any_column_df(df, query_text: str, case=False):
    """
    Filters the rows of a DataFrame based on whether any column contains the query text.
    """
    mask = df.apply(lambda column: column.astype(str).str.contains(query_text, case=case)).any(axis=1)
    filtered_df = df[mask]
    return filtered_df

# Set page title
st.set_page_config(page_title="PhoneBook")

# App title
st.title("PhoneBook")

# Search input
search_text = st.text_input("Search")

# Filter dataframe based on search input
if search_text:
    filtered_df = query_any_column_df(phonebook, search_text)
    
    # Display filtered dataframe
    if not filtered_df.empty:
        st.dataframe(filtered_df, use_container_width=True)
    else:
        st.write("No results found.")
else:
    # Display full dataframe when no search input
    st.dataframe(phonebook, use_container_width=True)
