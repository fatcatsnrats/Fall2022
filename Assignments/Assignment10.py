# 0001 11/14/2022
## Begin Omar A. Student here (11/14/2022)

def issue1():
    pi = 3.14159

    def sphere_volume(r):
        return (((4/3)*pi)*((r*r)*r))

    def main():
        print(sphere_volume(5))

    main()

def issue2():
    def print_range(start, end):
        if start > end:
            start, end = end, start
        for x in range(start, end + 1):
            print(x)

    def main():
        print_range(int(input()), int(input()))
    
    main()

def issue3():
    def gcd(a,b):
        if b == 0:
            return a
        else:
            return gcd(b, a % b)

    def main():
        print(gcd(int(input()), int(input())))
    main()

def issue4():
    import csv, json

    csvFilePath = r"C:\temp\SalesJan2009.csv"
    jsonFilePath = r"C:\temp\transaction_data.json"
    sales_data = []

    with open(csvFilePath) as csvFile:
        csvReader = csv.reader(csvFile)
        for row in csvReader:
            sales_data.append({'Transaction_date' : row[0].strip('"'),
            'Product' : row[1].strip('"'), 'Price' : row[2].strip('"'),
            'Payment_Type' : row[3].strip('"'), 'Name' : row[4].strip('"'),
            'City' : row[5].strip('"'), 'State' : row[6].strip('"'),
            'Country' : row[7].strip('"')})
    
    with open(jsonFilePath, 'w') as jsonFile:
        jsonFile.write(json.dumps(sales_data))

def issue5():
    import csv, json

    csvFilePath = r"C:\temp\SalesJan2009.csv"
    jsonFilePath = r"C:\temp\transaction_data.json"
    sales_data = [{}]

    with open(csvFilePath) as csvFile:
        csvReader = csv.reader(csvFile)
        for row in csvReader:
            sales_data.append({'Transaction_date' : row[0].strip('"'),
            'Product' : row[1].strip('"'), 'Price' : row[2].strip('"'),
            'Payment_Type' : row[3].strip('"'), 'Name' : row[4].strip('"'),
            'City' : row[5].strip('"'), 'State' : row[6].strip('"'),
            'Country' : row[7].strip('"')})
    for x in range(0, len(sales_data)):
        temp = sales_data[x]
        if 'Mastercard' in temp['Payment_Type']:
            sales_data.pop(x)
    print(sales_data)
issue5()

# 0001 11/14/2022
## END Omar A. Student here (11/14/2022)