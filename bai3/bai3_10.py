#họ và tên: Lê Tiến Lực
#Mssv: 245752021610103

import math  

def Tinh(R):
    # Kiểm tra bán kính hợp lệ
    if R <= 0:
        print("Giá trị bán kính không hợp lệ! Phải lớn hơn 0.")
        return
    
    # Tính chu vi và diện tích hình tròn
    chu_vi = 2 * math.pi * R
    dien_tich = math.pi * R ** 2

    # In kết quả
    print(f"Chu vi hình tròn là: {chu_vi:.2f}")
    print(f"Diện tích hình tròn là: {dien_tich:.2f}")

try:
    R = float(input("Nhập bán kính hình tròn: "))
    Tinh(R)
except ValueError:
    print("Vui lòng nhập một số hợp lệ!")
