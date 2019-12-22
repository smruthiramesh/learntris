#!/usr/bin/env python

import numpy as np

def createMatrix():
    mat = np.empty((22,10),dtype=str)
    mat.fill(".")
    return mat

args = input()
if args == 'q':
    pass
elif args == 'p':
    mat = createMatrix()
    for i in range(mat.shape[0]):
        print(" ".join(mat[i]))