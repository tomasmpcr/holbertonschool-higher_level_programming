#!/usr/bin/python3
def roman_to_int(roman_string):
    suma = 0

    if isinstance(roman_string, str) is False:
        return (0)

    for i in range(0, len(roman_string)):
        if i + 1 < len(roman_string):
            if roman_value(roman_string[i]) < roman_value(roman_string[i + 1]):
                suma -= roman_value(roman_string[i])
                continue
        suma += roman_value(roman_string[i])
    return (suma)


def roman_value(letter):
    switcher = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    return (switcher.get(letter, None))
