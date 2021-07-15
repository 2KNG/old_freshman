'''
A4 용지에 
양식 갖춰서

report
학과
이름

후 철하여 제출
'''

'''
문제1) 아래와 같이 호출하면 실행 결과와 같이 출력될 수 있도록 
calc 함수의 내용을 완성하시오.
'''

def calc(a, op, b):
    x = a
    y = b
    if op == "+":
        print("{:.2f}{}{:.2f}={:.2f}".format(a, op, b, a+b))
    elif op == "-":
        print("{:.2f}{}{:.2f}={:.2f}".format(a, op, b, a-b))
    elif op == "*":
        print("{:.2f}{}{:.2f}={:.2f}".format(a, op, b, a*b))
    elif op == "/":
        print("{:.2f}{}{:.2f}={:.2f}".format(a, op, b, a/b))
    else :
        print('올바른 정수 및 연산자를 입력하세요')
calc(10,'+',2)
calc(10.5,'-',2.1)
calc(10,'*',5)
calc(12,'/',5)
calc(12,12,2)


'''
문제2 ) 매개변수 x에 전달된 값이 y에 전달된 값의 배수인지 아닌지를 알려주는
DoubleNum 함수의 내용을 완성하시오.
x가 y의 배수이면 True 값을 돌려주고, 배수가 아니면 False 값을 돌려준다.
'''


def DoubleNum(x,y) :
    try :
        if x % y == 0 :
            print(x, "는", y, "의 배수입니다.", sep = "")
        elif x % y != 0 :
            print(x, "는", y, "의 배수가 아닙니다.", sep = "")
        else:
            raise Exception
    except :
        print('올바른 정수를 넣어주세요.') # 문자열과 같이 정수를 넣지않으면s 에려출력

DoubleNum(16,4)
DoubleNum(15,4)
DoubleNum("a","b")

'''
문제3) 어떤 숫자에서 어떤 숫자까지의 정수 값들의 합을 구하여 돌려주는 sum이라는 함수의 내용을 완성하시오.
'''


def plus(f, t): # from 으로 함수를 작성할 수 없어 f, t로 변경
    sum = 0
    for i in range(f, t+1):
        sum += i
    return print(sum)

plus(1,10)

'''
문제4) Fatorial 값을 돌려 받을 수 있는 Factorial 함수의 내용을 완성하시오.(재귀호출)
'''

def Fatorial(x):
    def Fatorialmul(x) :
        if x != 1 :
            return x * Fatorialmul(x-1)
        return 1
    print(Fatorialmul(x))

Fatorial(5)

'''
print(Factorial(n)) 이 번거로움으로 print 를 함수에 지정하여 
Factorial(n) 만 입력하면 터미널에 출력되도록 변경 
'''

# 문제5) 피보나치(Fibonacci) 수열 값을 구하여 돌려주는 Fibo라는 함수를 재귀호출 형태의 함수로 만드시오.
# 만일 Fibo(3)과 같이 호출하면 피보나치 수열의 3번째 값인 2가 return 되어지게 하면 된다.
# 피보나치 수열 : 1, 1, 2, 3, 5, 8, 13, 21

def Fibonacci(n):
    def Fibo(n):
        if n == 1 or n == 2 :
            return 1
        return Fibo(n-2) + Fibo(n-1)
    print("피보나치수열 ",n,"번째 값은 ",Fibo(n),"입니다.", sep="")

Fibonacci(10)    

# 문제6) ShowBit(67) 이라고 ShowBit 함수를 호출하면 출력 화면과 같이
# 2진수로 얼마인지 출력하는 ShowBit 함수의 내용을 완성하시오.

def ShowBit(n):
    cnt = 0
    k = [[0,0,0,0] for i in range(8)] # MSB
    
    for i in range(7, -1, -1) :
        for j in range(3, -1, -1) :
            x = n // 2
            y = n % 2
            if x != 0 : 
                k[i][j] = y
                n = x 
            else :
                k[i][j] = 1
                break 
        if x == 0 :
            break
            
    for i in range(8):
        for j in range(4):
            print(k[i][j], end = "")
        print(end = " ")
print()

ShowBit(2)

print()

# k = [[0,0,0,1] for i in range(8)] # MSB
# print(k[2][3])

# def ShowBit_K(n):
#     cnt = 0
#     k = [] # MSB
#     while n != 0 :
#         x = n // 2
#         y = n % 2
#         if x != 0 :
#             k.append(y)
#             n = x
#             cnt += 1
#         else :    
#             k.append(1)    
#             break 
#     print("unsigned", cnt+1, "BIT")
#     for i in range(len(k),0,-1) :
#         print(k[i-1], end = " ")


# ShowBit_K(128)

'''
문제7 ) Check(x); 라고 Check 함수를 호출하여 소수이면
True 값을 돌려주고, 아니면 False 값을 돌려주는 소수 정의.
'''

# 재귀호출로 만들어보았다.

def Check(x) :
    n = x - 1
    def dfn(n) :
        if 1 < n < x :
            if x % n != 0:
                return dfn(n-1)
            else :
                return False
        else :
            return True
    return dfn(n)

    

a = int(input("정수 입력해라 : "))
while  a < 2:
    print("2 이상인 숫자를 입력해라")
    a = int(input("입력해라 정수 : "))
if Check(a):
    print("{}는 소수다." .format(a))
else:
    print("{}는 소수가 아이다.".format(a))

