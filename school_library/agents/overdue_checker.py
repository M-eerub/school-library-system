import pandas as pd
import os
import streamlit as st
from datetime import datetime

def get_overdue_books():
    file_path = "data/books.csv"
    if not os.path.exists(file_path):
        st.warning("Books database not found.")
        return pd.DataFrame()

    df = pd.read_csv(file_path)

    if "due_date" not in df.columns:
        st.warning("'due_date' column not found in books.csv")
        return pd.DataFrame()

    df["due_date"] = pd.to_datetime(df["due_date"], errors="coerce")
    overdue = df[df["due_date"] < datetime.today()]
    return overdue
