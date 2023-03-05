import cv2
from cvzone.HandTrackingModule import HandDetector
import cvzone
import numpy as np


def drag_and_drop():
    cap = cv2.VideoCapture(0)
    cap.set(3, 1280)
    cap.set(4, 720)
    detector = HandDetector(detectionCon=0.8)
    colorR = (0, 0, 255)

    cx, cy, w, h = 100, 100, 200, 200

    class DragRect:
        def __init__(self, posCenter, size=None):
            if size is None:
                size = [200, 200]
            self.posCenter = posCenter
            self.size = size

        def update(self, cursor):
            cx, cy = self.posCenter[:2]
            w, h = self.size

            # If the index fingertip is in the rectangle region
            if cx - w // 2 < cursor[0] < cx + w // 2 and \
                    cy - h // 2 < cursor[1] < cy + h // 2:
                self.posCenter = cursor

    rectList = []
    for x in range(5):
        rectList.append(DragRect([x * 250 + 150, 150]))

    while True:
        success, img = cap.read()
        img = cv2.flip(img, 1)
        hands, img = detector.findHands(img)
        lmList = hands[0]["lmList"] if hands else None

        if lmList:
            l, _, _ = detector.findDistance(lmList[4][:2], lmList[8][:2], img)
            if l < 30:
                cursor = lmList[8]  # index finger tip landmark
                # call the update here
                for rect in rectList:
                    rect.update(cursor)

        imgNew = np.zeros_like(img, np.uint8)
        for rect in rectList:
            cx, cy = rect.posCenter[:2]
            w, h = rect.size
            cv2.rectangle(imgNew, (cx - w // 2, cy - h // 2),
                          (cx + w // 2, cy + h // 2), colorR, cv2.FILLED)
            cvzone.cornerRect(imgNew, (cx - w // 2, cy - h // 2, w, h), 20, rt=0)

        out = img.copy()
        alpha = 0.5
        mask = imgNew.astype(bool)
        out[mask] = cv2.addWeighted(img, alpha, imgNew, 1 - alpha, 0)[mask]

        cv2.imshow("Image", out)
        cv2.waitKey(1)


if __name__ == "__main__":
    drag_and_drop()
