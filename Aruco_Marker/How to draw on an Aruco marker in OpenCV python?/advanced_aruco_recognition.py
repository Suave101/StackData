import random

import cv2
import math

vid = cv2.VideoCapture(0)
dictionary = cv2.aruco.Dictionary_get(cv2.aruco.DICT_6X6_250)
parameters = cv2.aruco.DetectorParameters_create()
color_list = []
for x in range(0, 260):
    color_list.append((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))

while True:
    ret, frame = vid.read()
    markerCorners, markerIds, rejectedCandidates = cv2.aruco.detectMarkers(frame, dictionary, parameters=parameters)
    del rejectedCandidates
    if markerIds is not None:
        i = 0
        for marker in markerIds:
            k = str(markerCorners[i]).replace("\n", "").split("[")
            k2 = []
            for j in k:
                j = j.split("]")
                j2 = []
                for n in j:
                    n = n.split(".")
                    j2 = j2 + n
                k2 = k2 + j2
                del j2, j
            del k
            k3 = []
            for item in k2:
                try:
                    k3.append(int(item))
                except:
                    pass
            del k2
            k2 = [k3[i:i + 2] for i in range(0, len(k3), 2)]
            del k3
            x = k2[0][0]
            y = k2[0][1]
            w = int(math.dist(k2[0], k2[1]))
            h = int(math.dist(k2[3], k2[0]))
            frame = cv2.rectangle(frame, (x, y), (x + w, y + h), color_list[int(marker)], 1)
            frame = cv2.putText(frame, f'Marker: {int(marker)}', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9,
                                color_list[int(marker)], 2)
            i = i + 1
        del i, markerCorners, markerIds
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

vid.release()
cv2.destroyAllWindows()
