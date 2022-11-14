import random
import linecache
import pickle
import tkinter as tk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
import tkinter.scrolledtext as st

database = []

# This method is in charge of randomly generating all random database fields
# except for email.
def generator(length, objectType):
    tempInt = ''
    for i in range(length):
        tempInt += str(random.randint(0,9))

    if objectType == 'First Name':
        try:
            return linecache.getline(r'C:\temp\Project1\First Names.txt',
                int(tempInt)).lower().capitalize().rstrip('\n')
        except:
            generator(3, 'First Name')
    elif objectType == 'Last Name':
        try:
            return linecache.getline(r'C:\temp\Project1\Last Names.txt',
                int(tempInt)).lower().capitalize().rstrip('\n')
        except:
            generator(4, 'Last Name')
    elif objectType == 'Phone':
        return ("(" + tempInt[:3] + ")-" + tempInt[3:6] + "-" + tempInt[6:11])
    elif objectType == 'SSN':
        return tempInt[:3] + "-" + tempInt[3:5] + "-" + tempInt[5:]
    elif objectType == 'ID':
        return (tempInt[:8] + "-" + tempInt[8:])
    elif objectType == 'Manager':
        if tempInt == '0':
            return True
        return False
    elif objectType == 'Job Title':
        jobInt = int(tempInt)
        if jobInt < 5:
            return "Software Engineer"
        elif jobInt < 9:
            return "Data Analyst"
        return "Lawyer"
    elif objectType == 'Home Address':
        tempStr = linecache.getline(r'C:\temp\Project1\Cities&States.txt',
            int(tempInt[9:])).split(',', 3)
        try:
            return (str(tempInt[:5]) + ' ' + linecache.getline(
                r'C:\temp\Project1\Street Names.txt',
                int(tempInt[6:9])).rstrip('\n')
                + ', ' + tempStr[1] + ', ' + tempStr[2])
        except:
            generator(11, 'Home Address')
    elif objectType == 'Skills':
        tempStr = []
        skills = ["Carpentry", "Agriculture", "Hiding", "Tinkering",
            "Listening", "Clowning", "Construction", "Boating", "Burying",
            "Locksmith"]
        for x in range(3):
            tempStr.append(skills[int(tempInt[x])])
        return tempStr

# This method creates 'i' amount of random entries and appends it to database.
# This method also concoctates the entries' email from the first and last
# name, both of which are generated using the generator() method.
def create(i):
    addition = []
    for x in range (i):
        firstName = generator(3, 'First Name')
        lastName = generator(4, 'Last Name')
        email = lastName.lower() + '.' + firstName.lower() + '@forestview.com'
        address = None
        try:
            address = '[' + generator(11, 'Home Address') + ']'
        except:
            pass
        tempDict = {'Unique ID': generator(12, 'ID'), 'First Name': firstName,
            'Last Name': lastName, 'Phone': generator(20, 'Phone'),
            'Email': email, 'Address': address,
            'Social Security Number': generator(9, 'SSN'),
            'Job': generator(1, 'Job Title'),
            'Manager': generator(1, 'Manager'),
            'Skills': generator(3, 'Skills')}
        addition.append(tempDict)
        database.append(tempDict)
    # storeData()
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

# This method serializes the 'database' list,
# then appends it to 'Project1\database.txt'.
def storeData():
    databaseFile = open(r'C:\temp\Project1\database.txt', 'ab')
    pickle.dump(database, databaseFile, pickle.HIGHEST_PROTOCOL)
    databaseFile.close()

# This method de-serializes 'Project1\database.txt',
# then appends it to the 'database' list.
def loadData():
    databaseFile = open(r'C:\temp\Project1\database.txt', 'rb')
    fileContents = pickle.load(databaseFile, encoding='utf-8')
    print(fileContents)
    database.extend(fileContents)
    for x in fileContents:
        database.append(x)
        print(x)
    databaseFile.close()

