import streamlit as st

from components.form import agreement_form

from services.customer_service import get_customer_by_id

from services.agreement_service import generate_documents


def agreement_page():

    st.header(
        "📄 New Rent Agreement"
    )

    existing_data = None

    if "renew_customer_id" in st.session_state:

        existing_data = get_customer_by_id(
            st.session_state["renew_customer_id"]
        )

    data = agreement_form(
        existing_data
    )

    if st.button(
        "Generate Documents"
    ):

        try:

            result = generate_documents(
                data
            )

        except Exception as e:

            st.error(
                f"Error : {e}"
            )

            return

        st.success(
            "Documents Generated Successfully."
        )

        with open(
            result["agreement_pdf"],
            "rb"
        ) as file:

            st.download_button(

                "📄 Download Agreement",

                file,

                file_name="rent_agreement.pdf"

            )

        with open(
            result["noc_pdf"],
            "rb"
        ) as file:

            st.download_button(

                "👮 Download Police NOC",

                file,

                file_name="police_noc.pdf"

            )