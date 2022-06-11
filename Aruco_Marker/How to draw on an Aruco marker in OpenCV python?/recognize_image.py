import cv2

image = cv2.imread("path\\to\\image.png")

dictionary = cv2.aruco.Dictionary_get(cv2.aruco.DICT_6X6_250)
parameters = cv2.aruco.DetectorParameters_create()

markerCorners, markerIds, rejectedCandidates = cv2.aruco.detectMarkers(image, dictionary, parameters=parameters)

print(markerIds)
