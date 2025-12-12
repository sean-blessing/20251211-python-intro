# while loops
#generate 10 random die rolls
import random as r

i = 0
while i < 10:
    die_roll = r.randint(1,6)
    #print("die roll",i, ":", die_roll)
    print(f"die roll[{i}]: {die_roll}")
    i += 1

# while statement to control flow of a game
choice = "y"
while choice.lower() == "y":
    print(f"You rolled {r.randint(1,6)}.")
    choice = input("Continue? (y/n) ")
print("Bye!")