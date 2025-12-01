#họ và tên: lê tiến lực
#MSSV: 245752021610103

# Danh sách cần ghi vào file
my_list = ['Python', 'Java', 'C++', 'JavaScript']

# Ghi danh sách vào file
with open('output.txt', 'w', encoding='utf-8') as f:
    for item in my_list:
        f.write(item + '\n')  # Ghi từng phần tử trên một dòng
