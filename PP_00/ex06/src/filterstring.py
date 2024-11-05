#!/usr/bin/env python3.10
# -*- coding: utf-8 -*-?
""" list comprehension syntax:
newlist = [expression for item in iterable if condition == True] """


from ft_filter import ft_filter
import sys


def main():
    try:
        assert len(sys.argv) == 3, "wrong number of arguments"
        i = 1
        str = sys.argv[1]
        ac = sys.argv[2]
        while i <= 2:
            for char in sys.argv[i]:
                if not char.isalnum():
                    assert char.isspace(), "special char found"
                if i == 2 and not char.isdigit():
                    raise AssertionError("bad arguments")
            i += 1
        filtered_str = list(ft_filter(lambda x: len(x) > int(ac), str.split()))
        print("filtered_str:", filtered_str)
    except AssertionError as msg:
        print("AssertionError:", msg)
        exit(1)
    return 0


if __name__ == "__main__":
    main()
