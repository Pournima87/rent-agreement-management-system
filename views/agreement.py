import streamlit as st

from components.form import agreement_form

from services.customer_service import get_customer_by_id

from services.agreement_service import generate_documents


# =====================================
# Agreement Page
# =====================================

def agreement_page():

    st.header(
        "📄 New Rent Agreement"
    )

    # =================================
    # Existing Customer / Owner Data
    # =================================

    existing_data = None

    if "renew_customer_id" in st.session_state:

        existing_data = get_customer_by_id(
            st.session_state["renew_customer_id"]
        )

    elif "selected_owner" in st.session_state:

        owner = st.session_state["selected_owner"]

        existing_data = {

            "owner_name":
                owner["owner_name"],

            "owner_address":
                owner["owner_address"],

            "owner_mobile":
                owner["owner_mobile"]

        }

    # =================================
    # Agreement Form
    # =================================

    data = agreement_form(
        existing_data
    )

    # =================================
    # Generate Documents
    # =================================

    if st.button(
        "📄 Generate Documents",
        use_container_width=True
    ):

        try:

            result = generate_documents(
                data
            )

            # -----------------------------
            # Store result in session
            # -----------------------------

            st.session_state.generated_documents = result

            st.session_state.generated_tenant_name = (
                data["tenant_name"]
            )

            # -----------------------------
            # Clear temporary selection
            # -----------------------------

            if "selected_owner" in st.session_state:

                del st.session_state[
                    "selected_owner"
                ]

            if "renew_customer_id" in st.session_state:

                del st.session_state[
                    "renew_customer_id"
                ]

            st.success(
                "Documents Generated Successfully."
            )

        except Exception as e:

            st.error(
                f"Error : {e}"
            )

            return

    # =================================
    # Show Generated Document
    # =================================

    if "generated_documents" in st.session_state:

        result = st.session_state[
            "generated_documents"
        ]

        tenant_name = st.session_state.get(
            "generated_tenant_name",
            "Tenant"
        )

        safe_name = (

            tenant_name

            .replace(" ", "_")

            .replace("/", "-")

            .replace("\\", "-")

        )

        combined_name = (
            f"{safe_name}_Complete_Documents.pdf"
        )

        # ---------------------------------
        # Download Combined PDF
        # ---------------------------------

        try:

            with open(
                result["combined_pdf"],
                "rb"
            ) as file:

                st.download_button(

                    "📥 Download Complete Documents",

                    file,

                    file_name=combined_name,

                    mime="application/pdf",

                    use_container_width=True

                )

        except FileNotFoundError:

            st.warning(
                "The generated PDF is no longer available. "
                "Please generate the documents again."
            )