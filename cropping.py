from PIL import Image


def check_size(image):
    """Check size of the image. If not square, return False"""
    width = image.width
    height = image.height
    if width == height:
        return True
    else:
        return False


def cropping(image):
    """Cropping image into 9 parts"""

    image = Image.open(image)
    x = image.width
    k = 1  # for cropped images naming
    for i in range(1, 4):
        for j in range(1, 4):
            cropped = image.crop(((x/3)*(j-1), (x/3)*(i-1), (x/3)*j, (x/3)*i))
            cropped.save("cropped/im"+str(k)+".png")
            k += 1
