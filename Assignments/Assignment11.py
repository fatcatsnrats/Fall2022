import math

# This method checks to see what arguments were passed and returns
# a calculation. It returns: the area of a circle if radius is passed,
# the length of a cube if the volume is passed, the hypotenuse of a right
# triangle if the length and height are passed, or a customer requested
# problem. All calculations are rounded to two decimal places.
def areaOfShape(radius=None, volume=None, length=None, height=None):
    if not radius == None:
        return round((radius*radius) *3.1415, 2)
    elif not volume == None:
        return round(volume**(1./3.), 2)
    elif not (length == None and height == None):
        return round(math.sqrt((length*length) + (height*height)), 2)
    else:
        a = 4.172 + 9.131844
        line1 = (((a*a) *a) - 18)
        line2 = (((11.2-4.6) * ((7-2.91683)**(-4/10))) - 3.5)
        return round(math.sqrt(line1/line2), 2)

def f(a, b=4, c=5):
    print(a,b,c)

f(1,2)

def f(a, b, c=5):
    print(a,b,c)

f(1, c=3, b=2)

print(areaOfShape(radius=5))
print(areaOfShape(volume=729))
print(areaOfShape(length=10, height=18))
print(areaOfShape())