from tkinter import *
import tkinter as tk
import tkinter.scrolledtext as tkst
import time
import pickle
from datetime import datetime
import os
import random
from vlc import Instance
import ctypes
import geocoder
#--------------------------------------------------------Globals--------------------------------------------------------
badInput = ["!","@","#","$","%","^","&","*","^_^",":)"," ","",".",",","-","_","$pName","$aName","$bName","$liName"]

class g:
    inputResponse = "null"
    # global values
    
    currentRoom = "null"
    savedRoom = "null"
    txtSpeed = 0.000000001
    txtSize = 16

    food = "null"
    pName = "null"
    aName = "null"
    bName = "null"
    liName = "null"
    banditName = "null"
    mercName = "null"
    guardName = "null"
    magicianName = "null"
    bardName = "null"
    thiefName = "null"
    toughName = "null"
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

    # !!!Flags!!!
    firstTimeArc2 = "true"
    knowsDeath = "false"
    loosenedPlanks = "false"
    hasPotato = "false"
    muggerMissing = "false"
    metB = "false"
    firstMeeting = "true"
    seenForest = "false"

#=======


class VLC:
    def __init__(self):
        self.Player = Instance('--loop')
        self.mediaList = self.Player.media_list_new()
        self.listPlayer = self.Player.media_list_player_new()

    def fillPlaylist(self):
        path = "./music/"
        songs = os.listdir(path)
        random.shuffle(songs)
        for s in songs:
            self.mediaList.add_media(self.Player.media_new(os.path.join(path,s)))
        self.listPlayer.set_media_list(self.mediaList)

    def play(self):
        self.listPlayer.play()
        self.listPlayer.get_media_player().audio_set_volume(70)
    def next(self):
        self.listPlayer.next()
    def pause(self):
        self.listPlayer.pause()
    def previous(self):
        self.listPlayer.previous()
    def stop(self):
        self.listPlayer.stop()
    def playIntro(self):
        path = './music/title/crystalAir.mp3'
        self.mediaList.add_media(self.Player.media_new(path))
        self.listPlayer.set_media_list(self.mediaList)
        self.listPlayer.play()
        self.listPlayer.get_media_player().audio_set_volume(70)
music = VLC()

#-------------------------------------------------------Functions-------------------------------------------------------

def getLocation():
    g = geocoder.ip('me')
    return(g.city)

def get_display_name():
    GetUserNameEx = ctypes.windll.secur32.GetUserNameExW
    NameDisplay = 3

    size = ctypes.pointer(ctypes.c_ulong(0))
    GetUserNameEx(NameDisplay, None, size)

    nameBuffer = ctypes.create_unicode_buffer(size.contents.value)
    GetUserNameEx(NameDisplay, nameBuffer, size)
    return nameBuffer.value

def startBackgroundMusic():
    music.stop()
    music.fillPlaylist()
    music.next()
    music.next()
    music.play()

def postDeathPassage(toPrint):
    room_run(toPrint)

    choices = ["Continue..."]
    paths = [g.savedRoom]
    create_choices(choices, paths)

def loadGame(window):
    win.deiconify()
    with open('./savefile', 'rb') as f:
        data = pickle.load(f)
    list = vars(g)
    listy = list.items()
    for left, right in listy:
        if left.startswith("__") == False:
            left = data[left]
    #delete buttons
    list = frame2.pack_slaves()
    for x in list:
        if str(x) != str(list[0]):
            x.destroy()
    print("Game Loaded")
    disp_txt("\nLoading Game...\n")
    window.destroy()



    #If you physically altered the world, we need to Undo that here
    g.loosenedPlanks = "false"
    g.metB = "false"




    startBackgroundMusic()
    if g.currentRoom == "arc1_0":
        g.currentRoom = "arc1_1"

    #if you just died this is a special message for you :)
    if g.deathReturn == "arc2_17" or g.deathReturn == "arc2_42":
        g.deathReturn = "null"
        postDeathPassage('arc2_52')

    elif g.deathReturn == "arc2_18" or g.deathReturn == "arc2_35" or g.deathReturn == "arc2_36":
        g.deathReturn = "null"
        postDeathPassage('arc2_56')

    elif g.deathReturn == "arc2_30" or g.deathReturn=="arc2_48":
        g.deathReturn = "null"
        postDeathPassage('arc2_54')

    elif g.deathReturn == "arc2_31" or g.deathReturn=="arc2_47":
        g.deathReturn = "null"
        postDeathPassage('arc2_53')

    elif g.deathReturn == "arc2_43":
        g.deathReturn = "null"
        postDeathPassage('arc2_57')

    elif g.deathReturn == "arc2_44":
        g.deathReturn = "null"
        postDeathPassage('arc2_55')
    else:
        eval(g.savedRoom + "()")


