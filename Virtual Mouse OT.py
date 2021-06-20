import cv2
import numpy as np
import wx
from pynput.mouse import Controller, Button

lower = np.array([130,86,36])  # Min HSV 
upper = np.array([154,216,255])

kernelOpen = np.ones((5,5))
kernelClose = np.ones((15,15))
openX, openY, openW, openH = 0,0,0,0
app = wx.App(False)
scrX, scrY = wx.GetDisplaySize()
frameR = 50
wCam = 640
camX = wCam - 2*frameR
hCam = 480
camY = hCam - 2*frameR
mouse = Controller()
pinch = 0
mLocOld = np.array([0,0])
mLocNew = np.array([0,0])
dampner = 2.75

cap = cv2.VideoCapture(1)
# "http://192.168.0.103:8080/video"
while True:
    success, img = cap.read() 
    # img = cv2.resize(
    # img,(320,240))
    # img = cv2.flip(img,1)
    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(imgHSV,lower,upper)
    imgres = cv2.bitwise_and(img,img,mask=mask)
    maskOpen = cv2.morphologyEx(mask, cv2.MORPH_OPEN,kernelOpen)
    maskClose = cv2.morphologyEx(maskOpen, cv2.MORPH_CLOSE,kernelClose)

    maskFinal = maskClose.copy()
    conts, h = cv2.findContours(maskFinal, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    # cv2.drawContours(img, conts, -1,(0,0,255),3)
    cv2.rectangle(img,(frameR, frameR), (wCam-frameR, hCam-frameR), (0,0,255),2)
    if len(conts)==2: 
        if pinch ==1:
            pinch=0
            mouse.release(Button.left)
        x1,y1,w1,h1 = cv2.boundingRect(conts[0])
        cx1, cy1 = x1+w1//2, y1+h1//2
        x2,y2,w2,h2 = cv2.boundingRect(conts[1])
        cx2, cy2 = x2+w2//2, y2+h2//2
        cx, cy = (cx1+cx2)//2, (cy1+cy2)//2
        cv2.rectangle(img,(x1,y1), (x1+w1,y1+h1),(0,0,255),2)
        cv2.rectangle(img,(x2,y2), (x2+w2,y2+h2),(0,0,255),2)
        cv2.line(img,(cx1,cy1), (cx2,cy2),(0,0,255),2)
        cv2.circle(img, (cx,cy), 2, (255,255,255), 2)
        if cx in range(frameR,wCam-frameR) and cy in range(frameR,hCam-frameR):
            cv2.rectangle(img,(frameR, frameR), (wCam-frameR, hCam-frameR), (0,255,0),2)
            mLocNew = mLocOld+((cx,cy)-mLocOld)/dampner
            x3 = np.interp(mLocNew[0],(frameR,wCam-frameR),(0,scrX))
            y3 = np.interp(mLocNew[1],(frameR,hCam-frameR),(0,scrY))
            mouse.position=(x3, y3)
            # if mouse.position != (x3,y3):
            #     pass
            mLocOld = mLocNew
        openX, openY, openW, openH = cv2.boundingRect(np.array([[x1,y1],[x1+w1,y1+h1],[x2,y2],[x2+w2,y2+h2]]))
        
    # For clicking
    elif len(conts)==1:
        x,y,w,h = cv2.boundingRect(conts[0])
        cv2.rectangle(img,(x,y), (x+w,y+h),(0,0,255),2) 
        cx, cy = x+w//2, y+h//2
        if pinch == 0:
            if abs((w*h-openW*openH)*100/(w*h))<30:
                pinch=1
                mouse.press(Button.left)
                openX, openY, openW, openH = 0,0,0,0
       
        else:
            cv2.circle(img, (cx,cy), ((w+h)//4), (0,255,255), 2)
            mLocNew = mLocOld+((cx,cy)-mLocOld)/dampner
            x1 = np.interp(mLocNew[0],(frameR,wCam-frameR),(0,scrX))
            y1 = np.interp(mLocNew[1],(frameR,hCam-frameR),(0,scrY))
            if cx in range(frameR,wCam-frameR) and cy in range(frameR,hCam-frameR):
                cv2.rectangle(img,(frameR, frameR), (wCam-frameR, hCam-frameR), (0,255,0),2)
                mouse.position = x1, y1
                # if mouse.position != (x1,y1):
                #     pass
            mLocOld = mLocNew

        # Display images
    cv2.imshow('Camera',img)
    # cv2.imshow('mask', mask)
    # cv2.imshow('result', imgres)
    # cv2.imshow('maskOpen',maskOpen)
    # cv2.imshow('maskClose',maskClose)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()








# ## Imported Libraries

# ## Declaration of global variables

# while True:
#     ## Logic for Object detection and tracking
#     :
#     :
    
#     if(len(conts)==2):
#         ## Logic for open gesture, moving mouse without click
#         :
#         :
#     elif(len(conts)==1):
#         ## Logic for close gesture, left button clicking
#         :
#         :
    
#     cv2.imshow('Camera',img)
#     if cv2.waitKey(1) & 0xFF==ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()

# app = wx.App(False)
# scrX, scrY = wx.GetDisplaySize()
# frameR = 50
# wCam = 640
# camX = wCam - 2*frameR
# hCam = 480
# camY = hCam - 2*frameR

# cv2.rectangle(img,(frameR, frameR), (wCam-frameR, hCam-frameR), (0,0,255),2)