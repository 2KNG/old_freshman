import cv2
import numpy as np

image = cv2.imread("C:/sibal/moon.jpg", cv2.IMREAD_ANYCOLOR) # 경로 설정 시 바탕화면과 같은 경로 사용 금지 ( 에려발생 )
gray_image = cv2.imread("C:/sibal/moon.jpg", cv2.IMREAD_GRAYSCALE) # 흑백으로 변경한다. cv2.IMREAD_GRAYSCALE 대신 0을 넣어도 된다.
cvtimg = cv2.cvtColor(image,cv2.COLOR_RGB2GRAY) # cv2.cvtColor 를 이용하여 변경할 수도 있다.
# image = cv2.imread(fileName, flags) 는 로컬 경로의 이미지 파일을 읽어올 수 있다.
# fileName(파일경로)의 이미지 파일을 flags(플래그) 설정에 따라 불러온다.
# fileName(파일경로)는 상대 경로 또는 절대 경로를 사용하여 이미지를 불러온다.
# flags는 이미지를 초기에 불러올 때 적용할 초기 상태를 의미한다.
y, u, v = cv2.split(image) #YUV 값으로 나눈다.
b, g, r = cv2.split(image) #BGR 로 나누어주었따. 단, RGB 순서가 아닌 BGR 순서이다
# cv2.imshow("y", y)
# cv2.imshow("u", u)
# cv2.imshow("v", v)
# cv2.imshow("b", b)

# cv2.imshow("g", g)
# cv2.imshow("r", r)
bbr_img = cv2.merge((b,b,r))
bbg_img = cv2.merge((b,b,g))
cv2.imshow("bbb_img",bbr_img)
cv2.imshow("bbg_img",bbg_img)
cv2.imshow("basic",image)           # 이미지 표시 함수
# cv2.imshow("gray",gray_image)
# cv2.imshow("cvtgray",cvtimg)
cv2.waitKey(0)                      # 키입력 대기 함수
cv2.destroyAllWindows()             # 모든 윈도우 창 제거 함수
height, width, channal = image.shape
print(height, width, channal)
cv2.imwrite("C:/sibal/gray_moon.png", gray_image,[cv2.IMWRITE_PNG_COMPRESSION])
# imwrite로 사진을 저장한다.
# print([x for x in dir(cv2) if x.startswith('COLOR_')]) # all flag list 274가지 맛
'''
flags
cv2.IMREAD_UNCHANGED : 원본 사용
cv2.IMREAD_GRAYSCALE : 1 채널, 그레이스케일 적용
cv2.IMREAD_COLOR : 3 채널, BGR 이미지 사용
cv2.IMREAD_ANYDEPTH : 이미지에 따라 정밀도를 16/32비트 또는 8비트로 사용
cv2.IMREAD_ANYCOLOR : 가능한 3 채널, 색상 이미지로 사용
cv2.IMREAD_REDUCED_GRAYSCALE_2 : 1 채널, 1/2 크기, 그레이스케일 적용
cv2.IMREAD_REDUCED_GRAYSCALE_4 : 1 채널, 1/4 크기, 그레이스케일 적용
cv2.IMREAD_REDUCED_GRAYSCALE_8 : 1 채널, 1/8 크기, 그레이스케일 적용
cv2.IMREAD_REDUCED_COLOR_2 : 3 채널, 1/2 크기, BGR 이미지 사용
cv2.IMREAD_REDUCED_COLOR_4 : 3 채널, 1/4 크기, BGR 이미지 사용
cv2.IMREAD_REDUCED_COLOR_8 : 3 채널, 1/8 크기, BGR 이미지 사용
'''