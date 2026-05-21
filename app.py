import streamlit as st

from app_pages.dashboard import show_dashboard
from app_pages.prediction import show_prediction
from app_pages.analytics import show_analytics

st.set_page_config(
    page_title="Dynamic Pricing System",
    page_icon="💰",
    layout="wide"
)


with open("assets/styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "page" not in st.session_state:
    st.session_state.page = "Dashboard"


def login_page():

    st.markdown(
        """
        <div class='main-title'>
            AI Dynamic Pricing System
        </div>
        """,
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns([1, 1.2, 1])

    with col2:

        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)

        st.subheader("Login")

        email = st.text_input("Email")

        password = st.text_input("Password", type="password")

        remember = st.checkbox("Remember Me")

        if st.button("Login", use_container_width=True):

            if email == "admin@gmail.com" and password == "admin123":

                st.session_state.logged_in = True
                st.success("Login Successful")
                st.rerun()

            else:
                st.error("Invalid Credentials")

        st.markdown("</div>", unsafe_allow_html=True)

def sidebar_navigation():

    st.sidebar.markdown("# 💰 Dynamic Pricing")

    page = st.sidebar.radio(
        "Navigation",
        [
            "Dashboard",
            "Prediction",
            "Analytics"
        ]
    )

    if page == "Dashboard":
        st.session_state.page = "Dashboard"

    elif page == "Prediction":
        st.session_state.page = "Prediction"

    elif page == "Analytics":
        st.session_state.page = "Analytics"

    st.sidebar.markdown("---")

    if st.sidebar.button("Logout"):

        st.session_state.logged_in = False
        st.rerun()


# =========================
# MAIN APP
# =========================
if not st.session_state.logged_in:

    login_page()

else:

    sidebar_navigation()

    if st.session_state.page == "Dashboard":
        show_dashboard()

    elif st.session_state.page == "Prediction":
        show_prediction()

    elif st.session_state.page == "Analytics":
        show_analytics()