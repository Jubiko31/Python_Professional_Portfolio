import os
from PIL import Image

img = Image.open('imgs/test.png')
height, width = img.size

print(f"Before compress: {os.stat('imgs/test.png').st_size}")

compress = img.resize((height, width), Image.LANCZOS)
compress.save("imgs/test-compressed.png", optimize = True, quality = 10)

print(f"After compress: {os.stat('imgs/test-compressed.png').st_size}")
