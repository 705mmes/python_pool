#!/usr/bin/env python3.10
# -*- coding: utf-8 -*-?


import matplotlib.pyplot as plt
from scipy.ndimage import rotate
import cv2


def render_img(img, name):
    print("Press ESC to quit")
    cv2.imshow(name, img)
    key = cv2.waitKey(0)  # Waits indefinitely until a key is pressed
    if key == 27:  # ESC key
        cv2.destroyAllWindows()

    return


def ft_rotate(img, x=(400, 900), y=(0, 500)):
    """rotates an image"""
    sliced_img = img[y[0]:y[1], x[0]:x[1]]

    print("The shape of the image is:", sliced_img.shape)
    print(sliced_img)
    render_img(sliced_img, "Original Image")

    rotated_img = rotate(sliced_img, 90)

    fig, ax = plt.subplots(figsize=(8, 8))
    ax.imshow(rotated_img)

    # Set limits and labels for the cropped display
    ax.set_xlabel('X-axis (pixels)')
    ax.set_ylabel('Y-axis (pixels)')
    ax.set_title("Rotated image")

    print("New shape after rotating:", rotated_img.shape)

    plt.show()

    return rotated_img
