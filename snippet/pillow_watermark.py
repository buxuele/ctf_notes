import sys
from PIL import ImageDraw, ImageFont, Image

"""
add water-mark to an image 
"""

def watermark_text(filename,text, pos):
    photo = Image.open(filename)
 
    # make the image editable
    drawing = ImageDraw.Draw(photo)
 
    black = (3, 8, 12)
    font = ImageFont.truetype("/usr/share/fonts/truetype/tlwg/Kinnari-BoldOblique.ttf", 40)
    drawing.text(pos, text, fill=black, font=font)
    photo.show()
    photo.save("newImage" + filename)
 
 
if __name__ == '__main__':
    img = 'a.jpg'
    watermark_text(img,
                   text='www.mousevspython.com',
                   pos=(0, 0))

