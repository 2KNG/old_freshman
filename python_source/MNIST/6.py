
import numpy
import scipy.special
import matplotlib.pyplot as plt
import time


class neuralNetwork:

    def __init__(self, inputnodes, hiddennodes, outputnodes, learningrate):

        self.inodes = inputnodes
        self.hnodes = hiddennodes
        self.onodes = outputnodes

        self.wih = numpy.random.normal(0.0, pow(self.hnodes, -0.5), (self.hnodes, self.inodes))
        self.who = numpy.random.normal(0.0, pow(self.onodes, -0.5), (self.onodes, self.hnodes))

        self.lr = learningrate

        self.activation_function = lambda x: scipy.special.expit(x)

        pass

    def train(self, inputs_list, targets_list):
        inputs = numpy.array(inputs_list, ndmin=2).T
        targets = numpy.array(targets_list, ndmin=2).T

        hidden_inputs = numpy.dot(self.wih, inputs)
        hidden_outputs = self.activation_function(hidden_inputs)

        final_inputs = numpy.dot(self.who, hidden_outputs)
        final_outputs = self.activation_function(final_inputs)

        output_errors = targets - final_outputs
        hidden_errors = numpy.dot(self.who.T, output_errors)

        self.who += self.lr * numpy.dot((output_errors * final_outputs * (1.0 - final_outputs)),
                                        numpy.transpose(hidden_outputs))
        self.wih += self.lr * numpy.dot((hidden_errors * hidden_outputs * (1.0 - hidden_outputs)),
                                        numpy.transpose(inputs))

        pass

    def query(self, inputs_list):
        inputs = numpy.array(inputs_list, ndmin=2).T

        hidden_inputs = numpy.dot(self.wih, inputs)
        hidden_outputs = self.activation_function(hidden_inputs)

        final_inputs = numpy.dot(self.who, hidden_outputs)
        final_outputs = self.activation_function(final_inputs)

        return final_outputs


input_nodes = 784
hidden_nodes = 10
output_nodes = 10

learning_rate = 0.2



n = neuralNetwork(input_nodes, hidden_nodes, output_nodes, learning_rate)

training_data_file = open("mnist_dataset/mnist_train.csv", "r")
training_data_list = training_data_file.readlines()
training_data_file.close()

test_data_file = open("mnist_dataset/mnist_test.csv", "r")
test_data_list = test_data_file.readlines()
test_data_file.close()

e_step = []
e_step_performance = []

epochs = 8
for epoch in range(1, epochs):
    train_start = time.time()
    for e in range(epoch):
        for record in training_data_list:
            all_values = record.split(",")
            inputs = (numpy.asfarray(all_values[1:]) / 255.0 * 0.99) + 0.01
            targets = numpy.zeros(output_nodes) + 0.01
            targets[int(all_values[0])] = 0.99
            n.train(inputs, targets)

    train_end = time.time()
    print("???????????? =", round(train_end - train_start, 2))

    query_start = time.time()

    scorecard = []

    for record in test_data_list:
        all_values = record.split(',')

        correct_label = int(all_values[0])

        inputs = (numpy.asfarray(all_values[1:]) / 255.0 * 0.99) + 0.01
        outputs = n.query(inputs)

        label = numpy.argmax(outputs)

        if (label == correct_label):
            scorecard.append(1)
        else:
            scorecard.append(0)
            pass

    query_end = time.time()

    print("???????????? =", round(query_end - query_start, 2))
    print("??? ???????????? =", round(query_end - train_start, 2))
    scorecard_array = numpy.asarray(scorecard)
    performance = round((scorecard_array.sum() / scorecard_array.size) * 100, 2)
    print("performance =", performance)
    e_step.append(epoch)
    e_step_performance.append(performance)


plt.plot(e_step, e_step_performance)
plt.show()

