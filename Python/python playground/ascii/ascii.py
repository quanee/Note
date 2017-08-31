import argparse
import numpy as np
from PIL import Image
"""图片转ascii码文字图"""



# grayscale level values from:
# http://paulbourke.net/dataformats/asciiart/

# 70 levels of gray
gscale1 = "$@B%8&WM#*oahkbdpqwmZOOQLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "

# 10 levels of gray
gscale2 = '@%#*+=-:. '


def getAverageL(image):
    """
    Given PIL Image, return average value of grayscale value
    """

    # get image as numpy array
    im = np.array(image)
    # get the dimensions
    w, h = im.shape
    # get the average
    return np.average(im.reshape(w * h))


def covertImageToAscii(fileName, cols, scale, moreLevels):
    """
    Given Image and dimensions (rows, cols), returns an m*n list of Images
    """
    # declare globals
    global gscale1, gscale2
    # open image and convert to grayscale
    image = Image.open(fileName).convert('L')
    # store the image dimensions
    W, H = image.size[0], image.size[1]
    print("input image dims: %d x %d" % (W, H))
    # cpmpute tile width
    w = W / cols
    # compute tile height based on the aspect ratio and scale of the font
    h = w / scale
    # compute number of rows to use in the final grid
    rows = int(H / h)

    print("col: %d, rows: %d" % (cols, rows))
    print("tile dims: %d x %d" % (w, h))

    # chech if image size is too small
    if cols > W or rows > H:
        print("Image too small for specified cols!")