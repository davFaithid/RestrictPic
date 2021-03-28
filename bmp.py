from struct import pack
import sys

class Bitmap():
  def __init__(s, width, height):
    s._bfType = 19778 # Bitmap signature
    s._bfReserved1 = 0
    s._bfReserved2 = 0
    s._bcPlanes = 1
    s._bcSize = 12
    s._bcBitCount = 24
    s._bfOffBits = 26
    s._bcWidth = width
    s._bcHeight = height
    s._bfSize = 26+s._bcWidth*3*s._bcHeight
    s.clear()


  def clear(s):
    s._graphics = [(0,0,0)]*s._bcWidth*s._bcHeight


  def setPixel(s, x, y, color):
    if isinstance(color, tuple):
      if x<0 or y<0 or x>s._bcWidth-1 or y>s._bcHeight-1:
        raise ValueError('Coords out of range')
      if len(color) != 3:
        raise ValueError('Color must be a tuple of 3 elems')
      #s._graphics[y*s._bcWidth+y] = (color[2], color[1], color[0])
      #s._graphics[y*s._bcWidth-y] = (color[2], color[1], color[0])
      s._graphics[y*s._bcWidth+x] = (color[2], color[1], color[0])
      #s._graphics[y*s._bcWidth-x] = (color[2], color[1], color[0])
    else:
      raise ValueError('Color must be a tuple of 3 elems')


  def write(s, file):
    with open(file, 'wb') as f:
      f.write(pack('<HLHHL', 
                   s._bfType, 
                   s._bfSize, 
                   s._bfReserved1, 
                   s._bfReserved2, 
                   s._bfOffBits)) # Writing BITMAPFILEHEADER
      f.write(pack('<LHHHH', 
                   s._bcSize, 
                   s._bcWidth, 
                   s._bcHeight, 
                   s._bcPlanes, 
                   s._bcBitCount)) # Writing BITMAPINFO
      for px in s._graphics:
        f.write(pack('<BBB', *px))
      for i in range((4 - ((s._bcWidth*3) % 4)) % 4):
        f.write(pack('B', 0))



def main():
    side = 800
    b = Bitmap(side, side)
    #for j in range(0, side):
    with open(sys.argv[1],'rt+') as o:
        olines = o.readlines()
        for line in olines:
            x1=int(line.split(',')[0])
            y1=int(line.split(',')[1])
            color=line.split(',(')[1].split(')')[0]
            r = int(color.split(',')[0])
            g = int(color.split(',')[1])
            blue = int(color.split(',')[2])
            color = (r,g,blue)
            print(x1,y1,color)
            b.setPixel(x1,y1,color)
    b.write(sys.argv[2])


if __name__ == '__main__':
  main()