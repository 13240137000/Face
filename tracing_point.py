import cv2 as cv
import numpy as np


def main():

    capture = cv.VideoCapture(r"images/Demo.mp4")

    while True:

        ret, frame = capture.read()

        if not ret:
            break

        # hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
        #
        # lower_hsv = np.array([156, 43, 46])
        # upper_hsv = np.array([180, 255, 255])
        #
        # mask = cv.inRange(hsv, lowerb=lower_hsv, upperb=upper_hsv)
        #
        # cv.imshow("video", frame)
        # cv.imshow("tracing point", mask)

        dst = cv.pyrMeanShiftFiltering(frame, 10, 100)
        image = cv.cvtColor(dst, cv.COLOR_BGR2GRAY)
        circles = cv.HoughCircles(image, cv.HOUGH_GRADIENT, 1, 20, param1=50, param2=30, minRadius=20, maxRadius=40)
        circles = np.uint16(np.around(circles))

        for i in circles[0, :]:
            cv.circle(frame, (i[0], i[1]), i[2], (0, 0, 255), 2)

        cv.imshow("detection", frame)

        if cv.waitKey(1) & 0xFF == ord('q'):
            break


if __name__ == "__main__":
    main()
