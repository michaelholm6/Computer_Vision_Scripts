import cv2
import numpy as np
from matplotlib import pyplot as plt

input_image = cv2.imread('p3_image3.png')
gray = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)
_, binary_input_image = cv2.threshold(gray, 50, 255, cv2.THRESH_BINARY)
binary_input_image = ~binary_input_image
nb_blobs, im_with_separated_blobs, stats, _ = cv2.connectedComponentsWithStats(binary_input_image)
sizes = stats[:, -1]
sizes = sizes[1:]
nb_blobs -= 1
min_size = 400
max_size = 450
for blob in range(nb_blobs):
    if sizes[blob] > max_size or sizes[blob] < min_size:
        binary_input_image[im_with_separated_blobs == blob + 1] = 0
binary_input_image = cv2.dilate(binary_input_image, np.ones((3, 3)))
numbers = ['6', '5', '4', '3', '2', '1']
for number in numbers:
    se_template = cv2.imread(number + '_white.png')
    se_template_gray = cv2.cvtColor(se_template, cv2.COLOR_BGR2GRAY)
    _, se_template = cv2.threshold(se_template_gray, 50, 255, cv2.THRESH_BINARY)
    se_template = ~se_template
    se_dimensions = se_template.shape
    se_template = cv2.resize(se_template, [round(se_dimensions[0] * 1.7), round(se_dimensions[1] * 1.7)])
    se_template = cv2.erode(se_template, np.ones((8, 8)))
    eroded = cv2.erode(binary_input_image, se_template)
    eroded_size = eroded.shape
    plt.imshow(cv2.cvtColor(input_image, cv2.COLOR_BGR2RGB))
    for i in range(eroded_size[0]):
        for j in range(eroded_size[1]):
            if eroded[i, j] == 255 and i > 200 and j > 200:
                number_removal = cv2.dilate(eroded, se_template)
                binary_input_image = binary_input_image * ~number_removal
                plt.text(j, i, number, color='red')
plt.show()