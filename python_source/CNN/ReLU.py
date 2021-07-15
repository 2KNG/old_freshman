import numpy
import matplotlib.pyplot as plt
import numpy as np


def ReLU(x):
    return np.maximum(0, x)

# 0과 x 중에 큰값을 반환
# 즉 0 이하의 숫자가 들어오면 0 이 반환됨됨

x = np.arange(-5.0, 5.0, 0.1)
y = ReLU(x)

fig = plt.figure(figsize=(8,6))
fig.set_facecolor('white')

plt.title("ReLU", fontsize=30)
plt.xlabel('x', fontsize = 15)
plt.axvline(0.0, color='gray', linestyle="--", alpha=0.8)
plt.axhline(0.0, color='gray', linestyle="--", alpha=0.8)
plt.plot(x, y)
plt.show()

def Leaky_ReLU(x):
    return np.maximum(0.01*x, x)

x = np.arange(-100.0, 100.0, 0.1)
y = Leaky_ReLU(x)

fig = plt.figure(figsize=(8,6))
fig.set_facecolor('white')

plt.ylim(-5, 20)
plt.title("Leaky ReLU", fontsize=30)
plt.plot(x, y)
plt.show()



x = np.arange(0, 1, 0.01)
y = np.log(x)

plt.ylim(-5, 0)
plt.title("lnx", fontsize=30)
plt.plot(x, y)
plt.show()