#họ và tên: lê tiến lực
#MSSV: 245752021610103

def copy_file(source, destination):
    with open(source, 'r', encoding='utf-8') as file_src:
        data = file_src.read()          # đọc toàn bộ nội dung

    with open(destination, 'w', encoding='utf-8') as file_dest:
        file_dest.write(data)           # ghi sang file mới

    print("Đã sao chép thành công!")

# Gọi hàm
copy_file('D:/a.txt', 'D:/b.txt')
