#!/usr/bin/python
# coding:utf-8

import sys
sys.path.append('../utils')

import cv2
import util


filePath = "../images/figure.jpg"
img = cv2.imread(filePath, 1)

util.showOpenCVImagesGrid([img], 1, 2, titles=[''])