def saveGame(window):
    now = datetime.now()
    # dd/mm/YY H:M:S
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    data = {}
    list = vars(g)
    listy = list.items()
    g.savedRoom = g.currentRoom
    for left, right in listy:
        if left.startswith("__") == False:
            data[left] = right
    data['dateTime'] = dt_string

    if os.path.exists('./savefile'):
        os.remove('./savefile')
    with open('./savefile', 'wb') as f:
        pickle.dump(data, f)
    print("Game saved")

    disp_txt("\nYou are surrounded by a warm light. You are SAVED.\n")
    window.destroy()

def changeSettings(newSpeed, newSize):
    
    if newSpeed == "slow":
        g.txtSpeed = 0.2
    if newSpeed == "standard":
        g.txtSpeed = 0.05
    if newSpeed == "fast":
        g.txtSpeed = 0.01

    if newSize == "small":
        g.txtSize = 10
    if newSize == "standard":
        g.txtSize = 16
    if newSize == "large":
        g.txtSize = 24

    textWindow.config(font=("Calibri", g.txtSize))

def click_choice(choice):
    #delete all buttons
    list = frame2.pack_slaves()
    for x in list:
        if str(x) != str(list[0]):
            x.destroy()

    print("Player Chose: " + str(choice))
    eval(choice + "()")

def disp_txt(string):
    for char in string:
        
        textWindow.see(tk.END)
        textWindow.insert(tk.INSERT, char)
        if char == '\n':
            textWindow.insert(tk.INSERT, '\n')
        textWindow.update()
        time.sleep(g.txtSpeed)

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
    g.currentRoom = section
    to_display = replace_variables(story_content[section])
    disp_txt(to_display)

def replace_variables(string):
    list = vars(g)
    listy = list.items()

    for globy, value in listy:
        if globy.startswith("__") == False:
            print(str(globy) + " ---- " + str(value))
            string = string.replace("$"+globy, str(value))
    print("##################################")
    return string

def clear_screen():
    textWindow.delete(1.0, END)
    textWindow.update()

def acceptEntry(entry, pWindow):
    global badInput
    entry.strip()
    if entry.lower() in badInput:
        pWindow.destroy()
        getInput("That was a stupid answer. Try again")
    else:
        g.inputResponse = entry
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

#this is used for creating .txt files before importing the literature
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

    g.aName = random.choice(aNames)
    g.bName = random.choice(bNames)
    g.liName = random.choice(liNames)
    g.banditName = random.choice(banditNames)
    g.mercName = random.choice(mercNames)
    g.guardName = random.choice(guardNames)
    g.magicianName = random.choice(magicianNames)
    g.bardName = random.choice(bardNames)
    g.thiefName = random.choice(thiefNames)
    g.toughName = random.choice(toughNames)
    g.medicName = random.choice(medicNames)
    g.kingdomName = random.choice(kingdomNames)
    g.neighborName = random.choice(neighborNames)
    g.worldName = random.choice(worldNames)
    g.aHairColor = random.choice(aHairColors)
    g.bHairColor = random.choice(bHairColors)
    g.liHairColor = random.choice(liHairColors)
    g.aEyeColor = random.choice(aEyeColors)
    g.bEyeColor = random.choice(bEyeColors)
    g.liEyeColor = random.choice(liEyeColors)
    g.aSkinColor = random.choice(aSkinColors)
    g.bSkinColor = random.choice(bSkinColors)
    g.liSkinColor = random.choice(liSkinColors)
    g.aLocation = random.choice(aLocations)
    g.bLocation = random.choice(bLocations)
    g.merchantName = random.choice(merchantNames)


