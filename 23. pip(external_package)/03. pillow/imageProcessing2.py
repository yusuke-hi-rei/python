## Image reduction.

from PIL import Image

#! Exception processing is performed assuming
#! that the image file cannot be opened.

try:
    img1 = Image.open("image.jpg", "r")
    w, h = img1.size
    size = (int(w / 2), int(h / 2))
    img2 = img1.resize(size)
    img2.save("image_saved2.jpg", "JPEG")
    print("saved...")
except IOError as error:
    print(error)
