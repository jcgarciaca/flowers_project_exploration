import cv2
import numpy as np
import os
import sys

# ROOT_FOLDER = os.path.join(os.path.dirname(sys.path[0]), 'images')
ROOT_FOLDER = sys.argv[1]
IMG_FOLDER = os.path.join(ROOT_FOLDER, 'frames')

image_hsv = None
pixel = (20,60,80)

# mouse callback function
def pick_color(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        pixel = image_hsv[y,x]

        upper =  np.array([pixel[0] + 10, pixel[1] + 10, pixel[2] + 40])
        lower =  np.array([pixel[0] - 10, pixel[1] - 10, pixel[2] - 40])
        print(pixel, lower, upper)

        image_mask = cv2.inRange(image_hsv,lower,upper)
        cv2.namedWindow("mask", cv2.WINDOW_NORMAL)
        cv2.imshow("mask", image_mask)

def main():
    import sys
    global image_hsv, pixel

    img_name = os.path.join(IMG_FOLDER, 'test.jpg')
    print('Read image:', img_name)
    
    image_src = cv2.imread(img_name)
    if image_src is None:
        print ("the image read is None............")
        return
    cv2.namedWindow("bgr", cv2.WINDOW_NORMAL)
    cv2.imshow("bgr", image_src)

    cv2.namedWindow('hsv', cv2.WINDOW_NORMAL)
    cv2.setMouseCallback('hsv', pick_color)

    image_hsv = cv2.cvtColor(image_src,cv2.COLOR_BGR2HSV)
    cv2.namedWindow("hsv", cv2.WINDOW_NORMAL)
    cv2.imshow("hsv",image_hsv)

    save = False
    if save:
        cv2.imwrite(os.path.join(ROOT_FOLDER, 'hsv.jpg'), image_hsv)
        cv2.imwrite(os.path.join(ROOT_FOLDER, 'bgr.jpg'), image_src)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__=='__main__':
    main()
