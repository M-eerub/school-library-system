# agents/search_agent.py

import pandas as pd
import streamlit as st
import os

def search_books(query):
    file_path = "data/books.csv"
    if os.path.exists(file_path):
        df = pd.read_csv(file_path)
    else:
        st.warning("Books database not found.")
        return pd.DataFrame()

    if query.strip() == "":
        return df
    return df[df["title"].str.contains(query, case=False, na=False)]

def search_students(query):
    file_path = "data/students.csv"
    if os.path.exists(file_path):
        df = pd.read_csv(file_path)
    else:
        st.warning("Student database not found.")
        return pd.DataFrame()

    if query.strip() == "":
        return df
    return df[df["name"].str.contains(query, case=False, na=False)]

def run():
    st.subheader("🔍 Search")
    search_option = st.selectbox("Search for", ["Books", "Students"])
    query = st.text_input("Enter search query")

    if search_option == "Books":
        st.dataframe(search_books(query))
    elif search_option == "Students":
        st.dataframe(search_students(query))
