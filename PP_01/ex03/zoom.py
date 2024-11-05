#!/usr/bin/env python3.10
# -*- coding: utf-8 -*-?


import matplotlib.pyplot as plt
# from scipy.ndimage import zoom, rotate


def ft_zoom(img, zoom_factor=2, x=(400, 900), y=(0, 500)):
    """
    OUBLI AP
    """
    sliced_img = img[y[0]:y[1], x[0]:x[1]]

    fig, ax = plt.subplots(figsize=(8, 8))
    ax.imshow(sliced_img)

    # Set limits and labels for the cropped display
    ax.set_xlabel('X-axis (pixels)')
    ax.set_ylabel('Y-axis (pixels)')
    ax.set_title("Sliced image")

    print("New shape after slicing:", sliced_img.shape)

    plt.show()

    return sliced_img
