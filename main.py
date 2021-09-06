from PIL import Image

im = Image.open("im.png")
x = 0
y = 0
x2 = im.width
y2 = im.height

# [1, 0, 0] of im
cropped1 = im.crop((x, y, x2/3, y2))
cropped1.show()

# [0, 1, 0] of im
cropped2 = im.crop((x2/3, y, x2/3 * 2, y2))
cropped2.show()

# [0, 0, 1] of im
cropped3 = im.crop((x2/3 * 2, y, x2, y2))
cropped3.show()
