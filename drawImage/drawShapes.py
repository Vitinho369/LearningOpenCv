import cv2 as cv
import utils
import numpy as np

img = cv.imread('./Python/LearningOpenCv/lena.jpg')

print(img.shape)
cv.rectangle(img, (0,50), (150,150), (255,255,0), 5)

cv.circle(img, (100,200), 20, (255,0,0), 5)

pts = np.array([[50,50], [120,130], [140,40], [150, 100]], np.int32)


cv.polylines(img, [pts], False, (0,255,0), 3)

utils.imgShow(img)