#!/usr/bin/env python
# coding: utf-8

# In[9]:


import cv2
import mediapipe as mp

cap = cv2.VideoCapture(0)
mpDraw= mp.solutions.drawing_utils

mpPose=mp.solutions.pose
pose=mpPose.Pose()

mpHands = mp.solutions.hands
hands=mpHands.Hands(
    model_complexity=0,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5)


# In[10]:


tipId=[8,12,16,20]
point2=[7,11,15,19]
point3=[6,10,14,18]
knuckles=[5,9,13,17]
noseId=0
eyesId=[5,2]
mouthId=[9,10]
shouldersId=[12,11]


# In[11]:


def find_gesture(nose,eyes,mouth,lmList,shoulders,lengthLandmarks,handTypes,results_pose):
    text='nothing'
    if(lengthLandmarks==1):
    
    
         
                        
            
            
        #...................insult..............................
        if(text=='nothing'):
            if(eyes[0][1]<=lmList[7][2]<=nose[1]+20 and eyes[1][1]<=lmList[7][2]<=nose[1]+20 ):
                flag=True
                for knuckle_points,tip2_points in zip(knuckles,point2):
                    if knuckle_points==5:
                        continue
                    elif(lmList[knuckle_points][2]>lmList[tip2_points][2] or lmList[knuckle_points][1]<lmList[tip2_points][1]):
                    
                        flag=False
                if not(results_pose.pose_landmarks.landmark[8].x * w<=lmList[8][1]<=results_pose.pose_landmarks.landmark[1].x * w):
                    flag=False
                
                
                if(flag):
                    text='insult'
        #...............................die.........................................................................................
        if(text=='nothing'):
            if(mouth[0][1]<=lmList[12][2]<=shoulders[0][1]  and  mouth[1][1]<=lmList[12][2]<=shoulders[0][1] and mouth[0][1]<=lmList[12][2]<=shoulders[1][1]
              and mouth[1][1]<=lmList[12][2]<=shoulders[1][1]):
                flag=True
                for tip_points,point2_points,point3_points,knuckle_points in zip(tipId,point2,point3,knuckles):
                    if(lmList[tip_points][1]>lmList[point2_points][1] or lmList[point2_points][1]>lmList[point3_points][1] 
                        or lmList[point3_points][1]>lmList[knuckle_points][1]):
                        flag=False
                if (lmList[17][2]-lmList[5][2]>2*(lmList[17][2]-lmList[9][2])):
                    flag=False
                if(flag):
                    text='die'
        #........................lie.........................................................................................
        if(text=='nothing'):
            if(eyes[0][1]<=lmList[4][2]<=nose[1] and  eyes[1][1]<=lmList[4][2]<=nose[1] and -30<=lmList[4][1]-nose[0]<=30):
                flag=True
                for tip_points,point2_points,point3_points,knuckle_points in zip(tipId,point2,point3,knuckles):
                    if(lmList[tip_points][2]>lmList[point2_points][2] or  lmList[point2_points][2]>lmList[point3_points][2]
                       or lmList[point3_points][2]>lmList[knuckle_points][2]):
                        flag=False
                if(lmList[4][2]<results_pose.pose_landmarks.landmark[1].y * h or lmList[4][2]<results_pose.pose_landmarks.landmark[4].y * h):
                    flag=False
                if(flag):
                    text='lie'
        #...........................pain....................................................................................
        if(text=='nothing'):
            if(shoulders[1][1]<=lmList[4][2] and shoulders[0][1]<=lmList[4][2] and shoulders[1][1]<=lmList[20][2] and shoulders[0][1]<=lmList[20][2]):
                flag=True
                if(lmList[8][2]>lmList[12][2] or lmList[12][2]>lmList[16][2] or lmList[16][2]>lmList[20][2] ):
                   
                    flag=False
                for tip_points,point2_points,point3_points,knuckle_points in zip(tipId,point2,point3,knuckles):
                    
                    if(lmList[tip_points][1]>lmList[point2_points][1]  or lmList[point2_points][1]>lmList[point3_points][1] or lmList[point3_points][1]>lmList[knuckle_points][1] 
                       or not(-15<=lmList[tip_points][1]-lmList[point2_points][1]<=15)):
                       
                        flag=False
                if(flag):
                    text='pain'
        #............................................want......................................................................
        if(text=='nothing'):
            if(shoulders[0][1]<=lmList[12][2] and shoulders[1][1]<lmList[12][2]):
                flag=True
                for tip_points,point2_points,point3_points,knuckle_points in zip(tipId,point2,point3,knuckles):
                        if(lmList[tip_points][2]>lmList[point2_points][2] or lmList[point2_points][2]>lmList[point3_points][2] or 
                           lmList[point3_points][2]>lmList[knuckle_points][2] or lmList[knuckle_points][2]-lmList[point3_points][2]>70 
                          or not(-10<=lmList[tip_points][1]-lmList[point2_points][1]<=10)):
                            flag=False
               
                if(flag):
                    text='want'
        #...................................trouble....................................................................
        if(text=='nothing'):
            flag=True
            for tip_points in tipId:
                if(not(lmList[tip_points][1]<results_pose.pose_landmarks.landmark[7].x * w and lmList[tip_points][1]>results_pose.pose_landmarks.landmark[8].x * w)):
                    flag=False
                if(lmList[tip_points][2]>nose[1]):
                    flag=False
            if(flag):
                text='trouble'
        #...............................tease........................................................................
        if(text=='nothing'):
            flag=True
            for tip_points,point2_points,point3_points,knuckle_points in zip(tipId,point2,point3,knuckles):
                    if tip_points==8:
                        if(lmList[tip_points][1]>lmList[point2_points][1] or lmList[point2_points][1]>lmList[point3_points][1]
                          or lmList[point3_points][1]>lmList[knuckle_points][1]):
                            flag=False
                    else:
                        if(lmList[tip_points][1]<lmList[point2_points][1] or lmList[point2_points][1]<lmList[point3_points][1]):
                            flag=False
                            
            if(lmList[4][1]>lmList[3][1]):
                flag=False
            for tip_points in tipId:
                if(lmList[tip_points][2]<shoulders[0][1] or lmList[tip_points][2]<shoulders[1][1]  ):
                    flag=False
            if(flag):
                text='tease'
        #.................................hope............................................................................
        if(text=='nothing'):
            flag=True
            for tip_points,point2_points,point3_points,knuckle_points in zip(tipId,point2,point3,knuckles):
                if tip_points==8:
                    if(lmList[tip_points][2]>lmList[point2_points][2] or lmList[point2_points][2]>lmList[point3_points][2] or lmList[point3_points][2]>lmList[knuckle_points][2] ):
                        flag=False
                       
                else:
                    if(lmList[point2_points][1]>lmList[point3_points][1]):
                        flag=False
                       
            if(lmList[8][2]>results_pose.pose_landmarks.landmark[3].y * h):
                flag=False
                
            if(flag):
                text='hope'
                
        #..............................good................................................................................
        if(text=='nothing'):
            flag=True
            
            for tip_points,point2_points,point3_points,knuckle_points in zip(tipId,point2,point3,knuckles):
                if(tip_points==8):
                    if(lmList[tip_points][2]<lmList[point2_points][2] or lmList[point2_points][2]<lmList[point3_points][2]):
                        flag=False
                else:
                    if(lmList[tip_points][2]>lmList[point2_points][2] or lmList[point2_points][2]>lmList[point3_points][2] or lmList[point3_points][2]>lmList[knuckle_points][2] ):
                        flag=False
            #if(lmList[4][1]>lmList[3][1]):
                #flag=False

            if(flag):
                text='good'
        #............................................blind...........................................................
        if(text=='nothing'):
           
            flag=True
            if(lmList[8][2]>nose[1] or lmList[12][2]>nose[1]):
                flag=False
            for tip_points in tipId:
                if lmList[tip_points][2]< eyes[0][1] or lmList[tip_points][2]<eyes[1][1]:
                    flag=False
            for tip_poits,point2_points in zip(tipId,point2):
                if(tip_points==8 or tip_points==12):
                    if(lmList[tip_points][2]>lmList[point2_points][2]):
                        flag=False
                else:
                    if(lmList[tip_points][2]<lmList[point2_points][2]):
                        flag=False
                
                
            if(flag):
                text='blind'
                
                     
            
                
        
         
                        
    elif(lengthLandmarks==2):
        if(shoulders[0][1]<lmList[0][2] and shoulders[1][1]<lmList[0][2] and shoulders[0][1]<lmList[21][2] and shoulders[1][1]<lmList[21][2]):
            #.......................fear.............................................................................................
            if(text=='nothing'):
                count=0
                flag=True
                
                for tip_points,point2_points,point3_points,knuckle_points in zip(tipId,point2,point3,knuckles):
                    if count==0:
                        
                        if(lmList[tip_points][2]<lmList[point2_points][2] or lmList[point2_points][2]<lmList[point3_points][2]
                          or lmList[point3_points][2]<lmList[knuckle_points][2] or not(-60<=lmList[knuckle_points][1]-lmList[point3_points][1]<=60)):
                            flag=False
                    elif count==1:
                         if(lmList[tip_points+21][2]<lmList[point2_points+21][2] or lmList[point2_points+21][2]<lmList[point3_points+21][2]
                          or lmList[point3_points+21][2]<lmList[knuckle_points+21][2] or not(-60<=lmList[knuckle_points+21][1]-lmList[point3_points+21][1]<=60)):
                            flag=False
                    count+=1
                if(flag):
                    text='fear'
            
            if(text=='nothing'):
        
                
                flag=True
                #................cold......................................................................................
                for i in (0,1):
                    for tip_points,point2_points,point3_points,knuckle_points in zip(tipId,point2,point3,knuckles):
                        if(handTypes[i]=='Left'):
                            if(i==0):
                                if(lmList[tip_points][1]>lmList[point2_points][1] or lmList[point2_points][1]>lmList[point3_points][1] 
                                  or lmList[point3_points][1]<lmList[knuckle_points][1]):
                                    flag=False
                            elif(i==1):
                                 if(lmList[tip_points+21][1]>lmList[point2_points+21][1] or lmList[point2_points+21][1]>lmList[point3_points+21][1] 
                                  or lmList[point3_points+21][1]<lmList[knuckle_points+21][1]):
                                    flag=False
                        
                        
                                
                        elif(handTypes[i]=='Right'):
                            if(i==0):
                                if(lmList[tip_points][1]<lmList[point2_points][1] or lmList[point2_points][1]<lmList[point3_points][1] 
                                  or lmList[point3_points][1]>lmList[knuckle_points][1]):
                                    flag=False
                            elif(i==1):
                                 if(lmList[tip_points+21][1]<lmList[point2_points+21][1] or lmList[point2_points+21][1]<lmList[point3_points+21][1] 
                                  or lmList[point3_points+21][1]>lmList[knuckle_points+21][1]):
                                    flag=False
                        

                if(lmList[4][2]<lmList[1][2] and lmList[25][2]<lmList[22][2]):
                    flag=False
                if(flag):
                    text='cold'
            #..................wedding...........................................................................................
            if(text=='nothing'):
                flag=True
                for i in (0,1):
                    for tip_points,point2_points,point3_points,knuckle_points in zip(tipId,point2,point3,knuckles):
                        if(handTypes[i]=='Left'):
                            if(i==0):
                                if(lmList[tip_points][1]<lmList[point2_points][1] or lmList[point2_points][1]<lmList[point3_points][1] 
                                  or lmList[point3_points][1]<lmList[knuckle_points][1]):
                                    flag=False
                            elif(i==1):
                                 if(lmList[tip_points+21][1]<lmList[point2_points+21][1] or lmList[point2_points+21][1]<lmList[point3_points+21][1] 
                                  or lmList[point3_points+21][1]<lmList[knuckle_points+21][1]):
                                    flag=False
                        
                        
                                
                        elif(handTypes[i]=='Right'):
                            if(i==0):
                                if(lmList[tip_points][1]>lmList[point2_points][1] or lmList[point2_points][1]>lmList[point3_points][1] 
                                  or lmList[point3_points][1]>lmList[knuckle_points][1]):
                                    flag=False
                            elif(i==1):
                                 if(lmList[tip_points+21][1]>lmList[point2_points+21][1] or lmList[point2_points+21][1]>lmList[point3_points+21][1] 
                                  or lmList[point3_points+21][1]>lmList[knuckle_points+21][1]):
                                    flag=False
                if(lmList[8][2]<shoulders[0][1] or lmList[12][2]<shoulders[0][1] or lmList[16][2]<shoulders[0][1] or lmList[20][2]<shoulders[0][1]
                  or lmList[29][2]<shoulders[0][1] or lmList[33][2]<shoulders[0][1] or lmList[37][2]<shoulders[0][1] or lmList[41][2]<shoulders[0][1]):
                    flag=False
                        

                
                if(flag):
                    text='wedding'
            #...................thank you...........................................................................
            if(text=='nothing'):
                flag=True
                count=0
                for tip_points,point2_points,point3_points,knuckle_points in zip(tipId,point2,point3,knuckles):
                        if(count==0):
                            if(lmList[tip_points][2]>lmList[point2_points][2] or lmList[point2_points][2]>lmList[point3_points][2]
                              or lmList[point3_points][2]>lmList[knuckle_points][2]):
                                flag=False
                        elif(count==1):
                             if(lmList[tip_points+21][2]>lmList[point2_points+21][2] or lmList[point2_points+21][2]>lmList[point3_points+21][2]
                              or lmList[point3_points+21][2]>lmList[knuckle_points+21][2]):
                                flag=False
                                
                        count+=1
                        
                if not(nose[1]<lmList[12][2]<shoulders[0][1] or nose[1]<lmList[12][2]<shoulders[1][1] or nose[1]<lmList[33][2]<shoulders[0][1] or nose[1]<lmList[33][2]<shoulders[1][1] or
                  -60<=lmList[12][1]-lmList[33][1]<=60):
                    flag=False
                if(flag):
                    text='Thank you'
                        
                
                    

           
                    
            
                        
    return (text)


