from cv2 import * # initialize the camera 
from PIL import Image 
cam = VideoCapture(0) # 0 -> index of camera 
s, img = cam.read() 
if s: # frame captured without any errors namedWindow("cam-test",CV_WINDOW_AUTOSIZE) 
    imshow("cam-test",img) 
    waitKey(0) 
    destroyWindow("cam-test") 
    imwrite("test.jpg",img) #save image

    img = Image.open('test.jpg')
    
    img.show() 

