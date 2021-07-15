import cv2

src = cv2.imread("C:/sibal/moon.jpg", cv2.IMREAD_COLOR)

height, width, channel = src.shape
matrix = cv2.getRotationMatrix2D((width/2, height/2), 90, 1)
dst = cv2.warpAffine(src, matrix, (width,height))

cv2.imshow("src", src)
cv2.imshow("dst", dst)
cv2.waitKey()
cv2.destroyAllWindows()

'''
2×3 회전 행렬 생성 함수(cv2.getRotationMatrix2D)로 회전 변환 행렬을 계산합니다.
matrix = cv2.getRotationMatrix2D(center, angle, scale)는 
중심점(center), 각도(angle), 비율(scale)로 매핑 변환 행렬(matrix)을 생성합니다.
중심점(center)은 튜플(Tuple) 형태로 사용하며 회전의 기준점을 설정합니다.
각도(angle)는 중심점을 기준으로 회전할 각도를 설정합니다.
비율(scale)은 이미지의 확대 및 축소 비율을 설정합니다.

아핀 변환 함수(cv2.warpAffine)로 회전 변환을 계산합니다.
dst = cv2.warpAffine(src, M, dsize)는 원본 이미지(src)에 M(아핀 맵 행렬)을 
적용하고 출력 이미지 크기(dsize)로 변형해서 출력 이미지(dst)를 반환합니다.
아핀 맵 행렬(M)은 회전 행렬 생성 함수에서 반환된 매핑 변환 행렬을 사용합니다.
출력 이미지 크기(dsize)는 튜플(Tuple) 형태로 사용하며 출력 이미지의 너비와 높이를 의미합니다.
아핀 맵 행렬에 따라 회전된 이미지를 반환합니다.
'''

