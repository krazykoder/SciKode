# 
# Created by towshif ali (tali) on 4/2/2018
#

import os
import numpy as np
import matplotlib.pyplot as plt

from skimage import io
from scipy import ndimage as ndi
from scipy import misc
from skimage import feature

def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.299, 0.587, 0.114])


from skimage import io
# load image s
# filename = os.path.join('H:\\temp\\','000013_RT_01_SemAdcDef1_Pattern-Top_RID_000512.tif')
im = misc.imread('H:\\temp\\000013_RT_01_SemAdcDef1_Pattern-Top_RID_000512.tif', flatten=True)
#im = misc.imread('H:\\temp\\000013_RT_01_SemAdcDef1_Pattern-Top_RID_000512.tif')

# io.imshow(im)
# io.show()
#
# im = rgb2gray(im)
#
# io.imshow(im)
# io.show()


#im = ndi.gaussian_filter(im, 3)
im = im + 0.4 * im.std() * np.random.random(im.shape)

io.imshow(im)
io.show()

#gauss_denoised = ndi.gaussian_filter(noisy, 4)
im = ndi.median_filter(im, 2)

io.imshow(im)
io.show()

edges = feature.canny(im, low_threshold=70,high_threshold=180, sigma=1,use_quantiles=False)
io.imshow(edges)
io.show()