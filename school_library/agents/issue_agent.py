from datetime import datetime, timedelta
import pandas as pd
import os
import streamlit as st

def issue_book(title, student_id):
    file_path = "data/books.csv"

    if not os.path.exists(file_path):
        st.error("Books database not found.")
        return False

    df = pd.read_csv(file_path)

    available = df[(df["title"] == title) & (df["issued_to"].isnull())]
    if available.empty:
        st.warning("Book not available or already issued.")
        return False

    index = available.index[0]
    df.at[index, "issued_to"] = student_id
    df.at[index, "due_date"] = (datetime.today() + timedelta(days=7)).strftime("%Y-%m-%d")

    df.to_csv(file_path, index=False)
    st.success(f"Book '{title}' issued to Student {student_id}")
    return True
