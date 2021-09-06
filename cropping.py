from PIL import Image


def check_size(image):
    """Check size of the image. If not square, return False"""
    im = image.open("image.png")
    width = im.width
    height = im.height
    if width == height:
        return True
    else:
        return False


def cropping(image):
    """Cropping image into 9 parts"""

    im = Image.open(image)
    x = 0
    y = 0
    x2 = im.width
    y2 = im.height

    """Divide a square into 3 vertical parts"""

    # [1, 0, 0] of im
    cropped1 = im.crop((x, y, x2/3, y2))
    # [0, 1, 0] of im
    cropped2 = im.crop((x2/3, y, x2/3 * 2, y2))
    # [0, 0, 1] of im
    cropped3 = im.crop((x2/3 * 2, y, x2, y2))

    """The second part of cropping using cropped1"""

    # 1/9 of im
    im1 = cropped1.crop((x, y, x2/3, y2/3))
    im1.save('cropped/im1.png')

    # 2/9 of im
    im2 = cropped1.crop((x, y + y2/3, x2/3, y2/3 * 2))
    im2.save('cropped/im4.png')

    # 3/9 of im
    im3 = cropped1.crop((x, y + y2/3 * 2, x2/3, y2))
    im3.save('cropped/im7.png')

    """The third part of cropping using cropped2"""

    # 4/9 of im
    im4 = cropped2.crop((x, y, x2/3, y2/3))
    im4.save('cropped/im2.png')

    # 5/9 of im
    im5 = cropped2.crop((x, y + y2/3, x2/3, y2/3 * 2))
    im5.save('cropped/im5.png')

    # 6/9 of im
    im6 = cropped2.crop((x, y + y2/3 * 2, x2/3, y2))
    im6.save('cropped/im8.png')

    """The third part of cropping using cropped3"""

    # 7/9 of im
    im7 = cropped3.crop((x, y, x2/3, y2/3))
    im7.save('cropped/im3.png')

    # 8/9 of im
    im8 = cropped3.crop((x, y + y2/3, x2/3, y2/3 * 2))
    im8.save('cropped/im6.png')

    # 9/9 of im
    im9 = cropped3.crop((x, y + y2/3 * 2, x2/3, y2))
    im9.save('cropped/im9.png')
