def sum(n):
    if(n == 0):
        return 0
    return n + sum(n-1)

n = int(input("Enter a number: "))
print(f"The sum of {n} natural numbers is: {sum(n)}")