import numpy as np

a =  np.array([1,2,3,4,5,6,7,8,9])

index = np.arange(9)   #np.arange
np.random.seed(1)       #np.seed
np.random.shuffle(index)  #np.random.shuffle

print('a :',a)
print('index:',index)

