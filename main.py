from tkinter import *
import tkinter as tk
import tkinter.scrolledtext as tkst
import time
import pickle
from datetime import datetime
import os
from winsound import *
import random

#--------------------------------------------------------Globals--------------------------------------------------------

#input parsing
badInput = ["fuck", "bitch", "pussy", "", " ", "  ", "_", "cunt", "faggot", "fucker", "dick", "penis", "!", ".", "$"]
inputResponse = "null"
#global values
txtSpeed = 0.01
txtSize = 16
food = "null"
pName = "null"
currentRoom = "null"
aName = "null"
bName = "null"
liName = "null"
banditName = "null"
mercName = "null"
guardName = "null"
magicianName = "null"
bardName = "null"
thiefName = "null"
ToughName = "null"
medicName = "null"
kingdomName = "null"
neighborName = "null"
worldName = "null"
merchantName = "null"
aHairColor = "null"
aEyeColor = "null"
aSkinColor = "null"
bHairColor = "null"
bEyeColor = "null"
bSkinColor = "null"
liHairColor = "null"
liEyeColor = "null"
liSkinColor = "null"
deathReturn = "null"
pLocation = "null"
aLocation = "null"
bLocation = "null"


#!!!Flags!!!
firstTimeArc2 = "true"
knowsDeath = "false"
loosenedPlanks = "false"
hasPotato = "no"
muggerMissing = "false"
metB = "false"
firstMeeting = "true"
seenForest = "false"
#-------------------------------------------------------Functions-------------------------------------------------------

def postDeathPassage(toPrint, next):
    room_run(toPrint)

    choices = ["Continue..."]
    paths = [next]
    create_choices(choices, paths)

def loadGame(window):
    win.deiconify()
    global pName, currentRoom, food, txtSpeed, txtSize
    global firstTimeArc2, aName, bName, liName, banditName
    global mercName, guardName, magicianName, bardName
    global thiefName, toughName, medicName
    global kingdomName, neighborName, worldName, merchantName
    global aHairColor, aEyeColor, aSkinColor
    global bHairColor, bEyeColor, bSkinColor
    global liHairColor, liEyeColor, liSkinColor
    global deathReturn, hasPotato, muggerMissing, metB, firstMeeting
    global pLocation, aLocation, bLocation
    global knowsDeath, loosenedPlanks, seenForest


    with open('./savefile', 'rb') as f:
        data = pickle.load(f)

    pName = data['pName']
    currentRoom = data['currentRoom']
    food = data['food']
    txtSpeed = data['txtSpeed']
    txtSize = data['txtSize']
    firstTimeArc2 = data['firstTimeArc2']
    aName = data['aName']
    bName = data['bName']
    liName = data['liName']
    banditName = data['banditName']
    mercName = data['mercName']
    guardName = data['guardName']
    magicianName = data['magicianName']
    bardName = data['bardName']
    thiefName = data['thiefName']
    toughName = data['toughName']
    medicName = data['medicName']
    kingdomName = data['kingdomName']
    neighborName = data['neighborName']
    worldName = data['worldName']
    merchantName = data['merchantName']
    aHairColor = data['aHairColor']
    bHairColor = data['bHairColor']
    liHairColor = data['liHairColor']
    aEyeColor = data['aEyeColor']
    bEyeColor = data['bEyeColor']
    liEyeColor = data['liEyeColor']
    aSkinColor = data['aSkinColor']
    bSkinColor = data['bSkinColor']
    liSkinColor = data['liSkinColor']
    hasPotato = data['hasPotato']
    muggerMissing = data['muggerMissing']
    metB = data['metB']
    firstMeeting = data['firstMeeting']
    pLocation = data['pLocation']
    aLocation = data['aLocation']
    bLocation = data['bLocation']
    knowsDeath = data['knowsDeath']
    loosenedPlanks = data['loosenedPlanks']
    seenForest = data['seenForest']
    deathReturn = data['deathReturn']

    #delete buttons
    list = frame2.pack_slaves()
    for x in list:
        if str(x) != str(list[0]):
            x.destroy()

    disp_txt("\nLoading Game...\n")
    window.destroy()
    PlaySound(None, SND_ASYNC)
    if currentRoom == "arc1_0":
        currentRoom = "arc1_1"

    #if you just died this is a special message for you :)
    if deathReturn == "arc2_17" or deathReturn == "arc2_42":
        deathReturn = "null"
        postDeathPassage('arc2_52', currentRoom)

    elif deathReturn == "arc2_18" or deathReturn == "arc2_35" or deathReturn == "arc2_36":
        deathReturn = "null"
        postDeathPassage('arc2_56', currentRoom)

    elif deathReturn == "arc2_30" or deathReturn=="arc2_48":
        deathReturn = "null"
        postDeathPassage('arc2_54', currentRoom)

    elif deathReturn == "arc2_31" or deathReturn=="arc2_47":
        deathReturn = "null"
        postDeathPassage('arc2_53', currentRoom)

    elif deathReturn == "arc2_43":
        deathReturn = "null"
        postDeathPassage('arc2_57', currentRoom)

    elif deathReturn == "arc2_44":
        deathReturn = "null"
        postDeathPassage('arc2_55', currentRoom)
    else:
        eval(currentRoom + "()")


