#!/usr/bin/env python3
# -*- coding: utf-8 -*-?


def ft_filter(function, iterable):
    """Yields all values from the iterable for which\
the function returns a truthful value"""
    value = [item for item in iterable if function(item)]
    yield value
