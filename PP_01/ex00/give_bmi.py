#!/usr/bin/env python3.10
# -*- coding: utf-8 -*-?
"""oublie pas le append bouffon"""


def give_bmi(h: list[int | float], w: list[int | float]) -> list[float]:
    """gives user's bmi"""
    if len(h) != len(w):
        raise ValueError("Heights and weights lists sizes must be equal")
    results = []
    """The zip() function takes iterables (can be zero or more),
    aggregates them in a tuple, and returns it."""
    for height, weight in zip(h, w):
        if height > 0 and weight > 0:
            results.append(weight / (height ** 2))
        else:
            results.append(0)
    return results


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """creates array of values over the limit"""
    results = []
    for value in bmi:
        results.append(value >= limit)
    return results
