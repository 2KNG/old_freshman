# 3개층의 신경망으로 MNIST 데이터를 학습하는 코드

import numpy
# 시그모이드 함수 expit() 사용을 위해 scipy.special 불러오기
import scipy.special
# 행렬을 시각화하기 위한 라이브러리
import matplotlib.pyplot as plt


# 신경망 클래스의 정의
class neuralNetwork:

    # 신경망 초기화하기
    def __init__(self, inputnodes, hiddennodes, outputnodes, learningrate):
        # 입력, 은닉, 출력 계층의 개수 설정
        self.inodes = inputnodes
        self.hnodes = hiddennodes
        self.onodes = outputnodes

        # 가중치 행렬 wih(w_input_hidden)와 who(w_hidden_output)
        # 배열 내 가중치는 w_i_j로 표기, 노드 i에서 다음 계층의 노드 j로 연결됨을 의미
        # numpy.random.normal > 정규분포 표본추출(평균, 표준편차, 데이터 개수) - 정교한 가중치
        self.wih = numpy.random.normal(0.0, pow(self.hnodes, -0.5), (self.hnodes, self.inodes))
        self.who = numpy.random.normal(0.0, pow(self.onodes, -0.5), (self.onodes, self.hnodes))

        # 학습률
        self.lr = learningrate

        # 활성화 함수로는 시그모이드 함수를 이용
        # 시그모이드 함수를 사용하는 이유는 로지스틱 회귀에서 0 과 1의 커브를 만들기 위해서
        self.activation_function = lambda x: scipy.special.expit(x)

        pass

    # 신경망 학습시키기
    def train(self, inputs_list, targets_list):
        # 입력 리스트 2차원의 행렬로 변환
        inputs = numpy.array(inputs_list, ndmin=2).T
        targets = numpy.array(targets_list, ndmin=2).T

        # 은닉 계층으로 들어오는 신호를 계산
        hidden_inputs = numpy.dot(self.wih, inputs)
        # 은닉 계층에서 나가는 신로를 계산
        hidden_outputs = self.activation_function(hidden_inputs)

        # 최종 출력 계층으로 들어오는 신호를 계산
        final_inputs = numpy.dot(self.who, hidden_outputs)
        # 최종 출력 계층에서 나가는 신호를 계산
        final_outputs = self.activation_function(final_inputs)

        # 출력 계층의 오차는 (실제 값 - 계산 값)
        output_errors = targets - final_outputs
        # 은닉 계층의 오차는 가중치에 의해 나뉜 출력 계층의 오차들을 재조합해 계산
        hidden_errors = numpy.dot(self.who.T, output_errors)

        # 은닉 계층과 출력 계층 간의 가중치 업데이트
        self.who += self.lr * numpy.dot((output_errors * final_outputs * (1.0 - final_outputs)),
                                        numpy.transpose(hidden_outputs))
        self.wih += self.lr * numpy.dot((hidden_errors * hidden_outputs * (1.0 - hidden_outputs)),
                                        numpy.transpose(inputs))

        pass

    # 신경망에 질의하기
    def query(self, inputs_list):
        # 입력 리스트를 2차원 행렬로 변환
        inputs = numpy.array(inputs_list, ndmin=2).T

        # 은닉 계층으로 들어오는 신호를 변환
        hidden_inputs = numpy.dot(self.wih, inputs)
        # 은닉 계층에서 나가는 신호를 계산
        hidden_outputs = self.activation_function(hidden_inputs)

        # 최종 출력 계층으로 들어오는 신호를 계산
        final_inputs = numpy.dot(self.who, hidden_outputs)
        # 최종 출력 계층에서 나가는 신호를 계산
        final_outputs = self.activation_function(final_inputs)

        return final_outputs


