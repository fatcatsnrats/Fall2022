# 0001 11/14/2022
## Begin Omar A. Student here (11/14/2022)

from tkinter import *
import os

window = Tk()
windowFrame = Frame(bg= '#81b38e')
windowFrame1 = Frame(bg= '#81b38e')
windowFrame2 = Frame(bg= '#81b38e')
windowFrame3 = Frame(bg= '#81b38e')

def mainMenu():
    window.geometry('400x400')
    window.title("Mad Libs Generator")

    Label(windowFrame, text= 'Story Generator', fg= '#1c241c', bg= '#81b38e',
    font= 'calibri 26 bold').pack()
    Label(windowFrame, text= 'Click any button to continue', fg= '#1c241c',
    bg= '#81b38e', font= 'calibri 20').pack(pady= '15')

    buttonFrame = Frame(master= windowFrame, bg= '#b6dec0')
    Button(master= buttonFrame, text= 'The Photographer', font= 'calibri 16',
        command= photographerButton, fg= '#ffffff',
        bg= '#266136').pack(padx='5', pady= '5')
    Button(master= buttonFrame, text= 'Apples and Apples', font= 'calibri 16',
        command= applesButton, fg= '#ffffff',
        bg= '#266136').pack(padx='50', pady= '5')
    Button(master= buttonFrame, text= 'The Butterfly', font= 'calibri 16',
        command= butterflyButton, fg= '#ffffff',
        bg= '#266136').pack(padx='5', pady= '5')
    Button(master= buttonFrame, text= 'Quit', font= 'calibri 16',
        command= quit, fg= '#266136', bg= '#ffffff').pack(padx='5', pady= '5')
    windowFrame.pack(fill= BOTH, expand= TRUE)
    buttonFrame.pack(fill= Y)

def backButton3():
    windowFrame3.destroy()
    windowFrame = Frame(bg= '#81b38e')
    mainMenu()

def backButton2():
    windowFrame2.destroy()
    windowFrame = Frame(bg= '#81b38e')
    mainMenu()

def backButton1():
    windowFrame1.destroy()
    windowFrame = Frame(bg= '#81b38e')
    mainMenu()

def photographerButton():
    windowFrame.destroy()
    window.geometry('800x430')
    window.configure(bg= '#b6dec0')
    windowFrame3 = Frame(bg= '#81b38e').pack()
    Button(windowFrame3, text= 'Quit', font= 'calibri 16', command= quit,
        fg= '#ffffff', bg= '#266136').place(x = 740, y = 375)
    Button(windowFrame3, text= 'Go Back', font= 'calibri 16',
        command= backButton3, fg='#ffffff', bg='#266136').place(x = 640, y = 375)

    a = Label(windowFrame3, text= 'Say ', fg= '#1c241c', bg= '#b6dec0',
        font= 'calibri 16').place(x = 20, y = 30)
    food = Entry(windowFrame3, width= 14, fg= '#353635', bg= '#ffffff',
        font= 'calibri 16')
    b = Label(windowFrame3, 
        text=', the photographer said as the camera flashed!', fg= '#1c241c',
        bg= '#b6dec0', font= 'calibri 16').place(x = 220, y = 30)
    name = Entry(windowFrame3, width= 14, fg= '#353635', bg= '#ffffff',
        font= 'calibri 16')
    c = Label(windowFrame3, text= 'and I had gone to ', fg= '#1c241c',
        bg= '#b6dec0', font= 'calibri 16').place(x = 20, y = 90)
    place = Entry(windowFrame3, width= 17, fg= '#353635', bg= '#ffffff',
        font= 'calibri 16')
    d = Label(windowFrame3, text= 'to get our photos taken on my birthday.',
        fg= '#1c241c', bg= '#b6dec0', font= 'calibri 16').place(x = 380, y = 90)
    e = Label(windowFrame3, 
        text='The first photo we really wanted was a picture of us dressed as',
        fg= '#1c241c', bg= '#b6dec0', font= 'calibri 16').place(x = 20, y = 150)
    animals = Entry(windowFrame3, width= 14, fg= '#353635', bg= '#ffffff',
        font= 'calibri 16')
    f = Label(windowFrame3, text= 'pretending to be a ', fg= '#1c241c',
        bg= '#b6dec0', font= 'calibri 16').place(x = 20, y = 210)
    profession = Entry(windowFrame3, width= 14, fg= '#353635',
        bg= '#ffffff', font= 'calibri 16')
    g = Label(windowFrame3,
        text='. When we saw the second photo, it was exactly', fg= '#1c241c',
        bg= '#b6dec0', font= 'calibri 16').place(x = 350, y = 210)
    h = Label(windowFrame3, text= 'what I wanted. We both looked like ',
        fg= '#1c241c', bg= '#b6dec0', font= 'calibri 16').place(x = 20, y = 270)
    things = Entry(windowFrame3, width= 14, fg= '#353635', bg= '#ffffff',
        font= 'calibri 16')
    i = Label(windowFrame3, text= 'wearing ', fg= '#1c241c', bg= '#b6dec0',
        font= 'calibri 16').place(x = 500, y = 270)
    cloth = Entry(windowFrame3, width= 14, fg= '#353635', bg= '#ffffff',
        font= 'calibri 16')
    j = Label(windowFrame3, text= 'and ', fg= '#1c241c', bg= '#b6dec0',
        font= 'calibri 16').place(x = 20, y = 330)
    verb = Entry(windowFrame3, width= 14, fg= '#353635', bg= '#ffffff',
        font= 'calibri 16')
    k = Label(windowFrame3, text= ' -- exactly what I had in mind',
        fg= '#1c241c', bg= '#b6dec0', font= 'calibri 16').place(x = 200, y = 330)

    food.insert(0, 'Food')
    food.place(x = 65, y = 30)
    name.insert(0, 'Name')
    name.place(x = 625, y = 30)
    place.insert(0, 'Place')
    place.place(x = 180, y = 90)
    animals.insert(0, 'Animals')
    animals.place(x = 567, y = 150)
    profession.insert(0, 'Profession')
    profession.place(x = 190, y = 210)
    things.insert(0, 'Things')
    things.place(x = 337, y = 270)
    cloth.insert(0, 'Cloth')
    cloth.place(x = 580, y = 270)
    verb.insert(0, 'Verb')
    verb.place(x = 65, y = 330)


