import cv2 as cv
import utils

img = cv.imread('./Python/LearningOpenCv/lena.jpg')

cv.line(img, (0,0,), (150,150), (255,255,255), 5)

utils.imgShow(img)