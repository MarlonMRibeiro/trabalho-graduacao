import numpy
import cv2

webcam = cv2.VideoCapture(0)

aux = 0

if webcam.isOpened():
    validacao, frame = webcam.read()
    while validacao:
        validacao, frame = webcam.read()
        cv2.imshow("Captura da webcam", frame)
        key = cv2.waitKey(10)
        if key == 27: #ESC
            break
        if key == 80 or 112:
            cv2.imwrite(f"images/image_{aux}.png", frame)
            aux + 1

webcam.release()
cv2.destroyAllWindows()