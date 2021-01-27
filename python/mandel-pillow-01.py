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
#         - Pillow (pip install Pillow)
#

from PIL import Image, ImageDraw

amin = -2
amax = 1
bmin = -1.2
bmax = 1.2

XMAX = 900
YMAX = 720

MAX_ITER = 80

img = Image.new('RGB', (XMAX, YMAX), (0, 0, 0))
draw = ImageDraw.Draw(img)

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
                
        draw.point([px,py], (int(red), int(green), int(blue)))

img.show()
img.save('mandelbrot.png', 'PNG')
