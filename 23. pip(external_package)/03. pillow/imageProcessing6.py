## Increase brightness.

from PIL import Image, ImageOps

#! Exception processing is performed assuming
#! that the image file cannot be opened.

try:
    img1 = Image.open("image.jpg", "r")
    bw_img = img1.convert("L")
    #! Dot brightness is doubled.
    img2 = img1.point(lambda p: p * 2.0)

    img2.save("image_luminance.jpg", "JPEG")
    print("saved...")
except IOError as error:
    print(error)

