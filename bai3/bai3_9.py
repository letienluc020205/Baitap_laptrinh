#họ và tên: Lê Tiến Lực
#Mssv: 245752021610103


# hàm này cộng hai số
def add(x, y):
    return x + y

# hàm này trừ hai số  
def subtract(x, y):
    return x - y

# hàm này nhân hai số 
def multiply(x, y):
    return x * y

# hàm này chia hai số 
def divide(x, y):
    return x / y

print("Select operation.") 
print("1. Add") 
print("2. Subtract") 
print("3. Multiply") 
print("4. Divide") 

# Take input from the user  
choice = input("Enter choice (1/2/3/4): ") 
num1 = float(input("Enter first number: ")) 
num2 = float(input("Enter second number: ")) 

if choice == '1': 
    print(num1, "+", num2, "=", add(num1, num2)) 
elif choice == '2': 
    print(num1, "-", num2, "=", subtract(num1, num2)) 
elif choice == '3': 
    print(num1, "*", num2, "=", multiply(num1, num2)) 
elif choice == '4': 
    # Kiểm tra chia cho 0
    if num2 == 0:
        print("Error! Division by zero.")
    else:
        print(num1, "/", num2, "=", divide(num1, num2)) 
else: 
    print("Invalid input")
