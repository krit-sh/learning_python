def avf_func():
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    c = int(input("Enter the third number: "))
    average = (a + b + c) / 3
    print("Average using function without parameters:", average)

avf_func()

def avf_func2(a, b, c):
    average = (a + b + c) / 3
    print("Average using function with parameters:", average)

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))
avf_func2(a, b, c)

def avf_func3(name, ending="Thank you"):
    print(f"Hello, {name}! {ending}")

avf_func3("Alice", "Thanks")
avf_func3("Ritesh")


def rec_func(n):
    if(n==1 or n==0):
        return 1
    return n * rec_func(n-1)

n = int(input("Enter a number: "))
print(f"Factorial of {n} is: {rec_func(n)}")
