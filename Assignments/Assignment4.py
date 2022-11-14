# 0001 11/14/2022
## Begin Omar A. Student here (11/14/2022)

import random

class Ticket1:
    # This method first asks the user to input a string, then outputs the
    # class type of the input. Then it does the same but with an integer
    # output.
    def inputStrings():
        print("Please enter a string:")
        string1 = input()
        print("You entered " + string1 + " and its type is " 
        + str(type(string1)))
        print("Please enter an integer:")
        var2 = input()
        print("You entered " + var2 + " and its type is " 
        + str(type(var2)))

class Ticket2:
    # This method demonstrates triple double quotation marks.
    def strSpecificFormat():
        print(
        """Twinkle, twinkle, little star,
        How I wonder what you are!
                Up above the world so high,

                Like a diamond in the sky.
Twinkle, twinkle, little star,
        How I wonder what you are""")

class Ticket3:
    # This method accepts a user input and calculates the area of a circle.
    def circleArea():
        print("What is the radius?")
        radius = input()
        try:
            radius = int(radius)
            radius2 = radius * radius
            pi = 3.1415926535897932384626433832795
            print("Area = " + str(((pi)*radius2)))
        except:
            print("That is not an integer")
            Ticket3.circleArea()

class Ticket4:
    # This method asks for a one letter input and tests whether or not it is a
    # vowel.
    def vowelOrNot():
        print("Input a letter to test whether it is a vowel")
        char = input().lower()
        arr = ["a", "e", "u", "i", "o"]
        try:
            if not isinstance(char, (str)) or (len(char) > 1):
                int1 = 1
                int1 += char
            if char in arr:
                print("The letter is a vowel")
            else:
                print("The letter is not a vowel")
        except:
            print("That is not one letter")
            Ticket4.vowelOrNot()

class Ticket5:
    # This method displays the use of list comprehension. It first makes
    # a list from 0-19, then cubes all entries in the list.
    def listCubed():
        print(list(map(lambda i: (i * i) * (i * i), [i for i in range(19)])))

class Ticket6:
    # This method simulates a roulette wheel.
    def roulette():
        rouletteWheel = []
        log = []
        stillPlaying = True
        rouletteWheel.append("Green 00")
        rouletteWheel.append("Green 0")
        
        # This for loop is in charge of making the roulette wheel slots.
        for x in range(1,36):
            if (x < 10 or (x >= 19 and x <= 28)):
                if x % 2:
                    rouletteWheel.append("Red %s" %x)
                else:
                    rouletteWheel.append("Black %s" %x)
            else:
                if x % 2:
                    rouletteWheel.append("Black %s" %x)
                else:
                    rouletteWheel.append("Red %s" %x)

        # The game is ran in this while loop. It first prints all the roulette
        # wheel slots and asks the user to either choose one or enter 'r' for
        # a random slot. It then checks to see if the user's input is found
        # in the roulette wheel. If it is not, it will randomly select a slot
        # for you. After it appends your selection to the 'log' list, it
        # prints the 'log' list and asks if you want to keep playing.
        while stillPlaying:
            slotSelected = False
            print(rouletteWheel)
            print("Choose a slot or enter 'r' for a slot "
            + "to be randomly selected for you:")
            user = input()
            print()
            for x in rouletteWheel:
                if x.lower() == user.lower():
                    log.append(x)
                    slotSelected = True
            if (not slotSelected):
                log.append(random.choice(rouletteWheel))
            print("Here is your log:")
            print(log)
            print()
            print("Do you want to keep playing? y/n")
            playing = input()
            if playing == "n":
                stillPlaying = False

        

class Ticket7:
    dinnerGuests = []
    date = []
    tag = []

    # This method first finds out the tag size, then appends it to
    # the 'tag' list.
    def tagSwitch():
        print("Do they have a small tag? (y/n)")
        tagTemp = input()
        if tagTemp == "y":
            Ticket7.tag.append(True)
        elif tagTemp == "n":
            Ticket7.tag.append(False)
        else:
            print("That is not an acceptable answer, try again.")
            Ticket7.tagSwitch()

    # This method asks the user questions and puts the user's answers
    # into two lists. One list for the first and last names and the other
    # list for the date they were invited. After that this method calls
    # the tagSwitch() method then prints the persons name, date, and tag size.
    def userInput():
        print("How many guests are you having over?")
        try:
            guestsInt = int(input())
            print("Input the first and last names of your guests one-by-one.")
            stringTemp = input()
            for x in range(guestsInt):
                if x > 0:
                    print("Input another persons first and last name.")
                    stringTemp = input()
                Ticket7.dinnerGuests.append(stringTemp)
                print("Input the date they were invited.")
                Ticket7.date.append(input())
                Ticket7.tagSwitch()
            for x in range(guestsInt):
                if Ticket7.tag[x] == True:
                    print(Ticket7.dinnerGuests[x] + " was invited on "
                    + Ticket7.date[x] + " and has a small tag.")
                else:
                    print(Ticket7.dinnerGuests[x] + " was invited on "
                    + Ticket7.date[x] + " and has a big tag.") 
        except:
            print("That is not a number, try again")
            Ticket7.userInput()



# Ticket1.inputStrings()
# Ticket2.strSpecificFormat()
# Ticket3.circleArea()
# Ticket4.vowelOrNot()
# Ticket5.listCubed()
# Ticket6.roulette()
Ticket7.userInput()

# 0001 11/14/2022
## END Omar A. Student here (11/14/2022)
# 