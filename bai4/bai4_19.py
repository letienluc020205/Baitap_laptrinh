#họ và tên: Lê Tiến Lực
#Mssv:245752021610103

def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i ==0:
            return False
    return True

p = tuple(i for i in range(2, 1_000_000) if is_prime(i))
print("tuple p gồm các số nguyên tố nhỏ hơn 1 triệu.")
print("ví dụ 10 số đầu tiên:", p[:10])
