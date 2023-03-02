#!/usr/bin/env python3
import argparse
import pyclip

letters_lower = {
    "а": "a",
    "б": "b",
    "в": "v",
    "г": "g",
    "д": "d",
    "е": "e",
    "ё": "e",
    "ж": "zh",
    "з": "z",
    "и": "i",
    "й": "y",
    "к": "k",
    "л": "l",
    "м": "m",
    "н": "n",
    "о": "o",
    "п": "p",
    "р": "r",
    "с": "s",
    "т": "t",
    "у": "u",
    "ф": "f",
    "х": "h",
    "ц": "ts",
    "ч": "ch",
    "ш": "sh",
    "щ": "sch",
    "ъ": "",
    "ы": "y",
    "ь": "",
    "э": "e",
    "ю": "y",
    "я": "ya",
}


letters_upper = {
    "А": "A",
    "Б": "B",
    "В": "V",
    "Г": "G",
    "Д": "D",
    "Е": "E",
    "Ё": "E",
    "Ж": "Zh",
    "З": "Z",
    "И": "I",
    "Й": "Y",
    "К": "K",
    "Л": "L",
    "М": "M",
    "Н": "N",
    "О": "O",
    "П": "P",
    "Р": "R",
    "С": "S",
    "Т": "T",
    "У": "U",
    "Ф": "F",
    "Х": "H",
    "Ц": "Ts",
    "Ч": "Ch",
    "Ш": "Sh",
    "Щ": "Sch",
    "Ъ": "",
    "Ы": "Y",
    "Ь": "",
    "Э": "E",
    "Ю": "Y",
    "Я": "Ya",
}


def parse_args():
    parser = argparse.ArgumentParser(description="Simple CLI transliteration")

    parser.add_argument("text", help="cyrillic character set for transliteration")
    parser.add_argument("-c", "--copy", dest="copy",
                        action="store_true", help="copy to clipboard")

    return parser.parse_args()


def translit_text(text):
    result = ""

    for index, char in enumerate(text):
        if char in letters_lower:
            char = letters_lower[char]
        elif char in letters_upper:
            char = letters_upper[char]
            if len(text) > index + 1:
                if text[index + 1] not in letters_upper:
                    char = char.upper()
            else:
                char = char.upper()

        result += char

    return result


def main():
    args = parse_args()
    translited_text = translit_text(args.text)

    if args.copy:
        try:
            pyclip.copy(translited_text)
        except:
            pass

    print(translited_text)


if __name__ == "__main__":
    main()
