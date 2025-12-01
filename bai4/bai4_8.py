#họ và tên: Lê Tiến Lực
#Mssv:245752021610103

ds = input(" nhập dãy từ:").split()
maxlen = max(len(W) for W in ds)
for W in ds:
    if len(W) == maxlen:
        print(W)
