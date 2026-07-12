import streamlit as st

from services.customer_service import search_customer


def customer_search_page():

    st.header(
        "🔍 Customer Search"
    )

    keyword = st.text_input(
        "Search by Name, Mobile or Address"
    )

    if keyword == "":

        st.info(
            "Enter customer name or mobile."
        )

        return

    customers = search_customer(
        keyword
    )

    if len(customers) == 0:

        st.error(
            "No customer found."
        )

        return

    st.success(
        f"{len(customers)} Customer Found"
    )

    for customer in customers:

        with st.expander(

            customer["tenant_name"]

        ):

            st.write(
                f"### 👤 {customer['tenant_name']}"
            )

            st.divider()

            col1, col2 = st.columns(2)

            with col1:

                st.write(
                    f"**🏠 Owner :** {customer['owner_name']}"
                )

                st.write(
                    f"**📞 Mobile :** {customer['tenant_mobile']}"
                )

                st.write(
                    f"**💰 Rent : ₹ {customer['rent']}"
                )

                st.write(
                    f"**💵 Deposit : ₹ {customer['deposit']}"
                )

            with col2:

                st.write(
                    "**📍 Address :**"
                )

                st.write(
                    customer["property_address"]
                )

                st.write(
                    "**📅 Agreement :**"
                )

                st.write(
                    f"{customer['start_date']} ➜ {customer['end_date']}"
                )

            st.divider()

            col1, col2 = st.columns(2)

            with col1:

                st.button(

                    "📄 View Agreement",

                    key=f"agreement_{customer['customer_id']}"

                )

            with col2:

                if st.button(

                    "🔄 Renew Agreement",

                    key=f"renew_{customer['customer_id']}"

                ):

                    st.session_state[
                        "renew_customer_id"
                    ] = customer["customer_id"]

                    st.session_state.menu = "📄 New Agreement"

                    st.rerun()