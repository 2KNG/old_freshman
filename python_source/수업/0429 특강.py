'''
가변인자
'''
# def test(*args) :
#     print(type(args))

# def square2(x):
#     return x**2
# print(square2(3))

# #>>>

# square = lambda x : x**2
# print(square(2))

# add = lambda x, y: x+y
# print(add(3,6))

# #필터(filter)는 내장함수이다.

# nums = [i for i in range(10)]

# k = list(filter(lambda n:n%2==0,nums))

# x = [1, 2, 3, 4, 5]

# a = list(map(lambda n:n**2,x))
# print(a)

# k = [i**2 for i in range(1,6)]

# print(k)

'''
주어진 숫자 리스트의 평균을 구하는 함수를 출력
해당 숫자가 소수인지 아닌지 판별
2부터 해당 숫자사이에 소수가 몇개인지 출력
'''
from functools import reduce
k = [i for i in range(1,100)]
avg = reduce(lambda x, y : x + y, k)/len(k)
print(avg)

x = 13
xr = [i for i in range(i )]

sosu = reduce(lambda x : x % k, range(1,k))

print(A(13))
