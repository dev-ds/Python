# check if an image is made of single color

import cv2
import numpy as np
from collections import Counter

filename = '<Image name which you need to verify if its blank or filled with one color.>'

img = cv2.imread(filename)                         # Read Image
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)   # convert it to gray

colors = list(np.concatenate(img_gray).flat)       # merge the row pixels
color_count = Counter(colors)                      # count the colors

max_color = color_count.most_common(1)[0]          # Get Max populated color
all_colors = sum(color_count.values())             # Sum All colors

max_color_percentage = round((max_color[1]/all_colors) * 100, 2) # Get max color usage %

print(max_color_percentage, max_color[1], max_color[0]) # %, color count, color code. 0-black 255-white
