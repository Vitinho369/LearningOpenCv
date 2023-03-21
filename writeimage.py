import cv2 as cv

img = cv.imread('./Python/opencv/lena.jpg', cv.IMREAD_GRAYSCALE)

print(img.shape)
print(img)
cv.imshow('Lena', img)
cv.waitKey(0)
cv.destroyAllWindows()

cv.imwrite('./Python/opencv/lena_gray.jpg', img)
