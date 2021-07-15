n = 10
# for i in range(0,n):
#     print()
#     for j in range(0,n):
#         print("*",end="")

for i in range(0,n+1) :
    k = n-i
    print(" "*k, end = "")    
    for j in range(0,i):
        print("*", end = "")
    print("*"*(n-k-1))

#교수님 풀이

print(" "*(n-1),"*")
for i in range(1,n+1) :
    k = n-i
    print(" "*k, end = "")  
    print("*", end = "")
    for j in range(0,i):
        print(" ", end = "")  
    print(" "*(n-k-1),'*',sep="")
for i in range(n-1,0,-1) :
    k = n-i
    print(" "*k, end = "") 
    print("*", end = "") 
    for j in range(i,0,-1):
        print(" ", end = "")
    print(" "*(n-k-1),'*',sep="")
print(" "*(n-1),"*")

n =5
print(" "*(n-1),"*")
for i in range(1,n+1) :
    k = n-i
    print(" "*k, end = "")  
    print("*", end = "")
    print(" "*i, end = "")  
    print(" "*(n-k-1),'*',sep="")
for i in range(n-1,0,-1) :
    k = n-i
    print(" "*k, end = "") 
    print("*", end = "") 
    print(" "*i, end = "")
    print(" "*(n-k-1),'*',sep="")
print(" "*(n-1),"*")


n = int(input())


print(" "*(n-1),"*")

for i in range(1,n+1):
    print(" "*(n-i), end="")  
    print("*", end="")
    print(" "*i, end="")
    print(" "*(i-1) + '*')

    
for i in range(n-1,0,-1):
    print(" "*(n-i), end="")
    print("*", end="")
    print(" "*i, end="")
    print(" "*(i-1) + '*')
    
print(" "*(n-1),"*")