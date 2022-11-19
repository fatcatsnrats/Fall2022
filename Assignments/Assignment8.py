# 0001 11/14/2022
## Begin Omar A. Student here (11/14/2022)

def issue1():
    print('Enter a number')
    print(int((((int(input()) + 2) * 3) - 6) / 3), '\n')

# Customer needs to know what happens when you:
def issue2():
    var1 = 7.0
    var2 = 5
    print(var1 % var2)

    x = 4
    y = 5
    print(x//y)

    print(30-3**2+8/3**2*10, '\n')

# Customer needs to know what happens when you:
def issue3():
    print('Enter anything:')
    userInput = input()
    try:
        print(str(userInput))
    except:
        print('Unable to print string')
    try:
        print(int(userInput))
    except:
        print('Unable to print integer')
    try:
        print(float(userInput))
    except:
        print('Unable to print float')

# Customer needs to know what happens when you:
def issue4():
    a = 2**2**3
    b = 2**(2**3)
    c = (2**2)**3
    if (a & b == c):
        print("All expressions produce the same output")
    elif(a == c):
        print("Only expressions 'A' and 'C' produce the same output")
    elif(b == c):
        print("Only expressions 'B' and 'C' produce the same output")
    elif(a == b):
        print("\nOnly expressions 'A' and 'B' produce the same output\n")
    else:
        print("None of the expressions produce the same output")

# This is a simple game of chance. The user starts with $100 in the bank
# and can wager their money on chests. The user keeps playing until
# they run out of money.
def issue5():
    import random

    bank = 100
    while (bank > 0):
        print("You grabbed a chest!\nYou have $", bank, "in your bank. "
            "How much would you like to wager?")
        # Try catch is to filter out strings (with 'int(input())').
        try:
            wager = int(input())
            # User cannot wager more than they have.
            if (wager <= bank):
                randInt = random.randint(0,10)
                # Determines if the user won, lost, or got the jackpot.
                if (randInt < 8):
                    bank = bank - wager
                    print("Sorry, you lost $", str(wager),
                        "and now have $", str(bank),
                        "in your bank.")
                elif (randInt < 10):
                    bank = bank + wager
                    print("Congratulations! You won $", str(wager),
                        " and now have $", str(bank), " in your bank!")
                else:
                    bank = bank + (3 * wager)
                    print("Congratulations!!! You won 3X your wager! $",
                        str(3 * wager), " has been added to your bank ",
                        "for a total of $", str(bank), "!")
            else:
                print("You dont have enough money for that!")
        except:
            print("Thats not a number")


# Password simulator that tosses out bad passwords.
def issue6():
    import random

    # Goes through 'rockyou.txt' and checks to see if the generated password
    # matches one in the file. It returns a boolean value.
    def passwordAcceptable(password):
        file = open(r'C:\Users\omara\Downloads\rockyou.txt', encoding='ANSI')
        for x in file:
            if password == x:
                file.close()
                return False
        file.close()
        return True
            
    def main():
        for i in range(45):
            password = ""
            # Randomly generates a number 0-9 and assigns it to 'randChar'
            # then decides if it wants to add a letter, special character,
            # or number based on the 'randChar'. Keeps going until the string
            # its been building has a length of 12.
            while len(password) < 13:
                randChar = random.randint(0,9)
                if randChar < 3:
                    password += random.choice(['@', '!', "#", "$", "%", "^",
                        "&", "*", "(", ")", "?", "/", '"', "<", ">", '-', ':',
                        ';', '=', '+', '`', '~', '.'])
                elif randChar < 6:
                    password += str(random.randint(0,9))
                else:
                    password += chr(random.randint(33, 126))

            # Calls the 'passwordAcceptable()' method and passes
            # the generated password to check whether the generated password
            # is a forbidden password. If it is not, the generated password
            # is written to the 'PasswordArchive.txt' file
            # and displayed to the user.
            if passwordAcceptable(password):
                with open(r"C:\temp\PasswordArchive.txt", "a") as file:
                    file.write(password + "\n")
                    print(password)
            else:
                print('Forbidden password entered:', password)

    main()

# This method calculates process capability for the customer.
def issue7():
    usl = 17.5
    lsl = 15.5
    pAvg = 16.507
    avgRange = 0.561
    d2 = 2.326
    cpk = 0

    cpu = (usl - pAvg)/(3*(avgRange/d2))
    cpl = (pAvg - lsl)/(3*(avgRange/d2))

    if cpu < cpl:
        cpk = cpu
    else:
        cpk = cpl

    print("CPU = " + str(cpu))
    print("CPL = " + str(cpl))
    print("Cpk = " + str(cpk))

def issue8():
    primeArr = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53,
        59, 61, 67, 71, 73, 79, 83, 89, 97]

    # This methed checks to see if the float passed to it is a prime number.
    # It returns a boolean value. If it's argument is bigger than 1 and
    # cannot be divided by any whole number other than 1, it returns True.
    # Otherwise it returns False.
    def primeNumber(num):
        if num > 1:
            for x in range(2, num):
                if ((num % x) == 0):
                    return False
            return True
        return False
    
    # This checks to see if all numbers provided by the customer are prime.
    for x in primeArr:
        print(x, primeNumber(x))

def issue9():
    tipDict = {'poor': 0.1, 'decent': 0.15, 'good': 0.2, 'great': 0.25}
    p, d, g, a = tipDict.items()
    billLegal = False
    inputLegal = False
    
    # Keeps asking for the bill until you give a 'legal' answer (no strings).
    while not billLegal:
        bill = input('\nHow much was your bill?\n\n')
        # The try catch is to filter out strings.
        try:
            bill = float(bill)
            billLegal = True
            # Keeps asking for acceptable answer until one is entered.
            while not inputLegal:
                print('\nWas the service: poor, decent, good, or great?\n')
                userInput = input()
                for x in [p, d, g, a]:
                    if userInput.lower() == x[0]:
                        print('\nA', int(x[1] * 100), '% tip would be $',
                            round(bill * x[1], 2))
                        inputLegal = True
        except:
            print('\nInput a number.')

# 0001 11/14/2022
## END Omar A. Student here (11/14/2022)