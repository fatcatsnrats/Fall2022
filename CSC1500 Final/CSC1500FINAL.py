import random
import linecache
import tkinter as tk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
import tkinter.scrolledtext as st


database = []

# This method is in charge of randomly generating all random database fields
# except for email.
def generator(objectType):
    tempInt = ''

    if objectType == 'Name':
        dogNames = ["Buddy", "Daisy", "Max", "Charlie", "Lucy", "Molly",
            "Sadie", "Rocky", "Toby", "Coco", "Tucker", "Lady", "Bailey",
            "Zeus", "Ziggy", "Gizmo", "Maddie", "Milo", "Oscar", "Peanut",
            "Roxy", "Stella", "Sadie", "Stella", "Sasha", "Lola", "Chloe",
            "Leo", "Riley", "Peanut", "Bella", "Lily", "Roxy", "Maddie",
            "Sadie", "Charlie", "Zeus", "Ziggy", "Winston", "Lola", "Maddie",
            "Peanut", "Oliver", "Max", "Sammy", "Rocky", "Toby", "Tucker",
            "Stella", "Sadie"]
        return dogNames[random.randint(0, len(dogNames) - 1)]

    elif objectType == 'Phone':
        for i in range(12):
            tempInt += str(random.randint(0,9))
        return ("(" + tempInt[:3] + ")-" + tempInt[3:6] + "-" + tempInt[6:11])

    elif objectType == 'Age':
        if tempInt[1] < 4:
            return int('1' + tempInt[1])
        return (int(tempInt[0]) + 1)

    elif objectType == 'Breed':
        dogBreeds = ["Beagle", "Boxer", "Bulldog", "Chihuahua",
            "Cocker Spaniel", "Dachshund", "Dalmatian",
            "Golden Retriever", "Great Dane", "Greyhound",
            "Husky", "Labrador Retriever", "Poodle", "Pug",
            "Rottweiler", "Shar-Pei", "Shetland Sheepdog", "Shih Tzu",
            "Yorkshire Terrier"]
        return dogBreeds[int(random.random(0, len(dogBreeds) - 1))]

    elif objectType == 'Favorite Activities':
        favorite = []
        activities = ["Fetching balls", "Swimming", "Chewing bones",
            "Playing tug-of-war", "Sunbathing", "Jogging", "Jumping",
            "Chasing rabbits", "Napping", "Playing frisbee"]
        for x in range(3):
            favorite.append(activities[int(tempInt[x])])
        return favorite

# This method creates 'i' amount of random entries and appends it to database.
# This method also concoctates the entries' email from the first and last
# name, both of which are generated using the generator() method.
def create(i):
    addition = []
    for x in range (i):
        tempDict = {'Name': generator('Name'), 'Phone': generator('Phone'),
            'Age': generator('Age'), 'Breed': generator('Breed'),
            'Favorite Activities': generator('Favorite Activities')}
        addition.append(tempDict)
        database.append(tempDict)
    return addition

# This method checks to see if any forbidden characters were passed,
# If there isn't any, the method returns the string that was passed to it.
# If there is, the method returns the string 'Forbidden'.
def checkForbidden(userInput):
    forbidden = ['@', '!', "#", "$", "%", "^", "&", "*", "(", ")",
        "?", "/", '"', "<", ">", '-', ':', ';', '=', '+', '`', '~', '.']
    for x in forbidden:
        if x in userInput:
            userInput = 'Forbidden'
    return userInput

# This method acts as a query. It makes a new list of all results
# and returns it.
def databaseQuery(queryType, query):
    queryList = []
    for x in range(len(database)):
        if query.lower() in str(database[x][queryType]).lower():
            queryList.append(database[x])
    return queryList


# This class acts as the controller and allows switching between frames.
class DataBaseApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        windowFrame = tk.Frame(self)
        self.frames = {}

        self.minsize(800,370)
        self.maxsize(800,370)
        self.config(bg='#81b38e')
        windowFrame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        for x in (Home, Messages, Likes, Profile):
            frameName = x.__name__
            frame = x(parent=windowFrame, controller=self)
            self.frames[frameName] = frame
            frame.config(bg='#81b38e')

            frame.grid(row=0, column=0, sticky=tk.NSEW)
        self.display('UserAgreement')

    # This method is called to raise whatever frame you give it
    def display(self, frameName):
        frame = self.frames[frameName]
        frame.tkraise()

