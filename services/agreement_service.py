from uuid import uuid4

from datetime import date

from pdf.generator import generate_agreement_pdf

from pdf.noc_generator import generate_noc_pdf

from utils.customer_master import save_customer_master

from services.customer_service import save_customer


# =====================================
# Generate Documents
# =====================================

def generate_documents(data):

    agreement_pdf = generate_agreement_pdf(data)

    noc_pdf = generate_noc_pdf(data)

    data["agreement_pdf"] = agreement_pdf

    data["noc_pdf"] = noc_pdf

    data["customer_id"] = str(uuid4())[:8]

    data["created_date"] = str(date.today())

    # Excel Backup
    save_customer(data)

    save_customer_master(data)


    return {

        "agreement_pdf": agreement_pdf,

        "noc_pdf": noc_pdf,

        "customer_id": data["customer_id"]

    }