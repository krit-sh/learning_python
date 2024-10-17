a = 1
print(a)

username = input("Enter a username: ")

if len(username) > 12:
    print("This username is too long!")
elif not username.find(" ") == -1:
    print("This username contains spaces!")
elif not username.isalpha():
    print("Cannot contain numbers")
else:
    print(f"Welcome {username}!")
