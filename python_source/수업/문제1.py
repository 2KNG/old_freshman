def calc(a, op, b):
    x = a
    y = b
    if op == "+":
        print("{:.2f}{}{:.2f}={:.2f}".format(a, op, b, a+b))
    elif op == "-":
        print("{:.2f}{}{:.2f}={:.2f}".format(a, op, b, a-b))
    elif op == "*":
        print("{:.2f}{}{:.2f}={:.2f}".format(a, op, b, a*b))
    elif op == "/":
        print("{:.2f}{}{:.2f}={:.2f}".format(a, op, b, a/b))
    else :
        print('올바른 정수 및 연산자를 입력하세요')
calc(10,'+',2)
calc(10.5,'-',2.1)
calc(10,'*',5)
calc(12,'/',5)
calc(12,12,2)
