#họ và tên: lê tiến lực
#MSSV: 245752021610103

# Danh sách cần ghi vào file
my_list = ['hello', 'sinh vien', 'nganh', 'ky thuat đktđh']

with open('D:/a.txt', 'w', encoding='utf-8') as f:
    for item in my_list:
        f.write(item + '\n') 
        print(item)
       
