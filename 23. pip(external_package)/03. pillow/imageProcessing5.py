## Sepia tone.

from PIL import Image, ImageOps

#! Exception processing is performed assuming
#! that the image file cannot be opened.

try:
    img1 = Image.open("image.jpg", "r")
    bw_img = img1.convert("L")
    #! colorize requires a grayscale image in advance.
    #! An exception will be raised if you colorize the image in color.
    img2 = ImageOps.colorize(bw_img,
                             black = (0, 0, 0),
                             white = (255, 200, 150))
    img2.save("image_sepiatone.jpg", "JPEG")
    print("saved...")
except IOError as error:
    print(error)
