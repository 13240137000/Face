import cv2 as cv


def main():
    tpl = cv.imread("images/tpl.png")
    target = cv.imread("images/target.png")

    method = cv.TM_SQDIFF_NORMED
    th, tw = tpl.shape[:2]

    print(th, tw)

    ret = cv.matchTemplate(target, tpl, method)

    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(ret)

    tl = min_loc

    br = (tl[0] + tw, tl[1] + th)

    cv.rectangle(target, tl, br, (0, 0, 255), 2)
    cv.imshow("target", target)


if __name__ == "__main__":
    main()
    cv.waitKey(0)
