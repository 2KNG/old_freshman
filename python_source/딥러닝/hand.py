import cv2

import numpy as np


def Find(path):
    # 창 이름 설정

    cv2.namedWindow('image')

    # 이미지 파일 읽기

    img = cv2.imread(path, cv2.IMREAD_COLOR)

    # 이미지 사이즈 조정

    img = Resize(img)

    # 이미지 색 바꾸기

    # img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # img_ycrcb = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)

    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # 잡음 제거

    img_hsv = cv2.fastNlMeansDenoisingColored(img_hsv, None, 10, 10, 7, 21)

    lower = np.array([0, 48, 80], dtype="uint8")

    upper = np.array([20, 255, 255], dtype="uint8")

    img_hand = cv2.inRange(img_hsv, lower, upper)

    # 경계선 찾음

    contours, hierarchy = cv2.findContours(img_hand, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    # 가장 큰 영역 찾기

    max = 0

    maxcnt = None

    for cnt in contours:

        area = cv2.contourArea(cnt)

        if (max < area):
            max = area

            maxcnt = cnt

    # maxcontours의 각 꼭지점 다각선 만들기

    hull = cv2.convexHull(maxcnt)

    # img 다 0으로 만들기?

    mask = np.zeros(img.shape).astype(img.dtype)

    color = [255, 255, 255]

    # 경계선 내부 255로 채우기

    cv2.fillPoly(mask, [maxcnt], color)

    img_hand = cv2.bitwise_and(img, mask)

    cv2.drawContours(img_hand, [maxcnt], 0, (255, 0, 0), 3)

    cv2.drawContours(img_hand, [hull], 0, (0, 255, 0), 3)

    # 이미지 보여주기

    cv2.imshow('image', img_hand)

    # 창 esc 끄기

    while True:

        if cv2.waitKey(0) == 27:
            cv2.destroyWindow('image')

            break;

    return


def Resize(img):
    print(img.shape)

    width = 500

    ratio = width / img.shape[1]  # width * 사진 너비 = 비율

    height = int(ratio * img.shape[0])  # 비율 * 사진 높이

    # 축소 INTER_AREA

    # 확대 INTER_LINEAR

    resize = cv2.resize(img, dsize=(width, height), interpolation=cv2.INTER_AREA)

    # resize = cv2.resize(img, dsize = (0, 0), fx=1.5, fy=1.5, interpolation = cv2.INTER_AREA)

    print(resize.shape)

    return resize



Find("ok3.jpg")



