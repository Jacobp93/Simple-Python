from typing import Type
import numpy as np
from numpy.core.shape_base import hstack

heights = [189, 170, 189, 163, 183, 171, 185, 168, 173, 183, 173, 173, 175, 178, 183, 193, 178, 173, 174, 183, 183, 180,
           168, 180, 170, 178, 182, 180, 183, 178, 182, 188, 175, 179, 183, 193, 182, 183, 177, 185, 188, 188, 182, 185, 191]

ages = [57, 61, 57, 57, 58, 57, 61, 54, 68, 51, 49, 64, 50, 48, 65, 52, 56, 46, 54, 49, 51, 47,
        55, 55, 54, 42, 51, 56, 55, 51, 54, 51, 60, 62, 43, 55, 56, 61, 52, 69, 64, 46, 54, 47, 70]

heights_array = np.array(heights)
ages_array = np.array(ages)

# Convert into NP array ^^^^^

Dataset = np.vstack((heights_array, ages_array))
# Merge data sets together which becomes a 2d Array Vstack = Verticle Hstack = Horizontally

print(Dataset)
