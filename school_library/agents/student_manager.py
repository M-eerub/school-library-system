import pandas as pd
import streamlit as st
import os

def add_student(name, student_id):
    file_path = "data/students.csv"
    if os.path.exists(file_path):
        df = pd.read_csv(file_path)
    else:
        df = pd.DataFrame(columns=["name", "id"])

    new_row = pd.DataFrame([{"name": name, "id": student_id}])
    df = pd.concat([df, new_row], ignore_index=True)
    df.to_csv(file_path, index=False)
    st.success(f"Student '{name}' added successfully!")

def run():
    st.subheader("👨‍🎓 Student Manager")
    name = st.text_input("Student Name")
    student_id = st.text_input("Student ID")

    if st.button("Add Student"):
        add_student(name, student_id)
