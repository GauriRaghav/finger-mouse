import cv2 #to capture
import mediapipe as mp #to detect movements
import pyautogui #for functioning

# cv2 In-use
cap = cv2.VideoCapture(0)
hand_detector = mp.solutions.hands.Hands()
drawing_utils=mp.solutions.drawing_utils
screen_width, screen_height=pyautogui.size()
index_y=0

if not cap.isOpened():
    print("ERROR!: couldn't open video stream")
    
    
while True:
   _, frame=cap.read(); 
   frame=cv2.flip(frame,1)
   frame_height, frame_width,_=frame.shape
   rgb_frame=cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
   output = hand_detector.process(rgb_frame)
   hands=output.multi_hand_landmarks
   if hands:
       for hand in hands:
           drawing_utils.draw_landmarks(frame,hand)
           landmarks=hand.landmark
           for id, landmark in enumerate(landmarks):
               x=int(landmark.x*frame_width)
               y=int(landmark.y*frame_height)
               
               # for index finger
               if id==8:
                   cv2.circle(img=frame,center=(x,y), radius=16, color=(255,0,0))
                   index_x=screen_width/frame_width*x
                   index_y=screen_height/frame_height*y
                   pyautogui.moveTo(index_x,index_y)
                 
               # for thumb
               if id==4:
                   cv2.circle(img=frame,center=(x,y), radius=16, color=(255,0,0))
                   thumb_x=screen_width/frame_width*x
                   thumb_y=screen_height/frame_height*y  
                   print('outside',int(abs(index_y-thumb_y))) 
                   if abs(index_y-thumb_y)<=35:
                       pyautogui.click()
                       pyautogui.sleep(0.4)           
           
   cv2.imshow('MyMouse',frame)
   cv2.waitKey(1)