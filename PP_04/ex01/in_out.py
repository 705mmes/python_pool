#!/usr/bin/env python3.10
# -*- coding: utf-8 -*-?


def square(x: int | float) -> int | float:
    return x ** 2


def pow(x: int | float) -> int | float:
    return x ** x


def outer(x: int | float, function) -> object:
    count = 0
    def inner() -> float:
        nonlocal count
        if count == 0:
            count = (float)(function(x))
        else:
            count = (float)(function(count))
        return count
    return inner
