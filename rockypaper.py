from random import randint

robobot = randint(0, 2) #Generate a random number from 0 to 2 (possibilities: 0, 1, 2)
#                                           0: rock, 1: paper, 2: scissors
player = input("Rock, paper, or scissors? ")
player = player.lower()
def ask(robo):
    if player == "rock":
        if robo == "0":
            print("Tie game!")
        elif robo == "1":
            print("The computer won :(")
        elif robo == "2":
            print("You Win! Nice job, you shattered the computer.")
        else:
            print("An error occured while parsing the move.")
    elif player == "paper":
        if robo == "0":
            print("You Win! Nice job, you covered the computer. \nHey look, it's overheating!")
        elif robo == "1":
            print("Tie game!")
        elif robo == "2":
            print("The computer won :(")
        else:
            print("An error occured while parsing the move.")
    elif player == "scissors":
        if robo == "0":
            print("The computer won :(")
        elif robo == "1":
            print("You win! Nice job, you cut the computer. \nNot sure how you cut metal, but I'll still say you won.")
        elif robo == "2":
            print("Tie game!")
        else:
            print("An error occured while parsing the move.")
    else:
        print("You did not choose a valid move.")
ask(robobot)
