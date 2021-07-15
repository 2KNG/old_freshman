def ShowBit(n):
    k = [[0,0,0,0] for i in range(8)]   # 32bit 2차원 리스트 생성
    
    
    for i in range(7, -1, -1) :         # 첫번째 차원에 맨뒤부터 접근 후
        for j in range(3, -1, -1) :     # 두번째 차원 맨뒤로 접근한다.
            x = n // 2
            y = n % 2
            if x != 0 : 
                k[i][j] = y 
                n = x 
            else :
                k[i][j] = 1             # x == 0 이면 더 이상 나눌 값이 없음으로 
                break                   # 1을 마지막으로(MSB) 반복문 종료. 
        if x == 0 :                     # 바깥의 반복문도 x == 0 일 때 종료.
            break
            
    for i in range(8):
        for j in range(4):
            print(k[i][j], end = "")    # 리스트 처음부터 4자리씩 찍고,
        print(end = " ")                # 차원이 넘어갈 때 공백처리
    print()

ShowBit(2)
ShowBit(10)
ShowBit(1024)
from functools import reduce
ShowBit(reduce(lambda x, y : x + y, [2**i for i in range(32)]))


