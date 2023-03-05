from turtle import home
import cv2
import os
import numpy as np
from PIL import Image
from cvzone.HandTrackingModule import HandDetector
from handwriting_model import HandwritingModel
import time

colorsPath = "NavBar/Colors"
homepagePath = "NavBar/Homepage"
sizesPath = "NavBar/Sizes"
imListColors = os.listdir(colorsPath)
imListHomepage = os.listdir(homepagePath)
imListSizes = os.listdir(sizesPath)
colors = []
homepage = []
sizes = []
model = HandwritingModel()

for imPath in imListColors:
    image = cv2.imread(f'{colorsPath}/{imPath}')
    colors.append(image)

for imPath in imListHomepage:
    image = cv2.imread(f'{homepagePath}/{imPath}')
    homepage.append(image)

for imPath in imListSizes:
    image = cv2.imread(f'{sizesPath}/{imPath}')
    sizes.append(image)


def drawOnFeed(frame, canvas):
    gray = cv2.cvtColor(canvas, cv2.COLOR_BGR2GRAY)
    _, ImgInv = cv2.threshold(gray, 50, 255, cv2.THRESH_BINARY_INV)
    ImgInv = cv2.cvtColor(ImgInv, cv2.COLOR_GRAY2BGR)
    frame = cv2.bitwise_and(frame, ImgInv)
    frame = cv2.bitwise_or(frame, canvas)
    return frame


def real_time_writing():
    width, height = 1280, 720
    brushColor = [(0, 0, 255), (0, 255, 0), (255, 0, 80)]
    brushSize = [10, 20, 30]
    eraserSize = [25, 45, 60]
    currNavBar, currNavBarId, currColor, curBrushSize, currEraserSize = homepage[0], 0, brushColor[2], brushSize[1], \
        eraserSize[1]
    canvas = np.zeros((height, width, 3), dtype='uint8')

    cap = cv2.VideoCapture(0)
    cap.set(3, width)
    cap.set(4, height)

    xp, yp = 0, 0

    detector = HandDetector()

    while True:
        success, frame = cap.read()
        frame = cv2.flip(frame, 1)

        hands, frame = detector.findHands(frame, True)
        lm_list = hands[0]['lmList'] if hands else []

        if len(lm_list):
            fingers = detector.fingersUp(hands[0])
            xi, yi = lm_list[8][:2]
            xm, ym = lm_list[12][:2]

            # index finger
            if fingers == [1, 1, 0, 0, 0] or fingers == [0, 1, 0, 0, 0]:
                if xp == 0 and yp == 0:
                    xp, yp = xi, yi

                cv2.line(canvas, (xp, yp), (xi, yi), currColor, curBrushSize)
                xp, yp = xi, yi

            # index + middle fingers
            elif fingers == [1, 1, 1, 0, 0] or fingers == [0, 1, 1, 0, 0]:
                xp, yp = 0, 0

                if currNavBarId == 0:
                    if ym < 100:
                        if 100 < xm < 280:
                            currNavBar, currNavBarId = colors[0], 1

                        elif 400 < xm < 620:
                            currNavBar, currNavBarId = sizes[1], 2

                        elif 780 < xm < 940:
                            currNavBar, currNavBarId = sizes[0], 3

                elif currNavBarId == 1:
                    if ym < 100:
                        if 100 < xm < 280:
                            currNavBar, currColor = colors[0], brushColor[2]

                        elif 400 < xm < 620:
                            currNavBar, currColor = colors[2], brushColor[0]

                        elif 780 < xm < 940:
                            currNavBar, currColor = colors[1], brushColor[1]

                        elif 1080 < xm < 1200:
                            currNavBar, currNavBarId = homepage[0], 0

                elif currNavBarId == 2 or currNavBarId == 3:
                    if ym < 100:
                        if 100 < xm < 280:
                            currNavBar, curBrushSize = sizes[2], brushSize[0]

                        elif 400 < xm < 620:
                            currNavBar, curBrushSize = sizes[1], brushSize[1]

                        elif 780 < xm < 940:
                            currNavBar, curBrushSize = sizes[0], brushSize[2]

                        elif 1080 < xm < 1200:
                            currNavBar, currNavBarId = homepage[0], 0

            # index + middle + ring fingers
            elif fingers == [1, 1, 1, 1, 0] or fingers == [0, 1, 1, 1, 0]:
                xp, yp = 0, 0

            # index + middle + ring + pBrushColory fingers
            elif fingers == [1, 1, 1, 1, 1] or fingers == [0, 1, 1, 1, 1]:
                cv2.circle(frame, (xm, ym), currEraserSize, (0, 0, 0), -1)
                cv2.circle(canvas, (xm, ym), currEraserSize, (0, 0, 0), -1)
                xp, yp = 0, 0
            else:
                xp, yp = 0, 0

        # model.predict(canvas)
        frame = drawOnFeed(frame, canvas)
        frame[0:100, 0:1280] = currNavBar
        cv2.imshow('Live', frame)

        if cv2.waitKey(20) & 0xFF == ord('x'):
            break

    cv2.destroyAllWindows()
    cap.release()


if __name__ == "__main__":
    real_time_writing()
