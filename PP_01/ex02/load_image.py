#!/usr/bin/env python3.10
# -*- coding: utf-8 -*-?


import imageio as iio
import numpy as np


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
        img = iio.imread(path)
        print("The shape of the image is:", img.shape)
    except AssertionError as msg:
        print(msg)
        exit(1)
    return img
