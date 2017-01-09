from image import file2image,color2gray 
from plotting import plot

im = file2image("img01.png")

img = color2gray(im)
pts = [x+y*1j for x in range(len(img)) for y in range(len(img[x])) if img[x][y] < 120]
plot(pts,max([x.real for x in pts]))

def mean(numbers):
    return float(sum(numbers)) / max(len(numbers), 1)

def centr(pts):
    mean_x = mean([x.real for x in pts])
    mean_y = mean([x.imag for x in pts])
    return [(x.real-mean_x)+(x.imag-mean_y)*1j for x in pts]
    
ptsc = centr(pts)
plot(ptsc,max([x.real for x in pts]))


def flip90(h):
    return 1j*h
    
def scale(h,s):
    return h*s

ptscflip = [scale(flip90(x),s=0.5) for x in ptsc]

plot(ptscflip,max([x.real for x in pts]))


from math import e,pi

n=20
w= [e**(2*pi*(1j/x)) if x > 0 else 1 for x in range(0,n)]

plot(w)


def rot(h,r):
    return h * e**(r*1j)
    
    
ptsr = [rot(x,pi/4) for x in pts]   
plot(ptsr,max([x.real for x in pts]))


ptsrtr = [scale(rot(x,pi/4),0.5) for x in centr(pts)]   
plot(ptsrtr,max([x.real for x in pts]))


# 1.5
from GF2 import one
one * one
one * 0
one+one