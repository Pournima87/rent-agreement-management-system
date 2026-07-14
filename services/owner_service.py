from uuid import uuid4

from datetime import date

from database.owner_repository import (

  insert_owner,

  get_all_owners,

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