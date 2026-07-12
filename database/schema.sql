create table if not exists customer_master (

    customer_id text primary key,

    created_date date,

    owner_name text,
    owner_age text,
    owner_address text,
    owner_mobile text,

    tenant_name text,
    tenant_age text,
    tenant_address text,
    tenant_mobile text,

    aadhaar text,
    pan text,

    property_type text,
    property_address text,
    purpose text,

    agreement_date date,
    start_date date,
    end_date date,

    agreement_months text,

    rent text,
    rent_words text,

    deposit text,
    deposit_words text,

    rent_pay_date text,

    family_1_name text,
    family_1_relation text,

    family_2_name text,
    family_2_relation text,

    family_3_name text,
    family_3_relation text,

    family_4_name text,
    family_4_relation text,

    family_5_name text,
    family_5_relation text,

    family_6_name text,
    family_6_relation text,

    family_7_name text,
    family_7_relation text,

    previous_address text,

    male_count text,
    female_count text,
    child_count text,

    work_type text,

    office_details text,

    reference_1 text,
    reference_2 text,

    agent_details text,

    agreement_pdf text,

    noc_pdf text,

    status text,

    reminder_sent text,

    last_reminder_date text

);