'''
this application is video capture example
'''

import numpy as np
import cv2
from timer import Timer

timer = Timer()
timer.start()
cap = cv2.VideoCapture(0)
timer.end()
print "initialization elapsed : " + str(timer.elapsed())

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()