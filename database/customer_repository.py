from database.supabase_client import supabase

from database.customer_mapper import map_customer


# =====================================
# Insert Customer
# =====================================

def insert_customer(data):

    customer = map_customer(data)

    return (

        supabase

        .table("customer_master")

        .insert(customer)

        .execute()

    )


# =====================================
# Search Customers
# =====================================

def search_customers(keyword):

    return (

        supabase

        .table("customer_master")

        .select("*")

        .or_(

            f"tenant_name.ilike.%{keyword}%,"

            f"tenant_mobile.ilike.%{keyword}%,"

            f"tenant_address.ilike.%{keyword}%"

        )

        .execute()

    )


# =====================================
# Get Customer
# =====================================

def get_customer(customer_id):

    response = (

        supabase

        .table("customer_master")

        .select("*")

        .eq(

            "customer_id",

            customer_id

        )

        .single()

        .execute()

    )

    return response
# =====================================
# Get All Customers
# =====================================

def get_all_customers():

    response = (

        supabase

        .table("customer_master")

        .select("*")

        .execute()

    )

    return response.data


# =====================================
# Update Customer
# =====================================

def update_customer(
    customer_id,
    data
):

    customer = map_customer(data)

    return (

        supabase

        .table("customer_master")

        .update(customer)

        .eq(
            "customer_id",
            customer_id
        )

        .execute()

    )


# =====================================
# Mark Reminder Sent
# =====================================

def mark_reminder_sent(customer_id):

    return (

        supabase

        .table("customer_master")

        .update({

            "reminder_sent": "YES"

        })

        .eq(

            "customer_id",

            customer_id

        )

        .execute()

    )