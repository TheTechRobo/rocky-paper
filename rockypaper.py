from random import randint

robobot = randint(0, 2) #Generate a random number from 0 to 2 (possibilities: 0, 1, 2)
if robobot == 0:
    robobotMove = "rock"
elif robobot == 1:
    robobotMove = "paper"
elif robobot == 2:
    robobotMove = "scissors"
else:
    print("An error occured while choosing a move.")
player = input("Rock, paper, or scissors? ")
player.lower()
if player == rock:
    if robobotMove == "rock":
        print("Tie game!")
    elif robobotMove == "paper":
        print("The computer won :(")
    elif robobotMove == "scissors":
        print("You Win! Nice job, you shattere the computer.")
    else:
        print("An error occured while parsing the move.")
elif player == "paper":
    if robobotMove == "rock":
        print("You Win! Nice job, you covered the computer. \nHey look, it's overheating!")
    elif robobotMove == "paper":
        print("Tie game!")
    elif robobotMove == "scissors":
        print("The computer won :(")
    else:
        print("An error occured while parsing the move.")
elif player == "scissors":
    if robobotMove == "rock":
        print("The computer won :(")
    elif robobotMove == "paper":
        print("You win! Nice job, you cut the computer. \nNot sure how you cut metal, but I'll still say you won.")
    elif robobotMove == "scissors":
        print("Tie game!")
    else:
        print("An error occured while parsing the move.")
else:
    print("You did not choose a valid move.")
