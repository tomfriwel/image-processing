#!/usr/bin/python
# coding:utf-8
import os
wk_dir = os.path.dirname(os.path.realpath(__file__))
import sys
sys.path.append(wk_dir+'/../utils')

import cv2
import util

filePath = wk_dir+"/../images/figure.jpg"
img = cv2.imread(filePath, 1)

thr = cv2.threshold(img, 149, 255, cv2.THRESH_BINARY)[1]

util.showOpenCVImagesGrid([img, thr], 1, 2, titles=['original image', 'THRESH_BINARY'])



