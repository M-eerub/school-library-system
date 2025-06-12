# agents/book_manager.py

import pandas as pd
import streamlit as st
import os

def add_book(title, author, copies):
    file_path = "data/books.csv"
    if os.path.exists(file_path):
        df = pd.read_csv(file_path)
    else:
        df = pd.DataFrame(columns=["title", "author", "copies", "issued_to"])

    new_row = pd.DataFrame([{"title": title, "author": author, "copies": copies, "issued_to": None}])
    df = pd.concat([df, new_row], ignore_index=True)
    df.to_csv(file_path, index=False)
    st.success(f"Book '{title}' added successfully!")

def remove_book(title):
    file_path = "data/books.csv"
    if os.path.exists(file_path):
        df = pd.read_csv(file_path)
        original_count = len(df)
        df = df[df["title"] != title]
        if len(df) < original_count:
            df.to_csv(file_path, index=False)
            st.success(f"Book '{title}' removed.")
        else:
            st.warning(f"No book found with title '{title}'.")
    else:
        st.error("Book database not found.")

def run():
    st.subheader("📚 Book Manager")
    title = st.text_input("Title")
    author = st.text_input("Author")
    copies = st.number_input("Number of Copies", min_value=1, step=1)

    if st.button("Add Book"):
        add_book(title, author, copies)

    st.markdown("---")

    remove_title = st.text_input("Title to Remove")
    if st.button("Remove Book"):
        remove_book(remove_title)
