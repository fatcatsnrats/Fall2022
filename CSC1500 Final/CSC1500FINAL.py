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
        return random.choices(['Male', 'Female', 'Other'])

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
            print('Bingo!')
        database.append(tempDict)
    
def loadData():
    filepath = r'C:\Users\omara\Documents\Fall2022\CSC1500 Final\dog_database.txt'
    pickledData = open(filepath, "rb")
    data = pickle.load(pickledData)
    return data

def saveData():
    filepath = r'C:\Users\omara\Documents\Fall2022\CSC1500 Final\dog_database.txt'
    with open(filepath, 'wb') as file:
        pickle.dump(database, file)

# # This method creates 'i' amount of random entries and appends it to database.
# # This method also concoctates the entries' email from the first and last
# # name, both of which are generated using the generator() method.
# def create(i):
#     addition = []
#     for x in range (i):
#         tempDict = {'Name': generator('Name'), 'Photo' : generator('Photo'),
#             'Phone': generator('Phone'), 'Age': generator('Age'),
#             'Breed': generator('Breed'),
#             'Favorite Activities': generator('Favorite Activities')}
#         addition.append(tempDict)
#         database.append(tempDict)
#     return addition

# create(5)

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
    print(results)
    return results

def loginDatabase(email):
    database = loadData()
    for i in database:
        if (i['Email'] == email):
            return i
    return None


# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #


