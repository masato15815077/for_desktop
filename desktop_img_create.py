import cv2
import numpy as np
import argprase

"""
This is the program that creates a cany image as wallpaper.
The image will be binary-color, edge-only, 1440*810px from left-top. 
"""

#Acitvate argparse, and add the first cmd arg.
parser = argprase.ArgmentParser()
parser.add_argument('origin_image')
args = parser.parse_args()
print(args.origin_image)

img = cv2.imread(origin_image)

roi = img[0:810, 0:1440]

#cv2.imwrite('images/crop.jpg', roi)
cv2.imshow('image', roi)
cv2.waitKey(0)
cv2.destroyAllWindows()
