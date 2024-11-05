#!/usr/bin/env python3.10
# -*- coding: utf-8 -*-?


import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    try:
        assert isinstance(family, list), "`family` is not a list."
        assert all(isinstance(sublist, list) for sublist in family), \
            "Not all elements in `family` are lists."
        excepted_length = len(family[0])
        assert all(len(sublist) == excepted_length for sublist in family), \
            "Sublists in `family` do not have the same length."
    except AssertionError as msg:
        print("AssertionError:", msg)
        exit(1)
    r = np.array(family)
    new_r = r[start:end]
    print("My shape is:", r.shape)
    print("My new shape is:", new_r.shape)
    return new_r.tolist()
