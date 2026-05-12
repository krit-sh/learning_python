friends = ["Apple", "Orange", 5, 7.69, False, "Ritesh"]
print(friends)

friends.append("Anu")
print(friends)

n = len(friends)
print("Length of Lists is: ", n)

friends2 = ["Apple", "Orange", "Ritesh", "Anu"]
print(sorted(friends2))

l1 = [2,3,4,56,7,54]
l1.sort()
l1.reverse()
print(l1)

friends2.insert(2, 32423)
print(friends2)

friends2.pop(2)
print(friends2)