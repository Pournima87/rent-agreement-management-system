from services.customer_service import (

    expiring_customers,

    active_customers,

    total_customers

)


# =====================================
# Expiring Customers
# =====================================

def get_expiring_customers():

    customers = []

    for customer in expiring_customers():

        customers.append({

            "customer_id": customer["customer_id"],

            "owner": customer["owner_name"],

            "tenant": customer["tenant_name"],

            "mobile": customer["tenant_mobile"],

            "end_date": customer["end_date"],

            "days_left": customer["days_left"]

        })

    return customers


# =====================================
# Expired Customers
# =====================================

def get_expired_customers():

    return []


# =====================================
# Business Summary
# =====================================

def get_business_summary():

    expiring = get_expiring_customers()

    return {

        "total_customers": total_customers(),

        "active_customers": active_customers(),

        "expiring": len(expiring),

        "expired": 0,

        "pending_reminders": len(expiring)

    }