#!/usr/bin/python
# coding:utf-8
import os
wk_dir = os.path.dirname(os.path.realpath(__file__))
import sys
sys.path.append(wk_dir+'/../utils')

import cv2
import numpy as np
import util
# import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons

# load image
filePath = wk_dir+"/../images/lyf0.jpg"
img = cv2.imread(filePath, 0)

# proccess
thr0 = 50
thr1 = 200

edges = cv2.Canny(img, thr0, thr1, None, 3) # apertureSize 3,5,7

# util.showOpenCVImagesGrid([img, edges], 1, 2, titles=['original image', 'THRESH_BINARY'])
# util.showOpenCVImagesGrid([edges], 1, 1, titles=['Canny'])


plt,fig,im = util.getSinglePlt(edges, 'Canny')

#show
axcolor = 'lightgoldenrodyellow'
axfreq = plt.axes([0.0, 0.03, 0.5, 0.02], facecolor=axcolor)
axamp = plt.axes([0.0, 0.0, 0.5, 0.02], facecolor=axcolor)

sfreq = Slider(axfreq, 'Freq', 0.1, 255.0, valinit=thr0)
samp = Slider(axamp, 'Amp', 0.1, 255.0, valinit=thr1)


def updateThr0(val):
    thr0 = val
    edges = cv2.Canny(img, thr0, thr1)
    im.set_data(edges)
    fig.canvas.draw()

def updateThr1(val):
    thr1 = val
    edges = cv2.Canny(img, thr0, thr1)
    im.set_data(edges)
    fig.canvas.draw()

sfreq.on_changed(updateThr0)
samp.on_changed(updateThr1)

plt.show()

