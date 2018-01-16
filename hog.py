import matplotlib.pyplot as plt

from skimage import feature as ft
from skimage import data, exposure
import numpy as 

image = data.astronaut()

features = ft.hog(image,  # input image
                  orientations=8,  # number of bins
                  pixels_per_cell=(16, 16), # pixel per cell
                  cells_per_block=(1, 1), # cells per blcok
                  #block_norm = 'L1', #  block norm : str {‘L1’, ‘L1-sqrt’, ‘L2’, ‘L2-Hys’}
                  transform_sqrt = True, # power law compression (also known as gamma correction)
                  feature_vector=True, # flatten the final vectors
                  visualise=False) # return HOG map
print("ok")