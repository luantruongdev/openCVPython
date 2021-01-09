import cv2
import numpy as np

#CHAPTER 2: Basic function

img=cv2.imread("Resources/lena.png")

#convert to gray scale
imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

cv2.imshow("Gray Image",imgGray)
#cv2.waitKey(0)

#blur image
imgBlur=cv2.GaussianBlur(imgGray,(11,11),0) # 7,7 or 3,3 or 5,5 ksize=kernel size, it has to be odd number
cv2.imshow("Blur Image",imgBlur)
#cv2.waitKey(0)

#find the Edge of Image using Canny edge detector
imgCanny=cv2.Canny(img,150,150) #150 150 are values of threshold
cv2.imshow("Canny edge detector Image",imgCanny)
#cv2.waitKey(0)

#Image Dialation = make image thicker
kernel=np.ones((5,5),np.uint8) #create matrix of 1, type of value is unsigned integer of 8 bits (0 to 255)
imgDialition=cv2.dilate(imgCanny,kernel,iterations=2) #kernel is just a matrix that we need to define the size and the value
cv2.imshow("Dialation Image",imgDialition)
#cv2.waitKey(0)

#Image Erosion = make image thinner
imgEroded=cv2.erode(imgDialition,kernel,iterations=2)
cv2.imshow("Erosion Image",imgEroded)
cv2.waitKey(0)