
'''
matrix 연산을 할 수 있도록 
각각의 함수를 만들어서 모듈을 만든거얌
'''

import numpy as np

# x = np.array([[1,2,3,4],[5,6,7,8]])

# print(x)

# x = np.array(range(5))
# y = np.arange((5))
# a = np.array(range(1,10,2))
# b = np.arange(1,10,2)
# print(x)
# print(y)
# print(a)
# print(b)

# ones = np.ones((3,3))
# zeros = np.zeros((3,3))
# full = np.full((3,3),5)
# eye = np.eye(3,3)
# print(ones)
# print(zeros)
# print(full)
# print(eye)

'''
단위행렬
> 곱하면 자기자신이 나오는 곱셈
'''

# linear 선형적이다.

# xx = np.linspace(0,20,5)
# print(xx)
# print(type(xx[0]))
'''
정수 실수는 정해져있는게 없으니
그때그때 확인해서 사용한다
'''
# )
# print(x)
# y = x.reshape(3, 3)
# print(y)


import random

# np.random.seed(100)
# x = np.random.rand(2, 2)
# print(x)

# np.random.seed(100)
# x = np.random.randn(3, 3)
# print(x)

x = np.arange(12)
print(x)
print(np.ndim(x))
x = x.reshape(2,2,3)
print(np.ndim(x))
print(x)
print(x[1,0,1])
print(x[1])
print(x[0,:,1])
# 인덱싱
# print((x[0]))
# print(x[0,4])
# print(x[:,4]) # : 행전체를 나타넴
# print(x[:,1:4])

x[1] = np.arange(5,10)