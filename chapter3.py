import cv2
import numpy as np
#CHAPTER 3: Resizing and cropping

img=cv2.imread("Resources/lambo.png")
print(img.shape) #show image size

#resize image
imgResized=cv2.resize(img,(640,480)) #width x height
print(imgResized.shape)

#crop image
imgCropped=imgResized[200:400,400:600] #height x width
cv2.imshow("Image Cropped",imgCropped)

#cv2.imshow("Image Lambo",img)
cv2.imshow("Image resized",imgResized)
cv2.waitKey(0)
