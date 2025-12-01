#họ và tên: Lê Tiến Lực
#Mssv:245752021610103

chuoi= input("nhap chuoi:")
moi = ''
for ch in chuoi:
    if not ch.isalpha():
        moi += ch
print("chuoi moi:", moi)
