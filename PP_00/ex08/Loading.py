#!/usr/bin/env python3.10
# -*- coding: utf-8 -*-?


def ft_tqdm(lst: range) -> None:
    """prints a loading bar"""
    total = len(lst)
    for i in lst:
        percent = (i + 1) / total
        bar_length = 75
        filled_length = int(bar_length * percent)
        bar = "=" * filled_length + "-" * (bar_length - filled_length)
        print(f"\r{int(percent * 100)}%|{bar}| {i + 1}/{total}", end="")
        yield i
