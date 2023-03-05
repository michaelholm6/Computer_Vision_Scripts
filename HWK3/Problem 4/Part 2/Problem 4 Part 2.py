import cv2
import numpy as np

input_video = cv2.VideoCapture('p4_video3.avi')
result = cv2.VideoWriter('Problem_4_part_3.mp4',
                         cv2.VideoWriter_fourcc(*'MP4V'),
                         20, [960, 540])
triangleCoords = [138, 272, 420, 561, 707, 847, 1117, 1255, 1397, 1541, 1683, 1829]
verticalCoords = [420, 674]
boardLines = {'topLine': 416, 'bottomLine': 680, 'centerLineVertical': 982, 'centerLineHorizontal': 529}
pieceCounts = [[[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
               [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]]
centerCount = [0, 0]
"""initiating a game state, and defining geometry across the board"""
while input_video.isOpened():
    pieceCounts = [[[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
                   [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]]
    centerCount = [0, 0]
    ret, frame = input_video.read()

    if ret:
        originalFrame = frame
        originalFrame = cv2.resize(originalFrame, [540, 540])
        cv2.imshow('original', originalFrame)
        RGBframe = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        frameSize = np.shape(frame)
        rows = frameSize[0]
        circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, rows / 60, param1=80, param2=60, minRadius=35,
                                   maxRadius=45)
        """Basically, this whole if statement figures out where circles are on the board. Using the geometry defined
        earlier, this is binning the different pieces into the different key areas on the board. It's then writing this
        on every video frame."""
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
                    elif center[0] in range(boardLines['centerLineVertical'] - 5, boardLines['centerLineVertical'] + 5):
                        centerCount[0] += 1
                elif (frame[center[1], center[0]] > (150, 150, 150)).all() or (frame[center[1] - 15, center[0] - 15] > (150, 150, 150)).all():
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
                    elif center[0] in range(boardLines['centerLineVertical'] - 15, boardLines['centerLineVertical'] + 15):
                        if (frame[center[1], center[0]] > (200, 200, 200)).all() or (frame[center[1] - 15, center[0] - 15] > (200, 200, 200)).all():
                            centerCount[1] += 1
                        elif (frame[center[1], center[0], 0:1] < [20, 20]).all() and frame[center[1], center[0], 2] > 130 or \
                         (frame[center[1]-15, center[0]-15, 0:1] < [20, 20]).all() and frame[center[1]-15, center[0]-15, 2] > 130:
                            centerCount[0] += 1
        for verticalLocation in range(len(pieceCounts)):
            for horizontalLocation in range(len(pieceCounts[0])):
                if pieceCounts[verticalLocation][horizontalLocation][0] != 0:
                    pieceCountWrite = str(pieceCounts[verticalLocation][horizontalLocation][0]) + 'r'
                elif pieceCounts[verticalLocation][horizontalLocation][1] != 0:
                    pieceCountWrite = str(pieceCounts[verticalLocation][horizontalLocation][1]) + 'w'
                else:
                    pieceCountWrite = ' '
                cv2.putText(frame, pieceCountWrite, [triangleCoords[horizontalLocation], verticalCoords[verticalLocation]], cv2.FONT_HERSHEY_PLAIN, 3, (255, 255, 0), 3)
        if centerCount[0] != 0:
            centerCountWrite = str(centerCount[0]) + 'r'
            cv2.putText(frame, centerCountWrite, [boardLines['centerLineVertical'], boardLines['centerLineHorizontal']],
                        cv2.FONT_HERSHEY_PLAIN, 3, (255, 255, 0), 3)
        elif centerCount[1] != 0:
            centerCountWrite = str(centerCount[1]) + 'w'
            cv2.putText(frame, centerCountWrite, [boardLines['centerLineVertical'], boardLines['centerLineHorizontal']],
                        cv2.FONT_HERSHEY_PLAIN, 3, (255, 255, 0), 3)
        frame = cv2.resize(frame, [960, 540])
        cv2.imshow('video', frame)
        result.write(frame)
    else:
        break
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
input_video.release()
cv2.destroyAllWindows()