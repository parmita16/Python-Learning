a = int(input("Enter first side: "))
b = int(input("Enter second side: "))
c = int(input("Enter third side: "))

if a*a + b*b == c*c or a*a + c*c == b*b or b*b + c*c == a*a:
    print("Right Triangle")
else:
    print("Not Right Triangle")