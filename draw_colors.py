import cv2
import numpy as np
import os
import sys
import random

ROOT_FOLDER = sys.argv[1]
IMG_FOLDER = os.path.join(ROOT_FOLDER, 'frames')

img_name = os.path.join(IMG_FOLDER, 'img_0.jpg')
print('Read image:', img_name)

image = cv2.imread(img_name)

init_coordinates = (1420, 360)
radius = 40
delta = 2 * radius + 10
rows = 10
cols = 20
thickness = -1

for i in range(rows):
    for j in range(cols):
        if i == 0 and j == 0:
            color = (255, 255, 255)
        else:
            color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        center_coordinates = (init_coordinates[0] + delta * i, init_coordinates[1] + delta * j)
        image = cv2.circle(image, center_coordinates, radius, color, thickness)



cv2.namedWindow("image", cv2.WINDOW_NORMAL)
cv2.imshow("image", image)
cv2.imwrite(os.path.join(ROOT_FOLDER, 'test.jpg'), image)

cv2.waitKey(0)
cv2.destroyAllWindows()