import pandas as pd
import os
import streamlit as st

def return_book(title, student_id):
    file_path = "data/books.csv"
    if not os.path.exists(file_path):
        st.warning("CSV file not found.")
        return False

    df = pd.read_csv(file_path)

    # Normalize input and CSV columns
    title = title.strip().lower()
    student_id = str(student_id).strip()

    if not {"title", "issued_to"}.issubset(df.columns):
        st.warning("CSV is missing required columns.")
        return False

    # Normalize CSV fields
    df["title"] = df["title"].astype(str).str.strip().str.lower()
    df["issued_to"] = df["issued_to"].astype(str).str.strip()

    mask = (df["title"] == title) & (df["issued_to"] == student_id)

    if not mask.any():
        st.warning("No such record")
        return False

    df.loc[mask, "issued_to"] = None
    if "due_date" in df.columns:
        df.loc[mask, "due_date"] = None

    df.to_csv(file_path, index=False)
    st.success(f"Book '{title}' returned successfully.")
    return True
