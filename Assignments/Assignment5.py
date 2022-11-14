# 0001 11/14/2022
## Begin Omar A. Student here (11/14/2022)
import math

firstName = input().lower()
lastName = input().upper()
print("Hello, %s %s" %(firstName.upper(), lastName.lower()))
print()
print()
fullName = firstName + " " + lastName
print(fullName[fullName.index(lastName):len(fullName)])
fullName = (fullName[0:fullName.index(lastName)] 
    + "%s, Walsh College Student" %lastName)
print(fullName)

print()
print('''"Start by doing what's necessary; then do what's 
possible; and suddenly you are doing the impossible 
- Francis of Assisi"''')
print()

dec1 = 1.0
dec2 = 2.0
addition = dec1 + dec2
subtraction = dec1 - dec2
multipication = dec1 * dec2
division = dec1 / dec2

print("%s plus %s equals %s" %(dec1, dec2, addition))
print("{} minus {} equals {}".format(dec1, dec2, subtraction))
print(f"{dec1} times {dec2} equals {multipication}")
print(str(dec1) + " divided by " + str(dec2)
    + " equals " + str(division))

sq_root = round(math.sqrt(multipication), 2)
print("The square root of " + str(multipication)
    + " equals " + str(sq_root))

month = "October"
day = 6
print()
print("""      Today is day %s of the month of %s""" %(day, month))

# 0001 11/14/2022
## END Omar A. Student here (11/14/2022)