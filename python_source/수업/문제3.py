def plus(f, t): # from 으로 함수를 작성할 수 없어 f, t로 변경
    sum = 0
    for i in range(f, t+1):
        sum += i
    return sum

print(plus(1,10))
print(plus(1, 3) + plus(5, 7))
