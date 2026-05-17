def conversion(cel):
    faren = (cel*1.8)+32
    return faren

cel = float(input("Enter temperature in Celsius: "))
print(f"{cel} degrees Celsius is equal to {conversion(cel)} degrees Fahrenheit.")


