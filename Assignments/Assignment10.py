# 0001 11/14/2022
## Begin Omar A. Student here (11/14/2022)

def issue1():
    pi = 3.14159

    # This method gets passed the radius and returns the volume of the sphere.
    def sphere_volume(r):
        return (((4/3)*pi)*((r*r)*r))

    print(sphere_volume(5))

def issue2():
    # This method prints any range of numbers the use inputs.
    def print_range():
        playing = True
        while playing:
            print("Input two numbers or enter 'exit' to quit.\n")
            try:
                start = int(input())
                end = int(input())
                if start > end:
                    tempList = [i for i in range(end, start + 1)]
                    rangeList = tempList[::-1]
                else:
                    tempList = [i for i in range(start, end + 1)]
                    rangeList = tempList
                print(rangeList)
            except:
                playing = False
                print('Thanks for playing!')

    print_range()


def issue3():
    # This method finds the greatest common divisor.
    def gcd(a,b):
        if b == 0:
            return a
        else:
            return gcd(b, a % b)

    def main():
        playing = True
        while playing:
            try:
                print('Enter two numbers to find their greatest'
                    ' common divisor or enter "exit".')
                print(gcd(int(input()), int(input())))
            except:
                print('Thanks for playing!')
                playing = False
    main()

def issue4():
    import csv
    import json

    csvFilePath = r"C:\temp\SalesJan2009.csv"
    jsonFilePath = r"C:\temp\transaction_data.json"
    sales_data = []

    with open(csvFilePath) as csvFile:
        csvReader = csv.reader(csvFile)

        # Adds all entries to 'sales_data' list.
        for row in csvReader:
            sales_data.append({'Transaction_date': row[0].strip('"'),
                'Product': row[1].strip('"'), 'Price': row[2].strip('"'),
                'Payment_Type': row[3].strip('"'), 'Name': row[4].strip('"'),
                'City': row[5].strip('"'), 'State': row[6].strip('"'),
                'Country': row[7].strip('"')})
        print(sales_data)

    # Writes 'sales_data' list to json file
    with open(jsonFilePath, 'w') as jsonFile:
        jsonFile.write(json.dumps(sales_data))

def issue5():
    import csv

    csvFilePath = r"C:\temp\SalesJan2009.csv"
    sales_data = []
    manipulatedData = []

    with open(csvFilePath) as csvFile:
        csvReader = csv.reader(csvFile)

        # Adds all entries to 'sales_data' list.
        for row in csvReader:
            sales_data.append({'Transaction_date': row[0].strip('"'),
                'Product': row[1].strip('"'), 'Price': row[2].strip('"'),
                'Payment_Type': row[3].strip('"'), 'Name': row[4].strip('"'),
                'City': row[5].strip('"'), 'State': row[6].strip('"'),
                'Country': row[7].strip('"')})

    # List comprehension to check whether or not tansaction
    # used Mastercard. Appends False to 'copySD' list if Mastercard is used.
    copySD = [False if i['Payment_Type'] == 'Mastercard'
        else True for i in sales_data]

    # If 'copySD' is True, it gets appended to 'manipulatedData'.
    for x in range(len(sales_data)):
        if copySD[x]:
            manipulatedData.append(sales_data[x])

    # Prints original import without transactions using 'Mastercard'.
    print(manipulatedData)

# 0001 11/14/2022
## END Omar A. Student here (11/14/2022)
# HALF-LIFE / Ron Bass / John Richards Sr. / After-Burner Elite