'''
정수 3개를 입력하여 가장 큰 수를 출력
'''

# a = list(map(int, input('앙 입력띠').split()))
# max = a[0]
# min = a[0]
# print(a)
# for i in a:
#     if max < i :
#         max = i
# for j in a:
#     if min > j :
#         min = j 

# print("max = {}".format(max))
# print("min = {}".format(min))

'''
정수 (a,b) a가 b 보다 크면 a-b 계산하여 c에 저장하고, b는 0으로 바꾸시오
b가 a 보다 크면 b-a 계산하여 c에 저장하고, a는 0으로 바꾸시오
a와 b 가 같으므로 a-b 계산하여 c에 저장하고, a=0,b=0으로 바꾸시오.
마지막 a,b,c ㅎㅇ
'''

# a, b = map(int, input('앙 입력띠 ^^').split())
# c = 0
# if a > b :
#     c = a - b
#     b = 0
# elif b > a :
#     c = b - a
#     a = 0
# elif a == b :
#     c = a - b
#     a = 0
#     b = 0
# print(a,b,c)

# '''
# 정수(a) 입력받아 짝수이면 "짝수", 아니먄 "홀수"
# '''
# a = list(map(int, input("우리집강아지복슬복슬").split()))
# for i in a :
#     if i % 2 == 0 :
#         print("{} = 짝수".format(i))
#     else : 
#         print("{} = 홀수".format(i))


'''
정수(a) 입력받아 3의 배수면 "3배", 아니먄 "꽝"
'''
# a = list(map(int, input("우리집강아지복슬복슬").split()))
# for i in a :
#     if i % 3 == 0 :
#         print("{} = 3의 배수띠".format(i))
#     else : 
#         print("{} = 응 아니야~".format(i))

# a = [100,90,80,71,63]
# sum = 0
# cnt = 0
# for i in a:
#     if i % 2 == 0 :
#         sum += i
#         cnt += 1
# print(sum/cnt)

# a = [1,1,2]
# for i in range(2,20) :
#     if a[i] <= 100 :
#         a[i] = a[i-2] + a[i-1]
#         a.append(a[i])
#     else :
#         continue;

'''
3-100까지 피보나치 수열의 합계(y)
1,1,2,3,5,8,13,21,34,55...
a=1,b=1,y=2 초기값
'''
# a,b,c=1,1,2
# i = range(3,15)
# print(1,1, end = ' ')
# for k in i :
#     d = a + b
#     # c = c + d
#     a,b = b,d
#     print(d, end = ' ')
#     # print(c)
'''

# i=1
# cnt=0
# while a[i] <= 100 :
#     i += 1
#     a.append(a[i])
#     a[i] = a[i-2] + a[i-1]
#     cnt += 1

# print(a[:cnt+1])



# for i in range(212) :
#     if i % 2 == 0 :
#         print("무~야~호~♬ ",end = '')
#     else :
#         print("무~야~호~♪ ",end = '')
# print()
# print('"그만큼 신난다는거지"')
# print(
# '''
# ⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢠⣴⣾⣿⣶⣶⣆⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀
# ⢀⢀⢀⣀⢀⣤⢀⢀⡀⢀⣿⣿⣿⣿⣷⣿⣿⡇⢀⢀⢀⢀⣤⣀⢀⢀⢀⢀⢀
# ⢀⢀ ⣶⢻⣧⣿⣿⠇ ⢸⣿⣿⣿⣷⣿⣿⣿⣷⢀⢀⢀⣾⡟⣿⡷⢀⢀⢀⢀
# ⢀⢀⠈⠳⣿⣾⣿⣿⢀⠈⢿⣿⣿⣷⣿⣿⣿⣿⢀⢀⢀⣿⣿⣿⠇⢀⢀⢀⢀
# ⢀⢀⢀⢀⢿⣿⣿⣿⣤⡶⠺⣿⣿⣿⣷⣿⣿⣿⢄⣤⣼⣿⣿⡏⢀⢀⢀⢀⢀
# ⢀⢀⢀⢀⣼⣿⣿⣿⠟⢀⢀⠹⣿⣿⣿⣷⣿⣿⣎⠙⢿⣿⣿⣷⣤⣀⡀⢀⢀
# ⢀⢀⢀ ⢸⣿⣿⣿⡿⢀⢀⣤⣿⣿⣿⣷⣿⣿⣿⣄⠈⢿⣿⣿⣷⣿⣿⣷⡀⢀
# ⢀⢀⢀⣿⣿⣿⣿⣷⣀⣀⣠⣿⣿⣿⣿⣷⣿⣷⣿⣿⣷⣾⣿⣿⣿⣷⣿⣿⣿⣆
# ⣿⣿⠛⠋⠉⠉⢻⣿⣿⣿⣿⡇⡀⠘⣿⣿⣿⣷⣿⣿⣿⠛⠻⢿⣿⣿⣿⣿⣷⣦
# ⣿⣿⣧⡀⠿⠇⣰⣿⡟⠉⠉⢻⡆⠈⠟⠛⣿⣿⣿⣯⡉⢁⣀⣈⣉⣽⣿⣿⣿⣷
# ⡿⠛⠛⠒⠚⠛⠉⢻⡇⠘⠃⢸⡇⢀⣤⣾⠋⢉⠻⠏⢹⠁⢤⡀⢉⡟⠉⡙⠏⣹
# ⣿⣦⣶⣶⢀⣿⣿⣿⣷⣿⣿⣿⡇⢀⣀⣹⣶⣿⣷⠾⠿⠶⡀⠰⠾⢷⣾⣷⣶⣿
# ⣿⣿⣿⣿⣇⣿⣿⣿⣷⣿⣿⣿⣇⣰⣿⣿⣷⣿⣿⣷⣤⣴⣶⣶⣦⣼⣿⣿⣿⣷
# '''
# )



