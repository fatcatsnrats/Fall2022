import random
import string

userDict = {}

def main():
    run = True
    while run:
        uID = ''
        personArr = [input('Enter name (last, first, middle initial):'),
            input('Enter DoB:'), input('Enter SSN:'),
            input('Enter Current Position:'), input('Enter Useful Skills:'),
            input('Enter Hobbies:'), input('Enter Martial status:')]
        for x in range(8):
            uID += random.choice(string.ascii_letters)
        userDict[uID] = personArr

        if input('Do you want to continue? (y/n)').lower() == 'n':
            run = False

main()
print(userDict)