def saveGame(window):
    global pName, currentRoom, food, txtSpeed, txtSize
    global firstTimeArc2, aName, bName, liName, banditName
    global mercName, guardName, magicianName, bardName
    global thiefName, toughName, medicName
    global kingdomName, neighborName, worldName, merchantName
    global aHairColor, aEyeColor, aSkinColor
    global bHairColor, bEyeColor, bSkinColor
    global liHairColor, liEyeColor, liSkinColor
    global hasPotato, muggerMissing, metB, firstMeeting
    global pLocation, aLocation, bLocation
    global knowsDeath, loosenedPlanks, seenForest, deathReturn

    now = datetime.now()
    # dd/mm/YY H:M:S
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

    data = {
        'pName': pName,
        'currentRoom': currentRoom,
        'food': food,
        'txtSpeed': txtSpeed,
        'txtSize': txtSize,
        'dateTime': dt_string,
        'firstTimeArc2': firstTimeArc2,
        'aName': aName,
        'bName': bName,
        'liName': liName,
        'banditName': banditName,
        'mercName': mercName,
        'guardName': guardName,
        'magicianName': magicianName,
        'bardName': bardName,
        'thiefName': thiefName,
        'toughName': toughName,
        'medicName': medicName,
        'kingdomName': kingdomName,
        'neighborName': neighborName,
        'worldName': worldName,
        'merchantName': merchantName,
        'aHairColor': aHairColor,
        'bHairColor': bHairColor,
        'liHairColor': liHairColor,
        'aEyeColor': aEyeColor,
        'bEyeColor': bEyeColor,
        'liEyeColor': liEyeColor,
        'aSkinColor': aSkinColor,
        'bSkinColor': bSkinColor,
        'liSkinColor': liSkinColor,
        'hasPotato': hasPotato,
        'muggerMissing': muggerMissing,
        'metB': metB,
        'firstMeeting': firstMeeting,
        'pLocation': pLocation,
        'aLocation': aLocation,
        'bLocation': bLocation,
        'loosenedPlanks': loosenedPlanks,
        'knowsDeath': knowsDeath,
        'seenForest': seenForest,
        'deathReturn': deathReturn
        }
    if os.path.exists('./savefile'):
        os.remove('./savefile')
    with open('./savefile', 'wb') as f:
        pickle.dump(data, f)


    disp_txt("\nYou are surrounded by a warm light. You are SAVED.\n")
    window.destroy()

def changeSettings(newSpeed, newSize):
    global txtSpeed
    global txtSize

    if newSpeed == "slow":
        txtSpeed = 0.2
    if newSpeed == "standard":
        txtSpeed = 0.05
    if newSpeed == "fast":
        txtSpeed = 0.01

    if newSize == "small":
        txtSize = 10
    if newSize == "standard":
        txtSize = 16
    if newSize == "large":
        txtSize = 24

    textWindow.config(font=("Calibri", txtSize))

def click_choice(choice):
    #delete all buttons
    list = frame2.pack_slaves()
    for x in list:
        if str(x) != str(list[0]):
            x.destroy()

    print("clicked choice " + str(choice))
    eval(choice + "()")

def disp_txt(string):
    for char in string:
        global txtSpeed
        textWindow.see(tk.END)
        textWindow.insert(tk.INSERT, char)
        if char == '\n':
            textWindow.insert(tk.INSERT, '\n')
        textWindow.update()
        time.sleep(txtSpeed)

def disp_txt_at_speed(string, speed):
    for char in string:
        textWindow.see(tk.END)
        textWindow.insert(tk.INSERT, char)
        if char == '\n':
            textWindow.insert(tk.INSERT, '\n')
        textWindow.update()
        time.sleep(speed)

def room_run(section):
    clear_screen()
    global currentRoom
    currentRoom = section
    to_display = replace_variables(story_content[section])
    disp_txt(to_display)

def replace_variables(string):
    global food
    global pName
    global aName, bName, liName, banditName
    global mercName, guardName, magicianName, bardName
    global thiefName, toughName, medicName
    global kingdomName, neighborName, worldName
    global aHairColor, aEyeColor, aSkinColor
    global bHairColor, bEyeColor, bSkinColor
    global liHairColor, liEyeColor, liSkinColor
    global pLocation, aLocation, bLocation

    string = string.replace("$food", food)
    string = string.replace("$pName", pName)
    string = string.replace("$aName", aName)
    string = string.replace("$bName", bName)
    string = string.replace("$liName", liName)
    string = string.replace("$banditName", banditName)
    string = string.replace("$mercName", mercName)
    string = string.replace("$guardName", guardName)
    string = string.replace("$magicianName", magicianName)
    string = string.replace("$bardName", bardName)
    string = string.replace("$thiefName", thiefName)
    string = string.replace("$toughName", toughName)
    string = string.replace("$medicName", medicName)
    string = string.replace("$kingdomName", kingdomName)
    string = string.replace("$neighborName", neighborName)
    string = string.replace("$worldName", worldName)
    string = string.replace("$merchantName", merchantName)
    string = string.replace("$aHairColor", aHairColor)
    string = string.replace("$bHairColor", bHairColor)
    string = string.replace("$liHairColor", liHairColor)
    string = string.replace("$aEyeColor", aEyeColor)
    string = string.replace("$bEyeColor", bEyeColor)
    string = string.replace("$liEyeColor", liEyeColor)
    string = string.replace("$aSkinColor", aSkinColor)
    string = string.replace("$bSkinColor", bSkinColor)
    string = string.replace("$liSkinColor", liSkinColor)
    string = string.replace("$pLocation", pLocation)
    string = string.replace("$aLocation", aLocation)
    string = string.replace("$bLocation", bLocation)
    return string

