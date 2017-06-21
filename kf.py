import struct
from PIL import Image
im = Image.open('picture.jpeg')
pix = im.load()
print im.size
width = im.size[0]
print width
height = im.size[1]
print height
from PythonMagick import Image as Im
bilde = Im(('%dx%d'%(width,height)),'#12ff21')
print bilde.size
print pix[0,0]
for x in range(width):
    for y in range(height):
        if pix[x,y][1]>40 and pix[x,y][2]>60 and pix[x,y][0]>20:
            pix[x,y] = ((pix[x,y][2]),(pix[x,y][0]),(pix[x,y][1]))
        else:
            pix[x,y]=(0,0,0)
        bilde.pixelColor(x,y,("#%s"%(struct.pack('BBB',*pix[x,y][:3]).encode('hex'))))
bilde.write('filtrs4.jpeg')
