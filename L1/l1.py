import cv2

image = cv2.imread("C:\OpenCV with python\L1\Pikachu.jpg",cv2.IMREAD_COLOR)
cv2.imshow("Pikachu image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Read and display the image in gray scale

import cv2
image = cv2.imread("C:\OpenCV with python\L1\Pikachu.jpg",0)

cv2.imshow("GrayScale image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()


import cv2
import os
saved_directory = "C:\OpenCV with python"
image = cv2.imread("C:\OpenCV with python\L1\Pikachu.jpg",cv2.IMREAD_COLOR)
cv2.imshow("Saved image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

#print image in different colors

image = cv2.imread("C:\OpenCV with python\L1\Pikachu.jpg",1)
B,G,R = cv2.split(image)
cv2.imshow("Original image", image)
cv2.waitKey(0)

cv2.imshow("Blue image", B)
cv2.waitKey(0)

cv2.imshow("Green image", G)
cv2.waitKey(0)

cv2.imshow("Red image", R)
cv2.waitKey(0)
cv2.destroyAllWindows()