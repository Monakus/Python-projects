import sys
from PIL import Image

img_path = sys.argv[1]
img = Image.open(img_path)
img = img.convert('L')  # convert to greyscale

width = img.size[0]
height = img.size[1]
new_width = 300
new_height = int(new_width/width * height * 0.5)
img = img.resize((new_width, new_height))

greyscale_chars = "@%#*+=-!:. "
pixels = img.getdata()
ascii_art = "".join([greyscale_chars[(pixel // 25)] for pixel in pixels])   # convert the pixels to ascii characters
ascii_art = "\n".join(ascii_art[i:i+new_width] for i in range(0, new_height*new_width, new_width))  # add new lines

name_to_save = "".join(img_path.split('\\')[-1].split('.')[0]) + "_greyscale.txt"    # get the name to save the file as
with open(name_to_save, "w") as f:
    print(ascii_art, file=f)
