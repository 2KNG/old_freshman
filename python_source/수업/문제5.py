def Fibonacci(n):
    def Fibo(n):
        if n == 1 or n == 2 :
            return 1
        return Fibo(n-2) + Fibo(n-1)
    print("피보나치수열 ",n,"번째 값은 ",Fibo(n),"입니다.", sep="")



Fibonacci(5)
Fibonacci(8)
Fibonacci(100)



