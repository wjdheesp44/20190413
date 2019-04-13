a = int(input("첫 번째 정수 입력 : "))
b = int(input("두 번째 정수 입력 : "))
op = input("연산자 입력 : ")

if op == "+":
    print(a + b)
elif op == "-":
    print(a - b)
elif op == "*":
    print(a * b)
elif op == "/":
    print(a / b)
else:
    print("Unknown operator")
