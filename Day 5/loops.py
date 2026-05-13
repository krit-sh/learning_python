i=1
while(i<6):
    print(i)
    i+=1

print("\n")

for i in range(1,6):
    print(i)

print("\n")

l = ["Ritesh", 1, "Anu", False, "Ghumi Ghumi"]
i=0
while(i<len(l)):
    print(l[i])
    i+=1

print("********************************")

print("\n",l)

print("\n")

for i in range(1,11):
    j=2
    print(j,"*",i,"=",i*j)
    # j+=1

print("\n Tables")

n = int(input("Enter a number: "))
i=1
while(i<=10):
    print(f"{n} * {i} = {n*i}")
    i+=1

print("\n")

print("Prime number or not")
n = int(input("Enter a number: "))
for i in range(2,n):
    if(n%2==0):
        print("Not Prime")
        break
else:
        print("Prime") 

print("\n Sum of n natural numbers")

n = int(input("Enter a number: "))
# i=0
sum=0
for i in range(1,n+1):
    sum+=i

print(sum)

print("\n Factorial")

n = int(input("Enter a number: "))
i=1
prod=1
while(i<=n):
    prod*=i
    i+=1
print(prod)

print("\nStar series")

n = int(input("Enter a number: "))
for i in range(1,n+1):
    print(" "*(n-i),end="")
    print("*"*(2*i-1),end="")
    print("")

print("\nStar series 2")
n = int(input("Enter a number:"))
for i in range(1,n+1):
    print("*"*(i),end="")
    print("")

