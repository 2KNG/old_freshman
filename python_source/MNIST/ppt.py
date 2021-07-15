import numpy        # 배열의 이용을 위해 넘파이 호출
import matplotlib.pyplot as plt   # 맷플롯립.파이플롯 > 데이터 시각화를 위한 파이썬 확장 라이브러리

data_file = open('mnist_dataset/mnist_train_100.csv', 'r')
data_list = data_file.readlines()
data_file.close()

print(data_list[0])

all_values = data_list[0].split(',')
print(all_values)
image_array = numpy.asfarray(all_values[1:]).reshape((28,28))

onodes = 10
# 출력 노드는 10개
targets = numpy.zeros(onodes) + 0.01
# 모든 노드를 0으로 세팅하고 0.01을 더함
targets[int(all_values[0])] = 0.99
# 레코드 첫번째 인덱스, 즉 레이블을 정수형으로 변환하고 인덱스를 받은 후, 0.99로 세팅한다.
print(targets)


inodes = 784
hnodes = 100
onodes = 10

wih = numpy.random.normal(0.0, pow(hnodes, -0.5), (hnodes, inodes))
who = numpy.random.normal(0.0, pow(onodes, -0.5), (onodes, hnodes))

print(wih)
print(wih.shape())
# print(who)
