# -*- coding: utf-8 -*-

def convertunicode(data):
    dictionary = {
        "Auto": "साधन ",
        "Bank": "बैंक ",
        "Blog": "ब्लग",
        "Business interview": "ब्यापार",
        "Economy": "अर्थ तन्र",
        "Education": "शिक्षा ",
        "Employment": "रोजगार",
        "Entertainment": "मनोरन्जन",
        "Interview": "अन्तर्वाता",
        "Literature": "साहित्य",
        "National News": "राष्टृय समाचार",
        "Opinion": "राय",
        "Sports": "खेल्कुद",
        "Technology": "प्रविधी",
        "Tourism": "पर्यटन",
        "World": "संसार",

    }

    if data in dictionary:
        return dictionary[data]
    # return dictionary