# In[12]:


while True:
    ret,frame=cap.read()
    frame=cv2.flip(frame,1)
    framergb=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    

    h,w,c=frame.shape
    frame.flags.writeable = False
    results = hands.process(framergb)
    results_pose=pose.process(framergb)
    
    
    
    if results_pose.pose_landmarks:
        
        #mpDraw.draw_landmarks(frame,results_pose.pose_landmarks,mpPose.POSE_CONNECTIONS)
        
        nose=[results_pose.pose_landmarks.landmark[0].x * w,results_pose.pose_landmarks.landmark[0].y * h]
       
        eyes=[[results_pose.pose_landmarks.landmark[5].x * w,results_pose.pose_landmarks.landmark[5].y * h],
              [results_pose.pose_landmarks.landmark[2].x * w,results_pose.pose_landmarks.landmark[2].y * h]]
        mouth=[[results_pose.pose_landmarks.landmark[9].x * w,results_pose.pose_landmarks.landmark[9].y * h],
               [results_pose.pose_landmarks.landmark[10].x * w,results_pose.pose_landmarks.landmark[10].y * h]]
        shoulders=[[results_pose.pose_landmarks.landmark[12].x * w,results_pose.pose_landmarks.landmark[12].y * h],
               [results_pose.pose_landmarks.landmark[11].x * w,results_pose.pose_landmarks.landmark[11].y * h]]
        
    if results.multi_hand_landmarks:
        lengthLandMarks=len(results.multi_hand_landmarks)
      
        handTypes=[]       
        frame.flags.writeable = True
        count=0
        lmList=[]
        
        for handLms in results.multi_hand_landmarks:
            
            handType=results.multi_handedness[count].classification[0].label
            handTypes.append(handType)
           
            
            
            count+=1
           
            for id,lm in enumerate(handLms.landmark):
                
                cx,cy=int(lm.x*w),int(lm.y*h)
                lmList.append([id,cx,cy])
                    
                  
            #mpDraw.draw_landmarks(frame,handLms,mpHands.HAND_CONNECTIONS)
            
            
            
            if count==1:
                cv2.putText(frame,handType,(lmList[11][1],lmList[11][2]+5),2,1,(255,0,0),1,1)
            if count==2:
                cv2.putText(frame,handType,(lmList[31][1],lmList[11][2]+5),2,1,(255,0,0),1,1)
        if len(lmList)==21 or len(lmList)==42:
            
            text=find_gesture(nose,eyes,mouth,lmList,shoulders,lengthLandMarks,handTypes,results_pose)
        cv2.putText(frame,text,(25,25),2,1,(255,0,0),1,1)
        
    
        #for lndmrk in mpPose.PoseLandmark:
            #print(lndmrk)
     
     
                
    
               
    cv2.imshow('frame',frame)
    
            
                    
             
              
    # Flip the image horizontally for a selfie-view display.
        
        
    if cv2.waitKey(1) & 0xFF == 27:
        break
cap.release()
cv2.destroyAllWindows()


# In[ ]:





# In[ ]:




