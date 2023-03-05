import cv2
import numpy as np

input_video = cv2.VideoCapture('p4_video3.avi')
result = cv2.VideoWriter('Problem_4_part_3.mp4',
                         cv2.VideoWriter_fourcc(*'MP4V'),
                         20, [960, 540])

while input_video.isOpened():
    ret, frame = input_video.read()

    if ret:
        originalFrame = frame
        RGBframe = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        framesize = np.shape(frame)
        rows = framesize[0]
        circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, rows / 60, param1=80, param2=60, minRadius=35,
                                   maxRadius=45)
        originalFrame = cv2.resize(originalFrame, [540, 540])
        cv2.imshow('original', originalFrame)
        if circles is not None:
            circles = np.uint16(np.around(circles))
            for i in circles[0, :]:
                center = (i[0], i[1])
                """check if piece is red, if it is, draw a blue circle"""
                if (frame[center[1], center[0], 0] < 20 and frame[center[1], center[0], 1] < 20 and frame[center[1], center[0], 2] > 130) or (frame[center[1]-15, center[0]-15, 0] < 20 and frame[center[1]-15, center[0]-15, 1] < 20 and frame[center[1]-15, center[0]-15, 2] > 130):
                    radius = i[2]
                    cv2.circle(frame, center, radius, (255, 0, 0), 3)
                elif (frame[center[1]+15, center[0]] > (150, 150, 150)).all():
                    """check if piece is white, if it is, draw a green circle"""
                    radius = i[2]
                    cv2.circle(frame, center, radius-2, (0, 255, 0), 3)

        frame = cv2.resize(frame, [960, 540])
        cv2.imshow('video', frame)
        result.write(frame)
    else:
        break
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
input_video.release()
cv2.destroyAllWindows()