# while True :
#         print("무~야~호~♬ ",end = '')
#         print("무~야~호~♪ ",end = '')
#         print( '''

#         ⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢠⣴⣾⣿⣶⣶⣆⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀
#         ⢀⢀⢀⣀⢀⣤⢀⢀⡀⢀⣿⣿⣿⣿⣷⣿⣿⡇⢀⢀⢀⢀⣤⣀⢀⢀⢀⢀⢀
#         ⢀⢀ ⣶⢻⣧⣿⣿⠇ ⢸⣿⣿⣿⣷⣿⣿⣿⣷⢀⢀⢀⣾⡟⣿⡷⢀⢀⢀⢀
#         ⢀⢀⠈⠳⣿⣾⣿⣿⢀⠈⢿⣿⣿⣷⣿⣿⣿⣿⢀⢀⢀⣿⣿⣿⠇⢀⢀⢀⢀
#         ⢀⢀⢀⢀⢿⣿⣿⣿⣤⡶⠺⣿⣿⣿⣷⣿⣿⣿⢄⣤⣼⣿⣿⡏⢀⢀⢀⢀⢀
#         ⢀⢀⢀⢀⣼⣿⣿⣿⠟⢀⢀⠹⣿⣿⣿⣷⣿⣿⣎⠙⢿⣿⣿⣷⣤⣀⡀⢀⢀
#         ⢀⢀⢀ ⢸⣿⣿⣿⡿⢀⢀⣤⣿⣿⣿⣷⣿⣿⣿⣄⠈⢿⣿⣿⣷⣿⣿⣷⡀⢀
#         ⢀⢀⢀⣿⣿⣿⣿⣷⣀⣀⣠⣿⣿⣿⣿⣷⣿⣷⣿⣿⣷⣾⣿⣿⣿⣷⣿⣿⣿⣆
#         ⣿⣿⠛⠋⠉⠉⢻⣿⣿⣿⣿⡇⡀⠘⣿⣿⣿⣷⣿⣿⣿⠛⠻⢿⣿⣿⣿⣿⣷⣦
#         ⣿⣿⣧⡀⠿⠇⣰⣿⡟⠉⠉⢻⡆⠈⠟⠛⣿⣿⣿⣯⡉⢁⣀⣈⣉⣽⣿⣿⣿⣷
#         ⡿⠛⠛⠒⠚⠛⠉⢻⡇⠘⠃⢸⡇⢀⣤⣾⠋⢉⠻⠏⢹⠁⢤⡀⢉⡟⠉⡙⠏⣹
#         ⣿⣦⣶⣶⢀⣿⣿⣿⣷⣿⣿⣿⡇⢀⣀⣹⣶⣿⣷⠾⠿⠶⡀⠰⠾⢷⣾⣷⣶⣿
#         ⣿⣿⣿⣿⣇⣿⣿⣿⣷⣿⣿⣿⣇⣰⣿⣿⣷⣿⣿⣷⣤⣴⣶⣶⣦⣼⣿⣿⣿⣷
#         ''')

'''
while 문법
while 조건식: 조건에 만족하면(true) 반복적으로 돌고, false면 빠져나감
'''

# 고객 = "이민호"
# index = 5
# while index >= 1 :
#     print(f"{고객}님 주문하신 것을 받아가세요.{index}")
#     index = index - 1
#     if index == 0:
#         print("주문을 취소하겠다.")

