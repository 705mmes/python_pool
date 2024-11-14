#!/usr/bin/env python3.10
# -*- coding: utf-8 -*-?


import pandas as pd
from aff_life import display


def check_file(path):
    """checks if file is valid"""
    # Basic check for filename extension
    if not (path.endswith('.csv')):
        raise AssertionError("Error: wrong file extension")

    # Try opening the file to check if it has any content
    try:
        with open(path, 'rb') as file:
            content = file.read(1)
            if not content:
                raise AssertionError(f"Error: The file '{path}' is empty.")
    except FileNotFoundError:
        raise AssertionError(f"Error: The file '{path}' does not exist.")


def load(path: str) -> pd.DataFrame:
    """loads a dataset"""
    try:
        check_file(path)
        data = pd.read_csv(path)
        print("Loading dataset of dimensions", len(data), len(data.columns))
        return data

    except AssertionError as msg:
        print(msg)
        exit(1)


def main():
    data = load("life_expectancy_years.csv")
    print(data)
    display(data)
    return 0


if __name__ == main():
    main()
