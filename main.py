from cropping import cropping, check_size
from PIL import Image

if check_size(Image.open("image.png")):
    # call cropping function
    cropping("image.png")
else:
    print("Please, crop the image to a square.")
