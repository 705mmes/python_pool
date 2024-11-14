#!/usr/bin/env python3.10
# -*- coding: utf-8 -*-?

"""SciPy is a collection of mathematical algorithms and convenience functions
built on NumPy. It adds significant power to Python by providing the user with
high-level commands and classes for manipulating and visualizing data."""


import numpy as np
import cv2
from zoom import ft_zoom


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
    """loads and print images after zoom"""
    try:
        check_file(path)
        img = cv2.imread(path)

        if img is None:
            raise ValueError("Error: The image could not be loaded.")

        print("The shape of the image is:", img.shape)
        print(img)
        render_img(img, "Original Image")

        zoomed_img = ft_zoom(img)
        print(zoomed_img)

    except AssertionError as msg:
        print(msg)
        return None

    return img


def render_img(img, name):
    """renders images in a window"""
    print("Press ESC to quit")
    cv2.imshow(name, img)
    key = cv2.waitKey(0)  # Waits indefinitely until a key is pressed
    if key == 27:  # ESC key
        cv2.destroyAllWindows()

    return
