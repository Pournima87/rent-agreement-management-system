import urllib.parse
import webbrowser


# =====================================
# Open WhatsApp
# =====================================

def open_whatsapp(mobile, message):

    mobile = str(mobile).strip()

# Convert Marathi digits to English
    mobile = mobile.translate(
    str.maketrans(
        "०१२३४५६७८९",
        "0123456789"
        )
    )

    mobile = mobile.replace(" ", "")
    mobile = mobile.replace("-", "")
    mobile = mobile.replace("+", "")

    if not mobile.startswith("91"):

        mobile = "91" + mobile

    encoded_message = urllib.parse.quote(message)

    url = (
        f"https://wa.me/{mobile}"
        f"?text={encoded_message}"
    )
    print(url)
    webbrowser.open(url)

# =====================================
# Reminder Message
# =====================================

def create_reminder_message(customer):

    return f"""
नमस्कार {customer['tenant']} जी,

आपल्या भाडे कराराची मुदत
{customer['end_date']} रोजी संपत आहे.

नवीन करारासाठी कृपया
More Enterprises शी संपर्क साधावा.

धन्यवाद.
More Enterprises
"""