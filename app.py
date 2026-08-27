import streamlit as st

from database.supabase_client import supabase

from views.dashboard import dashboard_page
from views.agreement import agreement_page
from views.customer_search import customer_search_page
from views.reminders import reminder_page
from views.owner_management import owner_management_page


# =====================================
# Page Configuration
# =====================================

st.set_page_config(
    page_title="More Enterprises",
    page_icon="🏠",
    layout="wide"
)


# =====================================
# Login Function
# =====================================

def login_page():

    st.title("🏠 More Enterprises")

    st.subheader("🔐 Secure Login")

    st.write(
        "Please login to access the More Enterprises system."
    )

    email = st.text_input(
        "Email"
    )

    password = st.text_input(
        "Password",
        type="password"
    )

    if st.button(
        "🔐 Login",
        use_container_width=True
    ):

        if email == "" or password == "":

            st.warning(
                "Please enter both email and password."
            )

            return

        try:

            response = supabase.auth.sign_in_with_password(
                {
                    "email": email,
                    "password": password
                }
            )

            if response.user:

                st.session_state.logged_in = True
                st.session_state.user = response.user

                st.session_state.access_token = response.session.access_token
                st.session_state.refresh_token = response.session.refresh_token

                st.success(
                    "Login successful!"
                )

                st.rerun()

        except Exception as e:

            st.error(
                "Invalid email or password."
            )


# =====================================
# Authentication State
# =====================================

if "logged_in" not in st.session_state:

    st.session_state.logged_in = False


if "access_token" not in st.session_state:

    st.session_state.access_token = None


if "refresh_token" not in st.session_state:

    st.session_state.refresh_token = None

# =====================================
# Restore Supabase Authentication
# =====================================

if (
    st.session_state.logged_in
    and st.session_state.access_token
    and st.session_state.refresh_token
):

    try:

        supabase.auth.set_session(
            st.session_state.access_token,
            st.session_state.refresh_token
        )

    except Exception:

        st.session_state.logged_in = False
        st.session_state.access_token = None
        st.session_state.refresh_token = None

# =====================================
# Show Login Before Application
# =====================================

if not st.session_state.logged_in:

    login_page()

    st.stop()


# =====================================
# Navigation State
# =====================================

if "menu" not in st.session_state:

    st.session_state.menu = "🏠 Dashboard"


# =====================================
# Sidebar
# =====================================

st.sidebar.title(
    "🏠 More Enterprises"
)

st.sidebar.caption(
    "🔐 Secure Access"
)


st.session_state.menu = st.sidebar.radio(

    "Navigation",

    [

        "🏠 Dashboard",

        "👤 Owners",

        "📄 New Agreement",

        "🔍 Customer Search",

        "🔔 Reminder Center"

    ],

    index=[

        "🏠 Dashboard",

        "👤 Owners",

        "📄 New Agreement",

        "🔍 Customer Search",

        "🔔 Reminder Center"

    ].index(
        st.session_state.menu
    )

)


# =====================================
# Logout
# =====================================

st.sidebar.divider()

if st.sidebar.button(
    "🚪 Logout",
    use_container_width=True
):

    try:

        supabase.auth.sign_out()

    except Exception:

        pass

    st.session_state.logged_in = False
    st.session_state.user = None
    st.session_state.access_token = None
    st.session_state.refresh_token = None
    st.session_state.menu = "🏠 Dashboard"

    st.rerun()


# =====================================
# Pages
# =====================================

if st.session_state.menu == "🏠 Dashboard":

    dashboard_page()


elif st.session_state.menu == "👤 Owners":

    owner_management_page()


elif st.session_state.menu == "📄 New Agreement":

    agreement_page()


elif st.session_state.menu == "🔍 Customer Search":

    customer_search_page()


elif st.session_state.menu == "🔔 Reminder Center":

    reminder_page()