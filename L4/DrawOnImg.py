import cv2
import numpy as np

img = cv2.imread("C:\OpenCV with python\L4\Pikachu.jpg")

sp = (0,0)
size = (120,150)
thickness = 5
color = (225,200,75)

image = cv2.line(img,sp,size,color,thickness)
cv2.imshow("Line",image)

cv2.waitKey(0)
cv2.destroyAllWindows()

#Drawing a rectangle on the image
img = cv2.imread("C:\OpenCV with python\L4\Pikachu.jpg")

sp = (10,10)
size = (200,300)
thickness = 7
color = (150,250,100)

image = cv2.rectangle(img,sp,size,color,thickness)
cv2.imshow("Rect",image)

cv2.waitKey(0)
cv2.destroyAllWindows()

#Filled Rectangle
img = cv2.imread("C:\OpenCV with python\L4\Pikachu.jpg")

sp = (20,25)
size = (250,375)
thickness = -1 #-1 means fill the rectangle completly
color = (100,135,260)

image = cv2.rectangle(img,sp,size,color,thickness)
cv2.imshow("FilledRect",image)

cv2.waitKey(0)
cv2.destroyAllWindows()

#Draw a circle
img = cv2.imread("C:\OpenCV with python\L4\Pikachu.jpg")

centercoord = (150,250)
thickness = 10
radius = 100
color = (175,280,150)

image = cv2.circle(img,centercoord,radius,color,thickness)
cv2.imshow("Circle",image)

cv2.waitKey(0)
cv2.destroyAllWindows()

#Draw a filled circle
img = cv2.imread("C:\OpenCV with python\L4\Pikachu.jpg")

centercoord = (150,250)
thickness = -1
radius = 100
color = (100,300,150)

image = cv2.circle(img,centercoord,radius,color,thickness)
cv2.imshow("FilledCircle",image)

cv2.waitKey(0)
cv2.destroyAllWindows()

#Write a text on an image
img = cv2.imread("C:\OpenCV with python\L4\Pikachu.jpg")

font = cv2.FONT_HERSHEY_SIMPLEX
position = (300,350)
fontscale = 1
color = (300,0,300)
thickness = 3

image = cv2.putText(img,'OpenCV',position,font,fontscale,color,thickness,cv2.LINE_AA)
cv2.imshow("Text",image)

cv2.waitKey(0)
cv2.destroyAllWindows()