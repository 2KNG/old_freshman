import csv
# in_file = open("excel_data.csv", "r")
# data = csv.reader(in_file)
# for i in data :
#     print(i)
# in_file.close()

# with open("aa/excel_data2.csv", "w", encoding="utf-8-sig", newline="") as out_file: # newlinee 을 안박으면 개손해
#     data = csv.writer(out_file, delimiter=",")
#     data.writerow([i for i in range(1,3)])
#     data.writerow([i*10 for i in range(1,3)])



with open("aa/excel_data3.csv", "w", encoding="utf-8", newline="") as out_file :
    data = csv.DictWriter(out_file, fieldnames = ['name', 'age'])
    data.writeheader()
    data.writerow({"name":"hong", "age":10})
    data.writerow({"name":"kim", "age":18})

# # 읽기

# with open("aa/excel_data3.csv", "r", encoding="utf-8-sig") as  in_file:
#     data = csv.DictReader(in_file)
#     for line in data:
#         print(line)
    
