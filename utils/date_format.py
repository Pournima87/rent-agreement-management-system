def format_date(date):

    marathi_digits = str.maketrans(
        "0123456789",
        "०१२३४५६७८९"
    )


    formatted = date.strftime(
        "%d/%m/%Y"
    )


    return formatted.translate(
        marathi_digits
    )