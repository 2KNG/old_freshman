with open("aa/test.txt", "w", encoding = "utf-8-sig") as out_file :
# utf-8 = 유니코드방식 utf-8 로 하면 무난하게 실행이 가능
# 애플이나 리눅스 파일엔 맨앞에 utf 가 맨 앞에 부터 있는데 그걸 무시하려면
# sig(시그니처)를 붙여준다

    out_file.write("국어 : 100\n")
    out_file.write("영어 : 90\n")
    out_file.write("수학 : 80\n")
    out_file.write("과학 : 70\n")

'''
with open () as 를 사용하기 위해서는
들여쓰기를 꼭해주자
'''

with open("aa/test.txt", "r", encoding="utf-8-sig") as in_file:
    # print(in_file.read())
    print(in_file.readline(), end = '')
    # = 
    print(in_file.readline().rstrip())
    print(in_file.readline().rstrip())
    print(in_file.readline().rstrip())

# =

with open("aa/test.txt", "r", encoding="utf-8-sig") as in_file2:
    while True:
        line = in_file2.readline()
        if not line:
            break
        print(line, end = "")