"""
import cv2
import numpy as np

img1 = cv2.imread("lesson2/journeyash.png")
img2 = cv2.imread("lesson2/pikachu.png")

weightsum = cv2.addWeighted(img1,0.5,img2,0.4,0)

cv2.imshow("weighted image",weightsum)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""
import cv2
import numpy as np

img1 = cv2.imread("lesson2/journeyash.png")
img2 = cv2.imread("lesson2/pikachu.png")

suv = cv2.subtract(img1,img2)
cv2.imshow("subtract image",suv)
cv2.waitKey(0)
cv2.destroyAllWindows()