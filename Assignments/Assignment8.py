# 0001 11/14/2022
## Begin Omar A. Student here (11/14/2022)

def issue1():
    print('Enter a number')
    userInt = ((((int(input()) + 2) * 3) - 6) / 3)

# Customer needs to know what happens when you:
def issue2():
    var1 = 7.0
    var2 = 5
    print(var1 % var2)

    x = 4
    y = 5
    print(x//y)

    print(30-3**2+8/3**2*10)

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
        print("Only expressions 'A' and 'B' produce the same output")
    else:
        print("None of the expressions produce the same output")

# This is a simple game of chance.
def issue5():
    import random

    def playGame():
        bank = 100
        while (bank > 0):
            print("You grabbed a chest!")
            print("How much would you like to wager?")
            try:
                wager = int(input())
                if (wager <= bank):
                    randInt = random.randint(0,10)
                    if (randInt < 5):
                        bank = bank - wager
                        print("Sorry, you lost $" + str(wager) + " and now have $" + str(bank) + " in your bank.")
                    elif (randInt < 10):
                        bank = bank + wager
                        print("Congratulations! You won $" + str(wager) + " and now have $" + str(bank) + " in your bank!")
                    else:
                        bank = bank + (3 * wager)
                        print("Congratulations!!! You won 3X your wager! $" + str(3 * wager) + " has been added to your bank for a total of $" + str(bank) + "!")
                else:
                    print("You dont have enough money for that!")
            except:
                print("Thats not a number")

    playGame()

# Password simulator that tosses out bad passwords.
def issue6():
    import random

    # checks to see if passwords are good.
    def passwordAcceptable(password):
        if "1234" in password:
            return False
        if "4321" in password:
            return False
        if "9876" in password:
            return False
        if "6789" in password:
            return False
        return True

    # main loop that generates passwords.
    def main():
        for i in range(0,44):
            password = ""
            for j in range(0,11):
                password += str(random.randint(0,9))
            if passwordAcceptable(password):
                with open(r"C:\temp\PasswordArchive.txt", "a") as file:
                    file.write(password + "\n")
                    print(password)

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


issue5()
issue6()
issue7()

# 0001 11/14/2022
## END Omar A. Student here (11/14/2022)