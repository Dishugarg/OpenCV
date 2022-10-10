import cv2 as cv

img = cv.imread("Photos/cat.jpg")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
canny = cv.Canny(img, 125, 185)
contour, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
print(len(contour))
print(type(hierarchies))
cv.waitKey(0)

