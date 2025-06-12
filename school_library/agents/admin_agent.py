import pandas as pd
import streamlit as st
import os

def system_status():
    books = pd.read_csv("data/books.csv")
    students = pd.read_csv("data/students.csv")
    issued = books[books['issued_to'].notnull()]
    return f"📚 {len(books)} books | 👨‍🎓 {len(students)} students | 📦 {len(issued)} issued"

def run():
    st.subheader("🔒 Admin Panel")
    st.write(system_status())
