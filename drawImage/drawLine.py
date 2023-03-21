import cv2 as cv
import utils

img = cv.imread('./Python/LearningOpenCv/lena.jpg')

#Imagem, coordenadas de inicio, coordenadas de fim, cor, expessura 
cv.line(img, (0,0), (150,150), (255,255,255), 2)

utils.imgShow(img)