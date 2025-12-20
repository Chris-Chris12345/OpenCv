import cv2
import numpy as np

img1 = cv2.imread("C:\\OpenCV with python\\L3\\Pikachu.jpg")

img1[10,20] = [120,200,80]
(row,col) = img1.shape[0:2]
for i in range(row):
    for i2 in range(col):
        img1[i,i2] = sum(img1[i,i2]) * 0.33

cv2.imshow("GreyScale 1", img1)

cv2.waitKey(0)
cv2.destroyAllWindows()