import cv2
import math

video=cv2.VideoCapture("bb3.mp4")

# load the tracker
tracker=cv2.TrackerCSRT_create()
# print(tracker)

# tracker should take the first frame in video
returned,myImage=video.read()
#print(myImage)

bbox=cv2.selectROI("Tracking",myImage,False)
print("The bbox is: ",bbox)

p1=520
p2=300

newX=[]
newY=[]

goalReached=False


# init the tracker
tracker.init(myImage,bbox)

def drawBox(myImage,myBox):
    x,y,w,h=int(myBox[0]),int(myBox[1]),int(myBox[2]),int(myBox[3])

    cv2.rectangle(myImage,(x,y),(x+w,y+h),(0,255,0),2)
    cv2.putText(myImage,"Tracking",(100,100),cv2.FONT_HERSHEY_COMPLEX,0.7,(000,255,255),1)

def goalTracker(myImage,bbox):
    global goalReached
    x,y,w,h=int(myBox[0]),int(myBox[1]),int(myBox[2]),int(myBox[3])
    #Goal point
    cv2.circle(myImage,(p1,p2),3,(255, 0, 0),2)

    c1=x+int(w/2)
    c2=y+int(h/2)

    #center of box
    
    cv2.circle(myImage,(c1,c2),3,(255, 0, 0),2)

    #distance between 2 points(goal to bbox center)
    distance=math.sqrt(((c1-p1)**2)+((c2-p2)**2))
    print("the distance is:",distance)

    newX.append(c1)
    newY.append(c2)

    if distance>35 and goalReached==False:
     for i in range(len(newX)):
         cv2.circle(myImage,(newX[i],newY[i]),2,(0,255,0),2)

    if distance<=30:

        goalReached=True

        cv2.putText(myImage,"Goal Reached",(200,100),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
    

 

while True:
    dummy,frame=video.read()

    success,myBox= tracker.update(frame)
    
 
    # print(myBox)

    if(success==True):
        drawBox(frame,myBox)
    else:
        cv2.putText(frame,"Lost Object",(100,100),cv2.FONT_HERSHEY_COMPLEX,0.7,(000,255,255),1)

    goalTracker(frame,myBox)


    cv2.imshow("object tracking",frame)
    if cv2.waitKey(25)==32:                         
        break
video.release()
cv2.release()
cv2.destroyAllWindows()            