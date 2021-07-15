d = 100
f = 10.10
m = -99
p = 2
# s = str(1000)

# print(abs(m))
# print(pow(p,5))
# for i in range(11):
#     if i % 2 == 0:
#         continue
#     print(pow(p,i+1))

# print(max(m,p,f,d))
# print(min(d,f,m,p))

from math import*
# print(round(f))
# print(floor(f))
# print(ceil(f))

from random import*
# print(random()+1)
# print(random()*100)
# print(int(random()*10)+1)
for i in range(5):
    print(int(random()*45)+1)

print(round(random()*45)) # = 

k = random()*100
print(k)
print(round(k))
print(ceil(k))
print(floor(k))
print(randrange(1,46))
print(randint(1,45))

print(0xA5)
print(0b11011)
print(0o73)
print("%x" %165)
print("%o" %165)
# print("%x" %{}.format(k))

print(~5+1)
print(~4)
print(~-5)

a = '''
서울
우리집
강아지
'''

print(a)
print(a[0])
print(a[1])
print(a[2])
print(a[1:3])
print(a[1:2])
print("뉴뉴뉴뉴뉴뉴"+a[1:7])

sl = "abc"
su = "ABC"
sc = "abcDEF"
print(sc.lower())
print(sc.upper())

print(su.isupper())

print(sc.replace("abc","xyz"))
print(sc.find("F"))

print("우리집 강아지는 {견종}이고, 이름은 {강아지}입니다.".format(견종 = "포메라니안", 이름 = "단비"))
