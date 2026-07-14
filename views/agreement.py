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

    # Create Agreement from Owner
    elif "selected_owner" in st.session_state:

        owner = st.session_state["selected_owner"]

        existing_data = {

            "owner_name": owner["owner_name"],

            "owner_age": owner["owner_age"],

            "owner_address": owner["owner_address"],

            "owner_mobile": owner["owner_mobile"]

        }

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

            if "selected_owner" in st.session_state:

                del st.session_state["selected_owner"]

            if "renew_customer_id" in st.session_state:

                del st.session_state["renew_customer_id"]

        except Exception as e:

            st.error(
                f"Error : {e}"
            )

            return

        st.success(
            "Documents Generated Successfully."
        )

        safe_name = (

            data["tenant_name"]

            .replace(" ", "_")

            .replace("/", "-")

            .replace("\\", "-")

        )

        agreement_name = f"{safe_name}_Agreement.pdf"

        noc_name = f"{safe_name}_Police_NOC.pdf"


        with open(
            result["agreement_pdf"],
            "rb"
        ) as file:

            st.download_button(

                "📄 Download Agreement",

                file,

                file_name=agreement_name

            )

        noc_name = (

            f"{data['tenant_name']}_Police_NOC.pdf"

        )

        with open(
            result["noc_pdf"],
            "rb"
        ) as file:

            st.download_button(

                "👮 Download Police NOC",

                file,

                file_name=noc_name

            )