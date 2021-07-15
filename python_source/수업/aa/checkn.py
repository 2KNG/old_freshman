
def Check(n):
    for x in range(2, n + 1):
        if n == x:
            return True
        else:
            if n % x == 0: # n % x == 0일 때만 break
                return False


n = int(input())
print(Check(n))



