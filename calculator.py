a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
c = input("Choose operation + - * /: ")

if c == "+":
    print(int(a+b))
elif c == "-":
    print(int(a-b))
elif c == "/":
    print(int(a/b))
elif c == "*":
    print(int(a*b))
else:
    print("Unknown operation.")