def clear_screen():
    textWindow.delete(1.0, END)
    textWindow.update()

def acceptEntry(entry, pWindow):
    global inputResponse
    global badInput
    if entry.lower() in badInput:
        pWindow.destroy()
        getInput("That was a stupid answer. Try again")
    else:
        inputResponse = entry
        pWindow.destroy()

def getInput(prompt):
    # creating settings window
    pWindow = Toplevel()
    pWindow.title(prompt)
    pWindow.iconbitmap('./assets/treelarge_CKX_icon.ico')
    pWindow.geometry("400x80")
    pWindow.resizable(False, False)
    pWindow.config(bg = "#333333")

    entryField = Entry(pWindow, width=300, fg = "#333333", bg = "#EEEEEE", font=("Calibri", 20))
    entryField.pack(fill="x")
    send = Button(pWindow, text="Send", command=lambda: acceptEntry(entryField.get(), pWindow), bg = "#333333", fg = "#EEEEEE")
    send.pack(side=TOP)
    win.wait_window(pWindow)

def createTxtFiles(limit):
    for i in range(0, limit):
        name=("script/arc2_" + f"{i}"+ ".txt")
        file = open(name,"w+")
        file.close()

def rollCharacters():
    bNames = ['Alexia', 'Aphrodite', 'Domino', 'Jade', 'Karma', 'Destiny', 'Lyra', 'Quinn', 'Ripley', 'Trinity', 'Valkyrie']
    aNames = ['Phoebe', 'Valentina', 'Rose', 'Beatrice', 'Sophia', 'Charlotte', 'Emilia', 'Hazel', 'Faith', 'Iris', 'Ariel']
    liNames= ['Lacey', 'Chloe', 'Delila', 'Ashe', 'Lucy', 'Violet', 'Autumn', 'Nova', 'Elizabeth', 'Melody', 'Elise']
    banditNames = ['Axel', 'Wulrick', 'Jason', 'Tyrion']
    mercNames   = ['Karen', 'Britt', 'Candice', 'Maud']
    guardNames  = ['Garett', 'Gregory', 'George', 'Geoff']
    magicianNames=['Pluto', 'Mercury', 'Venus', 'Mars']
    bardNames   = ['Paganini', 'Vivaldi', 'Sarasate', 'Bach']
    thiefNames  = ['Tex', 'Lucas', 'Isaac', 'Noland']
    toughNames  = ['Brom', 'Diesel', 'Wulfe', 'Bruce']
    medicNames  = ['Daisy', 'Arya', 'Minneie', 'Sophia']
    merchantNames = ['Mickey', 'Mack', 'Meebley', 'Mitch']

    kingdomNames = ['Luxidium', 'Grandossia', 'Typhon', 'Belium']
    neighborNames= ['Arsenia', 'Dulchio', 'Syndio', 'Kleptorn']
    worldNames   = ["The Edge Lands", "The Forgotten Hills", "The Midnight Plains", "The Burned Paradise"]

    aHairColors = ['brunette', 'dark brown', "black"]
    bHairColors = ['pearl white', 'silver', "fiery red", 'blonde']
    liHairColors = ['strawberry blonde', 'caramel blonde', "light pink", "light blue"]

    aSkinColors = ['olive', 'brown', "dark", 'black', 'pale', 'white', "light", "light","tanned", 'bronze']
    bSkinColors = ['olive', 'brown', "dark", 'black', 'pale', 'white', "light", "light","tanned", 'bronze']
    liSkinColors = ['olive', 'brown', "dark", 'black', 'pale', 'white', "light", "light","tanned", 'bronze']

    aEyeColors = ['amber', 'light brown', "hazel", "dark brown"]
    bEyeColors = ['sapphire', 'amethyst', "emerald", "aquamarine", "ruby", "topaz"]
    liEyeColors = ['blue', 'light blue', "dark blue", 'blue-grey']

    aLocations = ['Pondwall','Cliffham','Moonburgh', 'Pinehorn', 'Newrock', 'Pinewood', 'Oldview', 'Limeacre' ]
    bLocations = ['Roseham', 'Emberport', 'Greencross', 'Clearbarrow', 'Rustpeak', 'Oxshell', 'Fayview', 'Edgehold']

    global aName, bName, liName, banditName
    global mercName, guardName, magicianName, bardName
    global thiefName, toughName, medicName
    global kingdomName, neighborName, worldName
    global aHairColor, aEyeColor, aSkinColor
    global bHairColor, bEyeColor, bSkinColor
    global liHairColor, liEyeColor, liSkinColor
    global aLocation, bLocation, merchantName

    aName = random.choice(aNames)
    bName = random.choice(bNames)
    liName = random.choice(liNames)
    banditName = random.choice(banditNames)
    mercName = random.choice(mercNames)
    guardName = random.choice(guardNames)
    magicianName = random.choice(magicianNames)
    bardName = random.choice(bardNames)
    thiefName = random.choice(thiefNames)
    toughName = random.choice(toughNames)
    medicName = random.choice(medicNames)
    kingdomName = random.choice(kingdomNames)
    neighborName = random.choice(neighborNames)
    worldName = random.choice(worldNames)
    aHairColor = random.choice(aHairColors)
    bHairColor = random.choice(bHairColors)
    liHairColor = random.choice(liHairColors)
    aEyeColor = random.choice(aEyeColors)
    bEyeColor = random.choice(bEyeColors)
    liEyeColor = random.choice(liEyeColors)
    aSkinColor = random.choice(aSkinColors)
    bSkinColor = random.choice(bSkinColors)
    liSkinColor = random.choice(liSkinColors)
    aLocation = random.choice(aLocations)
    bLocation = random.choice(bLocations)
    merchantName = random.choice(merchantNames)



