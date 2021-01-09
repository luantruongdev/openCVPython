import cv2
import numpy as np

#CHAPTER 8: CONTOUR, BOUNDING LINE, CORNER POINT and SHAPE

#Stack function
def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver

# create get Contour function
def getContours(img):

    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    # cv2.RETR_EXTERNAL is retrieval mode, it retrieves the extreme outer contour, we can use different mode here

    #cv2.CHAIN_APPROX_NONE is where we can use different method of openCV
    #to request for compressed values or it will reduce the point for you
    #in this case, we're gonna get all the contour, so we use CHAIN_APPROX_NONE

    # One we have our contour, they're stocked in the contours variable

    # We 're gonna loop through our contour, for each contour, we're gonna find the edge of it (we find the are of
                                                                                                # each contour)
    for cnt in contours:
        area=cv2.contourArea(cnt)
        print("Area:",area)

        #we draw them to see them clearly
        #cv2.drawContours(imgContour,cnt,-1,(255,0,0),3) #-1 cuz we want to draw all contour

        #Next, check for the minimum area, so we will give it a threshold
        #cuz, it's a good idea to give a minimum threshold for the area, so that it will not detect any noise
        if area>0:
            cv2.drawContours(imgContour, cnt, -1, (255, 0, 0), 3)

            #next, we calculate the Curve Length, Curve Length helps us approximate the corner of our shape
            peri=cv2.arcLength(cnt,True)
            print("Curve Length:",peri)

            #Next we want to know how many corner point we have, so 3 = 3 corner = triangle, 4 = 4 corner = rectangle
            approx=cv2.approxPolyDP(cnt,0.02*peri,True) #0.02*peri is epsilon = resolution
            print("Approximation:",len(approx))
            objCorner=len(approx)

            #Next, we create a bounding box around the detected object.
            #If we gonna create a bounding box around our object, what will be the X&Y and width and height

            x, y, w, h=cv2.boundingRect(approx)

            if objCorner==3: objectType = "Tri"
            elif objCorner==4:
                aspRatio= w/float(h)
                if aspRatio>0.95 and aspRatio < 1.05: objectType = "Square"
                            #deviation of 5%
                else: objectType="Rectangle"
            elif objCorner>4: objectType= "Circles"
            else:objectType="None"

            cv2.rectangle(imgContour,(x,y),(x+w,y+h),(255,255,255),2)
                #From the bounding boxes, we can get information such as what is the total width and height of object,
                #or what is the center point of object, these can be useful in another project

            cv2.putText(imgContour,objectType,
                            (x+(w//2)-10,y+(h//2)-10),cv2.FONT_HERSHEY_COMPLEX,0.6,
                            (0,0,0),2)



path="Resources/shape1.png"
img=cv2.imread(path)
imgContour=img.copy()

# first need to convert it to GrayScale
imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# Next, go Blur
imgBlur=cv2.GaussianBlur(imgGray,(7,7),1) # bigger sigma = more blur

#Next, find the Edge of Image using Canny edge detector
imgCanny=cv2.Canny(imgBlur,50,50)

#create image Blank with Numpy
imgBlank=np.zeros_like(img)

getContours(imgCanny)


imgStack=stackImages(0.8,([img,imgGray,imgBlur],
                          [imgCanny,imgContour,imgBlank]))

cv2.imshow("Image Stack",imgStack)
cv2.waitKey(0)