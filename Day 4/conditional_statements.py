m1 = int(input("Enter m1: "))
m2 = int(input("Enter m2: "))
m3 = int(input("Enter m3: "))

percent = (m1+m2+m3)*(100/300)

if(percent>=40 and m1>=33 and m2>=33 and m3>=33):
    print("PASS")
else:
    print("FAIL")