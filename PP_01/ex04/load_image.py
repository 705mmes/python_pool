#!/usr/bin/env python3.10
# -*- coding: utf-8 -*-?

"""SciPy is a collection of mathematical algorithms and convenience functions
built on NumPy. It adds significant power to Python by providing the user with
high-level commands and classes for manipulating and visualizing data."""


import numpy as np
import cv2
from rotate import ft_rotate


def check_file(path):
    """checks if file is valid"""
    # Basic check for filename extension
    if not (path.endswith('.jpg') or path.endswith('.jpeg')):
        raise AssertionError("Error: wrong file extension")

    # Try opening the file to check if it has any content
    try:
        with open(path, 'rb') as file:
            content = file.read(1)
            if not content:
                raise AssertionError(f"Error: The file '{path}' is empty.")
    except FileNotFoundError:
        raise AssertionError(f"Error: The file '{path}' does not exist.")


def ft_load(path: str) -> np.ndarray:
    """loads a file"""
    try:
        check_file(path)
        img = cv2.imread(path)

        if img is None:
            raise ValueError("Error: The image could not be loaded.")

        print(ft_rotate(img))

    except AssertionError as msg:
        print(msg)
        return None

    return img
