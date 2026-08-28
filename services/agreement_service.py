from uuid import uuid4
from datetime import date

from pdf.generator import generate_agreement_pdf
from pdf.noc_generator import generate_noc_pdf

from utils.pdf_merge import combine_pdfs

from utils.customer_master import save_customer_master
from services.customer_service import save_customer
from services.owner_service import get_or_create_owner


# =====================================
# Generate Documents
# =====================================

def generate_documents(data):

    # ---------------------------------
    # Ensure Owner Exists
    # ---------------------------------

    owner = get_or_create_owner(
        data
    )

    if owner is None:

        raise Exception(
            "Unable to create or find owner."
        )

    # ---------------------------------
    # Generate Agreement
    # ---------------------------------

    agreement_pdf = generate_agreement_pdf(
        data
    )

    # ---------------------------------
    # Generate Police NOC
    # ---------------------------------

    noc_pdf = generate_noc_pdf(
        data
    )

    # ---------------------------------
    # Generate ONE Customer ID
    # ---------------------------------

    customer_id = str(
        uuid4()
    )[:8]

    created_date = str(
        date.today()
    )

    # ---------------------------------
    # Store document information
    # ---------------------------------

    data["customer_id"] = customer_id

    data["created_date"] = created_date

    data["agreement_pdf"] = agreement_pdf

    data["noc_pdf"] = noc_pdf

    # ---------------------------------
    # Create Combined PDF Name
    # ---------------------------------

    tenant = (

        data["tenant_name"]

        .replace(" ", "_")

        .replace("/", "-")

        .replace("\\", "-")

    )

    combined_pdf = (

        tenant

        + "_Complete_Documents.pdf"

    )

    # ---------------------------------
    # Combine Agreement + NOC
    # ---------------------------------

    combined_pdf = combine_pdfs(

        agreement_pdf,

        noc_pdf,

        combined_pdf

    )

    # ---------------------------------
    # Save to Supabase
    # ---------------------------------

    save_customer(
        data
    )

    # ---------------------------------
    # Save Full Excel Master
    # ---------------------------------

    save_customer_master(
        data
    )

    # ---------------------------------
    # Return Results
    # ---------------------------------

    return {

        "agreement_pdf":
            agreement_pdf,

        "noc_pdf":
            noc_pdf,

        "combined_pdf":
            combined_pdf,

        "customer_id":
            customer_id

    }