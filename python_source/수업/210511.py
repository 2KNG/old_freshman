# class Math:
#     def add(self,a,b):        
#         return a+b

#     def mul(self,a,b):
#         return a*b

# m = Math()

# print(m.add(4,5))
# print(m.mul(4,5))

# class Math:
#     @staticmethod #정적 메쏘드
#     def add(a,b):        
#         return a+b

#     @staticmethod
#     def mul(a,b):
#         return a*b
#  #self 가 없다.
# m = Math()

# print(m.add(4,5))
# print(m.mul(4,5))


# #class 상속 
# class Person:

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def eat(self,food):
#         print('{}은 {}를 먹습니다.'.format(self.name,food))

#     def sleep(self,minute):
#         print('{}은 {}분을 잡니다.'.format(self.name,minute))

#     def work(self,minute):
#         print('{}은 {}를 일합니다..'.format(self.name,minute))




# class Student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

# class Empolyee:
#     pass

# jyp = Person('jyp',29)
# jyp.eat('apple')

# kkh = Student('kkh',29)
# kkh.sleep

# class Point:
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y

#     def __add__(self,pt):
#         new_x = self.x + pt.x
#         new_y = self.y + pt.y
#         return Point(new_x, new_y)

#     def print_pt(self):
#         print('{},{}'.format(self.x,self.y))

# p1 = Point(3,4)
# p2 = Point(5,6)
# # p3 = p1.add(p2)
# p3 = p1+p2
# p1.print_pt()
# p3.print_pt()