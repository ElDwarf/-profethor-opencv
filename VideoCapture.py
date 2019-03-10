import cv2

#cap = cv2.VideoCapture("http://131.173.8.23/mjpg/video.mjpg")
cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read()
    if ret:
    	cv2.imwrite('videìto.mp4')
        cv2.imshow('video', frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()