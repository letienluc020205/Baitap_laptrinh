#Họ và tên: Lê Tiến Lực
#Mssv: 245752021610103

class Nguoi:
    def getGender(self):
        return "unknown"
class Nam(Nguoi):
    def getGender(self):
        return "Nam"
class Nu(Nguoi):
    def getGender(self):
        return "nữ"
a = Nam()
b = Nu()
print(a.getGender())
print(b.getGender())
