from random import randint
import tkinter as gui
def rock():
    player = "rock"
    ask(robobot, player)
def paper():
    player = "paper"
    ask(robobot, player)
def scissors():
    player = "scissors"
    ask(robobot, player)
rockypaper = gui.Tk()
rockypaper.title("rockyPaper GUI")
robobot = randint(0, 2) #Generate a random number from 0 to 2 (possibilities: 0, 1, 2)
#                                           0: rock, 1: paper, 2: scissors
gui.Label(text="Choose an item:").pack()
gui.Button(text="Choose rock", command=rock).pack()
gui.Button(text="Choose paper", command=paper).pack()
gui.Button(text="Choose scissors", command=scissors).pack()
def ask(robo, player):
    if player == "rock":
        if robo == 0:
            gui.messagebox.showinfo("The results are in", "Tie game!")
        elif robo == 1:
            gui.messagebox.showerror("Results are in!", "The computer won :(")
        elif robo == 2:
            gui.messagebox.showinfo("Yayyyyy!", "You Win! Nice job, you shattered the computer.")
        else:
            gui.messagebox.showerror("An error occured while parsing the move.")
    elif player == "paper":
        if robo == 0:
            gui.messagebox.showinfo("The results have arrived!", "You Win! Nice job, you covered the computer. \nHey look, it's overheating!")
        elif robo == 1:
            gui.messagebox.showinfo("I received a letter", "It says: Tie game!")
        elif robo == 2:
            gui.messagebox.showerror("I'm sad", "The computer won :(")
        else:
            gui.messagebox.showerror("Error!", "An error occured while parsing the move.")
    elif player == "scissors":
        if robo == 0:
            gui.messagebox.showerror(":(", "The computer won :(")
        elif robo == 1:
            gui.messagebox.showinfo("YAYAYAYAY!!! :D", "You win! Nice job, you cut the computer. \nNot sure how you cut metal, but I'll still say you won.")
        elif robo == 2:
            gui.messagebox.showinfo("Well, it's not BAD exactly...", "Tie game!")
        else:
            gui.messagebox.showerror("Error!", "An error occured while parsing the move.")
    else:
        gui.messagebox.showerror("I am mad at you", "You did not choose a valid move.")
rockypaper.mainloop()
