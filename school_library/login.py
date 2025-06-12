import streamlit as st

USERS = {
    "admin": {"password": "admin123", "role": "admin"},
    "student1": {"password": "student123", "role": "student"},
}

def login_panel():
    st.sidebar.title("🔐 Login")
    username = st.sidebar.text_input("Username")
    password = st.sidebar.text_input("Password", type="password")
    login_button = st.sidebar.button("Login")

    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False
        st.session_state.role = None

    if login_button:
        user = USERS.get(username)
        if user and user["password"] == password:
            st.session_state.logged_in = True
            st.session_state.role = user["role"]
            st.success(f"Logged in as {username} ({user['role']})")
        else:
            st.error("Invalid credentials")

    if st.session_state.logged_in:
        if st.sidebar.button("Logout"):
            st.session_state.logged_in = False
            st.session_state.role = None
            st.rerun()

    return st.session_state.logged_in, st.session_state.role
