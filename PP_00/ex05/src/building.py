#!/usr/bin/env python3.10
# -*- coding: utf-8 -*-?

import sys


def count_tha_shit_up(string):
    """ Main OP function that calls all operations """
    upper_cases(string)
    lower_cases(string)
    spaces(string) - 1
    decimal(string)
    punctuation(string)


def upper_cases(string):
    """ Counts uppercases in string """
    res = 0
    for char in string:
        if char.isupper():
            res += 1
    print(res, "upper letters")
    return res


def lower_cases(string):
    """ Counts lowercases in string """
    res = 0
    for char in string:
        if char.isalpha():
            res += 1
        if char.isupper():
            res -= 1
    print(res, "lower letters")
    return res


def spaces(string):
    """ Counts spaces in string """
    res = 0
    for char in string:
        if char.isspace():
            res += 1
    print(res, "spaces")
    return res


def decimal(string):
    """ Counts digits in string """
    res = 0
    for char in string:
        if char.isdecimal():
            res += 1
    print(res, "digits")
    return res


def punctuation(string):
    """ Counts punctuations in string """
    res = 0
    for char in string:
        if char.isascii() and not (char.isdecimal() or char.isalpha() or char.isspace()):
            res += 1
    print(res, "punctuation marks")
    return res


def main():
    assert len(sys.argv) <= 2, "Too much arguments"
    if len(sys.argv) < 2:
        string = input("What is the text to count?\n")
        print("The text contains", len(string), "characters:")
        count_tha_shit_up(string)
    else:
        count_tha_shit_up(sys.argv[1])
    return 0


if __name__ == "__main__":
    main()
