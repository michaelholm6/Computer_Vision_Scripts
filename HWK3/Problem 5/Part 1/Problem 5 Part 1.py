import cv2
import numpy as np

input_video = cv2.VideoCapture('p5_video1.avi')
result = cv2.VideoWriter('Problem_5_part_1_answer_a.mp4',
                         cv2.VideoWriter_fourcc(*'MP4V'),
                         20, [960, 540], 0)
frameCount, previousFrame = 0, 0
tau = 10
"""Background subtractor method that open cv includes. Does automatic denoising itself."""
fgbg = cv2.createBackgroundSubtractorMOG2(60, 200)
while input_video.isOpened():
    """Subtract previous frame to start greying things out"""
    previousFrame = np.subtract(previousFrame, 255/tau)
    previousFrame = np.clip(previousFrame, 0, 255)

    ret, originalFrame = input_video.read()

    """end if a frame is not read"""
    if not ret:
        break

    originalFrameResized = cv2.resize(originalFrame, [540, 540])

    """apply earlier defined background filter to to video frame"""
    fgmask = fgbg.apply(originalFrameResized)
    fgmask = np.clip(fgmask, 0, 255)

    count = np.count_nonzero(fgmask)

    """see if pixels have moved compared to the previous frame"""
    if frameCount > 0 and count > 5:
        fgmask = np.where(fgmask > 0, 255, 0)
        fgmask = fgmask.astype(np.uint8)
    fgmask = fgmask + previousFrame
    previousFrame = fgmask
    fgmask = fgmask[:, :, np.newaxis]
    cv2.imshow('original', originalFrameResized)
    fgmask = fgmask.astype(np.uint8)
    cv2.imshow('fmask', fgmask)
    k = cv2.waitKey(100) & 0xff
    if k == 27:
        break

    fgmask = cv2.resize(fgmask, [960, 540])
    result.write(fgmask)
    frameCount += 1
input_video.release()
cv2.destroyAllWindows()