import sys
from PIL import Image

img = Image.open(sys.argv[1]).convert('L')  # open the image and convert it to grayscale
new_width = 300
new_height = int(new_width/img.size[0] * img.size[1] * 0.5)
img = img.resize((new_width, new_height))   # resize the image maintaining the ascpet ratio

greyscale_chars = "@%#*+=-!:. "
pixels = img.getdata()
ascii_art = "".join([greyscale_chars[(pixel // 25)] for pixel in pixels])   # convert the pixel to ascii characters
ascii_art = "\n".join(ascii_art[i:i+new_width] for i in range(0, new_height*new_width, new_width))  # add new lines

name = "".join(sys.argv[1].split('\\')[-1].split('.')[0]) + "_greyscale.txt"    # get the name to save the file as
with open(name, "w") as f:
    print(ascii_art, file=f)
