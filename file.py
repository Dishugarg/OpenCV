import numpy as np

import cv2 as cv


def rotate1(img, angle, rotationpoint):
    (height, width) = img.shape[:2]
    if rotationpoint is None:
        rotationpoint = (width // 2, height // 2)
    rotMat = cv.getRotationMatrix2D(rotationpoint, angle, 2.0)
    dimensions = (width, height)
    return cv.warpAffine(img, rotMat, dimensions)


def rotate(img, angle, rotationpoint):
    (height, width) = img.shape[:2]
    if rotationpoint is None:
        rotationpoint = (width // 2, height // 2)
    rotMat = cv.getRotationMatrix2D(rotationpoint, angle, 1.0)
    dimensions = (width, height)
    return cv.warpAffine(img, rotMat, dimensions)

def translate(img, x, y):
    transmat = np.float32([[1, 0, x], [0, 1, y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transmat, dimensions)


img = cv.imread('Photos/cat.jpg')
cv.imshow('cat', img)
# translation
# translated = translate(img, 100, 100)
# cv.imshow('translated', translated)
# rotated

rotated = rotate(img, 90, None)
cv.imshow('rotated', rotated)
rotated1 = rotate1(img, 90, None)
cv.imshow('rotated1', rotated1)
cv.waitKey(0)

