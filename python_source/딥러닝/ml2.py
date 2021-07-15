bream_length = [25.4, 26.3, 26.5, 29.0, 29.0, 29.7, 29.7, 30.0, 30.0, 30.7, 31.0, 31.0,
                31.5, 32.0, 32.0, 32.0, 33.0, 33.0, 33.5, 33.5, 34.0, 34.0, 34.5, 35.0,
                35.0, 35.0, 35.0, 36.0, 36.0, 37.0, 38.5, 38.5, 39.5, 41.0, 41.0]
bream_weight = [242.0, 290.0, 340.0, 363.0, 430.0, 450.0, 500.0, 390.0, 450.0, 500.0, 475.0, 500.0,
                500.0, 340.0, 600.0, 600.0, 700.0, 700.0, 610.0, 650.0, 575.0, 685.0, 620.0, 680.0,
                700.0, 725.0, 720.0, 714.0, 850.0, 1000.0, 920.0, 955.0, 925.0, 975.0, 950.0]

smelt_length = [9.8, 10.5, 10.6, 11.0, 11.2, 11.3, 11.8, 11.8, 12.0, 12.2, 12.4, 13.0, 14.3, 15.0]
smelt_weight = [6.7, 7.5, 7.0, 9.7, 9.8, 8.7, 10.0, 9.9, 9.8, 12.2, 13.4, 12.2, 19.7, 19.9]

length = bream_length + smelt_length   # 35개 도미, 14개 빙어
weight = bream_weight + smelt_weight   # 35개 도미, 14개 빙어

fish_data = [[l,w] for l,w in zip(length,weight)] #2차원 배열 만들기
fish_target = [1]*35 + [0]*14  #라벨을 붙인다.  도미 35, 빙어 14인지

#%%


import numpy as np

input_arr = np.array(fish_data)   #np.array
target_arr = np.array(fish_target)

index = np.arange(49)   #np.arange
np.random.seed(1)       #np.seed
np.random.shuffle(index)  #np.random.shuffle

train_input = input_arr[index[:35]]        #배열의 인덱싱
train_target = target_arr[index[:35]]

test_input = input_arr[index[35:]]
test_target = target_arr[index[35:]]

import matplotlib.pyplot as plt

plt.scatter(train_input[:,0],train_input[:,1])
plt.scatter(test_input[:,0],test_input[:,1])

plt.xlabel("length")
plt.ylabel("weight")

%##
from sklearn.neighbors import KNeighborsClassifier
kn = KNeighborsClassifier()
kn.fit(train_input, train_target)    #학습을 시킨다.   길이 와 무게를 주고 정답을 알려준다.

kn.score(test_input, test_target)  # 학습된 결과를 가지고 답을 준다.  정답이고.

