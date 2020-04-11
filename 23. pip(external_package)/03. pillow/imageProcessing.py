from PIL import Image

#! Exception processing is performed assuming
#! that the image file cannot be opened.

try:
    img1 = Image.open("image.jpg", "r")
    #! Rotate the image.
    #! (expand: Automatic image size adjustment.)
    img2 = img1.rotate(90, expand=True)
    img2.save("image_saved.jpg", "JPEG")
    print("saved...")
except IOError as error:
    print(error)
