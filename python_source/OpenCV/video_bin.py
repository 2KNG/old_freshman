import cv2
import numpy as np


#  Binarization , 이미지의 픽셀을 ( 0 흑 , 255 백 ) 으로 이진화 시킨다.

path= "Moon.jpg"
src =cv2.imread(path,cv2.IMREAD_COLOR)
# 원 이미지를 그대로 불러와서
grayimg = cv2.cvtColor(src,cv2.COLOR_BGR2GRAY)
# 그레이스케일로 컨버팅 한뒤

ret, dst = cv2.threshold(grayimg,100,255,cv2.THRESH_BINARY)
# dst라는 이름으로 이진화 시킨 값을 저장시킨다 .


ret, dst2 = cv2.threshold(grayimg,100,255,cv2.THRESH_BINARY_INV)
ret, dst2_1 = cv2.threshold(src,100,255,cv2.THRESH_BINARY_INV)

ret, dst3 = cv2.threshold(grayimg,100,255,cv2.THRESH_TRUNC)
ret, dst3_1 = cv2.threshold(src,100,255,cv2.THRESH_TRUNC)

ret, dst4 = cv2.threshold(grayimg,100,255,cv2.THRESH_TOZERO)
ret, dst4_1 = cv2.threshold(src,100,255,cv2.THRESH_TOZERO)

ret, dst5 = cv2.threshold(grayimg,100,255,cv2.THRESH_TOZERO_INV)
ret, dst5_1 = cv2.threshold(src,100,255,cv2.THRESH_TOZERO_INV)


cv2.imshow("title", dst)
cv2.imshow("title2", dst2)
cv2.imshow("title2", dst2_1)

cv2.imshow("title3", dst3)
cv2.imshow("title3", dst3_1)

cv2.imshow("title4", dst4)
cv2.imshow("title4", dst4_1)

cv2.imshow("title5", dst5)
cv2.imshow("title5", dst5_1)



if cv2.waitKey()&0xFF ==27:
    cv2.destroyAllWindows()