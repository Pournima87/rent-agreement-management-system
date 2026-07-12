from datetime import date, datetime

from database.customer_repository import (

    insert_customer,

    search_customers,

    get_customer,

    get_all_customers,

    update_customer,

    mark_reminder_sent as repository_mark_reminder_sent

)


# =====================================
# Save Customer
# =====================================

def save_customer(data):

    return insert_customer(data)


# =====================================
# Search Customer
# =====================================

def search_customer(keyword):

    response = search_customers(keyword)

    return response.data


# =====================================
# Get Customer By ID
# =====================================

def get_customer_by_id(customer_id):

    response = get_customer(customer_id)

    return response.data


# =====================================
# Total Customers
# =====================================

def total_customers():

    return len(
        get_all_customers()
    )


# =====================================
# Active Customers
# =====================================

def active_customers():

    customers = get_all_customers()

    return len(

        [

            customer

            for customer in customers

            if customer["status"] == "ACTIVE"

        ]

    )


# =====================================
# Expiring Customers
# =====================================

def expiring_customers(days=30):

    result = []

    today = date.today()

    for customer in get_all_customers():

        try:

            end_date = datetime.strptime(

                customer["end_date"],

                "%Y-%m-%d"

            ).date()

        except:

            continue

        remaining = (

            end_date - today

        ).days

        if 0 <= remaining <= days:

            customer["days_left"] = remaining

            result.append(customer)

    return result


# =====================================
# Reminder Sent
# =====================================

def mark_reminder(customer_id):

    return repository_mark_reminder_sent(

        customer_id

    )