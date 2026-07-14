# =====================================
# Owner Mapper
# =====================================

def map_owner(data):

    return {

        "owner_id": data.get("owner_id"),

        "owner_name": data.get("owner_name"),

        "owner_age": str(data.get("owner_age", "")),

        "owner_address": data.get("owner_address"),

        "owner_mobile": data.get("owner_mobile"),

        "owner_photo": None,

        "created_date": data.get("created_date")

    }