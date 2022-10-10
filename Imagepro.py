import cv2 as cv
import numpy as ns


def compress(x):
    pass


def imageprocess(x):
    img = cv.imread(x)
    cv.imshow(x,img)
    cv.waitKey(0)
    y = input()

