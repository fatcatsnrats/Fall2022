# 0003 11/23/2022
## Begin Omar A. Student here (11/23/2022)

employeeInfo = [1121, "Jackie Grainger", 22.22,
    1122, "Jignesh Thrakkar", 25.25,
    1127, "Dion Green", 28.75, False,
    24.32, 1132, "Jacob Gerber",
    "Sarah Sanderson", 23.45, 1137, True,
    "Brandon Heck", 1138, 25.84, True,
    1152, "David Toma", 22.65,
    23.75, 1157, "Charles King", False,
    "Jackie Grainger", 1121, 22.22, False,
    22.65, 1152, "David Toma"]

database = []
underpaidSalaries = []
companyRaises = []

def dataSort(arr):
    employeeDict = {}
    # Checks to see if employee is already in database.
    def checkDuplicate():
        if employeeDict.copy() in database:
            pass
        else:
            tempInt = employeeDict.copy()['Employee ID:']
            # Checks to see if incomplete employee data already in database.
            for i in range(len(database)-1):
                currentDict = database[i]
                if currentDict['Employee ID:'] == tempInt:
                    database.pop(i)
            return employeeDict.copy()
            # database.append(employeeDict.copy())

    # This is a generator that takes multiple entries from a list
    # until it makes up on person and makes a dictionary with those values.
    # It then yeilds the dictionary it created. It records how many entries
    # its inputted since the last person it has created and stores it
    # to 'lineIndex' then decides whether or not it has enough data
    # to make up a person. It knows it has enough data when:
    # "'lineIndex' is three and there IS NOT a boolean in the next list entry"
    # and when: "'lineIndex' is greater than three".
    def employeeGen(x):
        lineIndex = 0
        while lineIndex < 5:
            # Adds entries from imported list into a dictionary which
            # may later be appended to the 'database' list.
            if isinstance(arr[x + lineIndex], bool):
                employeeDict['(Unknown field):'] = arr[x + lineIndex]
                lineIndex += 1
            elif isinstance(arr[x + lineIndex], int):
                employeeDict['Employee ID:'] = arr[x + lineIndex]
                lineIndex += 1
            elif isinstance(arr[x + lineIndex], str):
                employeeDict['Employee Name:'] = arr[x + lineIndex]
                lineIndex += 1
            elif isinstance(arr[x + lineIndex], float):
                employeeDict['Employee Hourly Wage:'] = arr[x + lineIndex]
                lineIndex += 1

            # Checks to see whether all employee information
            # is in the dictionary. If it is, it will append
            # the current dictionary to the 'database' list
            # and clear the current dictionary.
            # The try: and except: is for the end of the list.
            try:
                if (lineIndex > 3 or ((lineIndex == 3) 
                    and (not isinstance(arr[x + lineIndex + 1], bool)))):
                    
                    lineIndex = 0
                    checkDuplicate()
                    yield employeeDict.copy()
                    employeeDict.clear()
            except:
                checkDuplicate()
                yield employeeDict.copy()
                lineIndex = 100
                
    # Appends values to the database list using the employeeGen() generator.
    try:
        for count, x in enumerate(arr):
            database.append(next(employeeGen(count)))
    except:
        pass

def totalHourly():
    # Goes through the 'database' list calculating the total hourly rate
    # and determining whether the employee is underpaid based on
    # their total hourly rate. If they are underpaid, it adds them to
    # the 'underpaidSalaries' list.
    for x in database:
        x['total_hourly_rate'] = round(x['Employee Hourly Wage:'] * 1.3, 2)
        if ((x['total_hourly_rate'] >= 28.15)
            and (x['total_hourly_rate'] <= 30.65)):
            underpaidSalaries.append(x)

def calculateRaise():
    for x in underpaidSalaries:
        hourly = x['Employee Hourly Wage:']
        raiseDict = {}
        # Determines how much of a raise the employee should get and adds
        # the employee's name and their wage said raise to
        # the 'companyRaises' list.
        if (hourly >= 22 and hourly <= 24):
            raiseDict['Employee Name:'] = x['Employee Name:']
            raiseDict['After Raise:'] = round(hourly * 1.05, 2)
        elif hourly <= 26:
            raiseDict['Employee Name:'] = x['Employee Name:']
            raiseDict['After Raise:'] = round(hourly * 1.04, 2)
        elif hourly <= 28:
            raiseDict['Employee Name:'] = x['Employee Name:']
            raiseDict['After Raise:'] = round(hourly * 1.03, 2)
        else:
            raiseDict['Employee Name:'] = x['Employee Name:']
            raiseDict['After Raise:'] = round(hourly * 1.02, 2)
        companyRaises.append(raiseDict)
        

dataSort(employeeInfo)
totalHourly()
calculateRaise()
print(database, '\n')
print(underpaidSalaries,'\n')
print(companyRaises, '\n')

# 0003 11/23/2022
## END Omar A. Student here (11/23/2022)