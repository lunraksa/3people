import random
print("Hello")
i =0
j =0
while True :
 randomgame =random.randint(1,3)
 user=input("input rock paper scissors!; ")


 if randomgame == 1 and user == "scissors":
    print("computer: rock, you input scissors so you lose")
    j +=1
 elif randomgame == 1 and user == "rock":
    print("computer: rock, you input rock so we're draw")
 elif randomgame == 1 and user == "paper":
    print("computer: rock, you input paper so you win")
    i +=1
 elif randomgame == 2 and user == "scissors":
    print("computer: paper, you input scissors so you win")
    i +=1
 elif randomgame == 2 and user == "paper":
    print("computer: paper, you input paper so you draw")

 elif randomgame == 2 and user == "rock":
    print("computer: paper, you input rock so you lose")
    j +=1
 elif randomgame == 3 and user == "rock":
    print("computer: scissors, you input rock so you win")
    i +=1
 elif randomgame == 3 and user == "paper":
    print("computer: scissors, you input paper so you lsoe")
    j +=1
 else:
    print("computer: scissors, you input scissors so you draw")
 if i ==2:
   print("you success fully win")
   break
 elif j ==2:
   print("computer success fully win")
   break

