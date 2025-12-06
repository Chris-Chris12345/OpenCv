#Arithmatic operation on an image
import cv2
import numpy as np

image1 = cv2.imread("C:\OpenCV with python\L2\Pikachu.jpg")
image2 = cv2.imread("C:\OpenCV with python\L2\Pokemon.jpg")
image2 = cv2.resize(image2,(image1.shape[1],image1.shape[0]))

weighted_sum = cv2.addWeighted(image1,0.5,image2,0.5,0)
cv2.imshow("Weighted image", weighted_sum)

cv2.waitKey(0)
cv2.destroyAllWindows()