def applesButton():
    windowFrame.destroy()
    window.geometry('800x430')
    window.configure(bg= '#b6dec0')
    windowFrame2 = Frame(bg= '#81b38e').pack()

    Label(windowFrame2, text= 'Today we picked apple from', fg= '#1c241c',
        bg= '#b6dec0', font= 'calibri 16').place(x = 20, y = 30)
    Label(windowFrame2, text= "'s Orchard. I had no idea there were so many",
        fg= '#1c241c', bg= '#b6dec0', font= 'calibri 16').place(x = 380, y = 30)
    Label(windowFrame2, text= "different varieties of apples. I ate",
        fg= '#1c241c', bg= '#b6dec0', font= 'calibri 16').place(x = 20, y = 90)
    Label(windowFrame2, text= "apples straight off the tree that tasted like",
        fg= '#1c241c', bg= '#b6dec0', font= 'calibri 16').place(x = 390, y = 90)
    Label(windowFrame2, text= ".Then there was a", fg= '#1c241c',
        bg= '#b6dec0',font= 'calibri 16').place(x = 90, y = 150)
    Label(windowFrame2, text= "apple that looked like a", fg= '#1c241c',
        bg= '#b6dec0', font= 'calibri 16').place(x = 355, y = 150)
    Label(windowFrame2, text= ".When our bags", fg= '#1c241c', bg= '#b6dec0',
        font= 'calibri 16').place(x = 640, y = 150)
    Label(windowFrame2,
        text="were full, we went on a free hay ride to"
        "                    and back. It ended at a hay pile",
        fg= '#1c241c', bg= '#b6dec0', font= 'calibri 16').place(x = 20, y = 210)
    Label(windowFrame2, text= "where we got to ", fg= '#1c241c', bg='#b6dec0',
        font= 'calibri 16').place(x = 20, y = 270)
    Label(windowFrame2,
        text=". I can hardly wait to get home and cook with the apples.",
        fg= '#1c241c', bg= '#b6dec0', font= 'calibri 16').place(x = 305, y = 270)
    Label(windowFrame2, 
        text="We are going to make apple"
        "                   and                     pies!", fg= '#1c241c',
        bg= '#b6dec0', font= 'calibri 16').place(x = 20, y = 330)

    person = Entry(windowFrame2, width= 9, fg= '#353635',
        bg= '#cef5d7', font= 'calibri 16')
    color = Entry(windowFrame2, width= 6, fg= '#353635',
        bg= '#cef5d7', font= 'calibri 16')
    foods = Entry(windowFrame2, width= 6, fg= '#353635',
        bg= '#cef5d7', font= 'calibri 16')
    adjective = Entry(windowFrame2, width= 8, fg= '#353635',
        bg= '#cef5d7', font= 'calibri 16')
    thing = Entry(windowFrame2, width= 6, fg= '#353635',
        bg= '#cef5d7', font= 'calibri 16')
    place = Entry(windowFrame2, width= 8, fg= '#353635',
        bg= '#cef5d7', font= 'calibri 16')
    verb = Entry(windowFrame2, width= 5, fg= '#353635',
        bg= '#cef5d7', font= 'calibri 16')
    adverb = Entry(windowFrame2, width= 6, fg= '#353635',
        bg= '#cef5d7', font= 'calibri 16')
    food = Entry(windowFrame2, width= 7, fg= '#353635',
        bg= '#cef5d7', font= 'calibri 16')
    things = Entry(windowFrame2, width= 8, fg= '#353635',
        bg= '#cef5d7', font= 'calibri 16')
    
    person.insert(0, 'Person')
    person.place(x = 275, y = 30)
    color.insert(0, 'Color')
    color.place(x = 310, y = 90)
    foods.insert(0, 'Foods')
    foods.place(x = 20, y = 150)
    adjective.insert(0, 'Adjective')
    adjective.place(x = 255, y = 150)
    thing.insert(0, 'Thing')
    thing.place(x = 565, y = 150)
    place.insert(0, 'Place')
    place.place(x = 363, y = 210)
    verb.insert(0, 'Verb')
    verb.place(x = 170, y = 270)
    adverb.insert(0, 'Adverb')
    adverb.place(x = 235, y = 270)
    food.insert(0, 'Food')
    food.place(x = 270, y = 330)
    things.insert(0, 'Things')
    things.place(x = 397, y = 330)


