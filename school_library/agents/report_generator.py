import pandas as pd
import os
import streamlit as st

def generate_report():
    book_path = "data/books.csv"
    student_path = "data/students.csv"

    # Load data safely
    if not os.path.exists(book_path) or not os.path.exists(student_path):
        st.warning("Book or Student data missing.")
        return pd.DataFrame()

    books = pd.read_csv(book_path)
    students = pd.read_csv(student_path)

    report = {
        "Total Books": [len(books)],
        "Books Issued": [books['issued_to'].notnull().sum()],
        "Total Students": [len(students)]
    }

    return pd.DataFrame(report)
