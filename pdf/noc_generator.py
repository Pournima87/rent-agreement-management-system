import fitz
from utils.date_format import format_date

TEMPLATE_PATH = "templates/police_noc_blank.pdf"

def add_text(
    page,
    x,
    y,
    text,
    size=13
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
        x + 350,
        y + 70
    )


    page.insert_htmlbox(
        rect,
        f"""
        <div style="
            margin:0;
            padding:0;
            font-family:Noto Sans Devanagari;
            font-size:12px;
            line-height:1.3;
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

def generate_noc_pdf(data):

    doc = fitz.open(
        TEMPLATE_PATH
    )


    page = doc[0]
    
    # ==================
    # PHOTOS
    # ==================

    add_photo(
        page,
        26,
        52,
        data["owner_photo"]
    )


    add_photo(
        page,
        474,
        52,
        data["tenant_photo"]
    )

    # ==================
    # OWNER DETAILS
    # ==================

    add_address(
        page,
        275,
        230,
        data["owner_name"]
        + ", वय : "
        + data["owner_age"]
        + ", "
        + data["owner_address"]
        + ", मो : "
        + data["owner_mobile"]
    )


    # ==================
    # TENANT DETAILS
    # ==================

    add_address(
        page,
        275,
        305,
        data["tenant_name"]
        + ", वय : "
        + data["tenant_age"]
        + ", "
        + data["tenant_address"]
        + ", मो : "
        + data["tenant_mobile"]
    )


    # Aadhaar

    add_single_line(
        page,
        335,
        360,
        data["aadhaar"]
    )


    # PAN

    add_single_line(
        page,
        335,
        388,
        data["pan"]
    )


    # Property Address

    add_address(
        page,
        275,
        455,
        data["property_address"]
    )

    # ==================
    # PREVIOUS ADDRESS
    # Row 5
    # ==================

    add_address(
        page,
        275,
        403,
        data["previous_address"]
    )


    # ==================
    # FAMILY COUNT
    # Row 7
    # ==================

    add_single_line(
        page,
        297,
        507,
        data["male_count"]
    )


    add_single_line(
        page,
        415,
        507,
        data["female_count"]
    )


    add_single_line(
        page,
        500,
        507,
        data["child_count"]
    )


    # ==================
    # WORK TYPE
    # Row 8
    # ==================

    add_single_line(
        page,
        335,
        525,
        data["work_type"]
    )


    # ==================
    # OFFICE DETAILS
    # Row 9
    # ==================

    add_address(
        page,
        275,
        550,
        data["office_details"]
    )


    # ==================
    # REFERENCES
    # Row 10
    # ==================

    add_address(
        page,
        300,
        599,
        "१) "
        + data["reference_1"]
        + "\n२) "
        + data["reference_2"]
    )


    # ==================
    # AGENT DETAILS
    # Row 11
    # ==================

    add_single_line(
        page,
        335,
        640,
        data["agent_details"]
    )


    # ==================
    # AGREEMENT PERIOD
    # Row 12
    # ==================

    add_single_line(
        page,
        335,
        675,
        format_date(data["agreement_date"])
        +
        " ते "
        +
        format_date(data["end_date"])
        )    

    tenant = data["tenant_name"].replace(
    " ",
    "_"
    )


    output = (
    tenant
    +
    "_Police_NOC.pdf"
    )


    doc.save(
        output
    )


    return output