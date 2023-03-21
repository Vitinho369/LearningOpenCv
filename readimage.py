import cv2 as cv

img = cv.imread('./Python/LearningOpenCv/lena.jpg')


print(img)
print(img.shape)
print(type(img))


cv.imshow('Lena', img)
cv.waitKey(0)
cv.destroyAllWindows()