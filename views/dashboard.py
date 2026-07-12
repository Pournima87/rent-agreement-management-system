import streamlit as st

from services.customer_service import (
    total_customers,
    active_customers,
    expiring_customers

)
from services.reminder_services import get_business_summary
from datetime import datetime


def dashboard_page():

    hour = datetime.now().hour

    if hour < 12:

        greeting = "☀️ Good Morning"

    elif hour < 17:

        greeting = "🌤️ Good Afternoon"

    else:

        greeting = "🌙 Good Evening"

    st.title(
        "🏠 MORE ENTERPRISES"
    )

    st.caption(
        f"{greeting}, Jagdish Sir 👋"
    )

    st.caption(
        "Rent Agreement Management System"
    )

    st.divider()

    # ==========================
    # Business Summary
    # ==========================

    summary = get_business_summary()

    if summary["expired"] > 0:

        st.error(
            f"""
### 🚨 ACTION REQUIRED

⚠️ {summary['expired']} Agreement(s) have already expired.

🔔 {summary['expiring']} Agreement(s) are expiring soon.

📱 {summary['pending_reminders']} Reminder(s) are pending.

Please open the Reminder Center.
"""
        )

    elif summary["expiring"] > 0:

        st.warning(
            f"""
### 🔔 Today's Business Summary

👥 Total Customers : {summary['total_customers']}

🔔 Expiring Agreements : {summary['expiring']}

📱 Pending Reminders : {summary['pending_reminders']}
"""
        )

    else:

        st.success(
            f"""
### ✅ Great!

No agreements require your attention today.

👥 Total Customers : {summary['total_customers']}
"""
        )

    st.divider()


    # ==========================
    # Summary Cards
    # ==========================

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "👥 Total Customers",
            total_customers()
        )

    with col2:

        st.metric(
            "🟢 Active Agreements",
            active_customers()
        )

    with col3:

        st.metric(
            "🔴 Expiring in 30 Days",
            len(expiring_customers())
        )

    st.divider()

    st.subheader("⚠ Agreements Expiring Soon")

    customers = expiring_customers()

    if len(customers) == 0:

        st.success(
            "No agreements are expiring in the next 30 days."
        )

    else:

        for customer in customers:

            with st.container():

                c1, c2, c3, c4 = st.columns(
                    [3, 2, 2, 2]
                )

                with c1:

                    st.write(
                        f"**{customer['tenant_name']}**"
                    )

                with c2:

                    st.write(
                        customer["tenant_mobile"]
                    )

                with c3:

                    st.write(
                        customer["end_date"]
                    )

                with c4:

                    if customer["days_left"] <= 7:

                        st.error(
                            f"{customer['days_left']} Days Left"
                        )

                    elif customer["days_left"] <= 15:

                        st.warning(
                            f"{customer['days_left']} Days Left"
                        )

                    else:

                        st.info(
                            f"{customer['days_left']} Days Left"
                        )

                st.divider()