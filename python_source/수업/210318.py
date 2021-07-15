'''
#정수를 문자열로 변환 : str() 
# , 정수, 쉼표로 출력 시 , 정수를 str() 변환하지 않아도 되고 쉼표로 인해 공백이 하나 생김
# a=b 오른쪽에 있는 값을 왼쪽에 저장하라 라는 뜻
# () < 함수라고 읽는다
'''
#은 줄주석 '''은 여러문장 주석


# age=10;
# print("당신의 나이는 "+str(age)+"입니다")
# print("당신의 나이는 ",age,"입니다")

'''
산술 연산자
파이썬또는 자바에서는 정수를 정수로 나누면 소숫점 값까지 모두 출력한다 
%는 나머지 // 는 몫이다
'''

# print(10+3)
# print(10-3)
# print(10*3)
# print(10/3)
# print(10%3)
# print(10//3)


'''
관계연산자
==은 같냐? 라고 물어보는것 3==3 ture
!=는 아니냐? 라고 물어보는것 4!=3 ture
'''

# print(3==3)
# print(4!=3)
# print(4<=3)

'''
우선순위
산술(+,-,*,/,%,//)>관계(==,!=,>=)>논리(not, and, or)
and는 & or은 |(돈표시 + shift)
'''

# print((3>1) & (2>3))
# print((3>1) | (2>3))
# print(not (2>3))

'''
대입연산자
'''

# num=10
# print(num)
# num=num+2 #num+=2 #< 1씩 증가
# print(num)
# num+=2
# print(num)
# num=num-2 #num-=2
# print(num)
# num=num*2 #num*=2
# print(num)
# num=num/2 #num/=2
# print(num)

'''
숫자함수
abs : 절대값
pow : 제곱 pow(3,2) #9
max : 최댓값
min : 최솟값
round : 소수이하 반올림
***import 사용 시 무 적권 윗쪽에 사용(예의가 없다)***
from math import * 사용 시
floor : 작은 정수로 변환
ceil : 큰 정수로 변환
from random import * 사용 시
random() : 0~1 정수, 소숫값(실수)
int(random()*6) : #1~6 (6개) 
int를 넣어야 소숫점이 안나오고 정수값이 나옴
int(난수*개수)+초기치
randrange(n1,n2) #n1부터 n2미만까지 (정수)
randint(n1,n2) #n1부터 n2까지 (정수)
'''

# print(abs(-5))
# print(pow(3,3))
# print(max(5,10,20))
# print(min(5,10,20))
# print(round(3.14))
# print(round(3.54))
# from math import *
# print(floor(-3.5))
# print(ceil(-3.5))
# print(floor(3.5))
# print(ceil(3.5))
# from random import *
# print(random())
# print(int(random()*6)+1) #1~6 사이 랜덤
# print(int(random()*45)+1) #1~45 사이 랜덤
# # int(난수*개수)+초기치
# print(randrange(1,46)) #1부터 46미만까지
# print(randint(1,45)) #1부터 45까지

'''
코딩도장
ID
it2161110053
PW
khkim1207
'''