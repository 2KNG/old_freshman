def DoubleNum(x,y) :
    try :
        if x % y == 0 :
            print(x, "는", y, "의 배수입니다.", sep = "")
        elif x % y != 0 :
            print(x, "는", y, "의 배수가 아닙니다.", sep = "")
        else:
            raise Exception
    except :
        print('올바른 숫자를 입력해주세요.')
        # 숫자를 넣지않으면 에려출력
DoubleNum(16,4)
DoubleNum(15.0,4.0)
DoubleNum("a","b")
