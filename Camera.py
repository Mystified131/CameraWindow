<<<<<<< HEAD
import cv2 as cv
 
capture = cv.VideoCapture(0)
 
while True:
    isTrue,frame = capture.read()
    cv.imshow('Video',frame)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
 
capture.release()
cv.destroyAllWindows()
=======
import cv2 as cv
 
capture = cv.VideoCapture(0)
 
while True:
    isTrue,frame = capture.read()
    cv.imshow('Video',frame)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
 
capture.release()
cv.destroyAllWindows()
>>>>>>> d5afd32200e948841f7274181de40d4be8ec639f
