"""
generateData.py

In this program, a given number of percolation data points are generated and
then labeled, using percolation.py.
"""

# imports

import numpy as np
# from random import *
import matplotlib.pyplot as plt
from skimage import io, viewer

import sys
print("\nYou are running python", sys.version, "\n")


# local imports

import princeton
# import princeton/stdio
# import princeton/stdarray


# The main object: the Matrix

class Matrix:
    def __init__(self, size, porefraction, name):
        self.name = name
        self.size = size
        self.array = np.random.rand(size, size)
        self.porefraction = porefraction # fraction of open states == pore-space
        self.isTest = False
        self.array[self.array >= (1-porefraction)] = 1 # first raise high
        self.array[self.array < (1-porefraction)] = 0 # then lower low
        self.percolates = False
        print("A", self.size, "x", self.size, "matrix", self.name,
            "was generated and filled with a fraction of",
            (1-self.porefraction), "obstacles")

    def print_size(self):
        print( "The size of" , self.name , "is " , self.size)

    def show_image(self):
        # viewer.ImageViewer(self.array).show()
        plt.imshow(self.array, cmap='Greys_r')
        plt.show()

# TO DO
#   + integrate percolation checker
#   + generate a dataset of 10000 matrices
#   + export as png images and a text file labeling the matrices by percolation

mat00001 = Matrix(128, .2, 'mat00001')

print(mat00001.array)
print(mat00001.array.size)
mat00001.show_image()