from random import randint
import tkinter
def rock():
    player = "rock"
def paper():
    player = "paper"
def scissors():
    player = "scissors"
rockypaper = tkinter.Tk()
rockypaper.title("rockyPaper GUI")
robobot = randint(0, 2) #Generate a random number from 0 to 2 (possibilities: 0, 1, 2)
#                                           0: rock, 1: paper, 2: scissors
tkinter.Label("text="Choose an item:").pack()
tkinter.Button(text="Choose rock", command=rock).pack()
tkinter.Button(text="Choose paper", command=paper).pack()
tkinter.Button(text="Choose scissors", command=scissors).pack()
def ask(robo):
    if player == "rock":
        if robo == 0:
            tkinter.messagebox.showinfo("The results are in", "Tie game!")
        elif robo == 1:
            tkinter.messagebox.showerror("Results are in!", "The computer won :(")
        elif robo == 2:
            tkinter.messagebox.showinfo("Yayyyyy!", "You Win! Nice job, you shattered the computer.")
        else:
            tkinter.messagebox.showerror("An error occured while parsing the move.")
    elif player == "paper":
        if robo == 0:
            print("You Win! Nice job, you covered the computer. \nHey look, it's overheating!")
        elif robo == 1:
            print("Tie game!")
        elif robo == 2:
            print("The computer won :(")
        else:
            print("An error occured while parsing the move.")
    elif player == "scissors":
        if robo == 0:
            print("The computer won :(")
        elif robo == 1:
            print("You win! Nice job, you cut the computer. \nNot sure how you cut metal, but I'll still say you won.")
        elif robo == 2:
            print("Tie game!")
        else:
            print("An error occured while parsing the move.")
    else:
        print("You did not choose a valid move.")
ask(robobot)
