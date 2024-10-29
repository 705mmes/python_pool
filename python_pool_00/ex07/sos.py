#!/usr/bin/env python3
# -*- coding: utf-8 -*-?

import sys


def main():

    FUCK_MORSE_CODE = {
        " ": "/ ",
        "A": ".- ",
        "B": "-... ",
        "C": "-.-. ",
        "D": "-.. ",
        "E": ". ",
        "F": "..-. ",
        "G": "--. ",
        "H": ".... ",
        "I": ".. ",
        "J": ".--- ",
        "K": "-.- ",
        "L": ".-.. ",
        "M": "-- ",
        "N": "-. ",
        "O": "--- ",
        "P": ".--. ",
        "Q": "--.- ",
        "R": ".-. ",
        "S": "... ",
        "T": "- ",
        "U": "..- ",
        "V": "...- ",
        "W": ".-- ",
        "X": ".- ",
        "Y": "-..- ",
        "Z": "--.. ",
        "1": ".---- ",
        "2": "..--- ",
        "3": "...-- ",
        "4": "....- ",
        "5": "..... ",
        "6": "-.... ",
        "7": "--... ",
        "8": "---.. ",
        "9": "----. ",
        "0": "----- "
    }

    try:
        assert len(sys.argv) == 2, "wrong number of arguments"
        res = ""
        for char in sys.argv[1]:
            if not char.isalnum():
                assert char.isspace(), "bad argument"
            res += FUCK_MORSE_CODE[char.upper()]
        print(res)
    except AssertionError as msg:
        print("AssertionError:", msg)
        exit(1)
    return 0


if __name__ == "__main__":
    main()
