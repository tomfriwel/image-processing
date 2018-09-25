#!/usr/bin/python
# coding:utf-8
import os
wk_dir = os.path.dirname(os.path.realpath(__file__))
import sys
sys.path.append(wk_dir+'/../utils')

import cv2
import numpy as np
import util

# load image
filePath = wk_dir+"/../images/lyf1.jpg"
img = cv2.imread(filePath, 0)

# proccess
edges = cv2.Canny(img, 50,200)

# util.showOpenCVImagesGrid([img, edges], 1, 2, titles=['original image', 'THRESH_BINARY'])
util.showOpenCVImagesGrid([edges], 1, 1, titles=['Canny'])



