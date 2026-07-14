import streamlit as st

from views.dashboard import dashboard_page
from views.agreement import agreement_page
from views.customer_search import customer_search_page
from views.reminders import reminder_page
from views.owner_management import owner_management_page

st.set_page_config(

    page_title="More Enterprises",

    page_icon="🏠",

    layout="wide"

)


# =====================================
# Navigation State
# =====================================

if "menu" not in st.session_state:
    st.session_state.menu = "🏠 Dashboard"


st.sidebar.title(
    "🏠 More Enterprises"
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

    ].index(st.session_state.menu)

)


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