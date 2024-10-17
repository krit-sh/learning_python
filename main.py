# Variables
a = 1
print(a)

# strings

username = input("Enter a username: ")

if len(username) > 12:
    print("This username is too long!")
elif not username.find(" ") == -1:
    print("This username contains spaces!")
elif not username.isalpha():
    print("Cannot contain numbers")
else:
    print(f"Welcome {username}!")

# operators
# and or not are logical operators
n=3
print(n)
n=-n
print(n)

a=5
b=4
print(a<b and b<5)

# conditional statements
# if else elif
# == != > < >= <= is 
a = 5
b = 4
if a > b:
    print("a is greater than b")
elif a == b:
    print("a is equal to b")
else:
    print("a is less than b")

# iterator
colors = ["red", "green", "blue"]
for i in colors:
    print(i)

i=1
while i<5:
    print(i)
    i+=1

x=0
while not (1<=x<=100):
    x = int(input("Enter a number between 1 and 100: "))
print("valid no", x)

for i in range(4):
    x= int(input("Enter a number between 1 and 100: "))
    if 1<=x<=100:
        print("valid no", x)
        break
    else:
        print("invalid no")

# functions
def greet():
    print("Hello")
greet()

def greet(name):
    print(f"Hello {name}")
greet("Sub")

def find_avg_marks(marks):
    s= sum(marks)
    total=len(marks)
    avg=s/total
    return avg 

def grade(avg):
    if avg>=80:
        return "A"
    elif avg>=60:
        return "B"
    elif avg>=50:
        return "C"
    else:
        return "F"
marks=[55,64,75,80,65]
avg=find_avg_marks(marks)
print(avg)
print(grade(avg))

# dictionaries
# key value pairs
s = {"name":"Sub", "age":21, "sex":"M"}
s.get("name")
s["name"] = "Subu"

for key, value in s.items():
    print(key, value)

if "name" in s:
    print("name is present")

print(len(s))

s["year"] = 2003

s.pop("2003")

s.popitem()

del s["name"]

s_copy = s.copy()

tea_shop = {
    "chai": {"Masaala": 10, "Ginger": 15},
    "coffee": {"black": 20, "latte": 30}
}

print(tea_shop["chai"]["Masaala"])

# tuple
# immutable
t = (1,2,3,4,5)
print(t)

t = (1,)
print(t)

# set
# unordered
# no duplicates
s = {1,2,3,4,5}
print(s)


# list
# mutable
l = [1,2,3,4,5]
print(l)

l.append(6)

l.insert(2, 7)

l.remove(7)

l.pop(2)

l.clear()

