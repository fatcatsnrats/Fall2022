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


def databaseQuery(queryType, query):
    counter = 0
    for x in range(0, len(dataBase)):
        if query.lower() in dataBase[x][queryType].lower():
            print(dataBase[x])
            counter += 1
    if counter == 0:
        print("No results found.")

def checkInput(expected1, expected2, expected3):
    if expected3 == '':
        userInput = input().lower()
        expected3, tempInput = False
    else:
        tempInput, userInput = queryInput
    while ((not (userInput == expected1))
        and (not (userInput == expected2))
        and (not (tempInput == expected3))):
        if not expected3:
            print("That was not an acceptable response. Type '"
                + expected1.capitalize() + "' or '" 
                + expected2.capitalize() + "'.")
            userInput = input()
        else:
            print("That was not an acceptable response. Type '"
                + expected1.capitalize() + "', '" 
                + expected2.capitalize() + "', or '" 
                + expected3.capitlize() + "'.")
            userInput = input()
    return userInput.lower()

def DatabaseGenerator():
    tempDict = {}
    print ("Do you want to 'randomly' generate a database?")
    if input().lower() == 'no':
        counter = 0
        addPerson = True
        while addPerson:
            tempDict.update({"UniqueID" : numberGenerator(12, 'ID')})
            print("Input a name:")
            tempDict.update({"Name" : input()})
            print("Input their address:")
            tempDict.update({"Address" : input()})

            print("Input their phone number without special characters:")
            tempInput = input()
            while isinstance(tempInput, int) == False:
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
            checkInput('yes', 'no', '').capitalize()})

            print("What is this persons job title?")
            tempDict.update({'Job Title' : input()})
            print("What skills does this person have?")
            tempDict.update({'Skills' : input()})

            dataBase.update({counter : tempDict})

            print("Do you want to add another person to the database?")
            if checkInput('yes', 'no', '') == 'no':
                addPerson = False

    else:
        for x in range(0,25):
            tempDict = {"UniqueID" : numberGenerator(12, 'ID'),
                "Name" : name[x],
                "Address" : address[x],
                "Phone" : numberGenerator(10, 'Phone'),
                "Social Security Number" : numberGenerator(9, 'SSN'),
                "Manager?" : numberGenerator(1, "Manager"),
                "Job Title" : numberGenerator(1, "Job Title"),
                "Skills" : numberGenerator(3, "Skills")}
            dataBase.update({x: tempDict})
        print("Database generated!")

def userContinue():
    print("Do you want to keep the program running?")
    if checkInput('yes', 'no', '') == 'no':
        return False
    return True

def main():
    DatabaseGenerator()
    queryType = ''
    databaseActive = True
    while databaseActive:
        print("Would you like to print all entries in the "
            + "database or query the database? Type 'Print' or 'Query'.")
        if checkInput('print', 'query', '') == 'print':
            for x in range(0,len(dataBase)):
                print(dataBase[x])
            databaseActive = userContinue()
        else :
            print("Do you want to query by Name, Skills,"
                + " or whether or not a person is a manager?"
                + " Type 'Name', 'Skills', or 'Manager'.")
            queryInput = input().lower()
            queryType = checkInput("name", "skills", "manager").capitalize()
            if queryInput.lower() == 'name':
                print("What is the person's name?")
                databaseQuery(queryType, input())
            elif queryInput.lower() == 'skills':
                print("What skills do you want to query?")
                databaseQuery(queryType, input())
            elif queryInput.lower() == 'manager':
                queryType += '?'
                print("Are you looking for people who are managers"
                    + " or people who are not? "
                    + "Type 'Who are' or 'Who are not'.")
                if (checkInput('who are', 'who are not', '') == 'who are'):
                    databaseQuery(queryType, 'Yes')
                else:
                    databaseQuery(queryType, 'No')
            databaseActive = userContinue()

main()

# 0001 11/14/2022
## END Omar A. Student here (11/14/2022)