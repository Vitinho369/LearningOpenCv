import cv2 as cv

def imgShow(img):
    cv.imshow('Image', img)
    cv.waitKey(0)
    cv.destroyAllWindows()