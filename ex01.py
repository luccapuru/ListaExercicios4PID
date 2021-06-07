import cv2
import numpy as np


def Roberts(img):
    kernelx = np.array([[1, 0],
                      [0, -1]])
    kernely = np.array([[0, -1],
                       [1, 0]])                 
    img1 = cv2.filter2D(img, -1, kernelx)
    img2 = cv2.filter2D(img, -1, kernely)
    # return cv2.convertScaleAbs(img1)+cv2.convertScaleAbs(img2)
    return img1+img2

def Prewitt(img):
    # kernelx = np.array([[1,1,1],
    #                    [0,0,0],
    #                    [-1,-1,-1]])
    # kernely = np.array([[-1,0,1],
    #                    [-1,0,1],
    #                    [-1,0,1]])
    kernelx = np.array([[-1,0,1],
                       [-1,0,1],
                       [-1,0,1]])
    kernely = np.array([[-1,-1,-1],
                       [0,0,0],
                       [1,1,1]])
    img1 = cv2.filter2D(img, -1, kernelx)
    img2 = cv2.filter2D(img, -1, kernely)
    return img1+img2

def Sobel(img):
    kernelx = np.array([[-1,0,1],
                       [-2,0,2],
                       [-1,0,1]])
    kernely = np.array([[-1,-2,-1],
                       [0,0,0],
                       [1,2,1]])
    img1 = cv2.filter2D(img, -1, kernelx)
    img2 = cv2.filter2D(img, -1, kernely)
    return img1+img2

def Laplace(img):
    # kernel = np.array([[0,-1,0],
    #                    [-1,4,-1],
    #                    [0,-1,0]])
    kernel = np.array([[-1,-4,-1],
                       [-4,20,-4],
                       [-1,-4,-1]])
    return cv2.filter2D(img, -1, kernel)

img = cv2.imread("images//cubo.jpg", 0)
# img = cv2.imread("images//bolas.jpg", 0)
imgRob = Roberts(img)
imgPrew = Prewitt(img)
imgSob = Sobel(img)
imgLap = Laplace(img)

cv2.imshow("Resultado - Roberts", imgRob)
cv2.imshow("Resultado - Prewitt", imgPrew)
cv2.imshow("Resultado - Sobel", imgSob)
cv2.imshow("Resultado - Laplace", imgLap)

cv2.imwrite("results//ex01ROberts.jpg", imgRob)
cv2.imwrite("results//ex01Sobel.jpg", imgSob)
cv2.imwrite("results//ex01Prewitt.jpg", imgPrew)
cv2.imwrite("results//ex01Laplace.jpg", imgLap)
cv2.waitKey()
