import cv2

cap = cv2.VideoCapture('vid.mp4')
vid = []
src_FPS = 30
dest_FPS = 15


# https://appdividend.com/2022/03/19/python-cv2-videocapture/#:~:text=To%20capture%20a%20video%20in,for%20the%20second%20camera%2C%20etc.



def is_important():
    return False

while(cap.isOpened()):
    if (len(vid) % 500) == 0:
        print('Loading frame %i' % len(vid))
  
    # Skip frames to reach target framerate
    for i in range(int(src_FPS / dest_FPS)):
        ret, frame = cap.read()
    
    if frame is None:
        break
        
    vid.append(frame)
