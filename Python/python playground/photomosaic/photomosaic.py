import argparse
import os
import random
from PIL import Image
import imghdr
import numpy as np


def getAverageRGB(image):
    """
    return the average collor value as (r, g, b) for each input image
    """

    # get each title image as a numpy array
    im = np.array(image)
    # get the shape of each input image
    w, h, d = im.shape
    # get the average RGB value
    return tuple(np.average(im.reshape(w * h, d), axis=0))


def splitImage(image, size):
    """
    given the image and dimensions (rows, cols), returns an m*n list of images
    """

    W, H = image.size[0], image.size[1]
    m, n = size
    w, h = int(W / n), int(H / m)
    # imgae lis
    imgs = []
    # generate a list of dimensions
    for j in range(m):
        for i in range(n):
            # append cropped image
            imgs.append(image.crop((i * w, j * h, (i + 1) * w, (j + 1) * h)))

    return imgs


def getImages(imageDir):
    """
    given a directory of images, return a list of Image
    """
    files = os.listdir(imageDir)
    images = []
    for file in files:
        filePath = os.path.abspath(os.path.join(imageDir, file))
        try:
            # explicit load so we don't run into a resource crunch
            fp = open(filePath, "rb")