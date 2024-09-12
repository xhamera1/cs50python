input = input("Expression: ")
x, y, z = input.split()
if y == "+":
    res = int(x) + int(z)
    print(float(res))
elif y == "*":
    res = int(x) * int(z)
    print(float(res))
elif y == "-":
    res = int(x) - int(z)
    print(float(res))
elif y == "/":
    res = float(x) / float(z)
    print(float(res))
else:
    print("incorrect input")
