## Gives an effect to the image.

from PIL import Image, ImageOps

#! Exception processing is performed assuming
#! that the image file cannot be opened.

try:
    img1 = Image.open("image.jpg", "r")
    img2 = ImageOps.posterize(img1, 1)
    img3 = ImageOps.equalize(img1)
    img4 = ImageOps.invert(img1)

    img2.save("image_savedPoster.jpg", "JPEG")
    img3.save("image_savedEqual.jpg", "JPEG")
    img4.save("image_savedInvert.jpg", "JPEG")
    print("saved...")
except IOError as error:
    print(error)