#--------------------------------------------------------GUI------------------------------------------------------------
def settingsconfig():
    #creating settings window
    settings_window = tk.Tk()
    settings_window.title("Settings Configuration")
    settings_window.iconbitmap('./assets/treelarge_CKX_icon.ico')
    settings_window.geometry("360x200")
    settings_window.resizable(False, False)
    settings_window.config(bg="#333333")

    # putting in the defaults
    global txtSize
    global txtSpeed
    speed = StringVar()
    textSize = StringVar()

    if txtSpeed == 0.01:
        speed.set("fast")
    if txtSpeed == 0.05:
        speed.set("standard")
    if txtSpeed == 0.2:
        speed.set("slow")

    if txtSize == 24:
        textSize.set("large")
    if txtSize == 16:
        textSize.set("standard")
    if txtSize == 10:
        textSize.set("small")

    #loadbutton logic
    if os.path.exists('./savefile'):
        with open('./savefile', 'rb') as f:
            data = pickle.load(f)

        loadButton = Button(settings_window, text="Load Game: " + str(data["dateTime"]), command=lambda: loadGame(settings_window), bg = "#333333", fg = "#EEEEEE").grid(row=1, column=1)
    else:
        loadButton = Button(settings_window, state=DISABLED, text="Load Game", command=lambda: loadGame(settings_window), bg = "#333333", fg = "#EEEEEE").grid(row=1, column=1)
    #menu

    saveButton = Button(settings_window, text="Save Game", command=lambda: saveGame(settings_window), bg = "#333333", fg = "#EEEEEE").grid(row=2, column=1)
    speedLabel = Label(settings_window, text="Text Scroll Speed", bg = "#333333", fg = "#EEEEEE").grid(row=3, column=1)
    radio1 = Radiobutton(settings_window, text="Slow", variable=speed, value="slow", bg = "#333333", fg = "#EEEEEE", selectcolor="#333333", activebackground="#333333").grid(row=4, column=0)
    radio2 = Radiobutton(settings_window, text="Standard", variable=speed, value="standard", bg = "#333333", fg = "#EEEEEE", selectcolor="#333333", activebackground="#333333").grid(row=4, column=1)
    radio3 = Radiobutton(settings_window, text="Fast", variable=speed, value="fast", bg = "#333333", fg = "#EEEEEE", selectcolor="#333333", activebackground="#333333").grid(row=4, column=2)
    sizeLabel = Label(settings_window, text="Text Size (May require you resize Window)", bg = "#333333", fg = "#EEEEEE").grid(row=5, column=1)
    radio4 = Radiobutton(settings_window, text="Small", variable=textSize, value="small", bg = "#333333", fg = "#EEEEEE", selectcolor="#333333", activebackground="#333333").grid(row=6, column=0)
    radio5 = Radiobutton(settings_window, text="Standard", variable=textSize, value="standard", bg = "#333333", fg = "#EEEEEE", selectcolor="#333333", activebackground="#333333").grid(row=6, column=1)
    radio6 = Radiobutton(settings_window, text="Large", variable=textSize, value="large", bg = "#333333", fg = "#EEEEEE", selectcolor="#333333", activebackground="#333333").grid(row=6, column=2)
    finishButton = Button(settings_window, text="Apply Changes",bg = "#333333", fg = "#EEEEEE", command=lambda: changeSettings(speed.get(), textSize.get()))
    finishButton.grid(row=8, column=1)

def create_choices(choiceList, pathList):
    #create buttons for the amount of options available, represtented by 'number'
    for i in range(0, len(choiceList)):
        button = Button(frame2, text=choiceList[i], command=lambda i=i: click_choice(pathList[i]), bg="#333333", fg="#EEEEEE")
        button.pack(fill='both', expand='yes')

#Unique Room for starting the game
def queue_start_story(window):
    window.destroy()
    PlaySound(None, SND_ASYNC)
    rollCharacters()
    win.deiconify()
    # CHANGE THIS AFTER TESTING
    arc2_0()
    room_run("arc1_0")
    choices = ["Continue..."]
    paths = ["arc1_1"]
    create_choices(choices, paths)


