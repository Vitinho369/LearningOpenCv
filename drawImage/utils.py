import cv2 as cv

def imgShow(img):
    cv.imshow('image', img)
    cv.waitKey(0)
    cv.destroyAllWindows()