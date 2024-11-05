#!/usr/bin/env python3.10
# -*- coding: utf-8 -*-?


import imageio as iio
import numpy as np
import os


def ft_load(path: str) -> np.ndarray:
    try:
        if not os.path.exists(path):
            raise AssertionError(f"Error: The file '{path}' does not exist.")
        if not path.endswith('.jpg') and not path.endswith('.jpeg'):
            raise AssertionError ("Error: wrong file extension")
        img = iio.imread(path)
        print("The shape of the image is:", img.shape)
    except AssertionError as msg:
        print(msg)
        exit(1)
    return img
