import random

computer = random.choice([-1, 0, 1])
youStr = input("Enter your choice (Snake, Water, Gun): ")
youDict = {"s": 1, "w": -1, "g": 0}
reversedYouDict = {1: "Snake", -1: "Water", 0: "Gun"}
you = youDict[youStr]

print(f"Computer chose: {reversedYouDict[computer]}")
print(f"You chose: {reversedYouDict[you]}")

if you == computer:
    print("It's a tie!")
elif (you == 1 and computer == -1) or (you == -1 and computer == 0) or (you == 0 and computer == 1):
    print("You win!")
else:
    print("Computer wins!")
