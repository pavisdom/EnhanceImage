import cv2
import numpy as np

# Load image, grayscale, Gaussian blur, threshold
image = cv2.imread('test.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
x, y, w, h = cv2.boundingRect(gray)
print(x,y,w,h)
img_h, img_w, _ = image.shape
img = cv2.imread('test.jpeg')

img = cv2.resize(img, (img_h, img_w), interpolation = cv2.INTER_CUBIC)

color = (0, 255, 0)
thickness = 2
# dimensions = img.shape
#
# print("dimensions",dimensions)

cv2.rectangle(img, (x,y), (x+w,y+h), color, thickness)
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# blur = cv2.GaussianBlur(gray, (3,3), 0)
# thresh = cv2.threshold(blur, 220, 255, cv2.THRESH_BINARY_INV)[1]
#
# # Find contours
# cnts = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# cnts = cnts[0] if len(cnts) == 2 else cnts[1]
# c = max(cnts, key=cv2.contourArea)
#
# # Obtain outer coordinates
# left = tuple(c[c[:, :, 0].argmin()][0])
# right = tuple(c[c[:, :, 0].argmax()][0])
# top = tuple(c[c[:, :, 1].argmin()][0])
# bottom = tuple(c[c[:, :, 1].argmax()][0])

# Draw dots onto image
# cv2.drawContours(image, [c], -1, (36, 255, 12), 2)
# cv2.circle(image, left, 8, (0, 50, 255), -1)
# cv2.circle(image, right, 8, (0, 255, 255), -1)
# cv2.circle(image, top, 8, (255, 50, 0), -1)
# cv2.circle(image, bottom, 8, (255, 255, 0), -1)
#
# print('left: {}'.format(left))
# print('right: {}'.format(right))
# print('top: {}'.format(top))
# print('bottom: {}'.format(bottom))
# cv2.imshow('thresh', thresh)
cv2.namedWindow("Resized_Window", cv2.WINDOW_NORMAL)

cv2.imshow('Resized_Window', img)
cv2.waitKey()