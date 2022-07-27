
import cv2
import matplotlib.pyplot as plt
import datetime
import os
import time


plt.style.use('seaborn')

cap = cv2.VideoCapture(1)
final2 = any
index = 1
def mouse_click(event, x, y,
                flags, param):
    global index
    if event == cv2.EVENT_LBUTTONDOWN:
        font = cv2.FONT_HERSHEY_TRIPLEX
        #cv2.imshow('image', img)
        path = 'D:/Photos/'
        date = str(datetime.datetime.now())
        ms = datetime.datetime.now()
        text = str(time.mktime(ms.timetuple())) + '.jpg'
        cv2.imwrite(os.path.join(path, text), final)

        cv2.imwrite(text, final2)
        index = index + 1

while (True):

    success, img = cap.read()
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_invert = cv2.bitwise_not(img_gray)
    img_smoothing = cv2.GaussianBlur(img_invert, (21, 21), sigmaX=0, sigmaY=0)
    final = cv2.divide(img_gray, 255 - img_smoothing, scale=255)
    final2 = final

    cv2.putText(img=final, text='Resim Kulubu Hatirasi 2022', org=(100, 50), fontFace=cv2.FONT_HERSHEY_COMPLEX, fontScale=1,
                color=(0, 255, 0), thickness=3)
    cv2.imshow('frame', final)

    cv2.setMouseCallback('frame', mouse_click)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


img.release()

cv2.destroyAllWindows()
