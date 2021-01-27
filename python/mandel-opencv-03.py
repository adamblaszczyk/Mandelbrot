#
# ---------------------------------------------
# Mandelbrot Set
# [ main program ]
# ---------------------------------------------
# Author: Adam Blaszczyk
#         http://wyciekpamieci.blogspot.com
# ---------------------------------------------
#
# Requirements:
#         - Python 3.x
#         - OpenCV (pip install opencv-python)
#         - NumPy  (pip install numpy)
#

import cv2
import numpy as np

def pix(image,x,y,r,g,b):
    image[y,x] = [b,g,r]


amin = -2
amax = 1
bmin = -1.2
bmax = 1.2

XMAX = 900
YMAX = 720

MAX_ITER = 40

img = np.zeros((YMAX,XMAX,3), np.uint8) #y,x

for px in range(XMAX):
    a = ((amax - amin) / XMAX) * px + amin
    
    for py in range(YMAX):
        b = -((bmax - bmin) / YMAX) * py + bmax;
        
        x = 0
        y = 0
        #i = 0
        for i in range(MAX_ITER):
            xtemp = x*x - y*y + a
            y = 2*x*y + b
            x = xtemp
            r2 = x*x + y*y
            if r2 > 4:
                red   = 128 + 256 * i / MAX_ITER
                green = 128 + 512 * i / MAX_ITER
                blue  = 128 + 1024 * i / MAX_ITER
                break
            else:
                red = 0
                green = 0
                blue = 0
                
        pix(img, px,py, red,green,blue)

cv2.imshow("Mandelbrot Set", img)

cv2.waitKey(0)
