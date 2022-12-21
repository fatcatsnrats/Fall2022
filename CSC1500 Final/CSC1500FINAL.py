import pickle
import random
from PIL import ImageTk, Image
import tkinter as tk
from tkinter import filedialog as fd
from tkinter import ttk
from tkinter.messagebox import showinfo, askyesnocancel
import tkinter.scrolledtext as st


database = []
dogProfile = None
activities = ["Fetching balls", "Swimming", "Chewing bones",
    "Playing tug-of-war", "Sunbathing", "Jogging", "Jumping",
    "Chasing rabbits", "Napping", "Playing frisbee"]
stockImage = (r'C:\Users\omara\Documents\Fall2022\CSC1500 Final'
    + r'\dog-cat-full-dataset\data\test\dogs\dog.8898.jpg')

# This method is in charge of randomly generating all random database fields
# except for email.
def generate(index):

    def name():
        dogNames = ["Buddy", "Daisy", "Max", "Charlie", "Lucy", "Molly",
            "Sadie", "Rocky", "Toby", "Coco", "Tucker", "Lady", "Bailey",
            "Zeus", "Ziggy", "Gizmo", "Maddie", "Milo", "Oscar", "Peanut",
            "Roxy", "Stella", "Sadie", "Stella", "Sasha", "Lola", "Chloe",
            "Leo", "Riley", "Peanut", "Bella", "Lily", "Roxy", "Maddie",
            "Sadie", "Charlie", "Zeus", "Ziggy", "Winston", "Lola", "Maddie",
            "Peanut", "Oliver", "Max", "Sammy", "Rocky", "Toby", "Tucker",
            "Stella", "Sadie"]
        return dogNames[random.randint(0, len(dogNames) - 1)]

    def gender():
        return random.choices(['Male', 'Female', 'Other'])[0]

    def photo():
        photo = None
        while photo is None:
            tempInt = ''
            for i in range(4):
                tempInt += str(random.randint(0,9))

            filePath = ((r'C:\Users\omara\Documents\Fall2022\CSC1500 Final'
                r'\dog-cat-full-dataset\data\test\dogs\example').replace(
                'example', ('dog.' + str(int(tempInt)) + '.jpg'
            )))

            try:
                photo = Image.open(filePath)
            except FileNotFoundError:
                pass
        return filePath

    def phone():
        tempInt = ''
        for i in range(12):
            tempInt += str(random.randint(0,9))
        return ("(" + tempInt[:3] + ")-" + tempInt[3:6] + "-" + tempInt[6:11])

    def age():
        tempInt = ''
        for i in range(2):
            tempInt += str(random.randint(0,9))
            
        if int(tempInt[1]) < 4:
            return int('1' + tempInt[1])
        return (int(tempInt[0]) + 1)

    def breed():
        dogBreeds = ["Beagle", "Boxer", "Bulldog", "Chihuahua",
            "Cocker Spaniel", "Dachshund", "Dalmatian",
            "Golden Retriever", "Great Dane", "Greyhound",
            "Husky", "Labrador Retriever", "Poodle", "Pug",
            "Rottweiler", "Shar-Pei", "Shetland Sheepdog", "Shih Tzu",
            "Yorkshire Terrier"]
        return dogBreeds[int(random.randint(0, len(dogBreeds) - 1))]

    def favoriteActivities():
        favorite = []
        for x in range(3):
            newEntry = activities[random.randint(0,9)]
            if newEntry in favorite:
                x -= 1
            else:
                favorite.append(newEntry)
        return favorite

    def email(x):
        if x == 0:
            return 'idk'
        return 'nonya'

    for x in range(index):
        tempDict = {'Name': name(), 'Phone': phone(), 'Age': age(),
            'Gender' : gender(), 'Breed': breed(), 'Photo': photo(),
            'Favorite Activities': favoriteActivities(), 'Email': email(x)}
        if x == 0:
            tempDict['Minimum Age'] = 6
            tempDict['Maximum Age'] = 12
        database.append(tempDict)
    
# This method deserializes the 'database' list.
def loadData():
    fp = r'C:\Users\omara\Documents\Fall2022\CSC1500 Final\dog_database.txt'
    pickledData = open(fp, "rb")
    data = pickle.load(pickledData)
    return data

