from PIL import Image, ImageFilter, ImageEnhance, ImageOps, ImageDraw
from PIL.ImageFilter import (
   BLUR, CONTOUR, DETAIL, EDGE_ENHANCE, EDGE_ENHANCE_MORE,
   EMBOSS, FIND_EDGES, SMOOTH, SMOOTH_MORE, SHARPEN
)
import os

cwd = os.getcwd()
image = Image.open('aging-man.jpg')
image = image.filter(SHARPEN)
enhancer = ImageEnhance.Brightness(image)
image = enhancer.enhance(1.2)

size = (1100, 1100)
mask = Image.new('L', size, 0)
draw = ImageDraw.Draw(mask) 
draw.ellipse((0, 0) + size, fill=255)

image = image.filter(SMOOTH_MORE)
enhancer = ImageEnhance.Contrast(image)
image = enhancer.enhance(0.9)
image = image.filter(DETAIL)

image = ImageOps.fit(image, mask.size, centering=(0.7, 0.5))
image.putalpha(mask)

image.save('NewMan.png', quality = 100)
image.show()
