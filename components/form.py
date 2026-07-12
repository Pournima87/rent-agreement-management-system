import streamlit as st
from datetime import date
from utils.number_words import marathi_number

def agreement_form(existing_data=None):

    if existing_data is None:

        existing_data = {}
    
    def get_value(key):
        return str(existing_data.get(key) or "")

    data = {}


    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(
        [
            "🏠 मालक",
            "👤 भाडेकरू",
            "🏡 जागा",
            "📅 करार",
            "👨‍👩‍👧 कुटुंब",
            "👮 पोलीस NOC"
        ]
    )


    with tab1:

        st.subheader("घर मालक माहिती")

        data["owner_name"] = st.text_input(
            "मालकाचे पूर्ण नाव",
            value=get_value("owner_name")
        )

        data["owner_age"] = st.text_input(
            "वय",
            value=get_value("owner_age")
        )

        data["owner_address"] = st.text_area(
            "मालकाचा पत्ता",
            value=get_value("owner_address")
        )

        data["owner_mobile"] = st.text_input(
            "मोबाईल नंबर",
            value=get_value("owner_mobile")
        )

        data["owner_photo"] = st.file_uploader(
            "मालकाचा फोटो",
            type=["jpg","png"]
        )


    with tab2:

        st.subheader("भाडेकरू माहिती")


        data["tenant_name"] = st.text_input(
            "भाडेकरूचे नाव",
            value=get_value("tenant_name")
        )


        data["tenant_age"] = st.text_input(
            "भाडेकरूचे वय",
            value=get_value("tenant_age")
        )


        data["tenant_address"] = st.text_area(
            "भाडेकरूचा कायमचा पत्ता",
            value=get_value("tenant_address")
        )


        data["tenant_mobile"] = st.text_input(
            "भाडेकरू मोबाईल नंबर",
            value=get_value("tenant_mobile")
        )


        data["aadhaar"] = st.text_input(
            "आधार नंबर",
            value=get_value("aadhaar")
        )


        data["pan"] = st.text_input(
            "पॅन नंबर",
            value=get_value("pan")
        )


        data["tenant_photo"] = st.file_uploader(
            "भाडेकरू फोटो",
            type=["jpg","png"]
        )



    with tab3:

        st.subheader("जागेची माहिती")


        data["property_type"] = st.selectbox(
            "जागेचा प्रकार",
            [
                "घर",
                "दुकान"
            ]
        )


        data["property_address"] = st.text_area(
            "भाड्याने दिलेल्या जागेचा पत्ता",
            value=get_value("property_address")
        )


        data["purpose"] = st.selectbox(
            "वापर",
            [
                "राहण्यासाठी",
                "व्यवसायासाठी"
            ]
        )      



    with tab4:


        st.subheader("करार माहिती")


        data["agreement_date"] = st.date_input(
            "करार तारीख",
            value=date.today()
        )


        data["start_date"] = st.date_input(
            "सुरुवात तारीख"
        )


        data["end_date"] = st.date_input(
            "समाप्त तारीख"
        )


        # Rent amount

        data["rent"] = st.text_input(
            "मासिक भाडे",
            value=get_value("rent")
        )


        if data["rent"]:

            data["rent_words"] = marathi_number(
                data["rent"]
            )

        else:

            data["rent_words"] = ""


        st.info(
            f"भाडे अक्षरी: {data['rent_words']}"
        )


        # Deposit amount

        data["deposit"] = st.text_input(
            "डिपॉझिट",
            value=get_value("deposit")
        )


        if data["deposit"]:

            data["deposit_words"] = marathi_number(
                data["deposit"]
            )

        else:

            data["deposit_words"] = ""


        st.info(
            f"डिपॉझिट अक्षरी: {data['deposit_words']}"
        )


        data["rent_pay_date"] = st.text_input(
            "भाडे भरण्याची तारीख",
            value=get_value("rent_pay_date")
        )


        # Auto agreement months

        months = (
            (data["end_date"].year - data["start_date"].year) * 12
            +
            (data["end_date"].month - data["start_date"].month)
        )


        data["agreement_months"] = str(months)


        st.success(
            f"करार कालावधी : {months} महिने"
        )


    with tab5:

        st.subheader("कुटुंब सदस्य")


        for i in range(1,8):

            col1, col2 = st.columns(2)


            with col1:

                data[f"family_{i}_name"] = st.text_input(
                    f"{i}) नाव",
                    value=get_value(f"family_{i}_name")
                )


            with col2:

                data[f"family_{i}_relation"] = st.text_input(
                    f"{i}) नाते",
                    value=get_value(f"family_{i}_relation")
                )


        # ======================
        # AUTO FAMILY COUNT
        # ======================

        male = 0

        female = 0

        child = 0


        for i in range(1,8):

            relation = data.get(
                f"family_{i}_relation",
                ""
            )


            if relation in [
                "वडील",
                "भाऊ",
                "आजोबा",
                "काका",
                "मामा",
                "पती",
                "मुलगा"
            ]:

                male += 1


            elif relation in [
                "आई",
                "बहीण",
                "आजी",
                "काकू",
                "मामी",
                "पत्नी",
                "मुलगी"
            ]:

                female += 1


            elif relation in [
                "मुल",
                "लहान मुलगा",
                "लहान मुलगी"
            ]:

                child += 1


        data["male_count"] = str(male)

        data["female_count"] = str(female)

        data["child_count"] = str(child)


        st.success(
            f"पुरुष: {male} | स्त्रिया: {female} | लहान मुले: {child}"
        )

    with tab6:

        st.subheader(
            "पोलीस NOC माहिती"
        )


        same_address = st.checkbox(
            "जुना पत्ता आणि कायमचा पत्ता सारखाच आहे"
        )


        if same_address:

            data["previous_address"] = data["tenant_address"]

            st.success(
                "पत्ता कॉपी झाला"
            )


        else:

            data["previous_address"] = st.text_area(
                "भाडेकरूचा जुना पत्ता",
                value=get_value("previous_address")
            )


        data["work_type"] = st.text_input(
            "कामाचे स्वरूप",
            value=get_value("work_type")

        )


        data["office_details"] = st.text_area(
            "कार्यालय नाव, पत्ता, मोबाईल",
            value=get_value("office_details")

        )


        data["reference_1"] = st.text_area(
            "ओळखीची व्यक्ती 1",
            value=get_value("reference_1")
        )


        data["reference_2"] = st.text_area(
            "ओळखीची व्यक्ती 2",
            value=get_value("reference_2")
        )


        data["agent_details"] = st.text_input(
            "एजेंट नाव व मोबाईल",
            value=get_value("agent_details")
        )

    return data