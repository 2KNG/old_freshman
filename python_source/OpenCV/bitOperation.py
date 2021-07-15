import cv2
import numpy as np

def bitOperation(hpos, vpos) :
    img1 = cv2.imread('ocean.jpg')
    img2 = cv2.imread('moon-2.jpg')

    # img2가 박힐 영역지정
    rows, cols, channels = img2.shape
    roi = img1[vpos : rows + vpos, hpos : cols + hpos]

    # img2를 위한 마스크와 역마스크 생성
    img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    ret, mask = cv2.threshold(img2gray, 160, 255, cv2.THRESH_BINARY)
    mask_inv = cv2.bitwise_not(mask)

    img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
    img2_fg = cv2.bitwise_and(img2, img2, mask=mask)

    # img2 배경을 cv2.add로 투명하게 만들고 ROI에 넣기
    dst = cv2.add(img1_bg, img2_fg)
    img1[vpos : rows + vpos, hpos : cols + hpos] = dst

    cv2.imshow('gray', img2gray)
    cv2.imshow('inv', mask_inv)
    cv2.imshow('result', img1)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

bitOperation(20, 0)

