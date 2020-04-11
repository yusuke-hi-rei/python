## Convert to monochrome.

from PIL import Image

#! Exception processing is performed assuming
#! that the image file cannot be opened.

try:
    img1 = Image.open("image.jpg", "r")
    #! L: grayscale.
    img2 = img1.convert("L")
    img2.save("image_saved3.jpg", "JPEG")
    print("saved...")
except IOError as error:
    print(error)
