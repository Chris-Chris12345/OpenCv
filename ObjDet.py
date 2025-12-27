import cv2
import numpy as np
import math

img = cv2.imread("C:\OpenCV with python\ObjDetection\Coin1.jpeg")


h, w = img.shape[:2]
center = (w // 2, h // 2)
outer_radius = 100
inner_radius = 40


points = []
for i in range(10):
    angle = i * math.pi / 5  # 36° steps
    r = outer_radius if i % 2 == 0 else inner_radius
    x = int(center[0] + r * math.sin(angle))
    y = int(center[1] - r * math.cos(angle))
    points.append((x, y))

star_points = np.array(points, np.int32)
cv2.fillPoly(img, [star_points], color=(0, 255, 255))

cv2.imshow("Star on Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
