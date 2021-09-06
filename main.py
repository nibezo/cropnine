from cropping import cropping
from PIL import Image

im = Image.open("image.png")
width = im.width
height = im.height

if width == height:
    # call cropping function
    cropping("image.png")
else:
    print("Please, crop the image to a square.")