# This method takes values from the imported file line by line and appends it
# to the 'database' list. This method also contains a manager() method which
# converts strings in the manager field to booleans. The manager() method is
# called for each entry being imported.
def importData(filepath, seperator, ms1, ms2, id,
    fn, ln, p, e, a, ssn, j, m, s):
    
    # Turns manager values given to it into boolean form. 
    def manager():
        if ((ms1 == None) and (ms2 == None)):
            return lineList[m-1]
        elif ms1 in lineList[m-1]:
            return True
        elif ms2 in lineList[m-1]:
            return False
        return None

    importedFile = open(filepath, 'r')
    file = importedFile.readlines()
    importList = []
    for line in file:
        lineList = line.split(seperator)
        phoneStr = lineList[p-1].strip('[]')
        skillsStr = lineList[s-1].strip('[]')
        phoneArr = phoneStr.split(',')
        skillsArr = skillsStr.split(',')

        for x in phoneArr:
            x.strip("'")
        for x in skillsArr:
            x.strip("'")

        newDict = {'Unique ID': lineList[id-1],
            'First Name': lineList[fn-1], 'Last Name': lineList[ln-1],
            'Phone': phoneArr, 'Email': lineList[e-1],
            'Address': lineList[a-1], 'Social Security Number': lineList[ssn-1],
            'Job': lineList[j-1], 'Manager': manager(), 'Skills': skillsArr}

        importList.append(newDict)
        database.append(newDict)
    # storeData()
    print(importList)

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

        for x in (ImportData, AddData, MainMenu, ReverseData,
        QueryData, LoadData, CreateData, UserAgreement):
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

