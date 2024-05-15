#Imported data from CSV file
import csv

csvFile = open ('playerbase.csv')
csvFileContent = (csvFile)
next (csvFile)

players = []

for row in csvFileContent:
    playerbase=row.strip().split(",")
    heading = ['firstname', 'surname', 'username', 'password']
    data = zip(heading,playerbase)
    playerDict = dict(data)
    players.append(playerDict)

print (players) # shows dictionary within a list



#check pupil exists on dictionary within list


username1 = input("please input username: ")
password1 = input("please input password: ")
for item in players:
    if item['username']!=username1:
        print ("incorrect username")
    elif item['password']!=password1:
        print ("incorrect password")
    elif item['username']==username1 and item['password']==password1:
        print ("welcome!")

username2 = input("\nplease input username: ")
password2 = input("please input password: ")
for item in players:
    if item['username']!=username2:
        print ("incorrect username")
    elif item['password']!=password2:
        print ("incorrect password")
    elif item['username']==username2 and item['password']==password2:
        print ("welcome!")



#rolls dice for first player
import random
total = 0
score = 0
print ("\n\n\nplayer1's go!!")
play=input("press enter to start!")
for number in range (5):
    dice1 = random.randrange(1,7)
    dice2 = random.randrange(1,7)
    print ("your dice are",dice1,"and",dice2)
    score = score + dice1 + dice2
    if score % 2 == 0:
        score = score + 10
    else:
        score = score -5
    if dice1 == dice2:
        print ("you rolled a double!!")
        dice3 = random.randrange(1,7)
        print ("extra roll:", dice3)
        score = score + dice3
    if score < 0:
        score= 0
    print ("this round's score:", score)
    total = total + score
print ("\nPlayer1's total is",total,"\n\n")

#rolls dice for second player
total2 = 0
score = 0
print ("player2's go!!")
play=input("press enter to start!")
for number in range (5):#this makes it 5 rounds
    dice1 = random.randrange(1,7)#these roll the dice
    dice2 = random.randrange(1,7)
    print ("your dice are",dice1,"and",dice2)
    score = score + dice1 + dice2
    if score % 2 == 0:#the following statements apply the rules
        score = score + 10
    else:
        score = score -5
    if dice1 == dice2:
        print ("you rolled a double!!")
        dice3 = random.randrange(1,7)
        print ("extra roll:", dice3)
        score = score + dice3
    if score < 0:
        score= 0
    print ("this round's score:", score)
    total2 = total2 + score
print ("\nPlayer2's total is",total2)

if total > total2:
    print ("\nplayer1 wins!!")
elif total2 > total:
    print ("\nPlayer2 wins!!")
else:
    print ("SUDDEN DEATH")
    SDdice1 = random.randrange(1,7)
    SDdice2 = random.randrange(1,7)
    print ("player1 got: ", SDdice1)
    print ("player2 got: ", SDdice2)

#saving scores to a CSV file
import csv
csvFile = open ('scoreboard.csv')
csvFileContent = (csvFile)
next(csvFile)

scoreboardList = []

for row in csvFileContent:
    scoreboard = row.strip().split(",")
    heading = ['username','score']
    data = zip(heading,scoreboard)
    scoreboardDict=dict(data)
    scoreboardList.append(scoreboardDict)

def enterData():
    scoreboardData={'username':username1, 'score':(total)}
    scoreboardData2={'username':username2, 'score':(total2)}
    scoreboardList.append (scoreboardData)
    scoreboardList.append (scoreboardData2)
    print(scoreboardList)

    saveData ()

def saveData():
    try:
        fileHandle = open ('scoreboard.csv','r+')
        filehandle.write('username,score\n')
        for item in scoreboardList:
            fileHandle.write('{username},{score}'.format(**item))
            fileHandle.write('\n')
        fileHandle.close()
    except OSError:
        print('can\'t write to file!')

enterData()
    
    
