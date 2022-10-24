import cv2
import face_recognition
path="ylm.png"
image=cv2.imread(path)
faceLocations=face_recognition.face_locations(image)
color=(0,255,0)
pt1_0=(145,146)
pt2_0=(235,245)
pt1_1=(402,128)
pt2_1=(509,235)
cv2.rectangle(image,pt1_0,pt2_0,color)
cv2.rectangle(image,pt1_1,pt2_1,color)
cv2.imsow("ylm",image)