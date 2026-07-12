
import fitz
from utils.date_format import format_date

TEMPLATE_PATH = "templates/agreement_blank.pdf"

FONT_PATH = "fonts/NotoSansDevanagari.ttf"

def add_text(
    page,
    x,
    y,
    text,
    size=14
):

    rect = fitz.Rect(
        x,
        y - 14,
        x + 300,
        y + 35
    )

    page.insert_htmlbox(
        rect,
        f"""
        <p style="
        margin:0;
        padding:0;
        font-family:Noto Sans Devanagari;
        font-size:{size}px;">
        {text}
        </p>
        """
    )



def add_address(
    page,
    x,
    y,
    text
):

    # convert enter key into html line break
    text = text.replace(
        "\n",
        "<br>"
    )


    rect = fitz.Rect(
        x,
        y - 14,
        x + 260,
        y + 140
    )


    page.insert_htmlbox(
        rect,
        f"""
        <div style="
            margin:0;
            padding:0;
            font-family:Noto Sans Devanagari;
            font-size:13px;
            line-height:1.7;
        ">
            {text}
        </div>
        """
    )




def add_single_line(
    page,
    x,
    y,
    text,
    size=12
):

    rect = fitz.Rect(
        x,
        y - 14,
        x + 250,
        y + 35
    )

    page.insert_htmlbox(
        rect,
        f"""
        <p style="
        margin:0;
        padding:0;
        font-family:Noto Sans Devanagari;
        font-size:{size}px;">
        {text}
        </p>
        """
    )

def add_photo(
    page,
    x,
    y,
    photo
):

    if photo is None:

        return


    # reset file pointer
    photo.seek(0)


    image_bytes = photo.read()


    if not image_bytes:

        return


    rect = fitz.Rect(
        x,
        y,
        x + 90,
        y + 110
    )


    page.insert_image(
        rect,
        stream=image_bytes,
        keep_proportion=True
    )


def generate_agreement_pdf(data):

    doc = fitz.open(
        TEMPLATE_PATH
    )


    # ---------- PAGE 1 ----------
    
    page = doc[0]



    # Owner Details

    add_text(
        page,
        200,
        555,
        data["owner_name"]
    )

    # Owner Address

    add_address(
        page,
        150,
        577,
        data["owner_address"]
    )



    # Tenant Details

    add_text(
        page,
        215,
        676,
        data["tenant_name"]
    )

    # Tenant Address

    add_address(
        page,
        150,
        699,
        data["tenant_address"]
    )

        # ---------- PAGE 2 ----------

    page = doc[1]


    # 1) Property Address
    # सदरहु मौजे ____________

    add_address(
        page,
        175,
        184,
        data["property_address"]
    )

    # Agreement months

    add_single_line(
        page,
        195,
        235,
    data["agreement_months"]
    )


    # 2) Start Date
    # आज दिनांक ____ पासून

    add_single_line(
        page,
        343,
        265,
        format_date(
            data["start_date"]
        )
    )


    # 3) End Date
    # ते ____ पर्यंत

    add_single_line(
        page,
        465,
        265,
        format_date(
            data["end_date"]
        )
    )


    # 4) Deposit Amount
    # अनामत रक्कम रुपये ______

    add_single_line(
        page,
        473,
        285,
        data["deposit"]
    )


    # 5) Deposit In Words
    # (अक्षरी रुपये ______ मात्र)

    add_single_line(
        page,
        190,
        311,
        data["deposit_words"]
    )


    # 6) Monthly Rent
    # रुपये रक्कम रु ______

    add_single_line(
        page,
        410,
        390,
        data["rent"]
    )


    # 7) Rent In Words
    # ( रु. ______ फक्त )

    add_single_line(
        page,
        160,
        411,
        data["rent_words"]
    )


    # 8) Rent Payment Date
    # महिन्याच्या ____ तारखेच्या आत

    add_single_line(
        page,
        427,
        435,
        data["rent_pay_date"]
    )

# ====================
# PAGE 3
# ====================

    page = doc[2]


# Deposit amount

    add_single_line(
    page,
    155,
    265,
    data["deposit"]
    )


# Deposit in words

    add_single_line(
    page,
    305,
    265,
    data["deposit_words"]
    )

# ====================
# PAGE 4
# Family Members
# ====================

    page = doc[3]

    family_y_positions = [
    180,
    202,
    226,
    250,
    272,
    296,
    320
    ]


    for i, y in enumerate(family_y_positions, start=1):


    # family member name

        add_single_line(
            page,
            115,
            y,
            data.get(
            f"family_{i}_name",
            ""
            )
        )


    # relation

        add_single_line(
            page,
            360,
            y,
            data.get(
            f"family_{i}_relation",
            ""
            )
        )

    add_photo(
    page,
    368,
    465,
    data["owner_photo"]
    )


    add_photo(
    page,
    368,
    596,
    data["tenant_photo"]
    )

# ====================
# PAGE 5
# Receipt
# ====================

    page = doc[4]


# Tenant name

    add_single_line(
    page,
    275,
    126,
    data["tenant_name"]
    )


# Deposit amount

    add_single_line(
    page,
    85,
    155,
    data["deposit"]
    )


# Deposit in words

    add_single_line(
    page,
    225,
    155,
    data["deposit_words"]
    )


# Agreement date

    add_single_line(
    page,
    165,
    185,
    format_date(
        data["agreement_date"]
    )
    )


    tenant = data["tenant_name"].replace(
    " ",
    "_"
    )


    output = (
    tenant
    +
    "_Rent_Agreement.pdf"
    )


    doc.save(
        output
    )


    doc.close()


    return output