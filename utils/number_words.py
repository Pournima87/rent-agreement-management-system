def marathi_number(num):

    num = int(num)

    ones = [
        "",
        "एक",
        "दोन",
        "तीन",
        "चार",
        "पाच",
        "सहा",
        "सात",
        "आठ",
        "नऊ",
        "दहा",
        "अकरा",
        "बारा",
        "तेरा",
        "चौदा",
        "पंधरा",
        "सोळा",
        "सतरा",
        "अठरा",
        "एकोणीस"
    ]


    tens = {

        20:"वीस",
        30:"तीस",
        40:"चाळीस",
        50:"पन्नास",
        60:"साठ",
        70:"सत्तर",
        80:"ऐंशी",
        90:"नव्वद"

    }


    special = {

        21:"एकवीस",
        22:"बावीस",
        23:"तेवीस",
        24:"चोवीस",
        25:"पंचवीस",
        26:"सव्वीस",
        27:"सत्तावीस",
        28:"अठ्ठावीस",
        29:"एकोणतीस",

        31:"एकतीस",
        32:"बत्तीस",
        35:"पस्तीस",
        45:"पंचेचाळीस",
        47:"सत्तेचाळीस",
        55:"पंचावन्न"

    }


    def below_100(n):

        if n < 20:
            return ones[n]

        if n in special:
            return special[n]

        if n in tens:
            return tens[n]

        return ""


    result = ""


    if num >= 100000:

        lakh = num // 100000

        result += below_100(lakh) + " लाख "

        num %= 100000



    if num >= 1000:

        thousand = num // 1000

        result += below_100(thousand) + " हजार "

        num %= 1000



    if num >= 100:

        hundred = num // 100

        result += ones[hundred] + "शे "

        num %= 100



    if num > 0:

        result += below_100(num)


    return result.strip()