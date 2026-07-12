import fitz


INPUT_PDF = "templates/police_noc_blank.pdf"


doc = fitz.open(INPUT_PDF)


page = doc[0]


# page size
width = page.rect.width
height = page.rect.height


# draw vertical lines

for x in range(0, int(width), 25):

    page.draw_line(
        (x, 0),
        (x, height),
        color=(1, 0, 0),
        width=0.5
    )

    page.insert_text(
        (x, 15),
        str(x),
        fontsize=6,
        color=(1, 0, 0)
    )


# draw horizontal lines

for y in range(0, int(height), 25):

    page.draw_line(
        (0, y),
        (width, y),
        color=(0, 0, 1),
        width=0.5
    )

    page.insert_text(
        (5, y),
        str(y),
        fontsize=6,
        color=(0, 0, 1)
    )


doc.save(
    "NOC_coordinate_map.pdf"
)