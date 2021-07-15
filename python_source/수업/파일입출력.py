import sys

out_file = open("test.txt","w",encoding = "utf-8") #w쓰기모드로 파일 open, encoding = "utf-8" 안처넣으면 다깨진다
print("국어 : 100", file = out_file)
print("영어 :  90", file = out_file)
out_file.close()

# xlsx = open("test.xlsx","w",encoding = "utf-8")
# print("\n","국어 : 100", file = xlsx)
# print("")
# xlsx.write("우리집 강아지는 복슬복슬 강아지 \n")
# xlsx.close()

with open ("test2.txt", "w",encoding = "utf-8") as out2_file:
    print("국어 : 100", file = out2_file)
    print("영어 :  90", file = out2_file)
    out2_file.write("과학 : 80\n")

with open ("sample.txt", "w", encoding = "utf-8") as out3_file:
    print("sample", end = "", file=out3_file)
    out3_file.write("테스트연습\n")

with open ("test11.txt", "a", encoding = "utf-8") as out4_file:
    out4_file.write("과학 : 80\n")
    out4_file.write("우리집 강아지 : 단비\n")

