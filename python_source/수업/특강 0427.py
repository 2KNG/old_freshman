'''
함수 = 맵핑
ex) len 함수는 리스트, 튜플등을 입력으로 전달하면 아이템의 개수를 출력 전달
'''

# a = [1, 2, 3, 4]
# length = len(a)
# print(length)

# summation = sum(a)
# print(summation)

# def add(x, y):
#     n = x + y
#     return n #return 은 함수의 출력값

# l = len([1, 2, 3])
# c = add(30, 300)
# print(l)
# print(c)

# def test():
#     print('haha')
#     print('good')

#     return 100

# a = test()
# print(a)

# def test1(x, y):
#     print(x,y)
#     n = x + y
#     return n

# a = test1(10,20)
# print(a)

'''
기본인자 default parameter
함수의 파라미터에 기본값 지정가능
파라미터를 명시하지 않을 경우, 지정된 기본값으로 대체
단, 기본파라미터는 일반 파라미터 앞에 올 수 없다
'''

# def add(x, y, z = 5) :
#     a = x + y + z
#     return a
# # x,y 만 입력될 경우 z에 5사용, z까지 입력 시 입력된 z 값 사용
# print(add(1,2))
# def test(x, y, z):
#     a = x + y + z
#     print(a)
#     return a
# print(test(10,20,3))

# def multiply(x, y):
#     if x > 10:
#         return x * y
#     return (x + 2) *y
#     print(x)
# #return 은 함수를 종료시켜주는 역할도 한다.
# print(multiply(1,5))

# def add_mul(x, y) :
#     s = x + y
#     m = x * y

#     return s, m

# c = add_mul(20,3)
# print(type(c))
# print(c)
# l = list(c)
# print(type(l))
# print(l)


'''
함수 = 재사용때문에 사용

def 함수이름(x, y, z)

변수의 범위 ? 
'''

# def 함수이름(x,y,z):
#     result = x + y + z 

#     return result

'''

함수의 기본적으로 순서대로 들어가지만, 
함수를 지정하여 넣을 시 순서를 바꾸어도 된다.

ex)
a = 함수이름(x = 20, z = 10, y = 30)
'''

# a = 함수이름(x = 20, z = 10, y = 30)

def add(x, y, z):
    result = x + y + z
    print(x, y, z)
    a = 40
    print(a)
    return result

a = 10
print(a)
b = add(10, 20)


print(b)
print(a)