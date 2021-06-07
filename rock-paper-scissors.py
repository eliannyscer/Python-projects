#from tkinter import *
from tkinter import *
from PIL import Image,ImageTk
from random import randint

#main window
root= Tk()
root.title("Rock-paper-scissors")
root.configure(background="black")

#pictures
rock_user= ImageTk.PhotoImage(image=Image.open("rock.png"))
paper_user= ImageTk.PhotoImage(image=Image.open("paper.png"))
scissor_user= ImageTk.PhotoImage(image=Image.open("scissor.png"))

rock_computer= ImageTk.PhotoImage(image=Image.open("rock-computer.png"))
paper_computer= ImageTk.PhotoImage(image=Image.open("paper-computer.png"))
scissor_computer= ImageTk.PhotoImage(image=Image.open("scissor-computer.png"))

#Insert pictures
user_label= Label(root, image= rock_user,bg= "black")
computer_label= Label(root,image= scissor_computer, bg= "black")
computer_label.grid(row=1, column=0)
user_label.grid(row=1, column=4)

#Scores
PlayerScore= Label(root,text= 0, font= 100, bg= "black", fg= "white")
ComputerScore= Label(root,text= 0, font= 100, bg= "black", fg= "white")
PlayerScore.grid(row= 1,column= 1)
ComputerScore.grid(row= 1,column= 3)

#Indicators
user_indicator= Label(root, font= 50, text= "USER",bg= "black", fg= "white")
computer_indicator= Label(root, font= 50, text= "COMPUTER",bg= "black", fg= "white")

user_indicator.grid(row= 0, column= 3)
computer_indicator.grid(row= 0, column= 1)

#Messages
msg = Label(root, font= 50, bg= "black", fg= "white")
msg.grid(row= 3, column= 2)

#We add later
#Update message

def update_message(x):
    msg['text'] = x

#Update user score
def update_user_score():
    score = int(PlayerScore["text"])
    score = score + 1
    PlayerScore["text"] = str(score)


#Update computer score
def update_comp_score():
    score = int(ComputerScore["text"])
    score = score + 1
    ComputerScore["text"] = str(score)


#Check winner

def check_winner(player,computer):
    if player == computer:
        update_message("It's A Tie!")
    elif player == "rock":
        if computer == "paper":
            update_message("You Lose!")
            update_comp_score()
        else:
            update_message("You Win!")
            update_user_score()
    elif player == "paper":
        if computer == "scissor":
            update_message("You Lose!")
            update_comp_score()
        else: 
            update_message("You Win!")
            update_user_score()
    elif player == "scissor":
        if computer == "rock":
            update_message("You lose!")
            update_comp_score()
        else:
            update_message("You win!")
            update_user_score()
    else:
        pass

#Update choices
choices = ["rock", "paper", "scissor"]
def updatechoices(x):

#For computer
    comp_choices = choices[randint(0,2)]
    if comp_choices == "rock":
        computer_label.configure(image= rock_computer)
    elif comp_choices == "paper":
        computer_label.configure(image=paper_computer)
    else:
        computer_label.configure(image=scissor_computer)
#For user    
    if x == "rock":
        user_label.configure(image=rock_user)
    elif x == "paper":
        user_label.configure(image=paper_user)
    else:
        user_label.configure(image=scissor_user)

    check_winner(x,comp_choices)

#Buttons
rock= Button(root, width= 20, height= 2, text= "ROCK",
        bg= "#FF3E4D", fg= "white", command = lambda:updatechoices("rock")).grid(row= 2, column= 1)
paper= Button(root, width= 20, height= 2, text= "PAPER",
            bg= "#FAD02E", fg= "white", command = lambda:updatechoices("paper")).grid(row= 2, column= 2)
scissor= Button(root, width= 20, height= 2, text= "SCISSOR",
        bg= "#0ABDE3", fg= "white", command = lambda:updatechoices("scissor")).grid(row= 2, column= 3)



root.mainloop()
