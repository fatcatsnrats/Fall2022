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

    for x in range(0, len(arr)):
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
    for x in database:
        x['total_hourly_rate'] = round(x['Employee Hourly Wage:'] * 1.3, 2)

        if ((x['total_hourly_rate'] >= 28.15)
            and (x['total_hourly_rate'] <= 30.65)):

            underpaidSalaries.append(x)

def calculateRaise():
    for x in underpaidSalaries:
        hourly = x['Employee Hourly Wage:']
        raiseDict = {}
        
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
print(database)
print('\n')
print(underpaidSalaries)
print('\n')
print(companyRaises)
print('\n')