#--------------------------------------------------------GUI------------------------------------------------------------
def settingsconfig():
    #creating settings window
    settings_window = tk.Toplevel()
    settings_window.title("Settings")
    settings_window.iconbitmap('./assets/treelarge_CKX_icon.ico')
    settings_window.geometry("230x230")
    settings_window.resizable(False, False)
    settings_window.config(bg="#333333")

    # putting in the defaults
    size = StringVar()
    speed = StringVar()

    if g.txtSize == 24:
        size.set("large")
    if g.txtSize == 16:
        size.set("standard")
    if g.txtSize == 10:
        size.set("small")

    if g.txtSpeed == 0.01:
        speed.set("fast")
    if g.txtSpeed == 0.05:
        speed.set("standard")
    if g.txtSpeed == 0.2:
        speed.set("slow")


    #loadbutton logic
    if os.path.exists('./savefile'):
        with open('./savefile', 'rb') as f:
            data = pickle.load(f)

        loadButton = Button(settings_window, text="Load Game: " + str(data["dateTime"]), command=lambda: loadGame(settings_window), bg = "#333333", fg = "#EEEEEE").grid(row=1, column=0, columnspan=3)
    else:
        loadButton = Button(settings_window, state=DISABLED, text="Load Game", command=lambda: loadGame(settings_window), bg = "#333333", fg = "#EEEEEE").grid(row=1, column=0, columnspan=3)
    #menu

    saveButton = Button(settings_window, text="     Save Game     ", command=lambda: saveGame(settings_window), bg = "#333333", fg = "#EEEEEE").grid(row=2, column=0, columnspan=3)
    speedLabel = Label(settings_window, text="Text Scroll Speed", bg = "#333333", fg = "#EEEEEE").grid(row=3, column=1)
    radio1 = Radiobutton(settings_window, text="    Slow    ",indicatoron=0, variable=speed, value="slow", bg = "#333333", fg = "#EEEEEE", selectcolor="#333333", activebackground="#333333").grid(row=4, column=0,sticky="nsew")
    radio2 = Radiobutton(settings_window, text="Standard",indicatoron=0, variable=speed, value="standard", bg = "#333333", fg = "#EEEEEE", selectcolor="#333333", activebackground="#333333").grid(row=4, column=1,sticky="nsew")
    radio3 = Radiobutton(settings_window, text="    Fast    ",indicatoron=0, variable=speed, value="fast", bg = "#333333", fg = "#EEEEEE", selectcolor="#333333", activebackground="#333333").grid(row=4, column=2,sticky="nsew")
    sizeLabel = Label(settings_window, text="Text Size", bg = "#333333", fg = "#EEEEEE").grid(row=5, column=1)
    radio4 = Radiobutton(settings_window, text="    Small    ",indicatoron=0, variable=size, value="small", bg = "#333333", fg = "#EEEEEE", selectcolor="#333333", activebackground="#333333").grid(row=6, column=0,sticky="ew")
    radio5 = Radiobutton(settings_window, text="Standard",indicatoron=0, variable=size, value="standard", bg = "#333333", fg = "#EEEEEE", selectcolor="#333333", activebackground="#333333").grid(row=6, column=1,sticky="ew")
    radio6 = Radiobutton(settings_window, text="    Large    ",indicatoron=0, variable=size, value="large", bg = "#333333", fg = "#EEEEEE", selectcolor="#333333", activebackground="#333333").grid(row=6, column=2,sticky="ew")
    musicLabel = Label(settings_window, text="Music Options", bg="#333333", fg="#EEEEEE").grid(row=7, column=1)
    pauseButton = Button(settings_window, text="Pause", bg="#333333", fg="#EEEEEE",command=lambda: music.pause()).grid(row=8, column=0,sticky="ew")
    playButton = Button(settings_window, text="Play", bg="#333333", fg="#EEEEEE", command=lambda: music.play()).grid(row=8, column=1,sticky="ew")
    skipButton = Button(settings_window, text="Skip", bg="#333333", fg="#EEEEEE", command=lambda: music.next()).grid(row=8, column=2,sticky="ew")
    finishButton = Button(settings_window, text="  Apply Changes  ", bg="#333333", fg="#EEEEEE",
                          command=lambda: changeSettings(speed.get(), size.get())).grid(row=9, column=1)

def create_choices(choiceList, pathList):
    #create buttons for the amount of options available, represtented by 'number'
    for i in range(0, len(choiceList)):
        button = Button(frame2, text=choiceList[i], command=lambda i=i: click_choice(pathList[i]), bg="#333333", fg="#EEEEEE")
        button.pack(fill='both', expand='yes')