# This class acts as the controller and allows switching between frames.
class DogTinderApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.mainFrame = tk.Frame(self, bg='#81b38e', height=670)
        self.buttonFrame = tk.Frame(self, bg='#81b38e', height=50)
        self.dogProfile = {}

        ldFile = r'C:\Users\omara\Documents\Fall2022\CSC1500 Final\liked.txt'
        pdFile = r'C:\Users\omara\Documents\Fall2022\CSC1500 Final\potential.txt'
        iFile = r'C:\Users\omara\Documents\Fall2022\CSC1500 Final\index.txt'
        message = r'C:\Users\omara\Documents\Fall2022\CSC1500 Final\message.txt'

        try:
            with open(ldFile, 'rb') as liked:
                self.likedDogs = list(pickle.load(liked))
        except:
            self.likedDogs = []

        try:
            with open(pdFile, 'rb') as potential:
                self.potentialDog = list(pickle.load(potential))
        except:
            self.potentialDog = []

        try:
            with open(iFile, 'rb') as liked:
                self.index = int(pickle.load(liked))
        except:
            self.index = 0

        try:
            with open(message, 'rb') as messaging:
                self.messagesList = int(pickle.load(messaging))
        except:
            self.messagesList = 0

        self.minsize(400,720)
        self.maxsize(400,720)
        self.config(bg='#81b38e')
        self.mainFrame.pack(fill=tk.BOTH, expand=True)
        emailPasswordFrame = tk.Frame(self.mainFrame, bg='#81b38e')
        userNameLabel = tk.Label(emailPasswordFrame, text='Username: ', bg='#81b38e')
        userNameEntry = tk.Entry(emailPasswordFrame)
        emailPasswordFrame.pack()
        login = tk.Button(self.mainFrame, command= lambda: goToMain(), text='Login')
        signUp = tk.Button(self.mainFrame, command= lambda: goToSignUp(), text='Sign Up')
        self.buttonFrame.pack()
        userNameLabel.grid(pady=15)
        userNameEntry.grid(row=1, column=0, pady=5)
        login.pack(pady=15)
        signUp.pack(pady=10)

        def goToSignUp():
            login.destroy()
            signUp.destroy()
            emailPasswordFrame.destroy()
            self.signUp()

        def goToMain():
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
                showinfo(title='Error', message='Incorrect Password')

    def main(self):
        self.refresh()
        # mainFrame = tk.Frame(self, bg='#81b38e', height=670)
        # buttonFrame = tk.Frame(self, bg='#81b38e', height=50)
        # mainFrame.pack()
        # buttonFrame.pack()

        # if dogProfile is None:
        #     showinfo(title='Create a profile', message='You must create a profile first!', )
        #     self.profile()

        def findMatches():
            tempDict = self.dogProfile['Favorite Activities']
            minDogAge = self.dogProfile['Minimum Age']
            maxDogAge = self.dogProfile['Maximum Age']

            if len(tempDict) > 0:
                for i in range(len(tempDict)):
                    for j in databaseQuery(tempDict[i]):
                        dogAge = database[j]['Age']
                        if (not ((dogAge >= maxDogAge) or (dogAge <= minDogAge))):
                            self.potentialDog.append(j)
                return list(set(self.potentialDog))
            else:
                showinfo(title='Incomplete Profile',
                    message='Enter your Favorite Activities to find matches!')
                self.profile()


        # gets rid of duplicates
        self.potentialDog = findMatches()

        print(self.potentialDog)
        try:
            dog = database[self.potentialDog[self.index]]
            print(dog['Photo'])
            self.im = Image.open(dog['Photo'])
            self.photo = ImageTk.PhotoImage(self.im.resize((380, 280)))
            self.dogImage = tk.Label(self.mainFrame, image=self.photo)
            self.dogImage.pack(pady=5)
        except IndexError or TypeError:
            showinfo(title='Sorry', message='No current matches :(')

        interactFrame = tk.Frame(self.mainFrame, bg='#81b38e')
        interactFrame.pack()
        like = tk.Button(interactFrame, text='Like', command=lambda: likeDog(self.index))
        dislike = tk.Button(interactFrame, text='Dislike', command=lambda: nextDog())
        name = tk.Label(interactFrame, bg='#81b38e', text=dog['Name'], font=12)
        age = tk.Label(interactFrame, bg='#81b38e', text=dog['Age'])
        gender = tk.Label(interactFrame, bg='#81b38e', text=dog['Gender'])
        like.pack(side=tk.RIGHT, padx=20)
        dislike.pack(side=tk.LEFT)
        name.pack(padx=40)
        gender.pack(padx=40)
        age.pack(padx=40)

        descFrame = tk.Frame(self.mainFrame, bg='#81b38e')
        descFrame.pack(pady=20)
        introLabel = tk.Label(descFrame, text=('More about ' + dog['Name']),
            bg='#81b38e', font=('calibre', 16))
        breedLabel = tk.Label(descFrame, text=('Breed: ' + dog['Breed']),
            bg='#81b38e', font=('calibre', 10))
        activitiesLabel = tk.Label(descFrame, text=('Favorite Activities: ' +
            ', '.join(dog['Favorite Activities'])), bg='#81b38e',
            font=('calibre', 10))
        introLabel.grid(sticky=tk.W, pady=10)
        breedLabel.grid(row=1, sticky=tk.W)
        activitiesLabel.grid(row=2, sticky=tk.W)


        mainButton = tk.Button(self.buttonFrame, bg='#81b38e', command=lambda: nextDog(), text='Home', height=3, width=14)
        messagesButton = tk.Button(self.buttonFrame, bg='#81b38e', command=lambda: messagesFrame(), text='Messages', height=3, width=14)
        profileButton = tk.Button(self.buttonFrame, bg='#81b38e', command=lambda: profileFrame(), text='Profile', height=3, width=14)
        mainButton.grid()
        messagesButton.grid(column=1, row=0)
        profileButton.grid(column=3, row=0)     

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
                    generate(100)
                    saveData()
                    self.store()
                    self.main()
                else:
                    self.profile()

        def likeDog(index):
            self.likedDogs.append(self.potentialDog[index])
            nextDog()

        def destroyAll():
            self.store()
            like.destroy()
            dislike.destroy()
            interactFrame.destroy()
            descFrame.destroy()
            self.dogImage.destroy()
            mainButton.destroy()
            messagesButton.destroy()
            profileButton.destroy()

        def messagesFrame():
            destroyAll()
            self.messages()    

        def profileFrame():
            destroyAll()
            self.profile()    


    def messages(self):
        self.refresh()
        # label = tk.Label(self.mainFrame, text='Hello', bg='#81b38e')
        # label.pack()

        newDogsFrame = tk.Frame(self.mainFrame, width=360, height=250, bg='#81b38e')
        currentMessages = tk.Frame(self.mainFrame, width=380, height=470, bg='#81b38e')
        newDogsFrame.pack()
        currentMessages.pack()

        if self.likedDogs:
            self.im1 = Image.open(self.likedDogs[0]['Photo'])
            self.photo1 = ImageTk.PhotoImage(self.im1.resize((85, 65)))
            self.dogImage1 = tk.Label(newDogsFrame, image=self.photo1)
            self.dogImage1.grid()

            self.im2 = Image.open(self.likedDogs[1]['Photo'])
            self.photo2 = ImageTk.PhotoImage(self.im2.resize((85, 65)))
            self.dogImage2 = tk.Label(newDogsFrame, image=self.photo2)
            self.dogImage2.grid(column=1, row=0)

            self.im3 = Image.open(self.likedDogs[2]['Photo'])
            self.photo3 = ImageTk.PhotoImage(self.im3.resize((85, 65)))
            self.dogImage3 = tk.Label(newDogsFrame, image=self.photo3)
            self.dogImage3.grid(column=2, row=0)

            self.im4 = Image.open(self.likedDogs[3]['Photo'])
            self.photo4 = ImageTk.PhotoImage(self.im4.resize((85, 65)))
            self.dogImage4 = tk.Label(newDogsFrame, image=self.photo4)
            self.dogImage4.grid(column=3, row=0)

            self.im5 = Image.open(self.likedDogs[4]['Photo'])
            self.photo5 = ImageTk.PhotoImage(self.im5.resize((85, 65)))
            self.dogImage5 = tk.Label(newDogsFrame, image=self.photo5)
            self.dogImage5.grid(column=0, row=1)

            self.im6 = Image.open(self.likedDogs[5]['Photo'])
            self.photo6 = ImageTk.PhotoImage(self.im6.resize((85, 65)))
            self.dogImage6 = tk.Label(newDogsFrame, image=self.photo6)
            self.dogImage6.grid(column=1, row=1)

            self.im7 = Image.open(self.likedDogs[6]['Photo'])
            self.photo7 = ImageTk.PhotoImage(self.im7.resize((85, 65)))
            self.dogImage7 = tk.Label(newDogsFrame, image=self.photo7)
            self.dogImage7.grid(column=2, row=1)

            self.im8 = Image.open(self.likedDogs[7]['Photo'])
            self.photo8 = ImageTk.PhotoImage(self.im8.resize((85, 65)))
            self.dogImage8 = tk.Label(newDogsFrame, image=self.photo8)
            self.dogImage8.grid(column=3, row=1)

        else:
            noLikes = tk.Label(newDogsFrame, text='You dont have any matches yet!', bg='#81b38e')
            noLikes.pack(pady=30)

        label = tk.Label(currentMessages,
            text='You have no current conversations', font=16, bg='#81b38e')
        label.pack(pady=50)
        




        mainButton = tk.Button(self.buttonFrame, bg='#81b38e', command=lambda: homeFrame(), text='Home', height=3, width=14)
        messagesButton = tk.Button(self.buttonFrame, bg='#81b38e', command=lambda: messagesFrame(), text='Messages', height=3, width=14)
        profileButton = tk.Button(self.buttonFrame, bg='#81b38e', command=lambda: profileFrame(), text='Profile', height=3, width=14)
        mainButton.grid()
        messagesButton.grid(column=1, row=0)
        profileButton.grid(column=3, row=0)

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


    def signUp(self):
        self.refresh()
        label = tk.Label(self.mainFrame, text='Sign Up!',font=16, bg='#81b38e')
        label.pack()
        profileFrame = tk.Frame(self.mainFrame, bg='#81b38e', width=380)
        profileFrame.pack()

        nameLabel = tk.Label(profileFrame, text="Name:", bg='#81b38e')
        ageLabel = tk.Label(profileFrame, text="Age:", bg='#81b38e')
        minAgeLabel = tk.Label(profileFrame, text="Minimum Age:", bg='#81b38e')
        maxAgeLabel = tk.Label(profileFrame, text="Maximum Age:", bg='#81b38e')
        genderLabel = tk.Label(profileFrame, text="Gender:", bg='#81b38e')
        phoneLabel = tk.Label(profileFrame, text="Phone Number:", bg='#81b38e')
        activitiesLabel = tk.Label(profileFrame, text="Favorite Activities:", bg='#81b38e')
        breedLabel = tk.Label(profileFrame, text='Breed:', bg='#81b38e')
        photoLabel = tk.Label(profileFrame, text='Photo:', bg='#81b38e')
        emailLabel = tk.Label(profileFrame, text='Email:', bg='#81b38e')

        # create text fields for each field
        nameField = tk.Entry(profileFrame)
        ageField = tk.Entry(profileFrame)
        minAgeField = tk.Entry(profileFrame)
        maxAgeField = tk.Entry(profileFrame)
        genderField = tk.Entry(profileFrame)
        phoneField = tk.Entry(profileFrame)

        comboBoxFrame = tk.Frame(profileFrame, bg='#81b38e')
        activBox1 = ttk.Combobox(comboBoxFrame, values=activities, width=17)
        activBox2 = ttk.Combobox(comboBoxFrame, values=activities, width=17)
        activBox3 = ttk.Combobox(comboBoxFrame, values=activities, width=17)
        activBox1.pack(pady=2)
        activBox2.pack(pady=2)
        activBox3.pack(pady=2)
        
        # activitiesField = tk.Text(profileFrame, height=3, width=15)
        breedField = tk.Entry(profileFrame)
        photoButton = tk.Button(profileFrame, text='Upload Photo', command=lambda: importImage())
        emailField = tk.Entry(profileFrame)
        
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

        submit = tk.Button(profileFrame, text='Submit', command=lambda: submitProfile())

        # use the grid layout manager to arrange the widgets
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
        photoLabel.grid(row=9, column=0, pady=2)
        photoButton.grid(row=9, column=1, pady=2)
        submit.grid(row=10, column=1, pady=5)

        def importImage():
            try:
                self.dogProfile['Photo'] = fd.askopenfilename(title='Import a file', initialdir='/')
                print(self.dogProfile['Photo'])
                showinfo(title='Image upload', message='Image upload successful!')
            except:
                showinfo(title='Image upload', message='Image upload unsuccessful')

        def submitProfile():
            if ((checkForbidden(nameField.get()) == 'Forbidden')
                or (checkForbidden(ageField.get()) == 'Forbidden')
                or (checkForbidden(genderField.get()) == 'Forbidden')
                or (checkForbidden(breedField.get()) == 'Forbidden')
                or (checkForbidden(minAgeField.get()) == 'Forbidden')
                or (checkForbidden(maxAgeField.get()) == 'Forbidden')
                or (checkForbidden(activBox1.get()) == 'Forbidden')
                or (checkForbidden(activBox2.get()) == 'Forbidden')
                or (checkForbidden(activBox3.get()) == 'Forbidden')):

                showinfo(title='Error',
                    message=('Forbidden Character Entered',
                    ' in Minimum/Maximum Age Field'))
                self.signUp()

            else:
                self.dogProfile['Name'] = nameField.get()
                self.dogProfile['Age'] = ageField.get()
                self.dogProfile['Gender'] = genderField.get()
                self.dogProfile['Breed'] = breedField.get()
                self.dogProfile['Phone'] = phoneField.get()
                self.dogProfile['Email'] = emailField.get()
                try:
                    self.dogProfile['Minimum Age'] = int(minAgeField.get())
                    self.dogProfile['Maximum Age'] = int(maxAgeField.get())
                except:
                    showinfo(title='Missing information required',
                    message='The Minimum/Maximum Age Fields only accept numbers')
                    self.signUp()

            favActivies = list(set([activBox1.get(), activBox2.get(), activBox3.get()]))
            self.dogProfile['Favorite Activities'] = favActivies
            # self.dogProfile['Favorite Activities'] = list((activitiesField.get("1.0", "end-1c")).split('\n'))
            print(self.dogProfile)
            self.store()
            label.destroy()
            profileFrame.destroy()
            comboBoxFrame.destroy()
            self.main()

    def profile(self):
        self.refresh()
        try:
            self.im = Image.open(self.dogProfile['Photo'])
            self.photo = ImageTk.PhotoImage(self.im.resize((380, 280)))
            self.dogImage = tk.Label(self.mainFrame, image=self.photo)
            self.dogImage.pack(pady=5)
        except IndexError:
            showinfo(title='Sorry', message='No current matches :(')
        except KeyError:
            self.im = Image.open(r'C:\Users\omara\Documents\Fall2022\CSC1500 Final\dog-cat-full-dataset\data\test\dogs\dog.8898.jpg')
            self.photo = ImageTk.PhotoImage(self.im.resize((380, 280)))
            self.dogImage = tk.Label(self.mainFrame, image=self.photo)
            self.dogImage.pack(pady=5)

        interactFrame = tk.Frame(self.mainFrame, bg='#81b38e')
        interactFrame.pack()
        name = tk.Label(interactFrame, bg='#81b38e', text=('Name: ' + self.dogProfile['Name']), font=12)
        age = tk.Label(interactFrame, bg='#81b38e', text=('Age: ' + str(self.dogProfile['Age'])))
        gender = tk.Label(interactFrame, bg='#81b38e', text=('Gender: ' + str(self.dogProfile['Gender'][0])))
        name.pack(padx=40)
        gender.pack(padx=40)
        age.pack(padx=40)

        descFrame = tk.Frame(self.mainFrame, bg='#81b38e')
        descFrame.pack(pady=20)
        introLabel = tk.Label(descFrame, text='Description: ',
            bg='#81b38e', font=('calibre', 16))
        breedLabel = tk.Label(descFrame, text=('Breed: ' + self.dogProfile['Breed']),
            bg='#81b38e', font=('calibre', 10))
        activitiesLabel = tk.Label(descFrame, text=('Favorite Activities: ' +
            ', '.join(self.dogProfile['Favorite Activities'])), bg='#81b38e',
            font=('calibre', 10))
        editProfileButton = tk.Button(descFrame, bg='#81b38e', command=lambda: editProfile(), text='Edit Profile')
        introLabel.grid(sticky=tk.W, pady=10)
        breedLabel.grid(row=1, sticky=tk.W)
        activitiesLabel.grid(row=2, sticky=tk.W)
        editProfileButton.grid(sticky=tk.S)



        mainButton = tk.Button(self.buttonFrame, bg='#81b38e', command=lambda: homeFrame(), text='Home', height=3, width=14)
        messagesButton = tk.Button(self.buttonFrame, bg='#81b38e', command=lambda: messagesFrame(), text='Messages', height=3, width=14)
        profileButton = tk.Button(self.buttonFrame, bg='#81b38e', text='Profile', height=3, width=14)
        mainButton.grid()
        messagesButton.grid(column=1, row=0)
        profileButton.grid(column=3, row=0)     

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
            self.signUp()

    def refresh(self):
        ldFile = r'C:\Users\omara\Documents\Fall2022\CSC1500 Final\liked.txt'
        pdFile = (r'C:\Users\omara\Documents\Fall2022\CSC1500 Final'
            + r'\potential.txt')
        iFile = r'C:\Users\omara\Documents\Fall2022\CSC1500 Final\index.txt'
        message = r'C:\Users\omara\Documents\Fall2022\CSC1500 Final\message.txt'

        with open(ldFile, 'rb') as liked:
            self.likedDogs = list(pickle.load(liked))
        with open(pdFile, 'rb') as potential:
            self.potentialDog = list(pickle.load(potential))
        with open(iFile, 'rb') as liked:
            self.index = int(pickle.load(liked))
        with open(message, 'rb') as messaging:
            self.messagesList = int(pickle.load(messaging))

    def store(self):
        ldFile = r'C:\Users\omara\Documents\Fall2022\CSC1500 Final\liked.txt'
        pdFile = (r'C:\Users\omara\Documents\Fall2022\CSC1500 Final'
            + r'\potential.txt')
        iFile = r'C:\Users\omara\Documents\Fall2022\CSC1500 Final\index.txt'
        message = r'C:\Users\omara\Documents\Fall2022\CSC1500 Final\message.txt'

        with open(ldFile, 'wb') as liked:
            pickle.dump(self.likedDogs, liked)
        with open(pdFile, 'wb') as potential:
            pickle.dump(self.potentialDog, potential)
        with open(iFile, 'wb') as liked:
            pickle.dump(self.index, liked)
        with open(message, 'wb') as messaging:
            pickle.dump(self.messagesList, messaging)



database = loadData()
print(len(database))

saveData()

# database = loadData()

print(len(loadData()))

# saveData()
# dogProfile = {}
# dogProfile['Photo'] = r'C:\Users\omara\Documents\Fall2022\CSC1500 Final\dog-cat-full-dataset\data\test\dogs\dog.0.jpg'
# dogProfile["Favorite Activities"] = ['Swimming', 'Jumping', 'Napping']
# dogProfile['Maximum Age'] = 12
# dogProfile['Minumum Age'] = 7

# dogProfile = create(1)

# print(create(5))
# database[3]['Email'] = 'idk'

app = DogTinderApp()
app.mainloop()