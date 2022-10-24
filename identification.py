from PIL import Image, ImageDraw
import face_recognition
import cv2

path="keanu.jpg"
image=cv2.imread("test.jpg")
reevesImage=face_recognition.load_image_file(path)
reevesImageEncoding=face_recognition.face_encodings(reevesImage)[0]

testPath="test.jpg"
testImage=face_recognition.load_image_file(testPath)
faceLoc=face_recognition.face_locations(testImage)
faceEnc=face_recognition.face_encodings(testImage,faceLoc)

topLeftX=291
topLeftY=118
bottomRightX=513
bottomRightY=341

matchedFaces=face_recognition.compare_faces(reevesImageEncoding,faceEnc)
if True in matchedFaces:
    cv2.rectangle(image,(topLeftX,topLeftY),(bottomRightX,bottomRightY),(0,255,0),2)
    cv2.putText(image,"Keanu Reeves",(topLeftX,topLeftY),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0))
    cv2.imshow("Face Detection",image)
else:
    cv2.rectangle(image, (topLeftX, topLeftY), (bottomRightX, bottomRightY), (0, 255, 0), 2)
    cv2.putText(image, "Unknow", (topLeftX, topLeftY), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0))
    cv2.imshow("Face Detection", image)