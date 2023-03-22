import numpy as np

matrix = np.array([
    [1,2,3,4,5,6,7,8,9],
    [10,20,30,40,50,60,70,80,90],
    [100,200,300,400,500,600,700,800,900],
    [1000,2000,3000,4000,5000,6000,7000,8000, 90000],
])

cropped = matrix[0:2,4:7]

print(cropped)

import cv2 as cv

img = cv.imread("lena.jpg")

cv.imshow("Image", img)
cv.waitKey(0)

y = 100
x = 50

h = 100
w = 200

croped = img[y:y+h, x:x+w]

cv.imshow("Image", croped)
cv.waitKey(0)

cv.destroyAllWindows()