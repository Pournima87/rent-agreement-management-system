import streamlit as st

from services.reminder_services import get_expiring_customers
from notifications.whatsapp import (
    create_reminder_message,
    get_whatsapp_url
)
from services.customer_service import mark_reminder

def reminder_page():

    st.header("🔔 Reminder Center")

    customers = get_expiring_customers()

    if not customers:

        st.success("✅ No agreements are expiring.")

        return


    st.warning(
        f"{len(customers)} Agreement(s) Expiring Soon"
    )


    for customer in customers:

        with st.container():

            col1, col2, col3, col4 = st.columns(
                [3,2,2,2]
            )

            with col1:

                st.write(
                    f"### 👤 {customer['tenant']}"
                )

                st.caption(
                    customer["owner"]
                )

            with col2:

                st.write("📞 Mobile")

                st.write(
                    customer["mobile"]
                )

            with col3:

                st.write("📅 End Date")

                st.write(
                    customer["end_date"]
                )

            with col4:

                days = customer["days_left"]

                if days <= 3:

                    st.error(
                        f"{days} Days Left"
                    )

                elif days <= 7:

                    st.warning(
                        f"{days} Days Left"
                    )

                else:

                    st.success(
                        f"{days} Days Left"
                    )

            action1, action2, action3, action4 = st.columns(
                [2, 2, 2, 4]
            )

            with action1:

                if st.button(
                    "🔄 Renew Agreement",
                    key=f"renew_{customer['customer_id']}"
                ):

                    st.session_state["renew_customer_id"] = customer["customer_id"]

                    st.session_state.menu = "📄 New Agreement"

                    st.rerun()

            with action2:

                tenant_message = create_reminder_message(
                    customer
                )

                tenant_url = get_whatsapp_url(

                    customer["mobile"],

                    tenant_message

                )

                st.link_button(

                    "👤 Tenant",

                    tenant_url,

                    use_container_width=True

                )

            with action3:

                owner_message = f"""
नमस्कार {customer['owner']} जी,

आपल्या मालमत्तेचा भाडे करार
{customer['end_date']} रोजी संपत आहे.

कृपया नवीन करारासाठी
More Enterprises शी संपर्क साधा.

धन्यवाद.
More Enterprises
"""

                owner_url = get_whatsapp_url(

                    customer["owner_mobile"],

                    owner_message

                )

                st.link_button(

                    "🏠 Owner",

                    owner_url,

                    use_container_width=True

                )

            st.divider()