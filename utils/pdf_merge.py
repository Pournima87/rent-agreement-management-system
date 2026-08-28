import fitz


# =====================================
# Combine Agreement + Police NOC
# =====================================

def combine_pdfs(
    agreement_pdf,
    noc_pdf,
    output_pdf
):

    agreement = fitz.open(
        agreement_pdf
    )

    noc = fitz.open(
        noc_pdf
    )

    combined = fitz.open()

    # Agreement first
    combined.insert_pdf(
        agreement
    )

    # Police NOC second
    combined.insert_pdf(
        noc
    )

    combined.save(
        output_pdf
    )

    agreement.close()
    noc.close()
    combined.close()

    return output_pdf