# 입력, 은닉, 출력 노드의 수
# 픽셀이 28 * 28의 크기이므로 입력 노드의 수는 784
# 100개의 은닉 노드를 선택한 이유에는 관학적 근거가 있는것은 아닙니다.
# 신경망은 입력 값에서 어떤 특징 또는 패턴을 찾아냅니다.
# 이런한 특징 또는 패턴은 입력 값의 수보다는 작은 형태로 표현되므로 일단 은닉 노드의 수는 784보다 크지는 않을것 입니다.
# 즉 입력 값의 수보다 작은 값을 선택함으로써 신경망이 주요 특징을 찾아내는 것입니다.
# 하지만 만약 우리가 너무 적은 수의 은닉 계층 노드를 선택한다면 충분히 더 많은 특징과 패턴을 찾아낼 수도 있는 신경망의 능력을 제한시키는 것입니다.
# 즉 이 경우에는 MNIST 데이터에 대한 이해도를 표현할 능력을 제거하는 셈입니다.
# 출력 계층에서 10개의 레이블을 구분해야 하므로 10개의 출력 노드가 필요하다는 점을 고려하면 은닉 계층에 100개의 노드를 선택한 것은 합리적인 선택으로 보입니다.
# 어떤 문제에 대해 은닉 노드를 몇 개로 해야 할지 결정하는데 대한 완벽한 방법롤은 존재하지 않습니다.
# 더 나아가 은닉 계층을 몇 개로해야 할는지에 대해서도 정답은 없습니다.
# 현재로서 최선의 접근 방법은 우리가 해결해야 하는 문제에서 최적의 설절을 찾을 때까지 실험을 반복함으로써 그것을 찾아내는 것입니다.
input_nodes = 784
hidden_nodes = 100
output_nodes = 10

# 학습률은 0.3 > 0.1 > 0.01 > 0.2
learning_rate = 0.2

# 신경망의 인스턴스 생성
n = neuralNetwork(input_nodes, hidden_nodes, output_nodes, learning_rate)

# mnist 학습 데이터인 csv 파일을 리스트로 불러오기
# training_data_file = open("mnist_dataset/mnist_train_100.csv", "r")
training_data_file = open("mnist_dataset/mnist_train.csv", "r")
training_data_list = training_data_file.readlines()
training_data_file.close()

# 신경망 학습시키기

# 학습 데이터 모음 내의 모든 레코드 탐색
for record in training_data_list:
    # 레코드를 쉼표에 의해 분리
    all_values = record.split(",")
    # 입력 값의 범위와 값 조정
    inputs = (numpy.asfarray(all_values[1:]) / 255.0 * 0.99) + 0.01
    # 결과 값 생성 (실제 값인 0.99 외에는 모두 0.1)
    targets = numpy.zeros(output_nodes) + 0.01
    # all_values[0]은 이 레코드에 대한 결과 값
    targets[int(all_values[0])] = 0.99
    n.train(inputs, targets)

    pass

# 테스트 데이터 레코드 불러오기

test_data_file = open("mnist_dataset/mnist_test.csv", "r")
test_data_list = test_data_file.readlines()
test_data_file.close()

all_values = test_data_list[0].split(',')
print(all_values[0])

image_array = numpy.asfarray(all_values[1:]).reshape((28, 28))
plt.imshow(image_array, cmap='Greys', interpolation='None')
plt.show()

n.query((numpy.asfarray(all_values[1:])/ 255.0 * 0.99) + 0.01)

# 신경망 테스트

# 신경망의 성능의 지표가 되는 성적표를 아무 값도 가지지 않도록 초기화
scorecard = []

# 테스트 데이터 모음 내의 모든 레코드 탐색

# 테스트 데이터의 모음 내의 모든 레코드 탐색
for record in test_data_list:
    all_values = record.split(',')

    correct_label = int(all_values[0])
    print(correct_label, "correct label")

    inputs = (numpy.asfarray(all_values[1:]) / 255.0 * 0.99) + 0.01
    outputs = n.query(inputs)

    label = numpy.argmax(outputs)
    print(label, "network's answer")

    if (label == correct_label):
        scorecard.append(1)
    else:
        scorecard.append(0)
        pass

print(scorecard)

scorecard_array = numpy.asarray(scorecard)
print("performance =", scorecard_array.sum() / scorecard_array.size)


epochs = 2

for e in range(epochs):
    for record in training_data_list:
        all_values = record.split(',')
        inputs = (numpy.asfarray(all_values[1:]) / 255.0 * 0.99) + 0.01
        targets = numpy.zeros(output_nodes) + 0.01
        targets[int(all_values[0])] = 0.99
        n.train(inputs, targets)
        pass
    pass