# This method serializes the 'database' list.
def saveData():
    fp = r'C:\Users\omara\Documents\Fall2022\CSC1500 Final\dog_database.txt'
    with open(fp, 'wb') as file:
        pickle.dump(database, file)

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
def databaseQuery(query):
    results = []
    for x in range(len(database)):
        if query in (database[x]['Favorite Activities']):
            results.append(x)
    return results

# This method returns the database entry that has its ['Email'] value
# matching the 'email' string.
def loginDatabase(email):
    database = loadData()
    for i in database:
        if (i['Email'] == email):
            return i
    return None


# This is where the GUI is contained.
class DogTinderApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.dogProfile = {}
        self.mainFrame = tk.Frame(self, bg='#81b38e', height=670)
        self.buttonFrame = tk.Frame(self, bg='#81b38e', height=50)

        # 'ldFile' is where likedDogs is serialized, pdFile is where
        # 'potentialDogs' is serialized, iFile is where
        # the 'index' is serialized, and message is where
        # 'messagesList' is serialized.
        self.ldFile = (
            r'C:\Users\omara\Documents\Fall2022\CSC1500 Final\liked.txt')
        self.pdFile = (
            r'C:\Users\omara\Documents\Fall2022\CSC1500 Final\potential.txt')
        self.iFile = (
            r'C:\Users\omara\Documents\Fall2022\CSC1500 Final\index.txt')
        self.message = (
            r'C:\Users\omara\Documents\Fall2022\CSC1500 Final\message.txt')

        self.minsize(400,720)
        self.maxsize(400,720)
        self.config(bg='#81b38e')
        self.mainFrame.pack(fill=tk.BOTH, expand=True)

        # Sign up / Login page
        emailPasswordFrame = tk.Frame(self.mainFrame, bg='#81b38e')
        userNameLabel = tk.Label(emailPasswordFrame,
        text='Email: ', bg='#81b38e')
        userNameEntry = tk.Entry(emailPasswordFrame)
        emailPasswordFrame.pack()
        login = tk.Button(self.mainFrame,
            command= lambda: goToMain(), text='Login')
        signUp = tk.Button(self.mainFrame,
            command= lambda: goToSignUp(), text='Sign Up')
        self.buttonFrame.pack()
        userNameLabel.grid(pady=15)
        userNameEntry.grid(row=1, column=0, pady=5)
        login.pack(pady=15)
        signUp.pack(pady=10)

        # Creates new values for the user and calls the signUp() method.
        def goToSignUp():
            self.index = 0
            self.messagesList = []
            self.potentialDog = []
            self.likedDogs = []
            self.store()
            login.destroy()
            signUp.destroy()
            emailPasswordFrame.destroy()
            self.signUp('Sign up to Dog Tinder!')

        # Since the user is trying to log in, this method tries to import
        # the user's data from their device. It then tries to find the email
        # the user submitted and checks to see if its in the database.
        def goToMain():
            try:
                with open(self.ldFile, 'rb') as liked:
                    self.likedDogs = list(pickle.load(liked))
            except:
                self.likedDogs = []
            try:
                with open(self.pdFile, 'rb') as potential:
                    self.potentialDog = list(pickle.load(potential))
            except:
                self.potentialDog = []
            try:
                with open(self.iFile, 'rb') as liked:
                    self.index = int(pickle.load(liked))
            except:
                self.index = 0
            try:
                with open(self.message, 'rb') as messaging:
                    self.messagesList = list(pickle.load(messaging))
            except:
                self.messagesList = []

            # If the inputted email is in the database,
            # this retrives the users profile from the database,
            # copies it into the 'dogProfile' list, and calls main().
            # Otherwise, it notifies the user the they inputted
            # the wrong email.
            self.store()
            dogFile = loginDatabase(userNameEntry.get())
            print(dogFile)
            if not dogFile is None:
                self.dogProfile = dogFile
                self.store()
                login.destroy()
                signUp.destroy()
                emailPasswordFrame.destroy()
                self.main()
            else:
                showinfo(title='Error', message='Email not found!')

    # This is where the user 'likes' and 'dislikes' other dog's profiles.
    # Shows dogs from the 'potentialDog' list.
    # Whenever the user likes a dog, it appends the dog
    # to the 'likedDogs' list and calls the nextDog() method.
    # When the user dislikes a dog, nexDog() is called.
    # nextDog() adds 1 to the index, calls methods that save data,
    # and loads a new dog from potentialDogs.
    # All dogs in potentialDog have at least one
    # matching favorite activity, are within the user's preffered
    # age range, and have a gender that matches the users preferences.
    def main(self):
        self.refresh()

        # If potentialDog has not been imported, it is an empty list
        # and needs to be generated.
        if ((not self.potentialDog)
                or (len(self.potentialDog) < (self.index + 1))):
            try:
                tempDict = self.dogProfile['Favorite Activities']
                minDogAge = self.dogProfile['Minimum Age']
                maxDogAge = self.dogProfile['Maximum Age']
                prefGender = self.dogProfile['Preffered Gender(s)']
                if len(tempDict) > 0:
                    for i in range(len(tempDict)):
                        for j in databaseQuery(tempDict[i]):
                            dogAge = database[j]['Age']
                            dogGender = database[j]['Gender']
                            if ((dogAge <= maxDogAge)
                                    and (dogAge >= minDogAge)
                                    and (dogGender in prefGender)):
                                self.potentialDog.append(j)
                    self.potentialDog = list(set(self.potentialDog))
            except KeyError:
                showinfo(title='Incomplete Profile',
                    message='Your profile is not yet complete!')
                self.signUp('Update Profile')

        # Displays the dogs image, the like button, the dislike button,
        # and additional information about the dog.
        try:
            dog = database[self.potentialDog[self.index]]
            self.im = Image.open(dog['Photo'])
            self.photo = ImageTk.PhotoImage(self.im.resize((380, 280)))
            self.dogImage = tk.Label(self.mainFrame, image=self.photo)
            self.dogImage.pack(pady=5)
            interactFrame = tk.Frame(self.mainFrame, bg='#81b38e')
            interactFrame.pack()
            like = tk.Button(interactFrame, text='Like',
                command=lambda: likeDog(self.index))
            dislike = tk.Button(interactFrame, text='Dislike',
                command=lambda: nextDog())
            name = tk.Label(interactFrame, bg='#81b38e', text=dog['Name'],
                font=12)
            age = tk.Label(interactFrame, bg='#81b38e', text=dog['Age'])
            gender = tk.Label(interactFrame, bg='#81b38e', text=dog['Gender'])
            like.pack(side=tk.RIGHT, padx=20)
            dislike.pack(side=tk.LEFT)
            name.pack(padx=40)
            gender.pack(padx=40)
            age.pack(padx=40)

            descFrame = tk.Frame(self.mainFrame, bg='#81b38e')
            descFrame.pack(pady=20)
            introLabel = tk.Label(descFrame,
                text=('More about ' + dog['Name']),
                bg='#81b38e', font=('calibre', 16))
            breedLabel = tk.Label(descFrame, text=('Breed: ' + dog['Breed']),
                bg='#81b38e', font=('calibre', 10))
            activitiesLabel = tk.Label(descFrame,
                text=('Favorite Activities: '
                + ', '.join(dog['Favorite Activities'])), bg='#81b38e',
                font=('calibre', 10))
            introLabel.grid(sticky=tk.W, pady=10)
            breedLabel.grid(row=1, sticky=tk.W)
            activitiesLabel.grid(row=2, sticky=tk.W)
        except IndexError or TypeError:
            showinfo(title='Sorry', message='No current matches :(')

        # Buttons on the bottom of the page that allow the user
        # to switch between the main page, the messages page,
        # and the profile page.
        mainButton = tk.Button(self.buttonFrame, bg='#81b38e',
            command=lambda: nextDog(), text='Home', height=3, width=14)
        messagesButton = tk.Button(self.buttonFrame, bg='#81b38e',
            command=lambda: messagesFrame(), text='Messages',
            height=3, width=14)
        profileButton = tk.Button(self.buttonFrame, bg='#81b38e',
            command=lambda: profileFrame(), text='Profile',
            height=3, width=14)
        mainButton.grid()
        messagesButton.grid(column=1, row=0)
        profileButton.grid(column=3, row=0)     

        # Adds 1 to the index, calls methods to store data, and calls main().
        # Also checks to see if the user ran out of potential dogs.
        # If the user had run out, it asks if the user wants 'buy'
        # more 'swipes'. If the user says yes, it will create 100 new dogs
        # in the database using the generate() method.
        def nextDog():
            destroyAll()
            if (len(self.potentialDog) > (self.index + 1)):
                self.index += 1
                self.store()
                self.main()
            else:
                reply = askyesnocancel(title='You ran out of swipes!',
                    message="Buy 'Tinder for Dogs' Gold for more swipes!")
                if reply:
                    self.potentialDog = []
                    self.index = 0
                    generate(100)
                    saveData()
                    self.store()
                    self.main()
                else:
                    self.profile()

        # Adds dogs to the 'likedDogs' list.
        def likeDog(index):
            self.likedDogs.append(database[self.potentialDog[index]])
            nextDog()

        # Destroys all widgets so the user can switch pages.
        def destroyAll():
            self.store()
            try:
                like.destroy()
                dislike.destroy()
                interactFrame.destroy()
                descFrame.destroy()
                self.dogImage.destroy()
                mainButton.destroy()
                messagesButton.destroy()
                profileButton.destroy()
            except:
                pass

        def messagesFrame():
            destroyAll()
            self.messages()    

        def profileFrame():
            destroyAll()
            self.profile()    

    # This is where the user would be able to message users they matched with.
    # On the top of the screen, there is a picture of eight dogs the user has
    # liked but not yet messaged.
    def messages(self):
        self.refresh()
        newDogsFrame = tk.Frame(self.mainFrame, width=360,
            height=250, bg='#81b38e')
        currentMessages = tk.Frame(self.mainFrame, width=380,
            height=470, bg='#81b38e')
        newDogsFrame.pack()
        currentMessages.pack()

        # Displays up to 8 dogs the user has liked but not yet messaged.
        if self.likedDogs:
            photoList = set({})
            for x in self.likedDogs:
                photoList.add(x['Photo'])
            photoList = list(photoList)
            try:
                self.im1 = Image.open(photoList[0])
                self.photo1 = ImageTk.PhotoImage(self.im1.resize((85, 65)))
                self.dogImage1 = tk.Label(newDogsFrame, image=self.photo1)
                self.dogImage1.grid()

                self.im2 = Image.open(photoList[1])
                self.photo2 = ImageTk.PhotoImage(self.im2.resize((85, 65)))
                self.dogImage2 = tk.Label(newDogsFrame, image=self.photo2)
                self.dogImage2.grid(column=1, row=0)

                self.im3 = Image.open(photoList[2])
                self.photo3 = ImageTk.PhotoImage(self.im3.resize((85, 65)))
                self.dogImage3 = tk.Label(newDogsFrame, image=self.photo3)
                self.dogImage3.grid(column=2, row=0)

                self.im4 = Image.open(photoList[3])
                self.photo4 = ImageTk.PhotoImage(self.im4.resize((85, 65)))
                self.dogImage4 = tk.Label(newDogsFrame, image=self.photo4)
                self.dogImage4.grid(column=3, row=0)

                self.im5 = Image.open(photoList[4])
                self.photo5 = ImageTk.PhotoImage(self.im5.resize((85, 65)))
                self.dogImage5 = tk.Label(newDogsFrame, image=self.photo5)
                self.dogImage5.grid(column=0, row=1)

                self.im6 = Image.open(photoList[5])
                self.photo6 = ImageTk.PhotoImage(self.im6.resize((85, 65)))
                self.dogImage6 = tk.Label(newDogsFrame, image=self.photo6)
                self.dogImage6.grid(column=1, row=1)

                self.im7 = Image.open(photoList[6])
                self.photo7 = ImageTk.PhotoImage(self.im7.resize((85, 65)))
                self.dogImage7 = tk.Label(newDogsFrame, image=self.photo7)
                self.dogImage7.grid(column=2, row=1)

                self.im8 = Image.open(photoList[7])
                self.photo8 = ImageTk.PhotoImage(self.im8.resize((85, 65)))
                self.dogImage8 = tk.Label(newDogsFrame, image=self.photo8)
                self.dogImage8.grid(column=3, row=1)
            except:
                pass
        else:
            noLikes = tk.Label(newDogsFrame,
                text='You dont have any matches yet!', bg='#81b38e')
            noLikes.pack(pady=30)

        label = tk.Label(currentMessages,
            text='You have no current conversations', font=16, bg='#81b38e')
        label.pack(pady=50)
        
        # Buttons on the bottom of the page that allow the user
        # to switch between the main page, the messages page,
        # and the profile page.
        mainButton = tk.Button(self.buttonFrame,
            bg='#81b38e', command=lambda: homeFrame(),
            text='Home', height=3, width=14)
        messagesButton = tk.Button(self.buttonFrame,
            bg='#81b38e', command=lambda: messagesFrame(),
            text='Messages', height=3, width=14)
        profileButton = tk.Button(self.buttonFrame,
            bg='#81b38e', command=lambda: profileFrame(),
            text='Profile', height=3, width=14)
        mainButton.grid()
        messagesButton.grid(column=1, row=0)
        profileButton.grid(column=3, row=0)

        # Destroys all widgets so the user can switch pages.
        def destroyAll():
            self.store()
            newDogsFrame.destroy()
            currentMessages.destroy()
            mainButton.destroy()
            messagesButton.destroy()
            profileButton.destroy()

        def homeFrame():
            destroyAll()
            self.main()

        def messagesFrame():
            destroyAll()
            self.messages()
        
        def profileFrame():
            destroyAll()
            self.profile()


    def signUp(self, title):
        prefGendersArr = []
        male = tk.IntVar()
        female = tk.IntVar()
        other = tk.IntVar()

        def dIndex():
            return database.index(loginDatabase(self.dogProfile['Email']))

        # Gets called when the user presses the prefferred gender buttons.
        # Acts as an on/off switch.
        def addPrefGender(gender):
            if gender in prefGendersArr:
                prefGendersArr.pop(prefGendersArr.index(gender))
            else:
                prefGendersArr.append(gender)

        self.refresh()

        # Title and frame
        label = tk.Label(self.mainFrame, text=title,font=14, bg='#81b38e')
        profileFrame = tk.Frame(self.mainFrame, bg='#81b38e', width=380)
        label.pack(side=tk.TOP)
        profileFrame.pack()

        # Text labels
        nameLabel = tk.Label(profileFrame, text="Name:", bg='#81b38e')
        ageLabel = tk.Label(profileFrame, text="Age:", bg='#81b38e')
        minAgeLabel = tk.Label(profileFrame, text="Minimum Age:",
            bg='#81b38e')
        maxAgeLabel = tk.Label(profileFrame, text="Maximum Age:",
            bg='#81b38e')
        genderLabel = tk.Label(profileFrame, text="Gender:", bg='#81b38e')
        phoneLabel = tk.Label(profileFrame, text="Phone Number:",
            bg='#81b38e')
        activitiesLabel = tk.Label(profileFrame, text="Favorite Activities:",
            bg='#81b38e')
        breedLabel = tk.Label(profileFrame, text='Breed:', bg='#81b38e')
        emailLabel = tk.Label(profileFrame, text='Email:', bg='#81b38e')
        prefGender = tk.Label(profileFrame, text='Preffered Gender(s):',
            bg='#81b38e')
        photoLabel = tk.Label(profileFrame, text='Photo:', bg='#81b38e')

        # Collects user entries
        nameField = tk.Entry(profileFrame)
        ageField = tk.Entry(profileFrame)
        minAgeField = tk.Entry(profileFrame)
        maxAgeField = tk.Entry(profileFrame)
        genderField = ttk.Combobox(profileFrame, width=17,
            values=['Male', 'Female', 'Other'])
        phoneField = tk.Entry(profileFrame)
        prefGenderFrame = tk.Frame(profileFrame, bg='#81b38e')
        prefGender1 = tk.Checkbutton(prefGenderFrame, text='Male',
            bg='#81b38e', command=lambda: addPrefGender('Male'),
            variable=male)
        prefGender2 = tk.Checkbutton(prefGenderFrame, text='Female',
            bg='#81b38e', command=lambda: addPrefGender('Female'),
            variable=female)
        prefGender3 = tk.Checkbutton(prefGenderFrame, text='Other',
            bg='#81b38e', command=lambda: addPrefGender('Other'),
            variable=other)
        prefGender1.pack(pady=2)
        prefGender2.pack(pady=2)
        prefGender3.pack(pady=2)
        comboBoxFrame = tk.Frame(profileFrame, bg='#81b38e')
        activBox1 = ttk.Combobox(comboBoxFrame,
            values=activities, width=17)
        activBox2 = ttk.Combobox(comboBoxFrame,
            values=activities, width=17)
        activBox3 = ttk.Combobox(comboBoxFrame,
            values=activities, width=17)
        activBox1.pack(pady=2)
        activBox2.pack(pady=2)
        activBox3.pack(pady=2)
        breedField = tk.Entry(profileFrame)
        photoButton = tk.Button(profileFrame, text='Upload Photo',
            command=lambda: importImage())
        emailField = tk.Entry(profileFrame)
        submit = tk.Button(profileFrame, text='Submit',
            command=lambda: submitProfile())
        
        # Pre-loads entries using the user's 'dogProfile'.
        def updateValues():
            try:
                nameField.insert(0,self.dogProfile['Name'])
            except KeyError:
                pass
            try:
                ageField.insert(0,self.dogProfile['Age'])
            except KeyError:
                pass
            try:
                genderField.insert(0,self.dogProfile['Gender'])
            except KeyError:
                pass
            try:
                breedField.insert(0,self.dogProfile['Breed'])
            except KeyError:
                pass
            try:
                minAgeField.insert(0,self.dogProfile['Minimum Age'])
            except KeyError:
                pass
            try:
                maxAgeField.insert(0,self.dogProfile['Maximum Age'])
            except KeyError:
                pass
            try:
                activBox1.insert(0,self.dogProfile['Favorite Activities'][0])
                activBox2.insert(0,self.dogProfile['Favorite Activities'][1])
                activBox3.insert(0,self.dogProfile['Favorite Activities'][2])
            except KeyError:
                pass
            try:
                phoneField.insert(0,self.dogProfile['Phone'])
            except KeyError:
                pass
            try:
                emailField.insert(0,self.dogProfile['Email'])
            except KeyError:
                pass

        updateValues()

        # Arranges and displays the text labels and entries.
        nameLabel.grid(row=0, column=0, pady=2)
        nameField.grid(row=0, column=1, pady=2)
        ageLabel.grid(row=1, column=0, pady=2)
        ageField.grid(row=1, column=1, pady=2)
        minAgeLabel.grid(row=2, column=0, pady=2)
        minAgeField.grid(row=2, column=1, pady=2)
        maxAgeLabel.grid(row=3, column=0, pady=2)
        maxAgeField.grid(row=3, column=1, pady=2)
        genderLabel.grid(row=4, column=0, pady=2)
        genderField.grid(row=4, column=1, pady=2)
        phoneLabel.grid(row=5, column=0, pady=2)
        phoneField.grid(row=5, column=1, pady=2)
        activitiesLabel.grid(row=6, column=0, pady=2)
        comboBoxFrame.grid(row=6, column=1, pady=2)
        breedLabel.grid(row=7, column=0, pady=2)
        breedField.grid(row=7, column=1, pady=2)
        emailLabel.grid(row=8, column=0, pady=2)
        emailField.grid(row=8, column=1, pady=2)
        prefGender.grid(row=9, column=0)
        prefGenderFrame.grid(row=9, column=1)
        photoLabel.grid(row=10, column=0, pady=2)
        photoButton.grid(row=10, column=1, pady=2)
        submit.grid(row=11, column=1, pady=5)

        # Gets called when user presses the upload image button.
        # Checks to see whether file is an image.
        # If so, it adds it to the user's profile.
        # If it isnt, it adds a stock photo to the user's profile
        def importImage():
            try:
                self.dogProfile['Photo'] = fd.askopenfilename(
                    title='Import a file', initialdir='/')
                saveData()
                self.store()
                try:
                    im = Image.open(self.dogProfile['Photo'])
                    if 'update' in title.lower():
                        database[dIndex()]['Photo'] = self.dogProfile['Photo']
                except KeyError or AttributeError:
                    self.dogProfile['Photo'] = stockImage
                    raise AttributeError
                print(self.dogProfile['Photo'])
                showinfo('Image Upload', 'Image upload was successful!')
            except:
                showinfo('Error Encountered',
                    'An error occured. Image upload was unsuccessful')
            

        # This method stores whatever field you give it to 'dogProfile'.
        # Also, if the field is empty, it notifies the user and prevents
        # the user from submitting their data.
        # The 'string' variable is used as a key in 'dogProfile',
        # while the 'field' variable is the field that collects user entries.
        def setProfile(string, field):
            try:
                if field.get() == '':
                    raise TypeError
                self.dogProfile[string] = field.get()
            except:
                field.delete(0, tk.END)
                field.insert(0, 'Empty')
                showinfo('Error', (string + ' field is empty.'))

        # This method is called when the user presses the 'submit' button.
        # It will not allow the user to submit data if:
        # forbidden characters are entered, field(s) are empty,
        # or if the three age fields are not numbers.
        def submitProfile():
            setProfile('Name', nameField)
            setProfile('Age', ageField)
            setProfile('Breed', breedField)
            setProfile('Phone', phoneField)
            setProfile('Email', emailField)
            setProfile('temp', activBox1)
            setProfile('temp', activBox2)
            setProfile('temp', activBox3)
            self.dogProfile.pop('temp')
            self.dogProfile['Preffered Gender(s)'] = prefGendersArr

            try:
                self.dogProfile['Gender'] = genderField.get()
            except:
                pass
            try:
                self.dogProfile['Age'] = int(ageField.get())
            except:
                self.dogProfile.pop('Age')
                ageField.delete(0, tk.END)
                ageField.insert(0, 'Empty')
                showinfo('Error', 'Age must be an integer.')
            try:
                self.dogProfile['Minimum Age'] = int(minAgeField.get())
                self.dogProfile['Maximum Age'] = int(maxAgeField.get())
            except:
                showinfo(title='Missing information required',
                    message='The Min/Max Age Fields only accept numbers')
                try:
                    self.dogProfile['Minimum Age'] = int(minAgeField.get())
                except:
                    minAgeField.delete(0, tk.END)
                    minAgeField.insert(0,'Empty')
                try:
                    self.dogProfile['Maximum Age'] = int(maxAgeField.get())
                except:
                    maxAgeField.delete(0, tk.END)
                    maxAgeField.insert(0, 'Empty')

            if not ('Empty' in 
                    [activBox1.get(), activBox2.get(),activBox3.get()]):

                favActivies = list(set([activBox1.get(), activBox2.get(),
                    activBox3.get()]))
                self.dogProfile['Favorite Activities'] = favActivies

            self.store()

            # Checks to see if criteria is met, if so it either adds
            # or updates the database with the user's informantion.
            if ((checkForbidden(nameField.get()) == 'Forbidden')
                    or (checkForbidden(ageField.get()) == 'Forbidden')
                    or (checkForbidden(genderField.get()) == 'Forbidden')
                    or (checkForbidden(breedField.get()) == 'Forbidden')
                    or (checkForbidden(minAgeField.get()) == 'Forbidden')
                    or (checkForbidden(maxAgeField.get()) == 'Forbidden')):
                favActivies.clear()
                showinfo('Error', 'Forbidden Character Entered!')
            elif ('Empty' in [nameField.get(), ageField.get(),
                        genderField.get(), breedField.get(), phoneField.get(),
                        minAgeField.get(), maxAgeField.get(), activBox1.get(),
                        activBox2.get(), activBox3.get()]):
                    favActivies.clear()
            else:
                label.destroy()
                profileFrame.destroy()
                comboBoxFrame.destroy()
                try:
                    im = Image.open(self.dogProfile['Photo'])
                except KeyError or AttributeError:
                    self.dogProfile['Photo'] = stockImage
                if 'sign up' in title.lower():
                    database.append(self.dogProfile)
                elif 'update' in title.lower():
                    database[dIndex()] = self.dogProfile
                saveData()
                self.main()

    # This is where the user can view their profile.
    def profile(self):
        self.refresh()

        # Displays the user's profile picture.
        self.im = Image.open(self.dogProfile['Photo'])
        self.photo = ImageTk.PhotoImage(self.im.resize((380, 280)))
        self.dogImage = tk.Label(self.mainFrame, image=self.photo)
        self.dogImage.pack(pady=5)
    
        # Displays the user's name, age and gender.
        interactFrame = tk.Frame(self.mainFrame, bg='#81b38e')
        interactFrame.pack()
        name = tk.Label(interactFrame, bg='#81b38e',
            text=('Name: ' + self.dogProfile['Name']), font=12)
        age = tk.Label(interactFrame, bg='#81b38e',
            text=('Age: ' + str(self.dogProfile['Age'])))
        gender = tk.Label(interactFrame, bg='#81b38e',
            text=('Gender: ' + str(self.dogProfile['Gender'])))
        name.pack(padx=40)
        gender.pack(padx=40)
        age.pack(padx=40)

        # Displays breed, favorite activites, and preffered age range.
        descFrame = tk.Frame(self.mainFrame, bg='#81b38e')
        descFrame.pack(pady=20)
        introLabel = tk.Label(descFrame, text='Description: ',
            bg='#81b38e', font=('calibre', 16))
        breedLabel = tk.Label(descFrame,
            text=('Breed: ' + self.dogProfile['Breed']),
            bg='#81b38e', font=('calibre', 10))
        activitiesLabel = tk.Label(descFrame, text=('Favorite Activities: ' +
            ', '.join(self.dogProfile['Favorite Activities'])), bg='#81b38e',
            font=('calibre', 10))
        prefLabel = tk.Label(descFrame, text=('Preffered Gender(s): ' +
            ', '.join(self.dogProfile['Preffered Gender(s)'])), bg='#81b38e',
            font=('calibre', 10))
        prefAgeLabel = tk.Label(descFrame,
            text=('Preffered Age Range ' + str(self.dogProfile['Minimum Age'])
                + ' - ' + str(self.dogProfile['Maximum Age'])),
            bg='#81b38e', font=('calibre', 10))
        editProfileButton = tk.Button(descFrame,
            bg='#81b38e', command=lambda: editProfile(), text='Edit Profile')
        introLabel.grid(pady=10)
        breedLabel.grid(row=1, column=0)
        activitiesLabel.grid(row=2, column=0)
        prefLabel.grid(row=3, column=0)
        prefAgeLabel.grid(row=4, column=0)
        editProfileButton.grid(row=5, column=0, pady=20)

        # Buttons on the bottom of the page that allow the user
        # to switch between the main page, the messages page,
        # and the profile page.
        mainButton = tk.Button(self.buttonFrame, bg='#81b38e',
            command=lambda: homeFrame(), text='Home',
            height=3, width=14)
        messagesButton = tk.Button(self.buttonFrame, bg='#81b38e',
            command=lambda: messagesFrame(), text='Messages',
            height=3, width=14)
        profileButton = tk.Button(self.buttonFrame, bg='#81b38e',
            text='Profile', height=3, width=14)
        mainButton.grid()
        messagesButton.grid(column=1, row=0)
        profileButton.grid(column=3, row=0)     

        # Destroys all widgets so the user can switch pages.
        def destroyAll():
            interactFrame.destroy()
            descFrame.destroy()
            self.dogImage.destroy()
            mainButton.destroy()
            messagesButton.destroy()
            profileButton.destroy()

        def messagesFrame():
            destroyAll()
            self.messages()

        def homeFrame():
            destroyAll()
            self.main()

        def editProfile():
            destroyAll()
            self.signUp('Update Profile')

    # This method deserializes ldFile, pdFile, iFile, and message,
    # and sets them equal to likedDogs, potentialDog, index, and messagesList.
    def refresh(self):
        with open(self.ldFile, 'rb') as liked:
            self.likedDogs = list(pickle.load(liked))
        with open(self.pdFile, 'rb') as potential:
            self.potentialDog = list(pickle.load(potential))
        with open(self.iFile, 'rb') as liked:
            self.index = int(pickle.load(liked))
        with open(self.message, 'rb') as messaging:
            self.messagesList = list(pickle.load(messaging))

    # This method takes likedDogs, potentialDog, index, and messagesList,
    # and serializes them to ldFile, pdFile, iFile, and message.
    def store(self):
        with open(self.ldFile, 'wb') as liked:
            pickle.dump(self.likedDogs, liked)
        with open(self.pdFile, 'wb') as potential:
            pickle.dump(self.potentialDog, potential)
        with open(self.iFile, 'wb') as liked:
            pickle.dump(self.index, liked)
        with open(self.message, 'wb') as messaging:
            pickle.dump(self.messagesList, messaging)

database = loadData()
print(len(database))

saveData()

app = DogTinderApp()
app.mainloop()