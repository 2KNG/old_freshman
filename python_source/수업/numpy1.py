import numpy as np
import matplotlib as mat
import random

print(np.random.rand(2, 3)) # 0과 1사이 배열생성
print(np.random.randn(3, 4)) # 정규분포로 샘플린된 랜덤 배열생성

np.random.seed(22)
print(np.random.randn(3, 4))
