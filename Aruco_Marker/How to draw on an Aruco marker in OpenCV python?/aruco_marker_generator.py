import cv2

import numpy as np

dictionary = cv2.aruco.Dictionary_get(cv2.aruco.DICT_6X6_250)
markerImage = np.zeros((300, 300), dtype=np.uint8)

for x in range(0, 250):
    markerImage = cv2.aruco.drawMarker(dictionary, x, 300, markerImage, 1)
    cv2.imwrite(f"marker{x}.png", markerImage)
