#while
#1부터 100까지 출력(1,2,3,...100)
# i = 1                   #초기값
# while i<=100:           #조건  
#     print(f"i={i}")     
#     i=i+1               #1씩 증가


# i = 1
# sum = 0
# while i <=100:
#     sum+=i
#     i+=1
# print(f"sum={sum}")

#100부터 1까지 3의 배수들의 합계
i = 100
sum = 0
cnt = 0
while i > 0:
    if i % 3 == 0:
        cnt += 1
        sum += i
        print(f"i={i}")
    i -= 1
print(f"cnt={cnt}")
print(f"sum={sum}")
print(f"avg={sum/cnt}")