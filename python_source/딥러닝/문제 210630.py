import random

i = random.randint(1,15)
print(i)

while x != i :
    x = int(input('줘요'))
    k = x
    if x == i :
        print('정답띠')
    elif i < 7 :
        if 7 < x:
            print("i는 7보다 작다")
        elif x < i < 7 :
            print("i는 7보다 작고 {}보다 커욤".format(x))
        elif i < x < 7 :
            print("i는 {}보다 작습니당".format(x))
    elif 7 <= i :
        if x < 7 :
            print("i는 7보다 크다")
        elif 7 < i < x :
            print("i는 7보다 크고 {}보다 작아욤".format(x))
        elif 7 <= x < i :
            print("i는 {}보다 큽니당".format(x))
    else :
        print('이게머선129')


print('i는 {}가 맞다'.format(i))



# 7보다 큰지 작은지
# 2진분류
# 랜덤값을 물어보면서 찾을 수 있게
#
#
# elif i < 7:
# if 7 < x:
#     print("i는 7보다 작다")
# elif x < i < 7:
#     print("i는 7보다 작고 {}보다 커욤".format(x))
# elif i < x < 7:
#     print("i는 {}보다 작습니당".format(x))
# elif 7 <= i:
#     if x < 7:
#         print("i는 7보다 크다")
#     elif 7 < i < x:
#         print("i는 7보다 크고 {}보다 작아욤".format(x))
#     elif 7 <= x < i:
#         print("i는 {}보다 큽니당".format(x))
#     else:
#     print('이게머선129')
