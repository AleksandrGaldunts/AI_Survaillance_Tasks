import cv2
vid_capture = cv2.VideoCapture('image.mp4')
if (vid_capture.isOpened() == False):
    print("Error opening the video file")
else:
    fps = vid_capture.get(5)
    print('Frames per second : ', fps, 'FPS')

    frame_count = vid_capture.get(cv2.CAP_PROP_FRAME_COUNT)
    print('Frame count : ', frame_count)

    frame_width = vid_capture.get(3)
    print("frame width", frame_width)

while (vid_capture.isOpened()):
    ret, frame = vid_capture.read()
    if ret == True:
        cv2.imshow('Frame', frame)
        key = cv2.waitKey(20)

        if key == ord('q'):
            break
    else:
        break

vid_capture.release()
cv2.destroyAllWindows()