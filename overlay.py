from math import sqrt

import os, sys
from PIL import Image, ImageOps

im = Image.open(sys.argv[1])
ogsize = im.size
im = ImageOps.flip(im)
#x = 3
#y = 4
im = im.resize((800,800))
pix = im.load()
w, h = im.size

C = (
    (0, 255, 0),
    (255, 0, 0),
    (0, 0, 255)
)

CO = (
    (0, 0, 0),
    (0, 255, 0),
    (255, 0, 0),
    (0, 0, 255),
    (255, 255, 255)
)

COLORS = (
    (0, 0, 0),
    (0, 255, 0),
    (255, 0, 0),
    (0, 0, 255),
    (255, 0, 255),
    (255, 255, 0),
    (0, 255, 255),
    (255, 255, 255)
)

def cthree(rgb):
    r, g, b = rgb
    color_diffs = []
    for color in C:
        cr, cg, cb = color
        color_diff = sqrt(abs(r - cr)**2 + abs(g - cg)**2 + abs(b - cb)**2)
        color_diffs.append((color_diff, color))
    return min(color_diffs)[1]
def cfive(rgb):
    r, g, b = rgb
    color_diffs = []
    for color in CO:
        cr, cg, cb = color
        color_diff = sqrt(abs(r - cr)**2 + abs(g - cg)**2 + abs(b - cb)**2)
        color_diffs.append((color_diff, color))
    return min(color_diffs)[1]
def ceight(rgb):
    r, g, b = rgb
    color_diffs = []
    for color in COLORS:
        cr, cg, cb = color
        color_diff = sqrt(abs(r - cr)**2 + abs(g - cg)**2 + abs(b - cb)**2)
        color_diffs.append((color_diff, color))
    return min(color_diffs)[1]
three = open("3","wt+")
five = open("5","wt+")
eight = open("8","wt+")
for x in range(0,w):
    for y in range (0,h):
        three.write(str(x)+","+str(y)+","+str(cthree((pix[x,y])))+"\n")
        five.write(str(x)+","+str(y)+","+str(cfive((pix[x,y])))+"\n")
        eight.write(str(x)+","+str(y)+","+str(ceight((pix[x,y])))+"\n")

import numpy as np
os.system('py -3.8 bmp.py 3 og1.bmp')
os.system('py -3.8 bmp.py 5 og2.bmp')
os.system('py -3.8 bmp.py 8 og3.bmp')
img = Image.open("og2.bmp")
img2 = Image.open("og1.bmp")
background = Image.open("og3.bmp")
im_rgba = img.copy()
im_rgba.putalpha(26)
im2_rgba = img2.copy()
im2_rgba.putalpha(52)
background.paste(im2_rgba, (0,0), im2_rgba)
bg2 =  background
bg2.paste(im_rgba, (0, 0), im_rgba)
bg2 = bg2.resize(ogsize)
bg2.save(sys.argv[1]+'_restricted.png',"PNG")
three.close()
five.close()
eight.close()
os.remove('3')
os.remove('5')
os.remove('8')
os.remove('og1.bmp')
os.remove('og2.bmp')
os.remove('og3.bmp')