import cv2

print(cv2.__version__)
dispW=800
dispH=600

cam = cv2.VideoCapture('/dev/video0')
cam.set(cv2.CAP_PROP_FRAME_WIDTH, dispW)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, dispH)
W=cam.get(cv2.CAP_PROP_FRAME_WIDTH)
H=cam.get(cv2.CAP_PROP_FRAME_HEIGHT)
print(f'Width: {int(W)}, Height: {int(H)}')

while True:
    ret, frame = cam.read()
    cv2.imshow('XavierCam', frame)
    cv2.moveWindow('XavierCam', 0,0)
    if cv2.waitKey(1)==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()
