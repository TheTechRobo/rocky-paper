from random import randint

robobot = randint(0, 2) #Generate a random number from 0 to 2 (possibilities: 0, 1, 2)
#                                           0: rock, 1: paper, 2: scissors
else:
    print("An error occured while choosing a move.")
player = input("Rock, paper, or scissors? ")
player.lower()
if player == "rock":
    if robobotMove == "0":
        print("Tie game!")
    elif robobotMove == "1":
        print("The computer won :(")
    elif robobotMove == "2":
        print("You Win! Nice job, you shattere the computer.")
    else:
        print("An error occured while parsing the move.")
elif player == "paper":
    if robobotMove == "0":
        print("You Win! Nice job, you covered the computer. \nHey look, it's overheating!")
    elif robobotMove == "1":
        print("Tie game!")
    elif robobotMove == "2":
        print("The computer won :(")
    else:
        print("An error occured while parsing the move.")
elif player == "scissors":
    if robobotMove == "0":
        print("The computer won :(")
    elif robobotMove == "1":
        print("You win! Nice job, you cut the computer. \nNot sure how you cut metal, but I'll still say you won.")
    elif robobotMove == "2":
        print("Tie game!")
    else:
        print("An error occured while parsing the move.")
else:
    print("You did not choose a valid move.")