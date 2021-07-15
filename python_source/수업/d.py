
def calc(a, op, b):
    x = a
    y = b
    if op == "+":
        re = a + b
    elif op == "-":
        re = a - b
    elif op == "*":
        re = a * b
    elif op == "/":
        re = a / b
    else :
        print('올바른 정수 및 연산자를 입력하세요')

    print("{:.1f} {} {:.1f} = {:.1f}".format(a, op, b, re))

calc(10,'+',2)
calc(10.5,'-',2.1)
calc(10,'*',5)
calc(12,'/',5)