def butterflyButton():
    windowFrame.destroy()
    window.geometry('800x430')
    window.configure(bg= '#b6dec0')
    windowFrame1 = Frame(bg= '#81b38e').pack()

    a = Label(windowFrame1,
        text='Last night I dreamed I was a                      butterfly with'
        '                splotches that looked like ', fg='#1c241c', bg='#b6dec0',
        font= 'calibri 16').place(x = 20, y = 30)
    b = Label(windowFrame1,
        text='.I flew to              with my bestfriend and                '
        'who was a          .', fg= '#1c241c', bg= '#b6dec0',
        font= 'calibri 16').place(x = 80, y = 90)
    c = Label(windowFrame1,
        text='We ate some                when we got there and then decided to'
        '                 and the dream', fg= '#1c241c', bg= '#b6dec0',
        font= 'calibri 16').place(x = 20, y = 150)
    d = Label(windowFrame1,
        text='ended when I said-- lets', fg= '#1c241c', bg= '#b6dec0',
        font= 'calibri 16').place(x = 20, y = 210)

    adjective = Entry(windowFrame1, width= 9, fg= '#353635',
        bg= '#cef5d7', font= 'calibri 16')
    color = Entry(windowFrame1, width= 6, fg= '#353635',
        bg= '#cef5d7', font= 'calibri 16')
    thing = Entry(windowFrame1, width= 5, fg= '#353635',
        bg= '#cef5d7', font= 'calibri 16')
    place = Entry(windowFrame1, width= 5, fg= '#353635',
        bg= '#cef5d7', font= 'calibri 16')
    person = Entry(windowFrame1, width= 6, fg= '#353635',
        bg= '#cef5d7', font= 'calibri 16')
    adjective1 = Entry(windowFrame1, width= 8, fg= '#353635',
        bg= '#cef5d7', font= 'calibri 16')
    insect = Entry(windowFrame1, width= 6, fg= '#353635',
        bg= '#cef5d7', font= 'calibri 16')
    food = Entry(windowFrame1, width= 6, fg= '#353635',
        bg= '#cef5d7', font= 'calibri 16')
    verb = Entry(windowFrame1, width= 6, fg= '#353635',
        bg= '#cef5d7', font= 'calibri 16')
    verb1 = Entry(windowFrame1, width= 6, fg= '#353635',
        bg= '#cef5d7', font= 'calibri 16')

    adjective.insert(0, 'adjective')
    color.insert(0, 'color')
    thing.insert(0, 'thing')
    place.insert(0, 'place')
    person.insert(0, 'person')
    adjective1.insert(0, 'adjective1')
    insect.insert(0, 'insect')
    food.insert(0, 'food')
    verb.insert(0, 'verb')
    verb1.insert(0, 'verb1')

    adjective.place(x = 265, y = 30)
    color.place(x = 493, y = 30)
    thing.place(x = 20, y = 90)
    place.place(x = 163, y = 90)
    person.place(x = 432, y = 90)
    adjective1.place(x = 602, y = 90)
    insect.place(x = 705, y = 90)
    food.place(x = 142, y = 150)
    verb.place(x = 557, y = 150)
    verb1.place(x = 230, y = 210)

mainMenu()
window.mainloop()

# 0001 11/14/2022
## END Omar A. Student here (11/14/2022)