import cv2
from cvzone.HandTrackingModule import HandDetector


def virtual_zoom(image_path="img.png"):
    cap = cv2.VideoCapture(0)
    cap.set(3, 1280)
    cap.set(4, 720)

    detector = HandDetector(detectionCon=0.8)
    startDist = None
    scale = 0
    cx, cy = 640, 360

    while True:
        success, img = cap.read()
        hands, img = detector.findHands(img)
        img = cv2.flip(img, 1)

        if len(hands) == 2:
            if detector.fingersUp(hands[0]) == [1, 1, 0, 0, 0] and detector.fingersUp(hands[1]) == [1, 1, 0, 0, 0]:
                lmList1 = hands[0]["lmList"]
                lmList2 = hands[1]["lmList"]
                # point 8 is the tip of the index finger
                if startDist is None:
                    length, info, img = detector.findDistance(lmList1[8][:2], lmList2[8][:2], img)
                    startDist = length
                else:
                    length, info, img = detector.findDistance(lmList1[8][:2], lmList2[8][:2], img)
                    scale = int(length - startDist) // 2
                    cx, cy = info[4:]
        else:
            startDist = None

        img1 = cv2.imread(image_path)
        if img1 is None:
            img1 = cv2.imread("img.png")

        try:
            h1, w1, _ = img1.shape
            newH, newW = ((h1 + scale) // 2) * 2, ((w1 + scale) // 2) * 2
            img1 = cv2.resize(img1, (newW, newH))
            img[cy - newH // 2:cy + newH // 2, cx - newW // 2:cx + newW // 2] = img1
        except ValueError:
            pass

        cv2.imshow("Image", img)
        cv2.waitKey(1)


if __name__ == "__main__":
    virtual_zoom()
