import streamlit as st

from services.owner_service import (
  find_owner,
  remove_owner
)

from components.owner_form import owner_form


def owner_management_page():

  st.title("👤 Owners")

  if "add_owner" not in st.session_state:

    st.session_state["add_owner"] = False

  if "edit_owner" not in st.session_state:

    st.session_state["edit_owner"] = None

  keyword = st.text_input(

    "🔍 Find Owner (Name or Mobile)"

  )

  if keyword == "":

    st.info("Search an existing owner.")

    if st.session_state["add_owner"]:

      owner_form()

    return

  owners = find_owner(keyword)

  if len(owners) == 0:

    st.warning("Owner not found.")

    if st.button(

      "➕ Add New Owner"

    ):

      st.session_state["add_owner"] = True

      st.rerun()

    if st.session_state["add_owner"]:

      owner_form()

    return

  st.success(

    f"{len(owners)} Owner(s) Found"

  )

  for owner in owners:

    with st.container():

      st.write(

        f"### 👤 {owner['owner_name']}"

      )

      st.caption(

        f"🆔 {owner['owner_id']}"

      )

      st.write(

        f"📞 {owner['owner_mobile']}"

      )

      st.write(

        f"📍 {owner['owner_address']}"

      )

      col1, col2, col3 = st.columns(3)

      with col1:

        if st.button(

          "✏ Edit",

          key=f"edit_{owner['owner_id']}"

        ):

          st.session_state["edit_owner"] = owner

          st.rerun()

      with col2:

        if st.button(

          "🗑 Delete",

          key=f"delete_{owner['owner_id']}"

        ):

          remove_owner(

            owner["owner_id"]

          )

          st.success(

            "Owner deleted successfully."

          )

          st.rerun()

      with col3:

        if st.button(

          "📄 Create Agreement",

          key=f"agreement_{owner['owner_id']}"

        ):
            st.session_state["selected_owner"] = owner

            st.session_state.menu = "📄 New Agreement"

            st.rerun()

      if (

        st.session_state["edit_owner"] is not None

        and

        st.session_state["edit_owner"]["owner_id"] == owner["owner_id"]

      ):

        owner_form(

          st.session_state["edit_owner"]

        )

      st.divider()