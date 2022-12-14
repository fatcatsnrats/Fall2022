# 0001 11/14/2022
## Begin Omar A. Student here (11/14/2022)

import random

dataBase = {}
queryInput = ''
name = ["Meera Hackett",
    "Demi-Lee Lord",
    "Konnor Kendall",
    "Keyaan Keith",
    "Ocean Lennon",
    "Cathy Villa",
    "Mert Lam",
    "Ibrahim Alston",
    "Kashif Shannon",
    "Lenny Frye",
    "Olaf Moreno",
    "Izabella Burgess",
    "Ellesse Ellison",
    "Molly Derrick",
    "Cecelia Choi",
    "Ayat Werner",
    "Yasser Butler",
    "Hajra Sears",
    "Umaima Mitchell",
    "Amelia-Lily Finch",
    "Rajveer Craft",
    "Shanice Hutchinson",
    "Evie-Mai Cassidy",
    "Saoirse Hollis",
    "Luciano Grainger"]

address = ["19 Ocean Street, Lawrence, MA 01841",
    "58 S. County Court, Clinton Township, MI 48035",
    "465 Brown Street, Trumbull, CT 06611",
    "8615 Overlook Lane, Bethesda, MD 20814",
    "7629 Baker Court, Willingboro, NJ 08046",
    "134 Trusel Street, Rock Hill, SC 29730",
    "345 E. Windfall Ave, Little Rock, AR 72209",
    "8948 Lyme Ave, Teaneck, NJ 07666",
    "395 Colonial Ave, Warren, MI 48089",
    "7916 Spring Avenue, Naples, FL 34116",
    "7377 N. Carriage Ave, Brainerd, MN 56401",
    "56 N. High Point St, Moses Lake, WA 98837",
    "649 S. Pin Oak Avenue, Sewell, NJ 08080",
    "887 W. Market Lane, Mchenry, IL 60050",
    "99 Del Monte Street, Willoughby, OH 44094",
    "187 Nut Swamp Circle, Mount Airy, MD 21771",
    "46 Prince Dr, Bay City, MI 48706",
    "189 North Shadow Brook Dr, Ithaca, NY 14850",
    "904 Circle Drive, Jeffersonville, IN 47130",
    "8793 Corona Ave, West Fargo, ND 58078",
    "65 Pulaski Street, Hixson, TN 37343",
    "644 Newport Street, Revere, MA 02151",
    "3 S. Princess Court, Mount Prospect, IL 60056",
    "50 Ryan Drive, Centereach, NY 11720",
    "469 Ridgewood Rd, Cookeville, TN 38501"]

skills = ["Carpentry",
    "Agriculture",
    "Hiding",
    "Tinkering",
    "Listening",
    "Clowning",
    "Construction",
    "Boating",
    "Burying",
    "Locksmith"]

# This method generates all random fields. It takes two arguments:
# what type of field it needs to generate ('type') and how many
# characters it needs to generate ('length').
def numberGenerator(length, type):
    tempInt = ""

    for i in range(0,length):
        tempInt += str(random.randint(0,9))

    if type == 'Phone':
        return ("(" + tempInt[:3] + ")-" + tempInt[3:6] + "-" + tempInt[6:])
    elif type == 'SSN':
        return (tempInt[:3] + "-" + tempInt[3:5] + "-" + tempInt[5:])
    elif type == 'ID':
        return (tempInt[:8] + "-" + tempInt[8:])
    elif type == 'Manager':
        if tempInt == '0':
            return "Yes"
        return "No"
    elif type == 'Job Title':
        jobInt = int(tempInt)
        if jobInt < 5:
            return "Software Engineer"
        elif jobInt < 9:
            return "Data Analyst"
        return "Lawyer"
    elif type == 'Skills':
        tempStr = ''
        for x in range (0,3):
            tempStr += skills[int(tempInt[x])]
            if x < 2:
                tempStr += ", "
        return tempStr

# This method querys the database. It loops through the database and prints
# any matching entries in the database.
def databaseQuery(queryType, query):
    counter = 0
    for x in range(0, len(dataBase)):
        if query.lower() in dataBase[x][queryType].lower():
            print(dataBase[x])
            counter += 1
    if counter == 0:
        print("No results found.")

# This method checks to make sure the users inputs are legal
# and takes two arguments.
def checkInput(expected1, expected2):
    userInput = input().lower()
    while ((not (userInput == expected1))
        and (not (userInput == expected2))):
        print("That was not an acceptable response. Type '"
            + expected1.capitalize() + "' or '" 
            + expected2.capitalize() + "'.")
        userInput = input().lower()
    return userInput

