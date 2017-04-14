import os
import cv2
import numpy as np
from matplotlib import pyplot as plt
import Image

# Draw rectangle

img = np.zeros((512, 512, 3), np.uint8)
cv2.rectangle(img, (20, 20), (411, 411), (55, 255, 155), 2)
plt.imshow(img, 'brg')
cv2.imwrite("/path/to/save/img.jpg", img)

# Use PIL to show ndarray

w,h = 512,512
data = np.zeros( (w,h,3), dtype=np.uint8)
data[256,256] = [255,0,0]
img = Image.fromarray(data, 'RGB')
img.save('my.png')

# Convert numpy multi-dim ndarray to 1-dim array

a = np.array(([1, 1, 1], [2, 2, 2]), dtype=np.int)
np.asarray(a).reshape(-1)

# Remove duplicate elements

values = [5, 5, 1, 1, 2, 3, 4, 4, 5] # Our input list
# Convert to a set and back into a list.
set = set(values)
result = list(set)
print(result)
#Output:
# >>> [1, 2, 3, 4, 5]

# Simple operations

os.getcwd()
path = '/path/to/target/dir'
os.chdir(path)
os.path.dirname(os.path.abspath(__file__))

# Sort array by column

from operator import itemgetter
a = ([2, 2, 2, 40], [5, 5, 5, 10], [1, 1, 1, 50], [3, 3, 3, 30], [4, 4, 4, 20])
sorted(a, key=itemgetter(3))
# output
# >>> [[5, 5, 5, 10], [4, 4, 4, 20], [3, 3, 3, 30], [2, 2, 2, 40], [1, 1, 1, 50]]

# Dynamically adding anaconda2 opencv path to system path

import sys
sys.path.insert(0, '/path/to/anaconda2/lib/python2.7/site-packages/')
import cv2

# sorting arrays in numpy by column
# [:,1] indicates the second column of a
a[a[:,1].argsort()]

# Sort Python dict by value

sorted(dict.items(), lambda x, y: cmp(x[1], y[1]))
sorted(dict.items(), lambda x, y: cmp(x[1], y[1]), reverse=True)
