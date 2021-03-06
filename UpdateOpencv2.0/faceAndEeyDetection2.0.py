import cv2

#Github: https://github.com/sujitmandal

#This programe is create by Sujit Mandal

"""
Github: https://github.com/sujitmandal
This programe is create by Sujit Mandal
LinkedIn : https://www.linkedin.com/in/sujit-mandal-91215013a/
Facebook : https://www.facebook.com/sujit.mandal.33671748
Twitter : https://twitter.com/mandalsujit37
"""

face = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye = cv2.CascadeClassifier('haarcascade_eye.xml')
video = cv2.VideoCapture(0)



while True:

    check, frame = video.read()
    print(frame)

    faces = face.detectMultiScale(frame)
    eyes = eye.detectMultiScale(frame)

    
    for(x, y, w, h) in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 3)
        for (x, y, w, h) in eyes:
            cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0), 3)
    
    
    cv2.imshow("frame",frame)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break

video.release()
cv2.destroyAllWindows()