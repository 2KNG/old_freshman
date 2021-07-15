import os
from os import path

print("구분")
cwd = os.getcwd()
print(cwd)
list = os.listdir()
print(list)
path = r'c:/'

list2 = os.listdir(path)

print(list2)
print(len(list2))