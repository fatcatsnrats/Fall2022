import math

def primeNumber(num):
    if num > 1:
        for x in range(2, int(num)):
            if ((int(num) % x) == 0):
                return False
    return True

def application():
    playing = True
    print("Enter 'stop' to stop playing.")
    while playing:
        userInput = None
        print('Enter any positive rational number.')
        try:
            userInput = float(input())
        except:
            print('That was not a rational number.')
        if (not isinstance(userInput, str)
            and not (userInput == None)):

            if userInput > 0:
                print(math.ceil(userInput))
                print(math.floor(userInput))
                print(bin(int(userInput)))
                if primeNumber(userInput):
                    print('This number is a prime number')
                else:
                    print('This number is not a prime number')
            else:
                print('That rational number was not positive.')
        else:
            if (not (userInput == None) and
                userInput.lower() == 'stop'):

                print('Thanks for playing!')
                playing = False

application()