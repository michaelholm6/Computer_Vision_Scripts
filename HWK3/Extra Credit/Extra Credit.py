import cv2
import numpy as np

input_video = cv2.VideoCapture('Checkers_video_2.mp4')
result = cv2.VideoWriter('Extra_credit_2.mp4',
                         cv2.VideoWriter_fourcc(*'MP4V'),
                         10, [540, 540])
frameCount, previousCenters = 0, 0
radius = 55

while input_video.isOpened():
    ret, originalFrame = input_video.read()

    """Skipping every other frame because for some frames the checkers don't actually move. This made
    the blue pieces have weird blinking going on."""
    if frameCount % 2 == 0:

        if not ret:
            break
        originalFrameEdited = originalFrame.copy()
        originalFrameEditedCropped = originalFrameEdited[270:1312, 601:1649, :]
        frameSize = np.shape(originalFrameEditedCropped)
        gray = cv2.cvtColor(originalFrameEditedCropped, cv2.COLOR_BGR2GRAY)
        circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, frameSize[1] / 80, param1=80, param2=30, minRadius=radius - 5,
                                   maxRadius=radius + 5)

        """This area tracks where circle are moving each frame, and if a circle has moved an appreciable distance
        it is checked if it's red. If it's red, a blue circle is made."""
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
                            if np.linalg.norm(previousCenters[i]/1000 - centers[j]/1000)*1000 < 9:
                                previousCenters[i] = [0, 0]
                                centers[j] = [0, 0]
                    for i in range(np.shape(centers)[0]):
                        if (centers[i] != [0, 0]).any() and (originalFrameEditedCropped[centers[i, 1], centers[i, 0], 0:2] < [10]).all() and originalFrameEditedCropped[centers[i, 1], centers[i, 0], 2] > 170:
                            cv2.circle(originalFrameEditedCropped, centers[i], radius + 3, (255, 0, 0), -1)
                previousCenters = centersUnedited

        originalFrameResized = cv2.resize(originalFrame, [540, 540])
        originalFrameEditedCroppedResized = cv2.resize(originalFrameEditedCropped, [540, 540])

        cv2.imshow('original', originalFrameResized)
        cv2.imshow('circles', originalFrameEditedCroppedResized)

        k = cv2.waitKey(1) & 0xff
        if k == 27:
            break
        result.write(originalFrameEditedCroppedResized)
    frameCount += 1
input_video.release()
cv2.destroyAllWindows()
