def Fatorial(x):
    def Fatorialmul(x) :
        if x != 1 :
            return x * Fatorialmul(x-1)
        return 1
    print(Fatorialmul(x))

Fatorial(5)
Fatorial(10)

'''
print(Factorial(n)) 이 번거로움으로 print 를 함수에 지정하여 
Factorial(n) 만 입력하면 터미널에 출력되도록 변경 
'''
