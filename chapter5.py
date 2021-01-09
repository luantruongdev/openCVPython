import cv2
import numpy as np

#CHAPTER 5: WARP Perspective
#To extract one part of image
#in this code, we will try to extract the Card 11 of Heart

img=cv2.imread("Resources/card.jpg")
print(img.shape)

width,height=(250,350)

pts1=np.float32([[795,93],[1197,319],[464,753],[901,966]]) #define 4 point
pts2=np.float32([[0,0],[width,0],[0,height],[width,height]]) #say which point is which
matrix = cv2.getPerspectiveTransform(pts1,pts2) #transformation matrix
imgOutput=cv2.warpPerspective(img,matrix,(width,height))

cv2.imshow("Cards",img)
cv2.imshow("output",imgOutput)
cv2.waitKey(0)