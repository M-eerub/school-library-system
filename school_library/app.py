import streamlit as st
import sys
import os

# Add the directory of this script to the system path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from agents import (
    book_manager,
    student_manager,
    issue_agent,
    return_agent,
    search_agent,
    overdue_checker,
    report_generator,
    admin_agent
)

from login import login_panel


st.title("📚 School Library System")

menu = st.sidebar.radio("Select Agent", [
    "Book Manager", "Student Manager", "Issue Book", "Return Book",
    "Search", "Overdue Checker", "Report Generator", "Admin"
])

if menu == "Book Manager":
    st.header("📘 Book Manager")
    title = st.text_input("Title")
    author = st.text_input("Author")
    copies = st.number_input("Copies", min_value=1, value=1)
    if st.button("Add Book"):
        book_manager.add_book(title, author, copies)
        st.success("Book added")
    if st.button("Remove Book"):
        book_manager.remove_book(title)
        st.warning("Book removed")

elif menu == "Student Manager":
    st.header("👩‍🎓 Student Manager")
    name = st.text_input("Student Name")
    student_id = st.text_input("Student ID")
    if st.button("Add Student"):
        student_manager.add_student(name, student_id)
        st.success("Student added")

elif menu == "Issue Book":
    st.header("📤 Issue Book")
    title = st.text_input("Book Title")
    student_id = st.text_input("Student ID")
    if st.button("Issue"):
        if issue_agent.issue_book(title, student_id):
            st.success("Book issued")
        else:
            st.error("Book not available")

elif menu == "Return Book":
    st.header("📥 Return Book")
    title = st.text_input("Book Title")
    student_id = st.text_input("Student ID")
    if st.button("Return"):
        if return_agent.return_book(title, student_id):
            st.success("Book returned")
        else:
            st.error("No such record")

elif menu == "Search":
    st.header("🔍 Search")
    query = st.text_input("Search Term")
    if st.button("Search Book"):
        st.dataframe(search_agent.search_books(query))
    if st.button("Search Student"):
        st.dataframe(search_agent.search_students(query))

elif menu == "Overdue Checker":
    st.header("⏰ Overdue Books")
    st.dataframe(overdue_checker.get_overdue_books())

elif menu == "Report Generator":
    st.header("📄 Issued Books Report")
    st.dataframe(report_generator.generate_report())

elif menu == "Admin":
    st.header("⚙️ System Status")
    st.info(admin_agent.system_status())
