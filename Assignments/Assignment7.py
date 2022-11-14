# 0001 11/14/2022
## Begin Omar A. Student here (11/14/2022)

names = ['joe', 'tom', 'barb', 'sue', 'sally']
scores = [10, 23, 13, 18, 12]
scoreDict = {}

def makeDictionary():

    def addValue():
        print("Add a name")
        newName = input()
        print("Add a score")
        try:
            newScore = int(input())
            scoreDict[newName.lower()] = newScore
        except:
            print("Thats not a number")

    def deleteValue():
        print('Who do you want removed?')
        userInput = input()
        scoreDict.pop(userInput.lower())

    def dictQuery():
        print("Who's score do you want to look up")
        userInput = input()
        print(scoreDict[userInput.lower()])
        
    def modifySortedDict():
        sortedDict = sorted(scoreDict)
        print("Do you want to add, delete, query, print or exit?")
        userInput = input()
        if userInput.lower() == 'add':
            addValue()
            modifySortedDict()
        elif userInput.lower() == 'delete':
            deleteValue()
            modifySortedDict()
        elif userInput.lower() == 'query':
            dictQuery()
            modifySortedDict()
        elif userInput.lower() == 'print':
            print(sortedDict)
        elif userInput.lower() == 'exit':
            print()

    for x in names:
        scoreDict[x] = scores[names.index(x)]
    userAdd = True
    while userAdd:
        print(scoreDict)
        print("Do you want to add more to this list? y/n")
        userInput = str(input())
        if userInput.lower() == 'n':
            userAdd = False
            modifySortedDict()
        else:
            addValue()
        sortedDict = sorted(scoreDict)
            
makeDictionary()

# 0001 11/14/2022
## END Omar A. Student here (11/14/2022)
# AlphaBeta/ manager: Sam Loomis / lead tech: Robert Burke/ project #: LE9000