from database.supabase_client import supabase

from database.owner_mapper import map_owner


# =====================================
# Insert Owner
# =====================================

def insert_owner(data):

  owner = map_owner(data)

  return (

    supabase.table(

      "owner_master"

    )

    .insert(owner)

    .execute()

  )


# =====================================
# Get All Owners
# =====================================

def get_all_owners():

  response = (

    supabase.table(

      "owner_master"

    )

    .select("*")

    .order(

      "owner_name"

    )

    .execute()

  )

  return response.data


# =====================================
# Search Owner
# =====================================

def search_owner(keyword):

  response = (

    supabase.table(

      "owner_master"

    )

    .select("*")

    .or_(

      f"owner_name.ilike.%{keyword}%,owner_mobile.ilike.%{keyword}%"

    )

    .execute()

  )

  return response.data


# =====================================
# Update Owner
# =====================================

def update_owner(owner_id, data):


  return (

    supabase.table(

      "owner_master"

    )

    .update({
      "owner_name": data["owner_name"],

      "owner_age": data["owner_age"],

      "owner_address": data["owner_address"],

      "owner_mobile": data["owner_mobile"]
    })

    .eq(

      "owner_id",

      owner_id

    )

    .execute()

  )


# =====================================
# Delete Owner
# =====================================

def delete_owner(owner_id):

  return (

    supabase.table(

      "owner_master"

    )

    .delete()

    .eq(

      "owner_id",

      owner_id

    )

    .execute()

  )