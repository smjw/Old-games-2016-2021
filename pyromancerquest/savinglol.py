import csv
csvFile= open('scorecsv.csv')
csvFileContent=(csvFile)
next(csvFile)

teams=[]
def enterData():
        scoreData={'teamname':teamname,'gems':gem,'score':score}
        teams.append(scoreData)

        enterData()
