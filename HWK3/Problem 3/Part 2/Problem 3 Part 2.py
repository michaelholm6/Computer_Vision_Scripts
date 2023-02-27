import cv2
import numpy as np

input_video = cv2.VideoCapture('p3_video1.avi')
result = cv2.VideoWriter('Problem_3_part_2.avi',
                        cv2.VideoWriter_fourcc(*'MJPG'),
                        20, [960, 540])

while input_video.isOpened():
    ret, frame = input_video.read()

    if ret:
        originalFrame = frame
        RGBframe = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        framesize = np.shape(frame)
        if (originalFrame[567, 402] != [62, 150, 218]).any():
            for i in range(280, 562):
                for j in range(535, 601):
                    if frame[j, i, 2] > 160 and frame[j, i, 0] > 90:
                        frame[j, i] = [0, 0, 255]
        originalFrame = cv2.resize(originalFrame, [540, 540])
        cv2.imshow('original', originalFrame)
        frame = cv2.resize(frame, [960, 540])
        cv2.imshow('video', frame)
        result.write(frame)
    else:
        break
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
input_video.release()
cv2.destroyAllWindows()