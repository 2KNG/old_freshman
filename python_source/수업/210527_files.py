for i in range(1,51):
    with open("aa/제"+str(i)+"주차.txt", "w", encoding="utf-8") as out_file:
        out_file.write("{}주차보고서\n".format(i))
        out_file.write("학번 : 000000\n")
        out_file.write("이름 : 홍길동\n")

import os

for i in range(1,100):
    if os.path.exists("aa/제"+str(i)+"주차.txt"):
        os.remove("aa/제"+str(i)+"주차.txt")