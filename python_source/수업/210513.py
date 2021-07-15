# def std_weight(height, gender):
#     if gender == "수":
#         return height*height*22
#     else:
#         return height*height*21

# myweight = int(input("몇근"))
# height = int(input("길이"))
# gender = input("암수구분")
# weight = std_weight(height/100, gender)
# weight = round(weight, 2)
# print("키", height, "표준체중", weight)
# print("감량해야 할 kg", round(myweight - weight,2))

'''
함수정의 정수들을 전달하여
1) 최대값을 구하는 max()함수
2) 최소값을 구하는 min()함수
3) 양수이면 1, 음수이면 -1, 0이면 0 sign()함수 정의
4) 단을 전달하여 구구단 출력함수
'''

score = map(int, input().split())

def max(*score) :
    ma = -999
    for a in score :
        if a > ma :
            ma = a
    return ma

def min(*score) :
    mi = 999
    for a in score :
        if a < mi :
            mi = a
    return mi

def sign(a):
    if a>0 :
        return 1
    elif a < 0 :
        return -1
    else :
        return 0

def gugudan(a) :
    for b in range(1, 10):
        print(a,b, "=" ,a*b )
