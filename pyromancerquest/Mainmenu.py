import turtle  # imports the various functions needed for 
from tkinter import*
import csv

csvFile = open('scorecsv.csv') # opens csv file so scores can be viewed
csvFileContent = (csvFile)
next (csvFile)

teams = []

for row in csvFileContent:
    scorecsv=row.strip().split(",")
    heading=['teamname','level', 'gems','score']
    data = zip(heading,scorecsv)
    scoreDict= dict(data)
    teams.append(scoreDict) #creates dictionary to present the top scores in a list


wn=turtle.Screen()
wn.title("Main Menu")
wn.bgcolor("white")
wn.bgpic('Titlescreen.png')
wn.setup(width=800,height=600)
wn.tracer(0) # sets up the window for the title screen and buttons

root = Tk()
root.title("enter team name") # makes window for the team name to be entered

e = Entry(root,width=50, bg="white", borderwidth=10)
e.pack()
e.insert(0,"Enter your teamname")



def saveTeamName(): # function to save the team name
    teamname=e.get()
    welcome="Welcome "+e.get()
    myLabel = Label(root, text=welcome) 
    myLabel.pack()

myButton = Button(root, text="Save team name?", padx=50, pady=30, command=saveTeamName, fg="black", bg="white")
myButton.pack() # button used to run the saveTeamName function

        
def myClick():
    myLabel= Label(root, text="level select")
    myLabel.pack()

def leaderboard(): # function to display the leaderboard
    leaderboardLabel=Label(root, text=teams)
    leaderboardLabel.pack()

def levelsList(): #function for the level select drop down menu 
    levels = [
        "Level 1",
        "Level 2",
        "Level 3",
    ]
    clicked = StringVar()
    clicked.set(levels[0])

    levelSelect = OptionMenu(root, clicked, *levels)
    levelSelect.pack()

def options(): #function for the controls to be displayed
    controls="Controls\n\n Player 1\n left arrow, right arrow, up arrow, down arrow\n\n Player 2\n W,A,S,D"
    controlLabel=Label(root, text=controls)
    controlLabel.pack()

def quit1(): # function to close the program
    root.destroy()

bLevelSelect= Button(text="Level Select",width=40, height=3)# defines the buttons that will run the functions
bOptions=Button(text="Options",width=40, height=3)
bLeaderboard=Button(text="leaderboard",width=40, height=3)
bQuitGame=Button(text="Quit Game",width=40, height=3)

bLevelSelect.pack() # puts the buttons on screen and makes them run the respective function
bLevelSelect.config(command=levelsList)
bOptions.pack()
bOptions.config(command=options)
bLeaderboard.pack()
bLeaderboard.config(command=leaderboard)
bQuitGame.pack()
bQuitGame.config(command=quit1)



while True: # main menu loop
    wn.update()
root.mainloop()