# This class controls the 'Home' frame and acts as the homepage. 
class Home(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        mainFrame = tk.Frame(self, bg='#81b38e')
        canvasFrame1 = tk.Frame(mainFrame, bg='#81b38e')
        middleFrame = tk.Frame(mainFrame, bg='#81b38e')
        canvasFrame2 = tk.Frame(mainFrame, bg='#81b38e')
        labelFrame = tk.Frame(middleFrame, bg='#81b38e')
        buttonFrame = tk.Frame(middleFrame, bg='#81b38e')
        label1 = tk.Label(labelFrame,text="SafeZone©",
            font=('calibre', 18), bg='#81b38e')
        label2 = tk.Label(labelFrame,text="by Forestview",
            font=('calibre', 10), bg='#81b38e')
        label1.pack(side=tk.TOP)
        label2.pack(side=tk.TOP)
        canvas1 = tk.Canvas(canvasFrame1, height=120, width=260,
            highlightthickness=1, highlightbackground="#266136", bg='#9bd1ae')
        canvas2 = tk.Canvas(canvasFrame2, height=120, width=260,
            highlightthickness=1, highlightbackground="#266136", bg='#9bd1ae')
        canvas1.create_text(130, 67, font=('calibre', 7),
            text="Press 'Import Data' to import a file to the database.\n"
            "Press 'Add Data' to add entries to the database one by one.\n"
            "Press 'Query Database' to search through the database.\n"
            "Press 'Print Database' to print all the entries\n"
            "   in the database.\n"
            "Press 'Randomly create more data' to add random entries\n"
            "   to the database.\n"
            "Press 'Print Reversed Data' to print all the entries\n"
            "   in the database.\n")
        canvas2.create_text(130, 60, font=('calibre', 7),
            text="We are currently working on AWS cloud implimentation")

        button1 = tk.Button(buttonFrame, text="Import Data",
            command=lambda: controller.display('ImportData'),
            fg='#ffffff', bg='#266136')
        button2 = tk.Button(buttonFrame, text="Add Data",
            command=lambda: controller.display('AddData'),
            fg='#ffffff', bg='#266136')
        button3= tk.Button(buttonFrame, text='Query Database',
            command=lambda: controller.display('QueryData'),
            fg='#ffffff', bg='#266136')
        button4= tk.Button(buttonFrame, text='Print Database',
            command=lambda: controller.display('LoadData'),
            fg='#ffffff', bg='#266136')
        button5= tk.Button(buttonFrame, text='Randomly create more data',
            command=lambda: controller.display("CreateData"),
            fg='#ffffff', bg='#266136')
        button6= tk.Button(buttonFrame, text='Print Reversed Data',
            command=lambda: controller.display('ReverseData'),
            fg='#ffffff', bg='#266136')

        labelFrame.pack(side=tk.TOP, fill=tk.X, pady=10)
        buttonFrame.pack(side=tk.TOP, fill=tk.X)

        canvasFrame1.grid()
        middleFrame.grid(column=1, row=0)
        canvasFrame2.grid(column=2, row=0)

        mainFrame.pack(side=tk.TOP)

        button1.pack(side=tk.TOP, pady=10)
        button2.pack(side=tk.TOP, pady=10)
        button3.pack(side=tk.TOP, pady=10)
        button4.pack(side=tk.TOP, pady=10)
        button5.pack(side=tk.TOP, pady=10)
        button6.pack(side=tk.TOP, pady=10)
        canvas1.pack(padx=20)
        canvas2.pack(padx=20)


# This class controls the 'Messages' frame and acts as the homepage. 
class Messages(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller







# This class controls the 'Likes' frame and acts as the homepage. 
class Likes(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller








# This class controls the 'Profile' frame and acts as the homepage. 
class Profile(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller


app = DataBaseApp()
app.mainloop()