# This class controls the 'ImportData' frame. It collects the order in which
# the fields are situated in their current form. It also collects the list
# separator values and the values that need to be stripped. This method
# also collects the 'True' and 'False' values for the manager status.
# This method then sends all the data it collected to the importData()
# method.
class ImportData(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        firstName = tk.StringVar(value='2')
        lastName = tk.StringVar(value='3')
        idNumber = tk.StringVar(value='1')
        address = tk.StringVar(value='6')
        phone = tk.StringVar(value='4')
        ssn = tk.StringVar(value='7')
        job = tk.StringVar(value='8')
        manager = tk.StringVar(value='9')
        skills = tk.StringVar(value='10')
        email = tk.StringVar(value='5')
        seperator = tk.StringVar(value=',')
        managerTrue = tk.StringVar()
        managerFalse = tk.StringVar()
        legal = tk.BooleanVar()

        def openFile():
            return fd.askopenfilename(title='Import a file', initialdir='/')

        # Checks to see if whatever the user inputed is 'legal'.
        # If the user's input is not legal, it will show a message box
        # informing the user and it will set 'legal' to False, which would
        # keep the user from moving forward.
        def seperatorCheck():
            seperatorCounter = 0
            for x in range(0, len(seperator.get())):
                if ' ' in seperator.get()[x]:
                    seperatorCounter+= 1
            if seperatorCounter == len(seperator.get()):
                showinfo(title='Database',
                    message='Forbidden characters entered to seperator field')
                legal.set(False)

        # First checks to see if any forbidden characters have been entered,
        # then then calls the 'seperatorCheck()' method. If the user's input
        # is not legal, it will show a message box informing the user and 
        # it will set 'legal' to False, which would keep the user from moving
        # forward.
        def importAction():
            legal.set(value=True)
            try:
                for x in (idNumber, firstName, lastName, phone, address,
                    ssn, job, skills, email, seperator, manager,
                    managerTrue, managerFalse):

                    if not (checkForbidden(x.get()) == x.get()):
                        showinfo(title='Database',
                            message='Forbidden characters entered!')
                        legal.set(False)

                seperatorCheck()
                if legal.get():
                    filepath = openFile()
                    importData(filepath, seperator.get(), managerTrue.get(),
                        managerFalse.get(), int(idNumber.get()),
                        int(firstName.get()), int(lastName.get()),
                        int(phone.get()), int(email.get()),
                        int(address.get()), int(ssn.get()), int(job.get()),
                        int(manager.get()), int(skills.get()))
                    showinfo(title='Database', message='Import successful')
                    app.display('MainMenu')
            except:
                showinfo(title='Database', message='Import unsuccessful')

        importDataFrame = tk.Frame(self, bg='#81b38e')
        otherFrame = tk.Frame(importDataFrame, bg='#81b38e')
        f1 = tk.Frame(otherFrame, bg='#81b38e')
        f2 = tk.Frame(otherFrame, bg='#81b38e')
        f3 = tk.Frame(otherFrame, bg='#81b38e')
        managerFrame = tk.Frame(f3, bg='#81b38e')
        managerFrame0 = tk.Frame(managerFrame, bg='#81b38e')
        managerFrame1 = tk.Frame(managerFrame, bg='#81b38e')
        managerFrame2 = tk.Frame(managerFrame, bg='#81b38e')
        valueOrderFrame = tk.Frame(importDataFrame, bg='#81b38e')

        titleLabel = tk.Label(valueOrderFrame,
        text='What order are the entries in?',
        font=('calibre', 14), bg='#81b38e')
        idLabel = tk.Label(valueOrderFrame, 
            text='     Unique ID:', font=('calibre', 10), bg='#81b38e')
        fNameLabel = tk.Label(valueOrderFrame,
            text='     First Name:', font=('calibre', 10), bg='#81b38e')
        lNameLabel = tk.Label(valueOrderFrame,
            text='     Last Name:', font=('calibre', 10), bg='#81b38e')
        phoneLabel = tk.Label(valueOrderFrame,
            text='     Phone Number(s):', font=('calibre', 10), bg='#81b38e')
        emailLabel = tk.Label(valueOrderFrame,
            text='     Email:', font=('calibre', 10), bg='#81b38e')
        addressLabel = tk.Label(valueOrderFrame,
            text='     Home Address:', font=('calibre', 10), bg='#81b38e')
        ssnLabel = tk.Label(valueOrderFrame,
            text='     SSN:', font=('calibre', 10), bg='#81b38e')
        jobLabel = tk.Label(valueOrderFrame,
            text='     Job Title:', font=('calibre', 10), bg='#81b38e')
        managerLabel = tk.Label(valueOrderFrame,
            text='     Manager Status:', font=('calibre', 10), bg='#81b38e')
        skillsLabel = tk.Label(valueOrderFrame,
            text='     Skills:', font=('calibre', 10), bg='#81b38e')
        seperatorLabel = tk.Label(f1,
            text='What character separates these values?',
            font=('calibre', 12), bg='#81b38e')
        managerStringLabel1 = tk.Label(managerFrame0,
            text='If manager status is not a boolean value,',
            font=('calibre', 12), bg='#81b38e')
        managerStringLabel2 = tk.Label(managerFrame0,
            text='enter the strings that signify true and false',
            font=('calibre', 12), bg='#81b38e')
        trueLabel = tk.Label(managerFrame1,
            text='True:', font=('calibre', 10), width=4, bg='#81b38e')
        falseLabel = tk.Label(managerFrame2,
            text='False:', font=('calibre', 10), width=4, bg='#81b38e')

        idEntry = tk.Entry(valueOrderFrame, textvariable=idNumber,
            font=('calibre', 10), width=4)
        fNameEntry = tk.Entry(valueOrderFrame, textvariable=firstName,
            font=('calibre', 10), width=4)
        lNameEntry = tk.Entry(valueOrderFrame, textvariable=lastName,
            font=('calibre', 10), width=4)
        phoneEntry = tk.Entry(valueOrderFrame, textvariable=phone,
            font=('calibre', 10), width=4)
        emailEntry = tk.Entry(valueOrderFrame, textvariable=email,
            font=('calibre', 10), width=4)
        addressEntry = tk.Entry(valueOrderFrame, textvariable=address,
            font=('calibre', 10), width=4)
        ssnEntry = tk.Entry(valueOrderFrame, textvariable=ssn,
            font=('calibre', 10), width=4)
        jobEntry = tk.Entry(valueOrderFrame, textvariable=job,
            font=('calibre', 10), width=4)
        managerEntry = tk.Entry(valueOrderFrame, textvariable=manager,
            font=('calibre', 10), width=4)
        skillsEntry = tk.Entry(valueOrderFrame, textvariable=skills,
            font=('calibre', 10), width=4)
        seperatorEntry = tk.Entry(f1, textvariable=seperator,
            font=('calibre', 10))
        managerStringEntry1 = tk.Entry(managerFrame1,
            textvariable=managerTrue, font=('calibre', 10))
        managerStringEntry2 = tk.Entry(managerFrame2,
            textvariable=managerFalse, font=('calibre', 10))

        titleLabel.grid(row=0, column= 0, columnspan= 2, pady=10)
        idLabel.grid(row=1, sticky= tk.W, column=0)
        idEntry.grid(row=1, sticky= tk.W, column=1)
        fNameLabel.grid(row=2, sticky= tk.W, column=0)
        fNameEntry.grid(row=2, sticky= tk.W, column=1)
        lNameLabel.grid(row=3, sticky= tk.W, column=0)
        lNameEntry.grid(row=3, sticky= tk.W, column=1)
        phoneLabel.grid(row=4, sticky= tk.W, column=0)
        phoneEntry.grid(row=4, sticky= tk.W, column=1)
        emailLabel.grid(row=5, sticky= tk.W, column=0)
        emailEntry.grid(row=5, sticky= tk.W, column=1)
        addressLabel.grid(row=6, sticky= tk.W, column=0)
        addressEntry.grid(row=6, sticky= tk.W, column=1)
        ssnLabel.grid(row=7, sticky= tk.W, column=0)
        ssnEntry.grid(row=7, sticky= tk.W, column=1)
        jobLabel.grid(row=8, sticky= tk.W, column=0)
        jobEntry.grid(row=8, sticky= tk.W, column=1)
        managerLabel.grid(row=9, sticky= tk.W, column=0)
        managerEntry.grid(row=9, sticky= tk.W, column=1)
        skillsLabel.grid(row=10, sticky= tk.W, column=0)
        skillsEntry.grid(row=10, sticky= tk.W, column=1)
        seperatorLabel.grid(row=0, column=0, padx= 5, pady= 10)
        seperatorEntry.grid(row=1, column=0, padx= 15)
        managerStringLabel1.grid(row=5, column=0)
        managerStringLabel2.grid(row=6, column=0)
        trueLabel.grid(row=0, sticky= tk.W, column=0)
        falseLabel.grid(row=1, sticky= tk.W, column=0)
        managerStringEntry1.grid(row=0, sticky= tk.W, column=1)
        managerStringEntry2.grid(row=1, sticky= tk.W, column=1)

        managerFrame0.pack(pady=10)
        managerFrame1.pack()
        managerFrame2.pack()
        valueOrderFrame.grid(column=0,row=1, padx= 30, pady= 5)
        otherFrame.grid(column=2, row=1, sticky= tk.N, pady= 50)
        importDataFrame.pack(anchor= tk.CENTER, pady= 5)
        managerFrame.grid(row=7, rowspan=9, column=0,
            columnspan=1, sticky= tk.NW, padx= 5)

        f1.grid(column=0,row=0, pady= 5)
        f2.grid(column=0,row=1, pady= 5)
        f3.grid(column=0,row=2, pady= 5)

        backButton = tk.Button(self, text='Back',
            command= lambda: app.display('MainMenu'), fg='#ffffff',
            bg='#266136')
        importButton = tk.Button(self, text='Import',
            command= lambda: importAction(), fg='#ffffff', bg='#266136')
        backButton.pack(side=tk.LEFT, padx= 20, pady= 20)
        importButton.pack(side=tk.RIGHT, padx= 20, pady= 20)

# This class controls the 'AddData' frame. It collects entries and sends them
# to the addData() method. 
class AddData(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        firstName = tk.StringVar()
        lastName = tk.StringVar()
        idNumber = tk.StringVar()
        address = tk.StringVar()
        phone = tk.StringVar()
        ssn = tk.StringVar()
        job = tk.StringVar()
        manager = tk.StringVar()
        skills = tk.StringVar()
        email = tk.StringVar()

        # This method takes arguments from AddData and appends it to
        # the 'database' list. It also calls the 'storeData()' method.
        def addData():
            m = None
            if manager.get() == '1':
                m = True
            else:
                m = False
            importedDict = {'Unique ID': idNumber.get(),
                'First Name': firstName.get(), 'Last Name': lastName.get(),
                'Phone': phone.get(), 'Email': email.get(),
                'Address': address.get(), 'Social Security Number': ssn.get(),
                'Job': job.get(), 'Manager': m,
                'Skills': (skills.get()).split(',')}

            database.append(importedDict)
            storeData()

        # Checks to see if all user inputs are 'legal'. If the user's input
        # is not legal, it will show a message box informing the user and 
        # it will set 'legal' to False, which would keep the user from moving
        # forward.
        def importAction():
            try:
                legal = True
                for x in (idNumber, firstName, lastName, phone, address,
                    ssn, job, skills, email):
                    if not (checkForbidden(x.get()) == x.get()):
                        legal = False
                if legal:
                    addData()
                    showinfo(title='Database',
                        message='Data transfer successful')
                    app.display('MainMenu')
                else:
                    showinfo(title='Database',
                        message='Forbidden characters entered!')
            except:
                showinfo(title='Database',
                    message='Data transfer unsuccessful')

        mainFrame = tk.Frame(self, bg='#81b38e')
        titleFrame = tk.Frame(mainFrame, bg='#81b38e')
        dataFrame = tk.Frame(mainFrame, bg='#81b38e')

        titleLabel = tk.Label(self, text='Enter Data:',
            font=('calibre', 18), bg='#81b38e')
        idLabel = tk.Label(dataFrame, text='Unique ID:',
            font=('calibre', 10), bg='#81b38e')
        fNameLabel = tk.Label(dataFrame, text='First Name:',
            font=('calibre', 10), bg='#81b38e')
        lNameLabel = tk.Label(dataFrame, text='Last Name:',
            font=('calibre', 10), bg='#81b38e')
        phoneLabel = tk.Label(dataFrame, text='Phone Number(s):',
            font=('calibre', 10), bg='#81b38e')
        emailLabel = tk.Label(dataFrame, text='Email:',
            font=('calibre', 10), bg='#81b38e')
        addressLabel = tk.Label(dataFrame, text='Home Address:',
            font=('calibre', 10), bg='#81b38e')
        ssnLabel = tk.Label(dataFrame, text='SSN:',
            font=('calibre', 10), bg='#81b38e')
        jobLabel = tk.Label(dataFrame, text='Job Title:',
            font=('calibre', 10), bg='#81b38e')
        managerLabel = tk.Label(dataFrame, text='Manager?:',
            font=('calibre', 10), bg='#81b38e')
        skillsLabel = tk.Label(dataFrame, text='Skills: (comma separated)',
            font=('calibre', 10), bg='#81b38e')

        idEntry = tk.Entry(dataFrame,
            textvariable=idNumber, font=('calibre', 10), width=40)
        fNameEntry = tk.Entry(dataFrame,
            textvariable=firstName, font=('calibre', 10), width=40)
        lNameEntry = tk.Entry(dataFrame,
            textvariable=lastName, font=('calibre', 10), width=40)
        phoneEntry = tk.Entry(dataFrame,
            textvariable=phone, font=('calibre', 10), width=40)
        emailEntry = tk.Entry(dataFrame,
            textvariable=email, font=('calibre', 10), width=40)
        addressEntry = tk.Entry(dataFrame,
            textvariable=address, font=('calibre', 10), width=40)
        ssnEntry = tk.Entry(dataFrame,
            textvariable=ssn, font=('calibre', 10), width=40)
        jobEntry = tk.Entry(dataFrame,
            textvariable=job, font=('calibre', 10), width=40)
        skillsEntry = tk.Entry(dataFrame,
            textvariable=skills, font=('calibre', 10), width=40)
        managerCheckButton = tk.Checkbutton(dataFrame,
            variable=manager, offvalue=0, onvalue=1, bg='#81b38e')

        titleLabel.pack(side=tk.TOP)
        titleFrame.grid(row=0, column= 0)
        idLabel.grid(row=1, column=0)
        idEntry.grid(row=1, column=1)
        fNameLabel.grid(row=2, column=0)
        fNameEntry.grid(row=2, column=1)
        lNameLabel.grid(row=3, column=0)
        lNameEntry.grid(row=3, column=1)
        phoneLabel.grid(row=4, column=0)
        phoneEntry.grid(row=4, column=1)
        emailLabel.grid(row=5, column=0)
        emailEntry.grid(row=5, column=1)
        addressLabel.grid(row=6, column=0)
        addressEntry.grid(row=6, column=1)
        ssnLabel.grid(row=7, column=0)
        ssnEntry.grid(row=7, column=1)
        jobLabel.grid(row=8, column=0)
        jobEntry.grid(row=8, column=1)
        managerLabel.grid(row=9, column=0)
        managerCheckButton.grid(row=9, column=1, sticky= tk.W)
        skillsLabel.grid(row=10, column=0)
        skillsEntry.grid(row=10, column=1)
        dataFrame.grid(row=0, column=1)
        mainFrame.pack(anchor= tk.CENTER, pady= 30)

        backButton = tk.Button(mainFrame, text='Back',
            command= lambda: app.display('MainMenu'),
            fg='#ffffff', bg='#266136')
        importButton = tk.Button(mainFrame,
            text='Import', command= lambda: importAction(),
            fg='#ffffff', bg='#266136')
        backButton.grid(row=1, column=0, padx= 50, sticky= tk.S)
        importButton.grid(row=1, column=2, padx= 60, sticky= tk.S)

# This class controls the 'QueryData' frame. It collects the values given to
# its widgets and sends them to the 'databaseQuery()' method. 
# 'databaseQuery()' then returns a list which this frame displays.
class QueryData(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        query = tk.StringVar(value='')
        queryType = tk.StringVar(value='')

        # This method is called when we want to switch to the first page.
        def main():

            # This method is called when the search button is triggered.
            # It first checks to see if the user's input is legal.
            # Once it does that, displays the query results and destroys
            # the previous 'page'.
            def search():

                # This method is called to destroy the current page and
                # go back to the first one.
                def backToMain():
                    textFrame.destroy()
                    buttonFrameTF.destroy()
                    main()
                
                a = []
                tempQuery = query.get()
                if not (checkForbidden(tempQuery) == tempQuery):
                    showinfo(title='Error',
                        message='You have entered forbidden characters!')
                else:
                    try:
                        a = databaseQuery(queryType.get(), tempQuery)
                        textFrame = tk.Frame(self,bg='#81b38e')
                        textbox = st.ScrolledText(textFrame, wrap= tk.WORD)
                        for x in range(0,len(a)):
                            textbox.insert(tk.INSERT, a[x])
                        textbox.configure(state='disabled', height=22,
                            width=80)
                        textbox.grid()
                        buttonFrameTF = tk.Frame(self, bg='#81b38e')
                        backButton = tk.Button(buttonFrameTF,
                            text='Main Menu:',
                            command=lambda: controller.display('MainMenu'),
                            fg='#ffffff', bg='#266136')
                        searchButton = tk.Button(buttonFrameTF,
                            text='Back to Query:', default='normal',
                            command=lambda: backToMain(),
                            fg='#ffffff', bg='#266136')
                        backButton.grid(column=1, row=0, pady=10)
                        searchButton.grid(column=1, row=1)
                        textFrame.pack(side=tk.LEFT)
                        buttonFrameTF.pack(pady=130)
                        masterFrame.destroy()
                    except:
                        showinfo(title='Database',
                            message='Please enter all fields')
            
            masterFrame = tk.Frame(self, bg='#81b38e')
            queryFrame = tk.Frame(masterFrame, bg='#81b38e')
            buttonFrame = tk.Frame(masterFrame, bg='#81b38e')
            bottomFrame = tk.Frame(masterFrame, bg='#81b38e')
            buttonFrame1 = tk.Frame(buttonFrame, bg='#81b38e')
            buttonFrame2 = tk.Frame(buttonFrame, bg='#81b38e')

            idButton = tk.Radiobutton(buttonFrame1, variable=queryType,
                value='Unique ID', text='Unique ID',
                font=('calibre', 10), bg='#81b38e')
            fNameButton = tk.Radiobutton(buttonFrame1, variable=queryType,
                value='First Name', text='First Name',
                font=('calibre', 10), bg='#81b38e')
            lNameButton = tk.Radiobutton(buttonFrame1, variable=queryType,
                value='Last Name', text='Last Name',
                font=('calibre', 10), bg='#81b38e')
            phoneButton = tk.Radiobutton(buttonFrame1, variable=queryType,
                value='Phone', text='Phone Number',
                font=('calibre', 10), bg='#81b38e')
            emailButton = tk.Radiobutton(buttonFrame1, variable=queryType,
                value='Email', text='Email',
                font=('calibre', 10), bg='#81b38e')
            addressButton = tk.Radiobutton(buttonFrame2, variable=queryType,
                value='Address', text='Home Address',
                font=('calibre', 10), bg='#81b38e')
            ssnButton = tk.Radiobutton(buttonFrame2, variable=queryType,
                value='Social Security Number', text='SSN',
                font=('calibre', 10), bg='#81b38e')
            jobButton = tk.Radiobutton(buttonFrame2, variable=queryType,
                value='Job', text='Job Title',
                font=('calibre', 10), bg='#81b38e')
            managerButton = tk.Radiobutton(buttonFrame2, variable=queryType,
                value='Manager', text='Manager Status',
                font=('calibre', 10), bg='#81b38e')
            skillsButton = tk.Radiobutton(buttonFrame2, variable=queryType,
                value='Skills', text='Skills',
                font=('calibre', 10), bg='#81b38e')
            queryLabel = tk.Label(queryFrame,
                text='What is it you are searching for?',
                font=('calibre', 14), bg='#81b38e')
            queryEntry =tk.Entry(queryFrame,
                textvariable=query, font=('calibre', 10))

            idButton.grid(row=0, column=0)
            fNameButton.grid(row=1, column=0)
            lNameButton.grid(row=2, column=0)
            phoneButton.grid(row=3, column=0)
            emailButton.grid(row=4, column=0)
            addressButton.grid(row=0, column=1)
            ssnButton.grid(row=2, column=1)
            jobButton.grid(row=3, column=1)
            managerButton.grid(row=4, column=1)
            skillsButton.grid(row=5, column=1)
            queryLabel.grid(row=0, column=0)
            queryEntry.grid(row=1, column=0, pady=20)
            buttonFrame1.grid(row=0,column=0)
            buttonFrame2.grid(row=0,column=1)

            queryFrame.grid()
            buttonFrame.grid(row=1, column=0)
            bottomFrame.grid()

            masterFrame.pack(anchor=tk.CENTER, pady=50)

            backButton = tk.Button(bottomFrame, text='Back',
                command=lambda: app.display('MainMenu'),
                fg='#ffffff', bg='#266136')
            searchButton = tk.Button(bottomFrame, text='Search:',
                default='normal', command=lambda: search(),
                fg='#ffffff', bg='#266136')
            backButton.grid(row=0, column=0, padx=10, pady=15)
            searchButton.grid(row=0, column=1, padx=10, pady=15)
                
        main()

# This class controls the 'ReverseData' frame. This class calls the
# 'loadData()' method when the refresh button is hit which returns with a list
# of the database. This class then reverses that list and prints it in a
# ScrolledText widget.
class ReverseData(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        entry = tk.StringVar(value='')

        # This method is called to referesh results
        def main():

            # This method is called to reverse the 'database' list.
            def reverseList(array):
                tempList = array[::-1]
                return tempList

            textFrame = tk.Frame(self)
            refreshFrame = tk.Frame(self, bg='#81b38e')
            textbox = st.ScrolledText(textFrame, wrap=tk.WORD)
            arr = database
            rArr = reverseList(arr)
            for x in range(0,len(rArr)):
                textbox.insert(tk.INSERT, rArr[x])
            textbox.configure(state='disabled', height=22, width=70)
            textbox.grid(column=0, row=0)
            textFrame.grid(column=0, row=0)
            tk.Entry(self, textvariable=entry)
            label1 = tk.Label(refreshFrame,
                text='Press refresh if changes have been made', bg='#81b38e')
            label2 = tk.Label(refreshFrame,
                text='to the database since opening the app', bg='#81b38e')
            button = tk.Button(refreshFrame, text='Refresh:',
                command=lambda: main(), fg='#ffffff', bg='#266136')
            backButton = tk.Button(refreshFrame, text='Main Menu:',
                command=lambda: controller.display('MainMenu'),
                fg='#ffffff', bg='#266136')
            
            label1.grid()
            label2.grid()
            button.grid()
            backButton.grid()
            refreshFrame.grid(column=1, row=0)
            
        main()

# This class controls the 'LoadData' frame. This class calls the
# 'loadData()' method when the refresh button is hit which returns with a list
# of the database. This class then prints that list in a ScrolledText widget.
class LoadData(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        entry = tk.StringVar(value='')

        # This method is called to referesh results.
        def main():
            textFrame = tk.Frame(self)
            refreshFrame = tk.Frame(self, bg='#81b38e')
            textbox = st.ScrolledText(textFrame, wrap=tk.WORD)
            arr = database
            for x in range(0,len(arr)):
                textbox.insert(tk.INSERT, arr[x])
            textbox.configure(state='disabled', height=22, width=70)
            textbox.grid(column=0, row=0)
            textFrame.grid(column=0, row=0)
            tk.Entry(self, textvariable=entry)
            label1 = tk.Label(refreshFrame,
                text='Press refresh if changes have been made', bg='#81b38e')
            label2 = tk.Label(refreshFrame,
                text='to the database since opening the app', bg='#81b38e')
            button = tk.Button(refreshFrame,
                text='Refresh:', command=lambda: main(),
                fg='#ffffff', bg='#266136')
            backButton = tk.Button(refreshFrame, text='Main Menu:',
                command=lambda: controller.display('MainMenu'),
                fg='#ffffff', bg='#266136')
            
            label1.grid()
            label2.grid()
            button.grid()
            backButton.grid()
            refreshFrame.grid(column=1, row=0)
            
        main()

# This class controls the 'UserAgreement' frame which is the first frame
# that is displayed when opening the app. It displays the user with the the
# User Agreement and the Unilateral Indemnity. It also gives the user two
# choices: to continue and accept, or to decline and quit the app.
class UserAgreement(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        textFrame = tk.Frame(self)
        buttonFrame = tk.Frame(self, bg='#81b38e')
        textbox = st.ScrolledText(textFrame, wrap=tk.WORD)
        acceptButton = tk.Button(buttonFrame, text='Accept',
            command=lambda: controller.display('MainMenu'), fg='#ffffff',
            bg='#266136')
        declineButton = tk.Button(buttonFrame, text='Decline',
            command=lambda: exit(), fg='#ffffff', bg='#266136')

        textbox.insert(tk.INSERT, 'USER MUST COMPLY WITH USER AGREEMENT '
            'AS A CONDITION TO THE DOWNLOADING OF THIS APPLICATION!'
            '\n\n'
            'User may not sell or distribute data without the '
            'express consent of Forestview.'
            '\n\n'
            'The User acknowledges that Forestview is precluded from any '
            'legal ramifications for any type of data breaches, zero-day '
            'attacks, and databaseworms (such as, but not limited to SQL '
            'injection).'
            '\n\n'
            'We at Forestview periodically do vulnerablility '
            'assessments against our system. We at Forestview also demand '
            'said preventative actions from all of our key vendors.'
            '\n\n'
            'Since technology and the overall security landscape changes, '
            'requirements will change over time.')
        textbox.configure(state='disabled', height=22, width=80)
        textbox.grid(column=0, row=0)
        textFrame.grid(column=0, row=0)
        buttonFrame.grid(column=1, row=0, padx=44)
        acceptButton.grid(column=0, row=0, sticky=tk.E)
        declineButton.grid(column=0, row=1, sticky=tk.E, pady=10)


# This class controls the 'CreateData' frame. It asks the user how many
# entries they would like to create and forwards that value to 
# the create() method.
class CreateData(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        amount = tk.StringVar()

        # This method is called when the user triggers the button2, it checks
        # to see if the input is 'legal'. If the input is legal, it calls the
        # create() method and sends the users input in integer form.
        def createAction():
            try:
                legal = True
                if not (checkForbidden(amount.get()) == amount.get()):
                    showinfo(title='Database',
                        message='Forbidden characters entered!')
                    legal = False
                if legal:
                    create(int(amount.get()))
                    string = 'You have successfuly created and stored ' \
                        + str(amount.get()) + ' new entries!'
                    showinfo(title='Database', message=string)
            except:
                if amount.get() == '':
                    showinfo(title='Database', message='Enter a number')
                else:
                    showinfo(title='Database',
                        message='Only numbers are accepted.')

        entry = tk.Entry(self, textvariable=amount, font=('calibre', 18))
        label = tk.Label(self,
            text="How many entries would you like to create?",
            font=('calibre', 18), bg='#81b38e')
        button1 = tk.Button(self, text="Back",
            command=lambda: controller.display("MainMenu"),
            fg='#ffffff', bg='#266136')
        button2 = tk.Button(self, text="Create",
            command=lambda: createAction(), fg='#ffffff', bg='#266136')

        label.pack(pady=30)
        entry.pack(pady=20)
        button2.pack(pady=20)
        button1.pack(pady=20)
        
# This class controls the 'MainMenu' frame and acts as the homepage. 
class MainMenu(tk.Frame):
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

        label3 = tk.Label(labelFrame,text="This ",
            font=('calibre', 10), bg='#81b38e')

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

storeData()
loadData()
create(9)
app = DataBaseApp()
app.mainloop()