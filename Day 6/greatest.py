def greatest(a,b,c):
    if a>b and a>c:
        print(f"{a} is greater than {b} and {c}")
    elif b>a and b>c:
        print(f"{b} is greater than {a} and {c}")
    elif c>b and c>a:
        print(f"{c} is greater than {a} and {b}")
    else:
        print("All numbers are equal")

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))
greatest(a, b, c)