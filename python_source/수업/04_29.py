# for i in range(1,10):
#     if (i<4) :
#         print(i)
#     elif (i>7) :
#         print("우리집강아지")
#     else :
#         print("복슬강아지")

# a = 1
# while a <= 10:
#     if a % 2 == 0 :
#         print(a)
#     a = a + 1

# print("sum =", "sum")

# a=10
# while True :
#     print(a)
#     a = a + 1
#     if a > 10 :
#         break;


# a = 0
# cnt = 0
# while a < 10 :
#     a += 1
#     if (a % 3 == 0) :
#         cnt += 1
#         continue;
#     print(a, end=" ")
# print()
# print("3의 배수의 개수 :",cnt)

# k = int(input("!값 = "))
# m = 1
# print(k, "! = ", end = "", sep="")
# while k > 1 :  
#     m = m * k
#     print(k,"*",end="", sep="")
#     k -= 1

# print("1 =", m)

customer = "홍길동"
na = 0
cnt = 0
while na != customer :
    print("{}님 주문하신 커피가 준비되었습니다.".format(customer))
    na = input("당신의 이름은?")
    cnt += 1
    if cnt == 5 :
        break;
print("안해 ^^ㅣ발")
