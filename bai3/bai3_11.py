#họ và tên: Lê Tiến Lực
#Mssv: 245752021610103

def benefit(t, n, k):
    # Kiểm tra dữ liệu hợp lệ
    if t < 0 or n <= 0 or k <= 0:
        print("Giá trị nhập vào không hợp lệ!")
        return
    
    # Tính tiền nhận được sau k tháng (lãi kép hàng tháng)
    # Công thức: A = n * (1 + t/100) ** k
    amount = n * (1 + t / 100) ** k

    # In kết quả
    print(f"Số tiền nhận được sau {k} tháng là: {amount:.2f} VND")
    
try:
    t = float(input("Nhập lãi suất (%/tháng): "))
    n = float(input("Nhập số vốn ban đầu (VND): "))
    k = int(input("Nhập số tháng gửi: "))
    benefit(t, n, k)
except ValueError:
    print("Vui lòng nhập dữ liệu hợp lệ!")
