import math

# This methed checks to see if the float passed to it is a prime number.
# It returns a boolean value. If it's argument is bigger than 1 and
# cannot be divided by any whole number other than 1, it returns True.
# Otherwise it returns False.
def primeNumber(num):
    if num > 1:
        for x in range(2, int(num)):
            if ((int(num) % x) == 0):
                return False
        return True
    return False

def application():
    playing = True
    while playing:
        print("\nEnter any positive rational number"
            " or enter 'stop' to stop playing.")
        userInput = input()

        # This try catch filters out strings by converting the user's input
        # into a float. A string will cause an error which will cause
        # the program to skip ahead.
        try:
            userInput = float(userInput)
            if userInput > 0:
                print('\nCeiling:', math.ceil(userInput),
                    '\nFloor:', math.floor(userInput),
                    '\nBinary:', bin(int(userInput)),
                    '\nPrime:', primeNumber(userInput))
            else:
                print('\nThat rational number was not positive.')
        except:
            # The program skips ahead to here once it receivs a string
            # and checks to see whether the user wants to stop the program.
            # If they dont, the program will tell the user
            # they did not enter a rational number.
            if userInput.lower() == 'stop':
                print('\nThanks for playing!')
                playing = False
            else:
                print('\nThat was not a rational number.')

application()