#Unique Room for starting the game
def queue_start_story(window):
    window.destroy()

    #PUT PLAYLIST HERE
    startBackgroundMusic()
    rollCharacters()
    win.deiconify()

    # CHANGE THIS AFTER TESTING!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    #arc2_58()

    room_run("arc1_0")
    getInput("Please Enter Character Name:")
    g.pName = g.inputResponse
    g.inputResponse = "null"
    choices = ["Continue..."]
    paths = ["arc1_8"]
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
textWindow.config(font=("Calibri", g.txtSize))
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

music.playIntro()

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
#I needed to move the name input to the beginning
def arc1_8():
    room_run("arc1_8")
    choices = ["Continue..."]
    paths = ["arc1_1"]
    create_choices(choices, paths)

def arc1_1():
    room_run("arc1_1")
    choices = ["Take Chocolate", "Take Potato Chips", "Do Nothing"]
    paths = ["arc1_2", "arc1_3", "arc1_4"]
    create_choices(choices, paths)

def arc1_2():
    g.food = "chocolate"
    room_run("arc1_2")
    choices = ["Continue..."]
    paths = ["arc1_5"]
    create_choices(choices, paths)

def arc1_3():
    g.food = "potato chips"
    room_run("arc1_3")
    choices = ["Continue..."]
    paths = ["arc1_5"]
    create_choices(choices, paths)

def arc1_4():
    g.food = "chocolate"
    room_run("arc1_4")
    choices = ["Continue..."]
    paths = ["arc1_5"]
    create_choices(choices, paths)

def arc1_5():
    room_run("arc1_5")
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
    if g.firstTimeArc2 == "true":
        room_run("arc2_1")
    else:
        room_run("arc2_51")

    g.firstTimeArc2 = "false"
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
    g.metB = "true"
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
    g.deathReturn = "arc2_17"

def arc2_18():
    room_run("arc2_18")
    g.deathReturn = "arc2_18"

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
    g.hasPotato = "true"
    choices = ["Head back the way you came to the central plaza", "Enter Tavern", "Continue along the path"]
    paths = ["arc2_24", "arc2_25", "arc2_26"]
    create_choices(choices, paths)

def arc2_23():
    room_run("arc2_23")
    g.hasPotato = "true"
    choices = ["Head back the way you came to the central plaza", "Enter Tavern", "Continue along the path"]
    paths = ["arc2_24", "arc2_25", "arc2_26"]
    create_choices(choices, paths)

def arc2_24():
    if g.hasPotato == "true":
        g.hasPotato = "false"
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
    if g.hasPotato == "true":
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
    if g.hasPotato == "true":
        choices = ["Run away!", "Share your potato with the starving man"]
        paths = ["arc2_28", "arc2_27"]
        g.hasPotato = "false"
        create_choices(choices, paths)
    else:
        choices = ["Run away!"]
        paths = ["arc2_28"]
        create_choices(choices, paths)

def arc2_27():
    room_run("arc2_27")
    g.muggerMissing = "true"
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
    if g.hasPotato == "true":
        g.hasPotato = "false"
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
    if g.muggerMissing == "true":
        g.muggerMissing = "false"
        arc2_46()
    room_run("arc2_29")

    if g.metB == "true":
        g.metB = "false"
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
    if g.firstMeeting == "true":
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
    if g.firstMeeting == "true":
        disp_txt("\nYou feel frozen, it is as if she has seen right through you. You shift uncomfortably again, "
                 "trying to think of a way to get her off your back. But how? The " + str(g.food) + " worked for a little"
                 " bit so maybe something similar could get her to back off. You feel in your pocket your "
                 "wallet and in the other your phone. Your phone! These people seem to come from a time before"
                 " electricity and surely they will respect you and be amazed by your tiny and seemingly"
                 " magical device.  ")

    choices = ["Continue..."]
    paths = ["arc2_60"]
    create_choices(choices, paths)

def arc2_60(): #Placed here because it is a continuation of arc 29 for simplicity
    room_run("arc2_60")
    getInput("what city/town are you from?")
    g.pLocation = g.inputResponse

    choices = ["Continue..."]
    paths = ["arc2_61"]
    create_choices(choices, paths)

def arc2_61(): #Placed here because it is a continuation of arc 29 for simplicity
    room_run("arc2_61")
    if g.firstMeeting == "true":
        disp_txt("\nYou aren’t really sure why but you know you have to join these people on their quest. "
                 "You also know that everything " + str(g.liName) + " just said is true, you truly offer little value. "
                 "The trick then will have to be convincing them to allow you to join, and then prove your "
                 "worth along the way. But how to convince them? The key to this is probably in this whole "
                 "‘Ancient Dragon’ thing…   ")

    choices = ["Continue..."]
    paths = ["arc2_62"]
    create_choices(choices, paths)

