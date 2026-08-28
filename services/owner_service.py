from uuid import uuid4

from datetime import date

from database.owner_repository import (

  insert_owner,

  get_all_owners,

  get_owner_by_mobile,

  search_owner,

  update_owner,

  delete_owner

)


# =====================================
# Save Owner
# =====================================

def save_owner(data):

  data["owner_id"] = str(uuid4())[:8]

  data["created_date"] = str(date.today())

  return insert_owner(data)

# =====================================
# Get Or Create Owner
# =====================================

def get_or_create_owner(data):

    owner_mobile = str(
        data.get("owner_mobile", "")
    ).strip()

    # ---------------------------------
    # Check existing owner
    # ---------------------------------

    if owner_mobile:

        existing_owner = get_owner_by_mobile(
            owner_mobile
        )

        if existing_owner:

            return existing_owner

    # ---------------------------------
    # Owner does not exist
    # Create new owner
    # ---------------------------------

    response = save_owner(
        data.copy()
    )

    if response.data:

        return response.data[0]

    return None

# =====================================
# Get All Owners
# =====================================

def owners():

  return get_all_owners()


# =====================================
# Search Owner
# =====================================

def find_owner(keyword):

  return search_owner(keyword)


# =====================================
# Update Owner
# =====================================

def edit_owner(owner_id, data):

  return update_owner(

    owner_id,

    data

  )


# =====================================
# Delete Owner
# =====================================

def remove_owner(owner_id):

  return delete_owner(

    owner_id

  )