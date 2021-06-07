import cv2
import numpy as np

def Limiar(img, limiar):
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            if img[i][j] >= limiar:
                img[i][j] = 255
            else:
                img[i][j] = 0

img = cv2.imread("images//all_souls_000026.jpg", 0)
# img = cv2.imread("images//cubo.jpg", 0)
limiar = input("Digite o valor do Limiar: ")
Limiar(img, int(limiar))
img1 = cv2.GaussianBlur(img,(5,5),0)
ret,th = cv2.threshold(img1,float(limiar),255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

cv2.imshow("Imagem Limiarizada", img)
cv2.imshow("Imagem Limiarizada de Otsu", th)
cv2.imwrite("results//ex03.jpg", img)
cv2.imwrite("results//ex04.jpg", th)
cv2.waitKey()