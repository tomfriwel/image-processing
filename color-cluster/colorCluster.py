# https://www.pyimagesearch.com/2014/05/26/opencv-python-k-means-color-clustering/

import os
wk_dir = os.path.dirname(os.path.realpath(__file__))
import sys
sys.path.append(wk_dir + '/../utils')

import util

from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import argparse
import utils
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
ap.add_argument("-c", "--clusters", required=True, type=int,
                help="# of clusters")
args = vars(ap.parse_args())

# load the image and convert it from BGR to RGB so that
# we can dispaly it with matplotlib
image = cv2.imread(args["image"])
showimage = image.copy()
# image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)


# show our image
# plt.figure()
# plt.axis("off")
# plt.imshow(image)

# resize https://stackoverflow.com/questions/4195453/how-to-resize-an-image-with-opencv2-0-and-python2-6
w = 400
# h = (image.shape[0] / image.shape[1]) * w
h = int(image.shape[0] / (image.shape[1] * 1.0) * w)
# exit()
small = cv2.resize(image, (w, h))
# small = cv2.resize(image, (0,0), fx=0.5, fy=0.5)
# reshape the image to be a list of pixels
image = small.reshape((small.shape[0] * small.shape[1], 3))

# cluster the pixel intensities
clt = KMeans(n_clusters=args["clusters"])
clt.fit(image)

# build a histogram of clusters and then create a figure
# representing the number of pixels labeled to each color
hist = utils.centroid_histogram(clt)
bar = utils.plot_colors(hist, clt.cluster_centers_)

# show our color bart
# plt.figure()
# plt.axis("off")
# plt.imshow(bar)
# plt.show()
util.showOpenCVImagesGrid([showimage, small, bar], 2, 2, axis="off")

# command $ python color-cluster/colorCluster.py -i ./images/atey-ghailan-167.jpg -c 10