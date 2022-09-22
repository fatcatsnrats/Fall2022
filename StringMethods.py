# 000 09/21/2022
## Begin Omar Almasri Student

class StringFormatting:
    def doubleQuotationMarks():
        # You can use apostrophys or quotation marks for strings
        print('"Ok"')

    def apostraphy():
        # You can use apostrophys or quotation marks for strings
        print("It's")

    def multipleLinesW():
        # To print multiple lines, use three quotation marks
        print("""
            Computer
                Fast
        """)

    def multipleLinesWo():
        # Use addition sign to stretch strings onto more
        # than one line
        print("Computer "
        + "Fast")

class StringFunctions:
    def printLen():
        string1 = "I should make spaghetti for dinner today"
        # len is valued as its arguments length.
        print(len(string1))

    def twoStrings():
        string1 = "alphabetically speaking,"
        string2 = "i am a wizard"
        # Strings can be added onto one another using an addition sign
        string3 = string1 + string2
        print(string3)

    def twoStringsWSpace():
        string1 = "therefore"
        string2 = "i dont have to pay taxes"
        # Strings can be added onto one another using an addition sign
        # You can also add a space between strings like this
        string3 = string1 + " " + string2
        print(string3)

    def sliceNotation():
        string4 = "bazinga"
        # For loop that goes through the string and sets x equal to the index
        for x in range(0,len(string4)):
            # Checks to see if the word 'zing' is within the string
            if (string4[x] == "z"
            and string4[x+1] == "i"
            and string4[x+2] == "n"
            and string4[x+3] == "g"):
                # Prints the length of 'zing' within the string where it contains 'zing'
                print(string4[x:x+4])

class StringMethods:
    def toLowerCase():
        # Array holds required strings
        arr = ["Animals", "Badger", "Honey Bee", "Honey Badger"]
        # Converts strings to lowercase and prints them one by one
        for x in arr:
            print(x.lower())

    def toUpperCase():
        # Array holds required strings
        arr = ["Animals", "Badger", "Honey Bee", "Honey Badger"]
        # Converts strings to uppercase and prints them one by one
        for x in arr:
            print(x.upper())

    def removeWhitespace():
        # Array holds required strings
        food = [" Filet Mignon", "Brisket ", " Cheeseburger "]
        # Strips strings from surrounding whitespace and prints them one by one
        for x in food:
            print(x.strip())

    def checkForBe():
        # Array holds required strings
        beArray = ["Becomes", "becomes", "BEAR", "bEautiful"]
        # Checks to see if string contains 'be' one by one
        for x in beArray:
            print(x.startswith("be"))

class InputMethods:
    def stringToInt():
        string = "4"
        # Converts string to int
        string = int(string)
        # Multiplys int by number and prints it
        # to confirm conversion was successful
        print(string * 8)

    def stringToFloat():
        string = "4"
        # Converts string to float
        string = float(string)
        # Multiplys float by number and prints it
        # to confirm conversion was successful
        print(string * 8)

    def stringAndInt():
        string = "4"
        number = 8
        # Prints string and int side by side within the same print statement
        # by converting int to string withing the print statement
        print(string + str(number))

    def multiplyUserInput():
        # Takes user inputs and turns them into float
        variable1 = float(input())
        variable2 = float(input())
        # Multiplies floats inputted by user
        variable3 = variable1 * variable2
        # First turns user inputs to int, then to string to get rid of decimal
        # and still be able to use withing print statement. Converted 
        # multiple to string as well.
        print("The product of " + str(int(variable1)) 
        +  " and " + str(int(variable2)) +  " is " + str((variable3)) + ".")

    def findStringMethod():
        string = "We have UNBELIEVIBLY fat cats & rats instock now!!!!!!"
        # Uses the find() method to find whether and where within the string 'fat cats' is
        print(string.find("fat cats"))
        
# 000 09/21/2022
## End Omar Almasri Student
# Zion Worship Cult/ Ram Vuduku/ Rich Eissen/ The Zion Project #

StringFormatting.doubleQuotationMarks()
StringFormatting.apostraphy()
StringFormatting.multipleLinesW()
StringFormatting.multipleLinesWo()
StringFunctions.printLen()
StringFunctions.twoStrings()
StringFunctions.twoStringsWSpace()
StringFunctions.sliceNotation()
StringMethods.toLowerCase()
StringMethods.toUpperCase()
StringMethods.removeWhitespace()
StringMethods.checkForBe()
InputMethods.stringToInt()
InputMethods.stringToFloat()
InputMethods.stringAndInt()
InputMethods.multiplyUserInput()
InputMethods.findStringMethod()
