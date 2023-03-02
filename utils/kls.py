#!/usr/bin/python3
import pyclip


def switch_layout(string):
    out_string = ''
    for char in string:
        if char in CYR:
            for key, value in result_dictionary.items():
                if char == value:
                    char = key
                    break
        elif char in LAT:
            char = result_dictionary[char]
        out_string += char

    return out_string


LAT = 'qwertyuiop[]asdfghjkl;\'zxcvbnm,.QWERTYUIOP{}ASDFGHJKL:"ZXCVBNM<>'
CYR = 'йцукенгшщзхъфывапролджэячсмитьбюЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ'

result_dictionary = dict(zip(LAT, CYR))

pyclip.copy(switch_layout(pyclip.paste(text=True)))
