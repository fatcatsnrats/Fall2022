# 0001 11/17/2022
## Begin Omar A. Student here (11/17/2022)

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
    lineIndex = 0
    # Checks to see if employee is already in database.
    def checkDuplicate():
        if employeeDict.copy() in database:
            return
        else:
            tempInt = employeeDict.copy()['Employee ID:']
            # Checks to see if incomplete employee data already in database.
            for i in range(len(database)-1):
                currentDict = database[i]
                if currentDict['Employee ID:'] == tempInt:
                    database.pop(i)
            database.append(employeeDict.copy())

    # Adds entries from imported list into a dictionary which
    # may later be appended to the 'database' list.
    for x in range(len(arr)):
        if isinstance(arr[x], bool):
            employeeDict['(Unknown field):'] = arr[x]
            lineIndex = 0
            checkDuplicate()
            employeeDict.clear()
        elif isinstance(arr[x], int):
            employeeDict['Employee ID:'] = arr[x]
            lineIndex += 1
        elif isinstance(arr[x], str):
            employeeDict['Employee Name:'] = arr[x]
            lineIndex += 1
        elif isinstance(arr[x], float):
            employeeDict['Employee Hourly Wage:'] = arr[x]
            lineIndex += 1

        # Checks to see whether all employee information is in the dictionary.
        # If it is, it will append the current dictionary to
        # the 'database' list and clear the current dictionary.
        # The try: and except: is for the end of the list.
        try:
            if ((lineIndex >= 3) and (not isinstance(arr[x+1], bool))):
                lineIndex = 0
                checkDuplicate()
                employeeDict.clear()
        except:
            checkDuplicate()

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

# 0001 11/17/2022
## END Omar A. Student here (11/17/2022)