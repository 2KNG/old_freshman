import numpy as np

D3 = np.array([[[1, 2],[3, 4]],[[5, 6], [7, 8]]])
print(D3)
print(np.ndim(D3))
print(D3.shape)
# A = np.array([1, 2, 3, 4])
# print(A)
# print(np.ndim(A)) 
# print(A.shape)
# print(A.shape[0])

'''
A는 1차원 배열이고 원소 4개로 구성
.shape 메서드는 튜플을 반환하며
이는 1차원일 때도 다차원 배열과 같이 반환한다 
'''


# B = np.array([[1, 2], [3, 4], [5, 6]])
# print(B)
# print(np.ndim(B))
# print(B.shape)

'''
3X2 배열인 B를 작성하였다.
3X2 배열의 의미는 
처음 차원에는 원소가 3개,
다음 차원에는 원소가 2개 있다는 의미이다.

이 때 처음 차원은 0번째 차원,
다음 차원은 1번째 차원에 대응한다.
(파이썬의 인덱스로 생각하면 편하다.)

2차원의 배열은 특히 행렬(matrix)라고 부르고
가로 방향을 행(row)
세로 방향을 열(column)이라고 한다.
'''

# A = np.array([[1, 2], [3, 4]])
# print(A.shape)
# B = np.array([[5, 6], [7, 8]])
# print(B.shape)
# print(np.dot(A, B))
# print(np.dot(B, A))
# X = np.array([1, 2])
# Y = np.array([5, 6])
# print(np.dot(X, Y)) # 1*5 + 2*6 = 17
# print(np.dot(A, X)) # 1*5 + 2*6 = 17 , 3*5 + 4*6 = 39

'''
2차원 배열의 곱은 
왼쪽행과 오른쪽열을 원소별로 곱하고 
값을 더하면 된다.

코드로는 넘파이 함수 np.dot()로 계산한다.
np.dot()은 입력이 1차원이면 벡터를 2차원이면 행렬 곱을 계산한다.
이 때 np.dot(A,B) 와 np.dot(B,A)는 다른 값이 될 수 있다.
'''

# A = np.array([[1, 2, 3], [4, 5, 6]])
# print(A.shape)

# B = np.array([[1, 2], [3, 4], [5, 6]])
# print(B.shape)

# print(np.dot(A, B))


A = np.array([[1, 2, 3], [4, 5, 6]])
B = np.array([[1, 2], [3, 4], [5, 6]])
C = np.array([1, 2])
D = np.array([5, 6])
E = np.array([[1, 2], [3, 4]])
F = np.array([[5, 6], [7, 8]])
G = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

# print("1.","\n",np.dot(A, B))                 #2X3 X 3X2 = 2X2 #2차원
# print("2.","\n",np.dot(C ,D))                 # 2  X  2  =  2   1*5 + 2*6 = 17 (1차원의 계산 벡터)
# print("3.","\n",np.dot(E, F))                 #2X2 X 2X2 = 2X2 #2차원
# # print("4.","\n",np.dot(A, C))               #          ValueError: shapes (2,3) and (2,) not aligned: 3 (dim 1) != 2 (dim 0)
# print("5.","\n",np.dot(C, A))                 # 2  X 2X3 = 1X3 #1차원
# print("6.","\n",np.dot(B, D))                 #3X2 X  2  = 3X1 #1차원
# # print("7.","\n",np.dot(D, B))               #          ValueError: shapes (2,) and (3,2) not aligned: 2 (dim 0) != 3 (dim 0)
# # print("8.","\n",np.dot(A, E))               #          ValueError: shapes (2,3) and (2,2) not aligned: 3 (dim 1) != 2 (dim 0)
# print("9.","\n",np.dot(E, A))                 #2X2 X 2X3 = 2X3 #2차원
# print("10.","\n",np.dot(B, G))                #2X2 X 2X3 = 2X3 #2차원
'''
첫번 째 행렬 1차원의 원소 수(열 수)와 
두번 째 행렬 0차원의 원소 수(행 수)가 같아야한다.
'''

X = np.array([1, 2])                    # 입력값 (x)을 1, 2 라고 지정
W = np.array([[1, 3, 5], [2, 4, 6]])    # 가중치 지정!! (갯 수는 입력값 (x)와 결과값(y의) 갯수에 따라 달라짐)
Y = np.dot(X, W)
print(X.shape)  
print(W.shape)
print(Y)


# X = [[1,2],[3,4]]
# W = [[5,6],[7,8]]
# X = np.array([1, 2])                    # 입력값 (x)을 1, 2 라고 지정
# W = np.array([[1, 3, 5], [2, 4, 6]])
# Y = [[sum([X[i][k]*W[k][j] for k in range(2)])
# for i in range(2)] for j in range(2)]
# print(Y)