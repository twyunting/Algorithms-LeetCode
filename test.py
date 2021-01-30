import cv2
import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import convolve2d as conv2d
import scipy.sparse as sps
from PIL import Image


a = np.array([[0, 0, 0], [0, 1, 0], [0, 0, 0]])
print(a)
b = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])/8
print(b)