#build main GUI------------------------------------------------------------------
win = tk.Tk()
win.geometry("600x800")
win.title("SAVED")
win.iconbitmap('./assets/treelarge_CKX_icon.ico')
#Text Frame
frame1 = tk.Frame(
    master = win,
    bg = "#696969"
)
frame1.pack(fill='both', expand='yes')
#Text Window
textWindow = tkst.ScrolledText(
    master = frame1,
    wrap   = tk.WORD,
    bg = "#333333",
    fg = "#EEEEEE"
)
textWindow.config(font=("Calibri", txtSize))
textWindow.pack(padx=5, pady=5, fill=tk.BOTH, expand=True,)

#Button Frame
frame2 = tk.Frame(
    master = win,
    bg = "#333333",
)
frame2.pack(fill='both', expand='yes')
settings = Button(frame2, text="Settings", command=settingsconfig,bg = "#333333", fg = "#EEEEEE")
settings.pack(side=RIGHT, fill=Y)

win.withdraw()

#build Main Menu


menu = Toplevel()
menu.geometry("600x880")
menu.title("SAVED")
menu.iconbitmap('./assets/treelarge_CKX_icon.ico')
menu.resizable(False, False)

PlaySound('./music/crystalAir.wav', SND_ALIAS | SND_ASYNC)

screen = tk.Canvas(
    master=menu,
    bg="#696969"
)
screen.pack(fill='both', expand='yes')
title = Label(screen, text="SAVED", bg = "#ffffff", fg = "#333333",pady=30, font=("Calibri", 35)).pack(fill='x', expand='yes')
photo = PhotoImage(file = './assets/tree.gif')
photoLabel = Label(screen, image = photo).pack()
button = Button(screen, text="New Game", command=lambda: queue_start_story(menu),bg = "#ffffff", fg = "#333333",pady=20, padx=80)
button_window = screen.create_window(480, 400, window=button)

if os.path.exists('./savefile'):
    with open('./savefile', 'rb') as f:
        data = pickle.load(f)

    loadButton = Button(screen, text="Load Game: " + str(data["dateTime"]),command=lambda: loadGame(menu), bg = "#ffffff", fg = "#333333",pady=20, padx=25)
    loadWindow = screen.create_window(480,480, window=loadButton)
else:
    loadButton = Button(screen, state=DISABLED, text="Load Game", command=lambda: loadGame(menu),bg = "#ffffff", fg = "#333333",pady=20, padx=25)
    loadWindow = screen.create_window(480,480, window=loadButton)

#----------------------------------------------Story Sections----------------------------------------------------------

def arc1_1():
    room_run("arc1_1")
    choices = ["Take Chocolate", "Take Potato Chips", "Do Nothing"]
    paths = ["arc1_2", "arc1_3", "arc1_4"]
    create_choices(choices, paths)

def arc1_2():
    global food
    food = "chocolate"
    room_run("arc1_2")
    choices = ["Continue..."]
    paths = ["arc1_5"]
    create_choices(choices, paths)

def arc1_3():
    global food
    food = "potato chips"
    room_run("arc1_3")
    choices = ["Continue..."]
    paths = ["arc1_5"]
    create_choices(choices, paths)

def arc1_4():
    global food
    food = "chocolate"
    room_run("arc1_4")
    choices = ["Continue..."]
    paths = ["arc1_5"]
    create_choices(choices, paths)

def arc1_5():
    global inputResponse
    global pName
    room_run("arc1_5")
    getInput("Please Enter your Name:")
    pName = inputResponse

    choices = ["Continue..."]
    paths = ["arc1_6"]
    create_choices(choices, paths)

def arc1_6():
    room_run("arc1_6")

    choices = ["Continue..."]
    paths = ["arc1_7"]
    create_choices(choices, paths)

def arc1_7():
    room_run("arc1_7")

    choices = ["Continue..."]
    paths = ["arc2_0"]
    create_choices(choices, paths)

def arc2_0():
    room_run("arc2_0")

    choices = ["Continue..."]
    paths = ["arc2_1"]
    create_choices(choices, paths)

def arc2_1():
    global firstTimeArc2
    if firstTimeArc2 == "true":
        room_run("arc2_1")
    else:
        room_run("arc2_51")

    firstTimeArc2 = "false"
    choices = ["Head over the brook towards Kingsbridge","Head the opposite direction along the path"]
    paths = ["arc2_2", "arc2_32"]

    create_choices(choices, paths)

def arc2_2():
    room_run("arc2_2")

    choices = ["Continue along to the Central Plaza", "Detour through the outskirts of Kingsbridge"]
    paths = ["arc2_3", "arc2_19"]
    create_choices(choices, paths)

def arc2_3():
    room_run("arc2_3")

    choices = ["Go to SpellBook Stall", "Enter History Room", "Enter Adventurer's Gear Store", "Continue exploring at random"]
    paths = ["arc2_4", "arc2_9", "arc2_12", "arc2_8"]
    create_choices(choices, paths)

def arc2_4():
    room_run("arc2_4")

    choices = ["Ask about Spell Books", "Ask Where you are"]
    paths = ["arc2_5", "arc2_6"]
    create_choices(choices, paths)

def arc2_5():
    room_run("arc2_5")

    choices = ["Continue..."]
    paths = ["arc2_7"]
    create_choices(choices, paths)

def arc2_6():
    room_run("arc2_6")

    choices = ["Continue..."]
    paths = ["arc2_7"]
    create_choices(choices, paths)

