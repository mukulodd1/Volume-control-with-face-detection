import cv2
import vlc,time

pl = vlc.MediaPlayer('anml.mp3')
pl.play()
v = cv2.VideoCapture(0)
fd = cv2.CascadeClassifier(r'C:\Users\Mukul\AppData\Local\Programs\Python\Python37\Lib\site-packages\cv2\data\haarcascade_frontalface_alt.xml')

while True:
    r,i = v.read()
    #i[50:80, 50:80, :]=0  
    #print(i)
   
    j = cv2.cvtColor(i,cv2.COLOR_BGR2GRAY)

    face = fd.detectMultiScale(j,1.3,7)
    #print("number of faces : ",str(len(face)))
    
    for(x,y,w,h) in face:
        cv2.rectangle(i,(x,y),(x+w,y+h),(0,0,0),-1)
        cv2.imshow('its_odd',i)
    var =0

    if(len(face)>0):
        var = (face[0][2])*(face[0][3])
        pl.audio_set_volume(int(100 - (var/37000)*100))
        #print(int(100 - (var/37000)*100))
    k = cv2.waitKey(1)    

    if(k==ord('q')):
        cv2.destroyAllWindows()
        v.release()
        break
