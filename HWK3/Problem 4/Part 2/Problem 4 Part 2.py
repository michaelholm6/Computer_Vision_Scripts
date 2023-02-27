import cv2
import numpy as np
from matplotlib import pyplot as plt

input_video = cv2.VideoCapture('p4_video2.avi')
result = cv2.VideoWriter('Problem_4_part_1.avi',
                         cv2.VideoWriter_fourcc(*'MJPG'),
                         20, [960, 540])
triangleCoords = [138, 272, 420, 561, 707, 847, 1117, 1255, 1397, 1541, 1683, 1829]
boardLines = {'topLine': 416, 'bottomLine': 680, 'centerLine': 982}
pieceCounts = [[[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
               [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]]
centerCount = [0, 0]

while input_video.isOpened():
    pieceCounts = [[[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
                   [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]]
    centerCount = [0, 0]
    ret, frame = input_video.read()

    if ret:
        originalFrame = frame
        RGBframe = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        frameSize = np.shape(frame)
        rows = frameSize[0]
        circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, rows / 25, param1=80, param2=60, minRadius=35,
                                   maxRadius=45)
        originalFrame = cv2.resize(originalFrame, [540, 540])
        cv2.imshow('original', originalFrame)
        if circles is not None:
            circles = np.uint16(np.around(circles))
            for i in circles[0, :]:
                center = (i[0], i[1])
                if (frame[center[1], center[0], 0:1] < [20, 20]).all() and frame[center[1], center[0], 2] > 130 or \
                        (frame[center[1]-15, center[0]-15, 0:1] < [20, 20]).all() and frame[center[1]-15, center[0]-15, 2] > 130:
                    radius = i[2]
                    cv2.circle(frame, center, radius, (255, 0, 0), 3)
                    if center[1] not in range(boardLines['topLine'], boardLines['bottomLine']):
                        if center[1] < boardLines['topLine']:
                            location = 0
                        else:
                            location = 1
                        for coord in range(len(triangleCoords)):
                            if center[0] in range(triangleCoords[coord] - 15, triangleCoords[coord] + 15):
                                pieceCounts[location][coord][0] += 1
                    elif center[0] in range(boardLines['centerLine'] - 5, boardLines['centerLine'] + 5):
                        centerCount[0] += 1
                elif (frame[center[1], center[0]] > (200, 200, 200)).all():
                    radius = i[2]
                    cv2.circle(frame, center, radius-2, (0, 255, 0), 3)
                    if center[1] not in range(boardLines['topLine'], boardLines['bottomLine']):
                        if center[1] < boardLines['topLine']:
                            location = 0
                        else:
                            location = 1
                        for coord in range(len(triangleCoords)):
                            if center[0] in range(triangleCoords[coord]-15, triangleCoords[coord]+15):
                                pieceCounts[location][coord][1] += 1
                    elif center[0] in range(boardLines['centerLine'] - 15, boardLines['centerLine'] + 15):
                        centerCount[0] += 1
        plt.imshow(RGBframe)
        plt.show()
        frame = cv2.resize(frame, [960, 540])
        cv2.imshow('video', frame)
        result.write(frame)
    else:
        break
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
input_video.release()
cv2.destroyAllWindows()