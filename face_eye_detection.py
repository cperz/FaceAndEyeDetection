"""Face and Eye Detection using OpenCV HaarCascade classifiers and Tkinter"""

import os 
import cv2 #opencv 
import tkinter as tk #GUI
from tkinter import filedialog #for image upload


def detect_Face_Eyes(img_format, display=False): #function for image format
    try:
        if img_format.lower().endswith('.png'):#endswith format
            image = cv2.imread(img_format)
        elif img_format.lower().endswith(('.jpg','.jpeg')):
            image = cv2.imread(img_format)
    except Exception as e:
        raise e #if format doesn't match rasies error

    # image scaling
    h = image.shape[0]#height of image
    w = image.shape[1]#width of image
    
    if (w/h) > (1500/700):
        image = cv2.resize(image, (1500, int(h*1500/w)))#resizes if image is bigger
    else:
        image = cv2.resize(image, (int(w*700/h),700))
    #image scaling impacts detection, can adjust scaling to get better results

    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY).copy()#cv only needs grayscale to detect
    

    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_alt.xml')#haarcascade for faces
    eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')#haarcascade for eyes

    
    faces = face_cascade.detectMultiScale(gray_image, scaleFactor = 1.05, minNeighbors = 5, minSize = (40,40))#parameters help detection be more accurate                                   
    eyes = eye_cascade.detectMultiScale(gray_image, scaleFactor = 1.05, minNeighbors = 40, minSize = (10,10))#scaleFactor for faces and eyes by camera
    #minNeighbors considers near by objects before detecting

    print('Faces detected in the image: ', len(faces))
    print('Eyes detected in the image: ',len(eyes))


    for (x,y,w,h) in faces: #rectangle around face
        cv2.rectangle(image,(x,y), (x+w, y+h), (0,255,0),2)
        
        for (ex,ey,ew,eh) in eyes: #rectangle around eyes
            cv2.rectangle(image,(ex,ey), (ex+ew, ey+eh), (204,0,204),2)

        
    cv2.imshow('Face and Eye Detection', image)
    cv2.waitKey(0)#function to wait until user has enteracted with enivorment 
    cv2.destroyAllWindows()

def main():
    root = tk.Tk()# for filedialog
    root.withdraw()
    img_format = filedialog.askopenfilename(initialdir = './photos',title = 'Select an image', filetypes = (('JPEG','*.jpg;*.jpeg'),('PNG','*.png')))
    output= detect_Face_Eyes(img_format, display=True)
    
if __name__ == "__main__": main()
                                        

                                        
