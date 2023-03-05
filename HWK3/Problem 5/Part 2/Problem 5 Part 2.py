import cv2
import numpy as np

input_video = cv2.VideoCapture('p5_video3.avi')
result = cv2.VideoWriter('Problem_5_part_2_answer_c.mp4',
                         cv2.VideoWriter_fourcc(*'MP4V'),
                         20, [540, 540])
frameCount, previousFrame = 0, 0
previousCenters = 0
motionLines = np.zeros([0, 4])
while input_video.isOpened():

    ret, originalFrame = input_video.read()

    if not ret:
        break

    originalFrameEdited = originalFrame.copy()
    frameSize = np.shape(originalFrame)
    gray = cv2.cvtColor(originalFrame, cv2.COLOR_BGR2GRAY)
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, frameSize[1] / 60, param1=80, param2=60, minRadius=35,
                               maxRadius=45)

    """This whole if statement is tracking if circle centers have moved an appreciable distance from their previous location.
    If they have, a line is drawn."""
    if circles is not None:
        circles = np.uint16(np.around(circles))
        centers = circles[0, :, 0:2]
        centersUnedited = centers.copy()
        if frameCount == 0:
            previousCenters = centers
        elif frameCount > 0:
            if np.shape(centers) == np.shape(previousCenters):
                for i in range(np.shape(previousCenters)[0]):
                    for j in range(np.shape(centers)[0]):
                        if np.linalg.norm(previousCenters[i]/1000 - centers[j]/1000)*1000 < 10:
                            previousCenters[i] = [0, 0]
                            centers[j] = [0, 0]
                for i in range(np.shape(centers)[0]):
                    if (centers[i] != [0, 0]).any():
                        previousCenter = previousCenters[np.nonzero(previousCenters)]
                        newLine = np.array([[centers[i][0], centers[i][1], previousCenter[0], previousCenter[1]]])
                        motionLines = np.append(motionLines, newLine, 0)
                        print('line made')
            previousCenters = centersUnedited
    if np.shape(motionLines)[0] > 0:
        for line in range(np.shape(motionLines)[0]):
            originalFrameEdited = cv2.line(originalFrameEdited, (int(motionLines[line, 0]), int(motionLines[line, 1])), (int(motionLines[line, 2]), int(motionLines[line, 3])), (255, 0, 0), 3)
    originalFrameResized = cv2.resize(originalFrame, [540, 540])
    editedFrameResized = cv2.resize(originalFrameEdited, [540, 540])

    cv2.imshow('original', originalFrameResized)
    cv2.imshow('lines', editedFrameResized)
    k = cv2.waitKey(1) & 0xff
    if k == 27:
        break

    frameCount += 1
    result.write(editedFrameResized)
input_video.release()
cv2.destroyAllWindows()
