import streamlit as st

from services.owner_service import (
  save_owner,
  edit_owner
)


def owner_form(owner=None):

  with st.form("owner_form"):

    owner_name = st.text_input(

      "Owner Name",

      value="" if owner is None else owner["owner_name"]

    )

    owner_age = st.text_input(

      "Owner Age",

      value="" if owner is None else str(owner["owner_age"])

    )

    owner_address = st.text_area(

      "Owner Address",

      value="" if owner is None else owner["owner_address"]

    )

    owner_mobile = st.text_input(

      "Owner Mobile",

      value="" if owner is None else owner["owner_mobile"]

    )

    if owner is None:

      submit = st.form_submit_button(

        "💾 Save Owner"

      )

    else:

      submit = st.form_submit_button(

        "💾 Update Owner"

      )

    if submit:

      data = {

        "owner_name": owner_name,

        "owner_age": owner_age,

        "owner_address": owner_address,

        "owner_mobile": owner_mobile

      }

      if owner is None:

        save_owner(data)

        st.success(

          "Owner Saved Successfully."

        )

      else:

        edit_owner(

          owner["owner_id"],

          data

        )

        st.success(

          "Owner Updated Successfully."

        )

      st.session_state["add_owner"] = False

      st.session_state["edit_owner"] = None

      st.rerun()