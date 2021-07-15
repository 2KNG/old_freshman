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

