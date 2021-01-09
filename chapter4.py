import cv2
import numpy as np

#CHAPTER 4: Draw Shapes, Lines and put Texts on Images

#show black Image
    #0 = black

img=np.zeros((512,512)) #matrix Zero with dim=512x512
#print(img)
print(img.shape)
#cv2.imshow("Image",img)

#colorize Image
img1=np.zeros((512,512,3),np.uint8) # 3 channels, of type unsigned integer 8 bits
print(img1)
    #img[height,width]
#img1[200:300,0:200]=255,0,0 #(255,0,0)=blue
cv2.imshow("Image1",img1)

#put line on image
img2=cv2.line(img1,(0,0),(300,300),(0,255,0),3) # (0,0): toa do diem bat dau, (300,300): toa do diem ket thuc
    #(0,255,0)=green
cv2.imshow("Put line on Image",img2)

img3=cv2.line(img1,(0,0),(img1.shape[1],img1.shape[0]),(0,255,0),3)
#img.shape[1]=width, img.shape[0]=height
cv2.imshow("Put full line",img3)

#put rectangle on image

cv2.rectangle(img1,(0,0),(250,350),(0,0,255),2)
cv2.imshow("Put rectangle",img1)

#put fully filled rectangle on image
cv2.rectangle(img1,(0,0),(250,350),(100,100,100),cv2.FILLED)  #(100,100,100) = BGR (RGB in openCV=BRG)
cv2.imshow("Put filled rectangle",img1)

#put circle on image
cv2.circle(img1,(400,100),30,(255,255,0),5) #(400,100) toa do cua tam duong tron, 30 la ban kinh duong tron
cv2.imshow("Put circle",img1)

#put Text on image
cv2.putText(img1,"OPENCV by Luan",(200,200),cv2.FONT_HERSHEY_COMPLEX,1,(0,150,0),2) # 1 is scale, 2 is thickness of text
cv2.imshow("Put text",img1)
cv2.waitKey(0)