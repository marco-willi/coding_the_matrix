# Lab
from image_mat_util import *

img_loc,img_col = file2mat('img01.png')

tt = mat2display(img_loc,img_col)

def identity(labels={'x','y','u'}):
    d = {}
    for l in labels:
        d[(l,l)] = 1
    return Mat((labels,labels),d)
    
    
def translation(alpha, beta):
    im = identity()
    im.f[('x','x')]
    