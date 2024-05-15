#rolls dice for first player
import random
total = 0
score = 0
print ("\n\n\nplayer1's go!!")
play=input("press enter to roll!")
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
play=input("press enter to roll!")
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

    
    
