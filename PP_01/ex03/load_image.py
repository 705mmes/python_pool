#!/usr/bin/env python3.10
# -*- coding: utf-8 -*-?

"""SciPy is a collection of mathematical algorithms and convenience functions
built on NumPy. It adds significant power to Python by providing the user with
high-level commands and classes for manipulating and visualizing data."""


import numpy as np
import os
import cv2
from zoom import ft_zoom


def ft_load(path: str) -> np.ndarray:
    try:
        if not os.path.exists(path):
            raise AssertionError(f"Error: The file '{path}' does not exist.")
        if not path.lower().endswith(('.jpg', '.jpeg')):
            raise AssertionError("Error: Wrong file extension.\
                                 Please provide a .jpg or .jpeg file.")
        if os.path.getsize(path) == 0:
            raise AssertionError("Error: The file is empty.")

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
    print("Press ESC to quit")
    cv2.imshow(name, img)
    key = cv2.waitKey(0)  # Waits indefinitely until a key is pressed
    if key == 27:  # ESC key
        cv2.destroyAllWindows()

    return
