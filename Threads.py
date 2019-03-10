from threading import Thread
from random import randint
import time,cv2
import hashlib
from collections import deque

class MyThread(object):
    def __init__(self):
        self.frame = deque(maxlen=5)

    def run(self):
        self.cap = cv2.VideoCapture(0)
        while(True):
            ret, lframe = self.cap.read()
            #print("LFRAME:",lframe)
            if ret:
                self.frame.append(lframe)

    def get_frame(self):
        try:
            return self.frame.popleft()
        except IndexError:
            return None

if __name__ == '__main__':
    myThreadOb1 = MyThread()
    th = Thread(target=myThreadOb1.run)
    th.start()
    while(True):
        image = myThreadOb1.get_frame()
        print("IMAGE:",image)
        if image:
            cv2.imshow('video', image)
        else:
            time.sleep(1)
            #import ipdb; ipdb.set_trace()
    myThreadOb1.join()
    cv2.destroyAllWindows()
    print('Main Terminating...')