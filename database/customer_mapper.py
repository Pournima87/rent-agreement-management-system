from datetime import date, datetime


# =====================================
# Convert Form Data
# To Supabase Data
# =====================================

def map_customer(data):

    customer = {}

    ignore_fields = [

        "owner_photo",

        "tenant_photo"

    ]

    for key, value in data.items():

        if key in ignore_fields:

            continue

        if isinstance(
            value,
            (date, datetime)
        ):

            value = value.isoformat()

        customer[key] = value

    return customer