import cv2

video_capture = cv2.VideoCapture(0)
anterior = 0

while True:
    if not video_capture.isOpened():
        print('Unable to load camera. Use the command "xhost +"')
        pass

    # Capture frame-by-frame
    ret, frame = video_capture.read()
    print(frame.shape)