def arc2_7():
    room_run("arc2_7")

    choices = ["Enter History Room", "Enter Adventurer's Gear Store", "Continue exploring at random"]
    paths = ["arc2_9", "arc2_12", "arc2_8"]
    create_choices(choices, paths)

def arc2_8():
    room_run("arc2_8")

    choices = ["Follow the woman in yellow", "Ignore her and continue exploring"]
    paths = ["arc2_29", "arc2_16"]
    create_choices(choices, paths)

def arc2_9():
    room_run("arc2_9")

    choices = ["Sneak past counter into the History Room", "Wait for the person manning the counter to return"]
    paths = ["arc2_11", "arc2_10"]
    create_choices(choices, paths)

def arc2_10():
    room_run("arc2_10")

    choices = ["Follow the woman in yellow", "Ignore her and continue exploring"]
    paths = ["arc2_29", "arc2_16"]
    create_choices(choices, paths)

def arc2_11():
    room_run("arc2_11")

    choices = ["Follow the woman in yellow", "Ignore her and continue exploring"]
    paths = ["arc2_29", "arc2_16"]
    create_choices(choices, paths)

def arc2_12():
    room_run("arc2_12")
    global metB
    metB = "true"
    choices = ["Beg Shopkeeper for a weapon", "Talk to Woman", "Leave"]
    paths = ["arc2_14", "arc2_15", "arc2_13"]
    create_choices(choices, paths)

def arc2_13():
    room_run("arc2_13")

    choices = ["Follow the woman in yellow", "Ignore her and continue exploring"]
    paths = ["arc2_29", "arc2_16"]
    create_choices(choices, paths)

def arc2_14():
    room_run("arc2_14")

    choices = ["Follow the woman in yellow", "Ignore her and continue exploring"]
    paths = ["arc2_29", "arc2_16"]
    create_choices(choices, paths)

def arc2_15():
    room_run("arc2_15")

    choices = ["Follow the woman in yellow", "Ignore her and continue exploring"]
    paths = ["arc2_29", "arc2_16"]
    create_choices(choices, paths)

def arc2_16():
    room_run("arc2_16")

    choices = ["Stay in Town", "Leave Kingsbridge"]
    paths = ["arc2_17", "arc2_18"]
    create_choices(choices, paths)

def arc2_17():
    room_run("arc2_17")
    global deathReturn
    deathReturn = "arc2_17"

def arc2_18():
    room_run("arc2_18")
    global deathReturn
    deathReturn = "arc2_18"

def arc2_19():
    room_run("arc2_19")

    choices = ["Enter 3 story building", "Enter Tavern", "Continue along the path"]
    paths = ["arc2_20", "arc2_25", "arc2_26"]
    create_choices(choices, paths)

def arc2_20():
    room_run("arc2_20")

    choices = ["I’m a believer", "Where am I and what is going on?"]
    paths = ["arc2_22", "arc2_23"]
    create_choices(choices, paths)

def arc2_22():
    room_run("arc2_22")
    global hasPotato
    hasPotato = "yes"
    choices = ["Head back the way you came to the central plaza", "Enter Tavern", "Continue along the path"]
    paths = ["arc2_24", "arc2_25", "arc2_26"]
    create_choices(choices, paths)

def arc2_23():
    room_run("arc2_23")
    global hasPotato
    hasPotato = "yes"
    choices = ["Head back the way you came to the central plaza", "Enter Tavern", "Continue along the path"]
    paths = ["arc2_24", "arc2_25", "arc2_26"]
    create_choices(choices, paths)

def arc2_24():
    global hasPotato
    if hasPotato == "yes":
        hasPotato = "no"
        clear_screen()
        disp_txt("You’ve had enough of this route and begin walking back the way you came. By the time you return back "
                 "to where the road split and you detoured, the chunk of potato in your pocket has become quite painful "
                 "rubbing against your leg so you decide to cut ties and toss it to the side. The potato hadn’t even "
                 "stopped rolling yet before a small boy shoots out of a nearby shack and snatches it up, disappearing "
                 "into the shack once again as quick as he came.")
        time.sleep(2)
    room_run("arc2_24")
    choices = ["Follow the woman in yellow", "Ignore her and continue exploring"]
    paths = ["arc2_29", "arc2_16"]
    create_choices(choices, paths)

def arc2_25():
    room_run("arc2_25")
    global hasPotato
    if hasPotato == "true":
        choices = ["Head back the way you came to the central plaza" "Continue along the path"]
        paths = ["arc2_24", "arc2_26"]
        create_choices(choices, paths)
    else:
        choices = ["Head back the way you came to the central plaza", "Enter 3 story building",
                   "Continue along the path"]
        paths = ["arc2_24", "arc2_20", "arc2_26"]
        create_choices(choices, paths)

def arc2_26():
    room_run("arc2_26")
    global hasPotato
    if hasPotato == "yes":
        choices = ["Run away!", "Share your potato with the starving man"]
        paths = ["arc2_28", "arc2_27"]
        hasPotato = "no"
        create_choices(choices, paths)
    else:
        choices = ["Run away!"]
        paths = ["arc2_28"]
        create_choices(choices, paths)

