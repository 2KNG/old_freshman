# # # # g = [30,10,20]
# # # # print(g)
# # # # print(g[2])

# # # # import turtle as t
# # # # t. shape ('turtle')
# # # # t. speed (0)
# # # # a=['red','orange','yellow','green','blue','black' ]
# # # # t. begin_fill()
# # # # for i in range(300):
# # # #     t. fd(i)
# # # #     t. rt(i)
# # # #     if i < len(a):
# # # #         t. color(a[i])
# # # #     else :
# # # #         t. color(a[i%5])
# # # #     t.end_fill()

# # # t= {1001:"홍길동", 1002:"이기자"}
# # # print(t[1001])
# # # print(t.get(1001))
# # # print(1002 in t)
# # # t[1003]="우리집"
# # # t[1001]="강아지"
# # # print(t)
# # # del t[1003]
# # # print(t)
# # # print(t.keys())
# # # print(t.values())
# # # print(t.items())

# # # print(t)
# # # a,b = set(t)
# # # print(a)
# # # print(b)

# # # b=set(a)
# # # primt(b)

# x = {"홍길동", "최고야", "이기자"}
# y = {"최고야", "이민호", "박호보"}
# print(x & y) #and
# print(x | y) #or
# a = x & y
# print(a)
# b = x | y
# print(b) # 순서가 없다
# x.add("단비")
# print(x)
# k = {"뉸뉴뉴뉸ㄴ뉴ㅠ":"우리집강아지"}
# print(k)
# x = list(x)
# print(x)
# y= tuple(y)
# print(y)
# k['단비'] = '우리집강아지'

# print(type(x))
# print(type(y))
# print(type(k))

# from random import*
# id = range(1,46)
# print(id)
# print(type(id))
# id=list(id)
# print(type(id))
# print(id)
# choice=sample(id,6)
# print(choice)
# print(choice[0])
# print(choice[1:])

# a, b = map(int, input(). split())
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a//b)
# print(a%b)

# weather = input("오늘 날씨는 비 or 눈 or 활사")
# temp = int(input("기온은 어때요? 정수입력"))
# if weather=="비" or weather=="눈":
#     print("우산준비")
# elif weather=="황사":
#     print("마스크준비")
# else :
#     print("준비물이 필요 없음")

'''
3개의 정수를 입력받아서
평균(점수)을 구한다
평균이 90이상 "A학점:,# 평균이 90이상 "B학점"
평균이 70이상 "C학점, 그외는 "F학점" 출력
평균이 60점 이상이고, 모든 정수가 40점 이상이면 "합격"출력"
평균이 60점 미만이거나, 한 과목이라도 40미만이면 "불합격" 출력
'''
#학번 : 2161110053 #이름 : 김강현
a, b, c = map(int, input().split())
avg = (a+b+c)/3

if 60 <= avg and 40 <= a and 40 <= b and 40 <= c :
    print("합격")
    if avg>=90 :
        print("A학점")
    elif avg>=80 :
        print("B학점")
    elif avg>=70 :
        print("C학점")
    else :
        print("F학점")
else :
    print("불합격")

'''
문제 2. 3개의 정수를 입력받아서
평균을 구하고}
평균이 60점 이상이거, 모든 정수가 40점 이상이면 "합격"출력"
평균이 60점 미만이거나, 한 과목이라도 40미만이면 "불합격" 출력
'''
