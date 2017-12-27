#!/usr/bin/python
# coding:utf-8

import cv2
import numpy as np
import matplotlib.pyplot as plt

def showOpenCVImagesGrid(images, x, y, titles=None, axis="on"):
    """
    Show multiple images, you can provide ervey image titles.
    @param images array of images
    """
    fig = plt.figure()
    i = 1

    for item in images:
        image = None
        title = None
        if type(images) is list:
            image = item
            if titles is not None:
                title = titles[i - 1]
        elif type(images) is dict:
            image = images[item]
            title = item

        if image is None:
            i += 1
            continue

        copy = image.copy()
        channel = len(copy.shape)

        cmap = None
        if channel == 2:
            cmap = "gray"
        elif channel == 3:
            copy = cv2.cvtColor(copy, cv2.COLOR_BGR2RGB)
        elif channel == 4:
            copy = cv2.cvtColor(copy, cv2.COLOR_BGRA2RGBA)

        fig.add_subplot(x, y, i)

        plt.title(title)
        plt.axis(axis)
        plt.imshow(copy, cmap=cmap)
        i += 1
    plt.show()