def arc2_27():
    room_run("arc2_27")
    global muggerMissing
    muggerMissing = "true"
    choices = ["Follow the woman in yellow", "Ignore her and continue exploring"]
    paths = ["arc2_29", "arc2_16"]
    create_choices(choices, paths)

def arc2_28():
    clear_screen()
    disp_txt("Without a moment of hesitation, you turn on your heels and sprint as hard as you can the way you had come."
             " Behind you, you hear the labored breathing of the old man as he chases you with the shoddy dagger raised."
             " His health is not even comparable to yours however, and you easily outrun him and leave him behind. "
             "Checking behind your back every so often, you make your way past the tavern and the three story building "
             "yet again. You continue north all the way until you get back to the detour you originally took, and then "
             "head for the plaza. You are careful to give wide berth to any area that even remotely resembles the scene "
             "of the attempted mugging, and you check every alleyway as you move along. ")
    time.sleep(2)
    global hasPotato
    if hasPotato == "yes":
        hasPotato = "no"
        disp_txt("\nYou’ve had enough of this route and begin walking back the way you came. By the time you return back "
                 "to where the road split and you detoured, the chunk of potato in your pocket has become quite painful "
                 "rubbing against your leg so you decide to cut ties and toss it to the side. The potato hadn’t even "
                 "stopped rolling yet before a small boy shoots out of a nearby shack and snatches it up, disappearing "
                 "into the shack once again as quick as he came.")
        time.sleep(2)

    room_run("arc2_28")
    choices = ["Follow the woman in yellow", "Ignore her and continue exploring"]
    paths = ["arc2_29", "arc2_16"]
    create_choices(choices, paths)

def arc2_29():
    global muggerMissing, metB
    if muggerMissing == "true":
        muggerMissing = "false"
        arc2_46()
    room_run("arc2_29")

    if metB == "true":
        metB = "false"
        disp_txt("\nHer white cloak gleams in the feeble sunlight that slips into the alleyway and you recognize "
                 "her as the woman from the adventurer’s gear shop. \n"
                 "[swordswoman] Ah, you. Hello again.\n")
    else:
        disp_txt("Her white cloak gleams in the feeble sunlight that slips into the alleyway, and you shrink a"
                 " little at her intimidating form."
                 "\n[swordswoman] Sorry about that mess…\n")

    choices = ["Continue..."]
    paths = ["arc2_58"]
    create_choices(choices, paths)

def arc2_58(): #Placed here because it is a continuation of arc 29 for simplicity
    room_run("arc2_58")
    global firstMeeting
    if firstMeeting == "true":
        disp_txt("\nYou feel a hint of sweat gathering on your temple and try not to look guilty. What you need "
                 "is a way to get out of this awkward conversation while simultaneously not ostracizing "
                 "yourself from the group. This may be your only chance to convince them to help you, and "
                 "already you are off on the wrong foot. Shifting uncomfortably and feeling the weight of the "
                 "silence bear down on you, you hear a faint crinkling noise and an idea comes to you. ")

    choices = ["Continue..."]
    paths = ["arc2_59"]
    create_choices(choices, paths)

def arc2_59(): #Placed here because it is a continuation of arc 29 for simplicity
    room_run("arc2_59")
    global firstMeeting,food
    if firstMeeting == "true":
        disp_txt("\nYou feel frozen, it is as if she has seen right through you. You shift uncomfortably again, "
                 "trying to think of a way to get her off your back. But how? The " + str(food) + " worked for a little"
                 " bit so maybe something similar could get her to back off. You feel in your pocket your "
                 "wallet and in the other your phone. Your phone! These people seem to come from a time before"
                 " electricity and surely they will respect you and be amazed by your tiny and seemingly"
                 " magical device.  ")

    choices = ["Continue..."]
    paths = ["arc2_60"]
    create_choices(choices, paths)

def arc2_60(): #Placed here because it is a continuation of arc 29 for simplicity
    room_run("arc2_60")
    global inputResponse
    global pLocation
    getInput("what city/town are you from?")
    pLocation = inputResponse

    choices = ["Continue..."]
    paths = ["arc2_61"]
    create_choices(choices, paths)

def arc2_61(): #Placed here because it is a continuation of arc 29 for simplicity
    room_run("arc2_61")
    global firstMeeting, liName
    if firstMeeting == "true":
        disp_txt("\nYou aren’t really sure why but you know you have to join these people on their quest. "
                 "You also know that everything " + str(liName) + " just said is true, you truly offer little value. "
                 "The trick then will have to be convincing them to allow you to join, and then prove your "
                 "worth along the way. But how to convince them? The key to this is probably in this whole "
                 "‘Ancient Dragon’ thing…   ")

    choices = ["Continue..."]
    paths = ["arc2_62"]
    create_choices(choices, paths)

def arc2_62(): #Placed here because it is a continuation of arc 29 for simplicity
    room_run("arc2_62")

    #next is choose which death or victory you get
    global knowsDeath, loosenedPlanks, firstMeeting
    firstMeeting = "false"
    if knowsDeath == "false" and loosenedPlanks == "false":
        choices = ["Join " + str(aName) + " and " + str(liName), "Join " + str(bName)]
        paths = ["arc2_31", "arc2_30"]
        create_choices(choices, paths)
    elif knowsDeath == "true" and loosenedPlanks == "false":
        choices = ["Join " + str(aName) + " and " + str(liName), "Join " + str(bName)]
        paths = ["arc2_47", "arc2_48"]
        create_choices(choices, paths)
    else:
        choices = ["Join " + str(aName) + " and " + str(liName), "Join " + str(bName)]
        paths = ["arc2_49", "arc2_50"]
        create_choices(choices, paths)

