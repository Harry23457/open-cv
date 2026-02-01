import cv2
"""
#Ing=cv2.imread("Lesson1/ant.jpg",cv2.IMREAD_COLOR)
Ing=cv2.imread("Lesson1/ant.jpg",cv2.IMREAD_GRAYSCALE)
cv2.imshow ("ant image",Ing)
cv2.waitKey(0)"""

ima2=cv2.imread("Lesson1/ant.jpg")
B, G, R =cv2.split(ima2)
cv2.imshow ("ant image",ima2)
cv2.waitKey(delay=5000)

cv2.imshow("Blue saturated image",B)
cv2.waitKey(delay=5000)

cv2.imshow("Green saturated image",G)
cv2.waitKey(delay=5000)

cv2.imshow("red saturated image",R)
cv2.waitKey(delay=5000)