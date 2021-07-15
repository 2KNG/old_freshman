import numpy as np
import cv2

img = cv2.imread('Moon.jpg')
# px = img[320,200]
# print(px)
#
# #Moon.jpg 사진의 320,200 위치에 있는 픽셀은 B = 157 G = 139 R = 102 이다
#
# B = img.item(340, 200, 0)
# G = img.item(340, 200, 1)
# R = img.item(340, 200 ,2)
#
# BGR = [B, G ,R]
# print(BGR)
#
# print(img.shape)
# print(img.size)
# print(img.dtype)

# cv2.imshow('original', img)
#
# subimg = img[300:750, 350:750]
# cv2.imshow('cutting',subimg)
#
# img[300:750, 0:400] = subimg
#
# print(img.shape)
# print(subimg.shape)
#
# cv2.imshow('modified', img)
#
# cv2.waitKey(0)
# cv2.destroyAllWindows()

b, g, r = cv2.split(img)

# print(img[100, 100])
# print(b[100, 100], g[100, 100], r[100, 100])

cv2.imshow('B channel', b)
cv2.imshow('G channel', g)
cv2.imshow('R channel', r)