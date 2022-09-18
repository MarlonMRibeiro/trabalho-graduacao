import numpy
import cv2
import cv2
import numpy as np
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# webcam = cv2.VideoCapture(0)

# aux = 0

# if webcam.isOpened():
#     validacao, frame = webcam.read()
#     while validacao:
#         validacao, frame = webcam.read()
#         cv2.imshow("Captura da webcam", frame)
#         key = cv2.waitKey(10)
#         if key == 27: #ESC
#             break
#         if key == 80 or 112:
#             cv2.imwrite(f"images/image_{aux}.png", frame)
#             aux + 1

# webcam.release()
# cv2.destroyAllWindows()
img = cv2.imread("images/sample3.png")

# 2. Resize the image
img = cv2.resize(img, None, fx=0.5, fy=0.5)

# 3. Convert image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 4. Convert image to black and white (using adaptive threshold)
adaptive_threshold = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 85, 11)
text = pytesseract.image_to_string(img)
print(text)

cv2.imshow("gray", gray)
cv2.imshow("adaptive th", adaptive_threshold)
cv2.waitKey(0)