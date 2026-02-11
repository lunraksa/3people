import random
print("Hello")
randomgame =random.randint(1,3)
user=input("input rock paper scissors!; ")
if randomgame == 1 and user == "scissors":
    print("computer: rock, you input scissors so you lose")
elif randomgame == 1 and user == "rock":
    print("computer: rock, you input rock so we're draw")
elif randomgame == 1 and user == "paper":
    print("computer: rock, you input paper so you win")
elif randomgame == 2 and user == "scissors":
    print("computer: paper, you input scissors so you win")
elif randomgame == 2 and user == "paper":
    print("computer: paper, you input paper so you draw")
elif randomgame == 2 and user == "rock":
    print("computer: paper, you input rock so you lose")
elif randomgame == 3 and user == "rock":
    print("computer: scissors, you input rock so you win")
elif randomgame == 3 and user == "paper":
    print("computer: scissors, you input paper so you lsoe")
elif randomgame == 3 and user == "scissors":
    print("computer: scissors, you input scissors so you draw")


