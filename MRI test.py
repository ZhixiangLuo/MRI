# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 11:10:39 2017

@author: jeffluo
"""

import numpy as np
import matplotlib.pyplot as plt

from skimage import data, color
from skimage.transform import hough_circle, hough_circle_peaks
from skimage.feature import canny
from skimage.draw import circle_perimeter
from skimage.util import img_as_ubyte

from PIL import Image
import dicom
import numpy
ds = dicom.read_file("C:\\Users\\jeffluo\\Desktop\\Python\\test.dcm")
pixel_bytes = ds.PixelData
#image = ds.pixel_array


mri=Image.open("C:\\Users\\jeffluo\\Desktop\\Python\\heart2.jpg")
image=np.array(mri.getdata(),np.uint8).reshape(mri.size[1], mri.size[0])
# Load picture and detect edges
# image = img_as_ubyte(data.coins()[160:230, 70:270])
edges = canny(image, sigma=3, low_threshold=10, high_threshold=90)



# Detect two radii
hough_radii = np.arange(30, 45, 1)
hough_res = hough_circle(edges, hough_radii)

# Select the most prominent 5 circles
accums, cx, cy, radii = hough_circle_peaks(hough_res, hough_radii,
                                           total_num_peaks=1)
plt.close("all")
# Draw them

fig, (ax,ax1) = plt.subplots(ncols=2, nrows=1, figsize=(12, 6))
image = color.gray2rgb(image)
for center_y, center_x, radius in zip(cy, cx, radii):
    circy, circx = circle_perimeter(center_y, center_x, radius)
    image[circy, circx] = (220, 20, 20)

ax.imshow(image, cmap=plt.cm.gray)
plt.show()

#plt.subplot(122)
x = 100-edges*100
#fig, ax = plt.subplots(ncols=1, nrows=1, figsize=(4, 4))
ax1.imshow(x, cmap=plt.cm.gray)
#plt.show()