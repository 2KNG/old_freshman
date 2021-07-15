'''
jumin="000101-1234567" #index 0~ 방 0~ 첨자 0~ 모두 0부터 시작
print("성별:"+jumin[7])
print("연:"+jumin[0:2]) #0부터 2까지
print("월:"+jumin[2:4]) #2부터 4까지
print("일:"+jumin[4:6]) #4부터 6까지
print("생년월일:"+jumin[:6]) #처음부터부터 6전까지
print("뒷자리:"+jumin[7:])
print("뒷자리:"+jumin[-7:])
'''
#문자열 함수
# temp = "bye Hello"
# print(temp.lower())
# print(temp.upper())
# print(temp[0].isupper()) #는 같냐?(=) 라는뜻 
# print(len(temp)) #길이정보(length)
# print(temp.replace('Hello','world')) #temp=world 교체후 출력
# a=temp.index("l")
# print(a)
# print(temp)
# print(temp.find("Hello")) #존재하면 위치값출력, 없으면 -1
# print(temp.index("Hello")) #존재하면 위치값출력, 없으면 에려
# print(temp.count("l"))

print("나의 이름은 %s 입니다." % "홍길동")
print("나이는 %d세입니다." %18)
print("키는 %lf 입니다."%158.5)
print("나의 이름과 나이는 %s, %d세 입니다." %("홍길동",18))
print("나의 이름은 {1}ㄴ이고 나이는 {1}세 입니다" .format("홍길동",18)) #.format()은 한 덩어리
print("나의 이름은 {name}이고 나이는 {age}세 입니다" .format(name="홍길동",age=18))

name="홍길동"
age=19
print("나의 이름은 %s이고 나이는 %d세 입니다" %(name, age))
print(f"나의 이름은 {name}이고 나이는 {age}세 입니다.")
kor, eng, mat=input().split() #공백을 넣어서 3개의 값을 입력받음 ex)76 56 35
ikor=int(kor)
ieng=int(eng)
imat=int(mat)
avg=(ikor+ieng+imat)/3
print(avg)