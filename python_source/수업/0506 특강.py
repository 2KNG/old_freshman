'''
부모 클래스에 모든 내용을 상속받음
>> 상속클래스
'''

# class Person : #클래스를 선언 하는 부분 ...
#     def __init__(self,na,ag): #파라미터 (변수) 함수를 선언하는 부분... 
#         print(self, '지금 생성 되었어요!!!')
#         self.name = na
#         self.age = ag
    
#     def age_increment(self): # 나이먹는 함수. ...
#         self.age += 1

# p1 = Person('Jhon',23)
# p2 = Person('Justin',)

# print(p1.name, p1.age)
# p1.age_increment() # 나이먹띠...
# print(p1.name,p1.age)


class Counter: #클래스 정의
    def __init__(self):
        self.num = 0
    
    def increment(self):
        self.num += 1 #self.num = self.num +1

    def reset(self):
        self.num = 0 

    def print_current_value(self):
        print("Current_value :",self.num)