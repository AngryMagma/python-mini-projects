from PIL import Image
import os
imgpos = input('Please enter the name of the image file that you want to process: ')
im = Image.open("E:\Python\Trys\image.png")
file = open("textimage.txt", "w")
im.convert("1").save("new _image.png")
img = Image.open('new _image.png')
width, height = img.size
pix = img.load()
for y in range(height):
    pval= ""
    for x in range(width):
        color = pix[x, y]
        if int(color) == 0 :
            pval = pval + "0"
        elif int(color) == 255 :
            pval = pval + "o"
        else :
            pval = pval + " "
    file.write(pval + "\n") 
os.remove('new _image.png')