def arc2_62(): #Placed here because it is a continuation of arc 29 for simplicity
    room_run("arc2_62")

    #next is choose which death or victory you get
    g.firstMeeting = "false"
    if g.knowsDeath == "false" and g.loosenedPlanks == "false":
        choices = ["Join " + str(g.aName) + " and " + str(g.liName), "Join " + str(g.bName)]
        paths = ["arc2_31", "arc2_30"]
        create_choices(choices, paths)
    elif g.knowsDeath == "true" and g.loosenedPlanks == "false":
        choices = ["Join " + str(g.aName) + " and " + str(g.liName), "Join " + str(g.bName)]
        paths = ["arc2_47", "arc2_48"]
        create_choices(choices, paths)
    else:
        choices = ["Join " + str(g.aName) + " and " + str(g.liName), "Join " + str(g.bName)]
        paths = ["arc2_49", "arc2_50"]
        create_choices(choices, paths)

def arc2_30():
    room_run("arc2_30")
    g.deathReturn = "arc2_30"
    g.knowsDeath = "true"

def arc2_31():
    room_run("arc2_31")
    g.deathReturn = "arc2_31"
    g.knowsDeath = "true"

def arc2_32():
    room_run("arc2_32")

    choices = ["climb tree onto platform", "continue along path"]
    paths = ["arc2_33", "arc2_34"]
    create_choices(choices, paths)

def arc2_33():
    room_run("arc2_33")
    if g.seenForest == "false":
        choices = ["follow path left along the outskirts", "enter the forest"]
        paths = ["arc2_37", "arc2_35"]
        create_choices(choices, paths)
    else:
        choices = ["follow path left along the outskirts", "enter the forest"]
        paths = ["arc2_37", "arc2_36"]
        create_choices(choices, paths)

def arc2_34():
    room_run("arc2_34")
    if g.seenForest == "false":
        choices = ["follow path left along the outskirts", "enter the forest"]
        paths = ["arc2_37", "arc2_35"]
        create_choices(choices, paths)
    else:
        choices = ["follow path left along the outskirts", "enter the forest"]
        paths = ["arc2_37", "arc2_36"]
        create_choices(choices, paths)

def arc2_35():
    room_run("arc2_35")
    g.deathReturn = "arc2_35"
    g.seenForest = "true"

def arc2_36():
    room_run("arc2_36")
    g.deathReturn = "arc2_36"
    g.seenForest = "true"

def arc2_37():
    room_run("arc2_37")
    if g.seenForest == "true":
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
    g.loosenedPlanks = "true"
    choices = ["Stay and ambush the killer", "Head into Kingsbridge"]
    paths = ["arc2_44", "arc2_45"]
    create_choices(choices, paths)

def arc2_39():
    room_run("arc2_39")

    if g.seenForest == "false":
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
    g.deathReturn = "arc2_42"

def arc2_43():
    room_run("arc2_43")
    g.deathReturn = "arc2_43"

def arc2_44():
    room_run("arc2_44")
    g.knowsDeath = "true"
    g.deathReturn = "arc2_44"

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
    g.deathReturn = "arc2_47"
    g.knowsDeath = "true"

def arc2_48():
    room_run("arc2_48")
    g.deathReturn = "arc2_48"
    g.knowsDeath = "true"

def arc2_49():
    room_run("arc2_49")

def arc2_50():
    room_run("arc2_49")


#-----------------------------------------------Program Start----------------------------------------------------------
#arc 1
story_sections = []
for i in range(0, 9):
    num = i
    story_sections.append("arc1_" + f"{num}")
#arc 2
for i in range(0, 63):
    num = i
    story_sections.append("arc2_" + f"{num}")

story_content = {}
i=0
for section in story_sections:
    if i<9:
        file_path = "script/arc1/" + section + ".txt"
    #arc 1 plus arc 2...
    elif i<73:
        file_path = "script/arc2/" + section + ".txt"

    with open(file_path, encoding="utf8") as file_reader:
        story_content[section] = file_reader.read()
    i=i+1







#-----------------------------------------------------MAIN-------------------------------------------------------------

#createTxtFiles(56)

win.mainloop()
