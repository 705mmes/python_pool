#!/usr/bin/env python3.10
# -*- coding: utf-8 -*-?


"""The cv2.addWeighted function blends the green overlay
and the original image based on the 0.5 parameter.
"""

import cv2
import numpy as np


def render_img(array, name):
    """render image in a window"""
    print("Press ESC to quit")
    cv2.imshow(name, array)
    key = cv2.waitKey(0)
    if key == 27:  # ESC key
        cv2.destroyAllWindows()

    return


def ft_green(array) -> np.ndarray:
    """applies green filter to image"""
    green_overlay = np.full(array.shape, (0, 255, 0), dtype=np.uint8)
    result = cv2.addWeighted(green_overlay, 0.5, array, 1 - 0.5, 0)

    render_img(result, "Green filter")

    return result


def ft_red(array) -> np.ndarray:
    """applies red filter to image"""
    red_overlay = np.full(array.shape, (0, 0, 255), dtype=np.uint8)
    result = cv2.addWeighted(red_overlay, 0.5, array, 1 - 0.5, 0)

    render_img(result, "Red filter")

    return result


def ft_blue(array) -> np.ndarray:
    """applies blue filter to image"""
    blue_overlay = np.full(array.shape, (255, 0, 0), dtype=np.uint8)
    result = cv2.addWeighted(blue_overlay, 0.5, array, 1 - 0.5, 0)

    render_img(result, "Blue filter")

    return result


def ft_grey(array) -> np.ndarray:
    """applies grey filter to image"""
    gray = cv2.cvtColor(array, cv2.COLOR_BGR2GRAY)
    gray_bgr = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)

    render_img(gray_bgr, "Grayscale Filter")
    return gray_bgr


def ft_invert(array) -> np.ndarray:
    """applies inverted filter to image"""
    inverted = cv2.bitwise_not(array)

    render_img(inverted, "Inverted Filter")
    return inverted
