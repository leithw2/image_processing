from matplotlib import pyplot as plt
import matplotlib.image as mpimg

from skimage import data
from skimage.color import rgb2gray
from skimage.feature import corner_harris, corner_subpix, corner_peaks
from skimage.transform import warp, AffineTransform
from skimage.filters import threshold_otsu
from skimage.draw import ellipse

import os

dirpath = os.getcwd()
print("current directory is : " + dirpath)
foldername = os.path.basename(dirpath)
print("Directory name is : " + foldername)

# Sheared checkerboard
tform = AffineTransform(scale=(1.3, 1.1), rotation=1, shear=0.7,
                        translation=(110, 30))
#image = warp(data.checkerboard()[:90, :90], tform.inverse,
#             output_shape=(200, 310))

'''codigo nuevo'''

image = mpimg.imread("photo.jpg")
image = rgb2gray(image)
#thresh = threshold_otsu(image)
binary = image > .300

'''/codigo nuevo'''

# Ellipse
rr, cc = ellipse(160, 175, 10, 100)
#image[rr, cc] = 1
# Two squares
image[30:80, 200:250] = .5
image[80:130, 250:300] = .1

coords = corner_peaks(corner_harris(binary), min_distance=30)
coords_subpix = corner_subpix(binary, coords, window_size=13)

fig, ax = plt.subplots()
ax.imshow(binary,plt.cm.gray)
ax.plot(coords[:, 1], coords[:, 0], color='cyan', marker='o',
        linestyle='None', markersize=6)
ax.plot(coords_subpix[:, 1], coords_subpix[:, 0], '+r', markersize=15)
ax.axis((0, 310, 200, 0))
plt.show()
