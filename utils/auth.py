import streamlit as st

MOCK_USERS = {
    "admin@gmail.com": {
        "password": "admin123",
        "name": "Alex Mercer",
        "company": "NexusTech Solutions",
        "role": "Pricing Analyst",
        "plan": "Pro",
        "joined": "Jan 2024"
    },
    "demo@nexus.ai": {
        "password": "demo2024",
        "name": "Priya Sharma",
        "company": "ShopSmart India",
        "role": "E-Commerce Manager",
        "plan": "Starter",
        "joined": "Mar 2024"
    }
}


def init_session():
    defaults = {
        "logged_in": False,
        "user_email": None,
        "user_data": None,
        "prediction_history": [],
        "total_predictions": 0,
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v


def login(email: str, password: str) -> bool:
    user = MOCK_USERS.get(email.strip().lower())
    if user and user["password"] == password:
        st.session_state.logged_in = True
        st.session_state.user_email = email
        st.session_state.user_data = user
        return True
    return False


def logout():
    st.session_state.logged_in = False
    st.session_state.user_email = None
    st.session_state.user_data = None
    st.rerun()


def require_auth():
    init_session()
    if not st.session_state.logged_in:
        st.switch_page("app.py")


def get_user() -> dict:
    return st.session_state.get("user_data", {})