# This method checks to make sure the users inputs are legal and takes
# three arguments. I made these before I learned about *args.
def checkInput3(expected1, expected2, expected3):
    userInput = input().lower()
    while ((not (userInput == expected1))
        and (not (userInput == expected2))
        and (not (userInput == expected3))):
        print("That was not an acceptable response. Type '",
            expected1.capitalize(), "', '",
            expected3.capitalize(), "' or '", 
            expected2.capitalize(), "'.")
        userInput = input().lower()
    return userInput

# This method will either generate a database or manually add entries
# to the database depending on what the user desires.
def DatabaseGenerator(*args, generate= False, userAnswer= None, tempDict= {}):
    if not generate:
        print ("Do you want to 'randomly' generate a database?")
        userAnswer = input().lower()
    if userAnswer == 'no':
        counter = 0
        addPerson = True
        while addPerson:
            # This is where entries are manually added.
            tempInput = input('Input a Unique ID:\n')
            while not isinstance(tempInput, int):
                try:
                    tempInput = int(tempInput)
                except:
                    print("That was not a number. Input their Unique ID "
                        + "without special characters:")
                    tempInput = input()
            tempDict.update({"UniqueID" : str(tempInput)})
            print("Input their name:")
            tempDict.update({"Name" : input()})
            print("Input their address:")
            tempDict.update({"Address" : input()})
            print("Input their phone number without special characters:")
            tempInput = input()
            while not isinstance(tempInput, int):
                try:
                    tempInput = int(tempInput)
                except:
                    print("That was not a number. Input their phone number "
                        + "without special characters:")
                    tempInput = input()
            tempDict.update({'Phone' : str(tempInput)})
            print("Input their Social Security Number "
                + "without special characters:")
            tempInput = input()
            while isinstance(tempInput, int) == False:
                try:
                    tempInput = int(tempInput)
                except:
                    print("That was not a number."
                        + " Input their Social Security "
                        + "Number without special characters:")
                    tempInput = input()
            tempDict.update({'Social Security Number' : str(tempInput)})
            print("Is this person a manager?")
            tempDict.update({'Manager?' : 
            checkInput('yes', 'no').capitalize()})
            print("What is this persons job title?")
            tempDict.update({'Job Title' : input()})
            print("What skills does this person have?")
            tempDict.update({'Skills' : input()})
            
            dataBase.update({counter : tempDict})

            print("Do you want to manually add another person"
                " to the database?")
            if checkInput('yes', 'no') == 'no':
                print("Would you like to add any 'randomly'"
                    " generated people to the database?")
                if checkInput('yes', 'no') == 'yes':
                    DatabaseGenerator(generate= True, userAnswer = 'yes',
                        tempDict= tempDict)
                addPerson = False
    else:
        # This is where the database is randomly generated
        dictLen = 0
        if generate:
            dictLen = int(len(tempDict) / 8)
            for x in range(dictLen):
                dataBase.update({x: tempDict})
        for x in range(25):
            tempDict = {"UniqueID" : numberGenerator(12, 'ID'),
                "Name" : name[x],
                "Address" : address[x],
                "Phone" : numberGenerator(10, 'Phone'),
                "Social Security Number" : numberGenerator(9, 'SSN'),
                "Manager?" : numberGenerator(1, "Manager"),
                "Job Title" : numberGenerator(1, "Job Title"),
                "Skills" : numberGenerator(3, "Skills")}
            dataBase.update({x + dictLen: tempDict})
        print("Database generated!")

# Just checks to see if the user wants to keep the program running.
def userContinue():
    print("Do you want to keep the program running?")
    if checkInput('yes', 'no') == 'no':
        return False
    return True

# This method allows the user to either print or query the database. It keeps
# asking the user whether they want to print or query until the user quits.
def main():
    DatabaseGenerator()
    queryType = ''
    databaseActive = True
    while databaseActive:
        print("Would you like to print all entries in the "
            + "database or query the database? Type 'Print' or 'Query'.")

        if checkInput('print', 'query') == 'print':
            for x in range(0,len(dataBase)):
                print(dataBase[x])
            databaseActive = userContinue()
        else :
            print("Do you want to query by Name, Skills,"
                + " or whether or not a person is a manager?"
                + " Type 'Name', 'Skills', or 'Manager'.")
            queryType = checkInput3("name", "skills", "manager")
            if queryType == 'name':
                print("What is the person's name?")
                databaseQuery(queryType.capitalize(), input())
            elif queryType == 'skills':
                print("What skills do you want to query?")
                databaseQuery(queryType.capitalize(), input())
            elif queryType == 'manager':
                queryType += '?'
                print("Are you looking for people who are managers"
                    + " or people who are not? "
                    + "Type 'Who are' or 'Who are not'.")
                if (checkInput('who are', 'who are not') == 'who are'):
                    databaseQuery(queryType.capitalize(), 'Yes')
                else:
                    databaseQuery(queryType.capitalize(), 'No')
            databaseActive = userContinue()

main()

# 0001 11/14/2022
## END Omar A. Student here (11/14/2022)