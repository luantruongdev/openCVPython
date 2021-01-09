import cv2
#numpy version 1.19.3
#opencv-python version 4.2.0.32
print("Package Imported")


#CHAPTER 1: Read Images Video Webcam

#import image
# img = cv2.imread("Resources/lena.png")
#
# cv2.imshow("Output",img)
# cv2.waitKey(0)

#import video
video=cv2.VideoCapture("Resources/test_video.mp4")

#video=cv2.VideoCapture(0) #0 for webcam
video.set(3,640) #set width of video, id 3
video.set(4,480) #set height of video, id 4

video.set(10,100) #set brightness of video, id 10

while True:
    success, img=video.read()
    cv2.imshow("This is video",img)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break






