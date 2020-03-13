import cv2
import os

from datetime import date
from datetime import datetime

now = datetime.now()

def extractFrames(pathIn, pathOut):
    os.mkdir(pathOut)
 
    cap = cv2.VideoCapture(pathIn)
    count = 0
 
    while (cap.isOpened()):
 
        # Capture frame-by-frame
        ret, frame = cap.read()
 
        if ret == True:
            cv2.imshow('Original',frame)
            print('Read %d frame: ' % count, ret)
            dt_string = now.strftime("%d_%m_%Y_%H_%M_%S")
            cv2.imwrite(os.path.join(pathOut, "frame_{:d}.jpg".format(dt_string), frame)  # save frame as JPEG file with timestamp
            count += 1
            # Wait for 'a' key to stop the program  
            if cv2.waitKey(1) & 0xFF == ord('a'): 
                break
        else:
            break
 
    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()
 
def main():
    extractFrames(0, 'data')
 
if __name__=="__main__":
    main()