def arc2_30():
    room_run("arc2_30")
    global deathReturn, knowsDeath
    deathReturn = "arc2_30"
    knowsDeath = "true"

def arc2_31():
    room_run("arc2_31")
    global deathReturn, knowsDeath
    deathReturn = "arc2_31"
    knowsDeath = "true"

def arc2_32():
    room_run("arc2_32")

    choices = ["climb tree onto platform", "continue along path"]
    paths = ["arc2_33", "arc2_34"]
    create_choices(choices, paths)

def arc2_33():
    room_run("arc2_33")
    global seenForest
    if seenForest == "false":
        choices = ["follow path left along the outskirts", "enter the forest"]
        paths = ["arc2_37", "arc2_35"]
        create_choices(choices, paths)
    else:
        choices = ["follow path left along the outskirts", "enter the forest"]
        paths = ["arc2_37", "arc2_36"]
        create_choices(choices, paths)

def arc2_34():
    room_run("arc2_34")
    global seenForest
    if seenForest == "false":
        choices = ["follow path left along the outskirts", "enter the forest"]
        paths = ["arc2_37", "arc2_35"]
        create_choices(choices, paths)
    else:
        choices = ["follow path left along the outskirts", "enter the forest"]
        paths = ["arc2_37", "arc2_36"]
        create_choices(choices, paths)

def arc2_35():
    room_run("arc2_35")
    global deathReturn, seenForest
    deathReturn = "arc2_35"
    seenForest = "true"

def arc2_36():
    room_run("arc2_36")
    global deathReturn, seenForest
    deathReturn = "arc2_36"
    seenForest = "true"

def arc2_37():
    room_run("arc2_37")
    global seenForest
    if seenForest == "true":
        choices = [" 'I'm afraid your husband is dead' ", " 'I promise to try to find him' ", " 'I'm afraid I can't help you, I'm just passing through' "]
        paths = ["arc2_38", "arc2_39", "arc2_41"]
        create_choices(choices, paths)
    else:
        choices = [" 'I promise to try to find him' ",
                   " 'I'm afraid I can't help you, I'm just passing through' "]
        paths = ["arc2_39", "arc2_41"]
        create_choices(choices, paths)

def arc2_38():
    room_run("arc2_38")

    choices = ["Stay and ambush the killer", "Head into Kingsbridge"]
    paths = ["arc2_44", "arc2_45"]
    create_choices(choices, paths)

def arc2_39():
    room_run("arc2_39")

    global seenForest
    if seenForest == "false":
        choices = ["Enter the forest"]
        paths = ["arc2_35"]
        create_choices(choices, paths)
    else:
        choices = ["Enter the forest"]
        paths = ["arc2_36"]
        create_choices(choices, paths)

def arc2_41():
    room_run("arc2_41")

    choices = ["Yep!", "Nope!"]
    paths = ["arc2_43", "arc2_42"]
    create_choices(choices, paths)

def arc2_42():
    room_run("arc2_42")
    global deathReturn
    deathReturn = "arc2_42"

def arc2_43():
    room_run("arc2_43")
    global deathReturn
    deathReturn = "arc2_43"

def arc2_44():
    room_run("arc2_44")
    global deathReturn, knowsDeath
    knowsDeath = "true"
    deathReturn = "arc2_44"

def arc2_45():
    room_run("arc2_45")

    choices = ["Follow the woman in yellow", "Ignore her and continue exploring"]
    paths = ["arc2_29", "arc2_16"]
    create_choices(choices, paths)

def arc2_46():
    room_run("arc2_46")

    choices = ["Stay in Town", "Leave Kingsbridge"]
    paths = ["arc2_17", "arc2_18"]
    create_choices(choices, paths)

def arc2_47():
    room_run("arc2_47")
    global deathReturn, knowsDeath
    deathReturn = "arc2_47"
    knowsDeath = "true"

def arc2_48():
    room_run("arc2_48")
    global deathReturn, knowsDeath
    deathReturn = "arc2_48"
    knowsDeath = "true"

def arc2_49():
    room_run("arc2_49")

def arc2_50():
    room_run("arc2_49")


#-----------------------------------------------Program Start----------------------------------------------------------
#arc 1
story_sections = []
for i in range(0, 8):
    num = i
    story_sections.append("arc1_" + f"{num}")
#arc 2
for i in range(0, 63):
    num = i
    story_sections.append("arc2_" + f"{num}")

story_content = {}
i=0
for section in story_sections:
    if i<8:
        file_path = "script/arc1/" + section + ".txt"
    #arc 1 plus arc 2...
    elif i<72:
        file_path = "script/arc2/" + section + ".txt"

    with open(file_path, encoding="utf8") as file_reader:
        story_content[section] = file_reader.read()
    i=i+1

#-----------------------------------------------------MAIN-------------------------------------------------------------

#createTxtFiles(56)

win.mainloop()
