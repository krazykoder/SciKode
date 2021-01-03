# 
# Created by towshif ali (tali) on 6/21/2018
#

from PIL import Image
import numpy as np


w, h = 512, 512
data = np.zeros((h, w, 3), dtype=np.uint8)
data[256, 256] = [255, 0, 0]
img = Image.fromarray(data, 'RGB')
# img.save('my.png')
# img.show()


import scipy.misc
from scipy.ndimage import median_filter
import numpy as np

random_array = np.random.random_sample((512,512,3))

random_array[random_array < 0.999] *= 0.25

filtered_array = median_filter(random_array, size=3)

scipy.misc.imsave('white_specs.png', random_array)
scipy.misc.imsave('white_specs-F.png', filtered_array)