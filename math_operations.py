import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

def show(img):
    plt.imshow(img)
    plt.show()

img = cv.imread("lena.jpg")
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
show(img)
print(img[55,55])

img[55,55] = np.array([0,0,0])
img[50:100, 100:250] = [255,255,255]

show(img)

img2 = cv.imread("lena.jpg")
img =  img*img2

show(img)

img2 = cv.imread("lena.jpg")
im =  img-img2

show(im)

img2 = cv.imread("lena.jpg")
im =  cv.add(img2,img)

show(im)