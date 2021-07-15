import cv2

src = cv2.imread("C:/sibal/moon.jpg", cv2.IMREAD_COLOR)
dst = cv2.flip(src, 0)

'''
대칭 함수(cv2.flip)로 이미지를 대칭할 수 있습니다.
dst = cv2.flip(src, flipCode)는 원본 이미지(src)에 대칭 축(flipCode)을 기준으로 대칭한 출력 이미지(dst)를 반환합니다.
대칭 축은 상수를 입력해 대칭할 축을 설정할 수 있습니다.
flipCode < 0은 XY 축 대칭(상하좌우 대칭)을 적용합니다.
flipCode = 0은 X 축 대칭(상하 대칭)을 적용합니다.
flipCode > 0은 Y 축 대칭(좌우 대칭)을 적용합니다.
'''

cv2.imshow("src", src)
cv2.imshow("dst", dst)
cv2.waitKey()
cv2.destroyAllWindows()
