import sys
try:
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
    from threading import Thread
except Exception as error:
    with open('~/Desktop/ERRORLOG', 'wb') as f:
        f.write(error)
        f.write(sys.exc_type)
        f.write("\n\nError Importing. Make sure computer OS and VLC are updated and installed.")
    f.close()
    print("ERROR")
#--------------------------------------------------------Globals--------------------------------------------------------
badInput = ["!","@","#","$","%","^","&","*","^_^",":)"," ","",".",",","-","_","$pName","$aName","$bName","$liName"]
maudAnswers = ["0", 0, "zero", "none", "nothing", "no fingers", "there aren't any"]
class g:
    inputResponse = "null"
    # global values
    
    currentRoom = "null"
    savedRoom = "null"
    txtSpeed = 0.000001#0.05
    txtSize = 16

    food = "null"
    pName = "null"
    aName = "null"
    bName = "null"
    liName = "null"
    mName = "null"
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
    loadTimes = 0
    hName = "null"
    horseColor = "null"
    failCounter = 0

    # !!!Flags!!!
    firstTimeArc2 = "true"
    knowsDeath = "false"
    loosenedPlanks = "false"
    hasPotato = "false"
    muggerMissing = "false"
    metB = "false"
    firstMeeting = "true"
    seenForest = "false"
    takenTrial = "false"
    bishopMelt = "false"
    firstAmbush = "false"
    talkedTo = "null"
    watchedTorture = "false"

#=======


class VLC:
    def fillPlaylist(self):
        self.Player = Instance('--loop')
        self.mediaList = self.Player.media_list_new()
        self.listPlayer = self.Player.media_list_player_new()
        path = "./music/"
        songs = os.listdir(path)
        random.shuffle(songs)
        for s in songs:
            self.mediaList.add_media(self.Player.media_new(os.path.join(path,s)))
        self.listPlayer.set_media_list(self.mediaList)

    def play(self):
        self.listPlayer.play()
        self.listPlayer.get_media_player().audio_set_volume(60)
    def next(self):
        self.listPlayer.next()
    def pause(self):
        self.listPlayer.pause()
    def previous(self):
        self.listPlayer.previous()
    def stop(self):
        self.listPlayer.stop()
    def playIntro(self):
        self.Player = Instance('--loop')
        self.mediaList = self.Player.media_list_new()
        self.listPlayer = self.Player.media_list_player_new()
        path = './title/crystalAir.mp3'
        self.mediaList.add_media(self.Player.media_new(path))
        self.listPlayer.set_media_list(self.mediaList)
        self.listPlayer.play()
        self.listPlayer.get_media_player().audio_set_volume(50)
    def playSadSong1(self):
        #This is for playing op85 during town death scenes. They need a unique timer on a thread to work.
        time.sleep(647)

        self.stop()
        self.Player = Instance('--loop')
        self.mediaList = self.Player.media_list_new()
        self.listPlayer = self.Player.media_list_player_new()
        self.mediaList.add_media(self.Player.media_new('./title/op85.mp3'))
        self.listPlayer.set_media_list(self.mediaList)
        self.listPlayer.play()
        self.listPlayer.get_media_player().audio_set_volume(100)
    def playSadSong2(self):
        # This is for playing op85 during town death scenes. They need a unique timer on a thread to work.
        time.sleep(749)

        self.stop()
        self.Player = Instance('--loop')
        self.mediaList = self.Player.media_list_new()
        self.listPlayer = self.Player.media_list_player_new()
        self.mediaList.add_media(self.Player.media_new('./title/op85.mp3'))
        self.listPlayer.set_media_list(self.mediaList)
        self.listPlayer.play()
        self.listPlayer.get_media_player().audio_set_volume(100)
    def startBackgroundMusic(self):
        self.stop()
        self.fillPlaylist()
        self.play()
        self.listPlayer.get_media_player().audio_set_volume(60)
    def playKulning(self):
        self.stop()
        self.Player = Instance('--loop')
        self.mediaList = self.Player.media_list_new()
        self.listPlayer = self.Player.media_list_player_new()
        self.mediaList.add_media(self.Player.media_new('./title/kulning.mp3'))
        self.listPlayer.set_media_list(self.mediaList)
        self.listPlayer.play()
        self.listPlayer.get_media_player().audio_set_volume(80)

music = VLC()


#-------------------------------------------------------Functions-------------------------------------------------------



def getLocation():
    #returns your city
    g = geocoder.ip('me')
    return(g.city)

def getDisplayName():
    #make sure to make name all caps
    GetUserNameEx = ctypes.windll.secur32.GetUserNameExW
    NameDisplay = 3

    size = ctypes.pointer(ctypes.c_ulong(0))
    GetUserNameEx(NameDisplay, None, size)

    nameBuffer = ctypes.create_unicode_buffer(size.contents.value)
    GetUserNameEx(NameDisplay, nameBuffer, size)
    return nameBuffer.value


def checkLoadTimes():

    #if changing how many loads it takes to go crazy, don't forget to change the text on create_choices as well
    if g.loadTimes > 3 and g.loadTimes < 8:
        clear_screen()
        string = "Your brain stings, your very soul aches in pain. It feels as if a small part of yourself was lost.\n\n"
        disp_txt(string)
        time.sleep(2)

    if g.loadTimes > 7 and g.loadTimes < 12:
        clear_screen()
        string = "Your spirit screams in agony. Your soul wails in despair. You have dealt irreparable damage to yourself, but the consequences" \
                 " are yet to seen.\n\n"
        disp_txt(string)
        time.sleep(2)
    if g.loadTimes > 11 and g.loadTimes < 16:
        clear_screen()
        string = "You feel your very sanity slipping, your soul withers away. Something core to who you are has been lost to the void forever. You start to chuckle.\n[" \
                 + g.pName + "] haha... HAHAHAHA...\n\n"
        disp_txt(string)
        time.sleep(2)
    if g.loadTimes > 15 and g.loadTimes < 20:
        clear_screen()
        string = "HAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHA.\n[" \
                 "HAHAHA] HAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHA\n\n HAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHA\n\n"
        disp_txt(string)
        time.sleep(2)


def postDeathPassage(toPrint):
    checkLoadTimes()
    room_run(toPrint)
    choices = ["Continue..."]
    paths = [g.savedRoom]
    create_choices(choices, paths)

def deadChecker():
    # if you just died this is a special message for you :)
    if g.currentRoom == "arc5_13":
        checkLoadTimes()
        eval('arc5_14()')
    if g.deathReturn == "arc2_17" or g.deathReturn == "arc2_42":
        g.deathReturn = "null"
        postDeathPassage('arc2_52')

    elif g.deathReturn == "arc2_18" or g.deathReturn == "arc2_35" or g.deathReturn == "arc2_36":
        g.deathReturn = "null"
        postDeathPassage('arc2_56')

    elif g.deathReturn == "arc2_30" or g.deathReturn == "arc2_48":
        g.deathReturn = "null"
        postDeathPassage('arc2_54')

    elif g.deathReturn == "arc2_31" or g.deathReturn == "arc2_47":
        g.deathReturn = "null"
        postDeathPassage('arc2_53')

    elif g.deathReturn == "arc2_43":
        g.deathReturn = "null"
        postDeathPassage('arc2_57')

    elif g.deathReturn == "arc2_44":
        g.deathReturn = "null"
        postDeathPassage('arc2_55')
    else:
        checkLoadTimes()
        print(g.savedRoom)
        eval(g.savedRoom + "()")


def loadGame(window):
    win.deiconify()
    with open('./savefile', 'rb') as f:
        data = pickle.load(f)
    list = vars(g)
    listy = list.items()
    for left, right in listy:
        if left.startswith("__") == False:
            g.left = data[left]
    #delete buttons
    list = frame2.pack_slaves()
    for x in list:
        if str(x) != str(list[0]):
            x.destroy()
    print("Game Loaded")
    disp_txt("\nLoading Game...\n")
    window.destroy()
    g.loadTimes += 1

    #If you physically altered the world, we need to Undo that here
    g.loosenedPlanks = "false"
    g.metB = "false"

    music.startBackgroundMusic()
    if g.currentRoom == "arc1_0":
        g.currentRoom = "arc1_1"
    if g.currentRoom == "arc5_13":
        g.currentRoom = "arc5_14"
        g.savedRoom = "arc5_14"
    deadChecker()

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
        g.txtSpeed = 0.1
    if newSpeed == "standard":
        g.txtSpeed = 0.05
    if newSpeed == "fast":
        g.txtSpeed = 0.0001

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

def textOutput(string):
    for char in string:
        if g.txtSpeed != 0.0001:
            textWindow.see(tk.END)
        textWindow.insert(tk.INSERT, char)
        if char == '\n':
            textWindow.insert(tk.INSERT, '\n')
        textWindow.update()
        time.sleep(g.txtSpeed)

def disp_txt(string):
    textThread = Thread(target=textOutput(string))
    textThread.start()

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
            #print(str(globy) + " ---- " + str(value))
            string = string.replace("$"+globy, str(value))
    print("##################################")

    if g.loadTimes > 11 and g.loadTimes < 16:
        string = string.replace('a', 'ha')

    if g.loadTimes > 15 and g.loadTimes < 20:
        string = string.replace(g.pName, 'HAHAHA')
        string = string.replace(g.aName, 'HAHAHA')
        string = string.replace(g.bName, 'HAHAHA')
        string = string.replace(g.liName, 'HAHAHA')

    if g.loadTimes > 19:
        string = "HAHAHAHAHHAHAHAHAHAHAHAHAHAHAHAHAHAHAAHAHAHAHAHAHAHHAHAHAAHAHAHAHAHAHAHAHHAHAAHHAHAHHAA" \
                 "HAHAHAHAHHAHAHAHAHAHAHAHAHAHAHAHAHAHAAHAHAHAHAHAHAHHAHAHAAHAHAHAHAHAHAHAHHAHAAHHAHAHHAA" \
                 "HAHAHAHAHHAHAHAHAHAHAHAHAHAHAHAHAHAHAAHAHAHAHAHAHAHHAHAHAAHAHAHAHAHAHAHAHHAHAAHHAHAHHAA" \
                 "HAHAHAHAHHAHAHAHAHAHAHAHAHAHAHAHAHAHAAHAHAHAHAHAHAHHAHAHAAHAHAHAHAHAHAHAHHAHAAHHAHAHHAA" \
                 "HAHAHAHAHHAHAHAHAHAHAHAHAHAHAHAHAHAHAAHAHAHAHAHAHAHHAHAHAAHAHAHAHAHAHAHAHHAHAAHHAHAHHAA" \
                 "HAHAHAHAHHAHAHAHAHAHAHAHAHAHAHAHAHAHAAHAHAHAHAHAHAHHAHAHAAHAHAHAHAHAHAHAHHAHAAHHAHAHHAA" \
                 "HAHAHAHAHHAHAHAHAHAHAHAHAHAHAHAHAHAHAAHAHAHAHAHAHAHHAHAHAAHAHAHAHAHAHAHAHHAHAAHHAHAHHAA" \
                 "HAHAHAHAHHAHAHAHAHAHAHAHAHAHAHAHAHAHAAHAHAHAHAHAHAHHAHAHAAHAHAHAHAHAHAHAHHAHAAHHAHAHHAA"
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
        name=("script/arc7_" + f"{i}"+ ".txt")
        file = open(name,"w+")
        file.close()

def rollCharacters():
    bNames = ['Alexia', 'Aphrodite', 'Domino', 'Jade', 'Karma', 'Destiny', 'Lyra', 'Quinn', 'Ripley', 'Trinity', 'Valkyrie']
    aNames = ['Phoebe', 'Valentine', 'Rose', 'Beatrice', 'Sophia', 'Charlotte', 'Emilia', 'Hazel', 'Faith', 'Iris', 'Ariel']
    liNames= ['Chloe', 'Delila', 'Ashe', 'Lucy', 'Violet', 'Autumn', 'Nova', 'Elizabeth', 'Melody', 'Mai', 'Lilith']
    mNames=['Blain', 'Copper', 'Harry', 'Penn']
    bardNames   = ['Paganini', 'Vivaldi', 'Sarasate']
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
    horsecolors = ['Brown', 'Yellow', 'White', 'Black']

    g.aName = random.choice(aNames)
    g.bName = random.choice(bNames)
    g.liName = random.choice(liNames)
    g.mName = random.choice(mNames)
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
    g.horseColor = random.choice(horsecolors)


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

    if g.txtSpeed == 0.0001:
        speed.set("fast")
    if g.txtSpeed == 0.05:
        speed.set("standard")
    if g.txtSpeed == 0.1:
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
    radio3 = Radiobutton(settings_window, text="    fast    ",indicatoron=0, variable=speed, value="fast", bg = "#333333", fg = "#EEEEEE", selectcolor="#333333", activebackground="#333333").grid(row=4, column=2,sticky="nsew")
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
        if g.loadTimes > 15:
            button = Button(frame2, text="HAHAHAHA", command=lambda i=i: click_choice(pathList[i]), bg="#333333", fg="#EEEEEE")
            button.pack(fill='both', expand='yes')
        else:
            button = Button(frame2, text=choiceList[i], command=lambda i=i: click_choice(pathList[i]), bg="#333333", fg="#EEEEEE")
            button.pack(fill='both', expand='yes')

#Unique Room for starting the game ################################################################################
def queue_start_story(window):
    window.destroy()
    music.startBackgroundMusic()
    rollCharacters()
    win.deiconify()

    room_run("arc1_0")
    #getInput("Please Enter Character Name:")
    g.pName = "tester" # g.inputResponse
    g.inputResponse = "null"
    choices = ["Continue..."]
    paths = ["arc6_0"] # if resetting, send to 1_8
    create_choices(choices, paths)

def quit_me():
    print('quit')
    win.quit()
    win.destroy()

def makeTears():
    if g.talkedTo == "chef":
        return ["arc6_23"]
    elif g.talkedTo == "aName":
        return ["arc6_21"]
    elif g.talkedTo == "liName":
        return ["arc6_20"]
    elif g.talkedTo == "bardName":
        return ["arc6_22"]
    elif g.talkedTo == "mName":
        return ["arc6_24"]
    else:
        print("error finding sad part")
        return "arc6_20"


#####################################################################################################################
#build main GUI------------------------------------------------------------------
win = tk.Tk()
win.protocol("WM_DELETE_WINDOW", quit_me)
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
#I neededed to move the name input to the beginning
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

    t1 = Thread(target=music.playSadSong1)
    t1.start()
    room_run("arc2_30")

    g.deathReturn = "arc2_30"
    g.knowsDeath = "true"

def arc2_31():
    t1 = Thread(target=music.playSadSong2)
    t1.start()
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
    choices = ["Continue..."]
    paths = ["arc3_0"]
    create_choices(choices, paths)

def arc2_50():
    room_run("arc2_49")

def arc3_0():
    room_run("arc3_0")
    choices = ["Continue..."]
    paths = ["arc3_1"]
    create_choices(choices, paths)

def arc3_1():
    room_run("arc3_1")
    choices = ["Continue..."]
    paths = ["arc3_2"]
    getInput("Please Enter Horse's Name:")
    g.hName = g.inputResponse
    g.inputResponse = "null"
    create_choices(choices, paths)

def arc3_2():
    room_run("arc3_2")
    choices = ["Continue..."]
    paths = ["arc3_3"]
    create_choices(choices, paths)

def arc3_3():
    room_run("arc3_3")
    choices = ["Sneak In", "Attack Directly"]
    paths = ["arc3_4", "arc3_5"]
    create_choices(choices, paths)

def arc3_4():
    room_run("arc3_4")
    choices = ["Continue..."]
    paths = ["arc3_6"]
    create_choices(choices, paths)

def arc3_5():
    room_run("arc3_5")
    choices = ["Continue..."]
    paths = ["arc3_6"]
    create_choices(choices, paths)

def arc3_6():
    room_run("arc3_6")
    choices = ["Spare Him", "Kill Him"]
    paths = ["arc3_7", "arc3_8"]
    create_choices(choices, paths)

def arc3_7():
    room_run("arc3_7")
    choices = ["Continue..."]
    paths = ["arc4_0"]
    create_choices(choices, paths)

def arc3_8():
    room_run("arc3_8")
    choices = ["Continue..."]
    paths = ["arc4_0"]
    create_choices(choices, paths)

def arc4_0():
    room_run("arc4_0")
    choices = ["Continue..."]
    paths = ["arc4_1"]
    create_choices(choices, paths)

def arc4_1():
    room_run("arc4_1")
    choices = ["Continue..."]
    paths = ["arc4_2"]
    create_choices(choices, paths)

def arc4_2():
    music.playKulning()
    room_run("arc4_2")
    choices = ["Continue..."]
    paths = ["arc4_3"]

    create_choices(choices, paths)

def arc4_3():
    music.startBackgroundMusic()
    room_run("arc4_3")
    choices = ["Fight your way through the cultists", "Sneak Through the Camp", "use " + g.mName + " as a sacrifice and "
    "run past the guards", "Abandon your friends and go in by yourself"]
    paths = ["arc4_4", "arc4_4", "arc4_4", "arc4_4"]

    create_choices(choices, paths)

def arc4_4():
    room_run("arc4_4")
    choices = ["Continue..."]
    paths = ["arc4_5"]
    create_choices(choices, paths)

def arc4_5():
    room_run("arc4_5")
    choices = ["Continue..."]
    paths = ["arc4_6"]
    create_choices(choices, paths)

def arc4_6():
    room_run("arc4_6")
    getInput("Please enter the correct four letters")
    string = g.inputResponse
    if string.lower() == "uiop" or string.lower() == "u i o p":
        choices = ["Continue..."]
        paths = ["arc4_8"]
    else:
        choices = ["Continue..."]
        paths = ["arc4_7"]
    g.inputResponse = "null"

    create_choices(choices, paths)

def arc4_7():
    room_run("arc4_7")

def arc4_8():
    room_run("arc4_8")
    if g.takenTrial == "true":
        choices = ["Continue..."]
        paths = ["arc4_10"]
    if g.takenTrial == "false":
        choices = ["Continue..."]
        paths = ["arc4_9"]
    create_choices(choices, paths)

def arc4_9():
    room_run("arc4_9")
    choices = ["Continue..."]
    paths = ["arc4_11"]
    create_choices(choices, paths)

def arc4_10():
    room_run("arc4_10")
    choices = ["Continue..."]
    paths = ["arc4_26"]
    create_choices(choices, paths)

def arc4_11():
    room_run("arc4_11")
    choices = ["Do Nothing", "Pull the Lever"]
    paths = ["arc4_13", "arc4_12"]
    create_choices(choices, paths)

def arc4_12():
    room_run("arc4_12")
    choices = ["Do Nothing", "Push the man in front of the Train"]
    paths = ["arc4_15", "arc4_14"]
    create_choices(choices, paths)

def arc4_13():
    room_run("arc4_13")
    choices = ["Do Nothing", "Pull the Lever"]
    paths = ["arc4_17", "arc4_16"]
    create_choices(choices, paths)

def arc4_14():
    room_run("arc4_14")
    choices = ["Do Nothing", "Step in front of the Train"]
    paths = ["arc4_19", "arc4_18"]
    create_choices(choices, paths)

def arc4_15():
    room_run("arc4_15")
    choices = ["Do Nothing", "Push the man in front of the Train"]
    paths = ["arc4_21", "arc4_20"]
    create_choices(choices, paths)

def arc4_16():
    room_run("arc4_16")
    choices = ["Step in front of the Train", "Do Nothing"]
    paths = ["arc4_22", "arc4_23"]
    create_choices(choices, paths)

def arc4_17():
    room_run("arc4_17")
    choices = ["Do Nothing", "Press the Red Button"]
    paths = ["arc4_25", "arc4_24"]
    create_choices(choices, paths)

def arc4_18():
    g.takenTrial = "true"
    room_run("arc4_18")
    choices = ["Continue..."]
    paths = ["arc4_26"]
    create_choices(choices, paths)

def arc4_19():
    g.takenTrial = "true"
    room_run("arc4_19")
    choices = ["Continue..."]
    paths = ["arc4_26"]
    create_choices(choices, paths)

def arc4_20():
    g.takenTrial = "true"
    room_run("arc4_20")
    choices = ["Continue..."]
    paths = ["arc4_26"]
    create_choices(choices, paths)

def arc4_21():
    g.takenTrial = "true"
    room_run("arc4_21")
    choices = ["Continue..."]
    paths = ["arc4_26"]
    create_choices(choices, paths)

def arc4_22():
    g.takenTrial = "true"
    room_run("arc4_22")
    choices = ["Continue..."]
    paths = ["arc4_26"]
    create_choices(choices, paths)

def arc4_23():
    g.takenTrial = "true"
    room_run("arc4_23")
    choices = ["Continue..."]
    paths = ["arc4_26"]
    create_choices(choices, paths)

def arc4_24():
    g.takenTrial = "true"
    room_run("arc4_24")
    choices = ["Continue..."]
    paths = ["arc4_26"]
    create_choices(choices, paths)

def arc4_25():
    g.takenTrial = "true"
    room_run("arc4_25")
    choices = ["Continue..."]
    paths = ["arc4_26"]
    create_choices(choices, paths)

def arc4_26():
    room_run("arc4_26")
    choices = ["Do Not Read The Script", "Read The Script"]
    paths = ["arc4_28", "arc4_27"]
    create_choices(choices, paths)

def arc4_27():
    music.stop()
    room_run("arc4_27")
    choices = ["Continue..."]
    paths = ["arc4_29"]
    create_choices(choices, paths)
    path = os.path.realpath('./script/arc4')
    os.startfile(path)

def arc4_28():
    room_run("arc4_28")
    choices = ["Continue..."]
    paths = ["arc4_29"]
    create_choices(choices, paths)

def arc4_29():
    music.startBackgroundMusic()
    room_run("arc4_29")
    choices = ["Continue..."]
    paths = ["arc4_30"]
    create_choices(choices, paths)

def arc4_30():
    room_run("arc4_30")
    choices = ["Continue..."]
    paths = ["arc5_0"]
    create_choices(choices, paths)

def arc5_0():
    room_run("arc5_0")
    choices = ["Continue..."]
    paths = ["arc5_1"]
    create_choices(choices, paths)

def arc5_1():
    room_run("arc5_1")
    choices = ["Continue..."]
    paths = ["arc5_2"]
    create_choices(choices, paths)

def arc5_2():
    room_run("arc5_2")
    choices = ["Continue..."]
    paths = ["arc5_3"]
    create_choices(choices, paths)

def arc5_3():
    room_run("arc5_3")
    choices = ["Enter the mysterious Sewer Entrance", "Continue to wander the streets, bored"]
    paths = ["arc5_5", "arc5_4"]
    create_choices(choices, paths)

def arc5_4():
    room_run("arc5_4")
    choices = ["Enter the mysterious Sewer Entrance", "Continue to wander the streets, bored"]
    paths = ["arc5_5", "arc5_4"]
    create_choices(choices, paths)

def arc5_5():
    room_run("arc5_5")
    choices = ["Go forwards along the tunnel", "Turn and go the opposite direction along the tunnel"]
    paths = ["arc5_6", "arc5_6"]
    create_choices(choices, paths)

def arc5_6():
    room_run("arc5_6")
    choices = ["Take Left Path", "Take Right Path"]
    paths = ["arc5_7", "arc5_7"]
    create_choices(choices, paths)

def arc5_7():
    room_run("arc5_7")
    choices = ["Continue..."]
    paths = ["arc5_8"]
    create_choices(choices, paths)

def arc5_8():
    room_run("arc5_8")
    choices = ["Continue..."]
    paths = ["arc5_9"]
    create_choices(choices, paths)

def arc5_9():
    room_run("arc5_9")
    choices = ["Continue..."]
    paths = ["arc5_10"]
    create_choices(choices, paths)

def arc5_10():
    room_run("arc5_10")
    choices = ["Scout using Balcony", "Charge!"]
    paths = ["arc5_11", "arc5_12"]
    create_choices(choices, paths)

def arc5_11():
    room_run("arc5_11")
    choices = ["Continue..."]
    paths = ["arc5_13"]
    create_choices(choices, paths)

def arc5_12():
    room_run("arc5_12")
    if g.bishopMelt == "false":
        choices = ["Continue..."]
        paths = ["arc5_13"]
    else:
        choices = ["Continue..."]
        paths = ["arc5_14"]
    create_choices(choices, paths)

def arc5_13():
    room_run("arc5_13")
    g.bishopMelt = "true"

def arc5_14():
    room_run("arc5_14")
    choices = ["Continue..."]
    paths = ["arc5_15"]
    create_choices(choices, paths)

def arc5_15():
    room_run("arc5_15")
    choices = ["Continue..."]
    paths = ["arc6_0"]
    create_choices(choices, paths)

def arc6_0():
    room_run("arc6_0")
    choices = ["Continue..."]
    paths = ["arc6_1"]
    create_choices(choices, paths)

def arc6_1():
    room_run("arc6_1")
    if g.failCounter == 5:
        choices = ["Continue..."]
        paths = ["arc6_25"]
    else:
        if g.firstAmbush == "false":
            choices = ["Continue..."]
            paths = ["arc6_2"]
        else:
            choices = ["Continue..."]
            paths = ["arc6_4"]
    create_choices(choices, paths)

def arc6_2():
    room_run("arc6_2")
    choices = ["Continue..."]
    paths = ["arc6_3"]
    create_choices(choices, paths)

def arc6_3():
    room_run("arc6_3")
    g.firstAmbush = "true"

def arc6_4():
    room_run("arc6_4")
    choices = ["Speak with Chef", "speak with "+g.aName, "speak with "+g.bardName, "speak with "+g.liName, "speak with "+g.mName]
    paths = ["arc6_8", "arc6_6", "arc6_7", "arc6_5", "arc6_9"]
    create_choices(choices, paths)

def arc6_5():
    room_run("arc6_5")
    choices = ["Continue..."]
    paths = ["arc6_10"]
    g.talkedTo = "liName"
    create_choices(choices, paths)

def arc6_6():
    room_run("arc6_6")
    choices = ["Continue..."]
    paths = ["arc6_10"]
    g.talkedTo = "aName"
    create_choices(choices, paths)

def arc6_7():
    room_run("arc6_7")
    choices = ["Continue..."]
    paths = ["arc6_10"]
    g.talkedTo = "bardName"
    create_choices(choices, paths)

def arc6_8():
    room_run("arc6_8")
    choices = ["Continue..."]
    paths = ["arc6_10"]
    g.talkedTo = "chef"
    create_choices(choices, paths)

def arc6_9():
    room_run("arc6_9")
    choices = ["Continue..."]
    paths = ["arc6_10"]
    g.talkedTo = "mName"
    create_choices(choices, paths)

def arc6_10():
    room_run("arc6_10")
    choices = ["Ask "+g.aName+" for help", "Attempt to Fight on your own", "Ask "+g.liName+" for help"]
    paths = ["arc6_15", "arc6_11", "arc6_12"]
    create_choices(choices, paths)

def arc6_11():
    room_run("arc6_11")
    g.failCounter += 1

def arc6_12():
    room_run("arc6_12")
    choices = ["Frontal Attack", "Flank, using yourself as bait"]
    paths = ["arc6_13", "arc6_14"]
    create_choices(choices, paths)

def arc6_13():
    g.failCounter += 1
    room_run("arc6_13")
    choices = ["Continue..."]
    paths = makeTears()
    create_choices(choices, paths)

def arc6_14():
    g.failCounter += 1
    room_run("arc6_14")
    choices = ["Continue..."]
    paths = makeTears()
    create_choices(choices, paths)

def arc6_15():
    room_run("arc6_15")
    choices = ["Sneak out of the Town and avoid Conflict", "Ask Maud for Help"]
    paths = ["arc6_16", "arc6_17"]
    create_choices(choices, paths)

def arc6_16():
    g.failCounter += 1
    room_run("arc6_16")
    choices = ["Continue..."]
    paths = makeTears()
    create_choices(choices, paths)
    g.watchedTorture = "true"

def arc6_17():
    room_run("arc6_17")
    choices = ["Cut off the fingers on "+g.aName+"'s right hand", "Refuse Maud's offer and leave"]
    paths = ["arc6_18", "arc6_19"]
    create_choices(choices, paths)

def arc6_18():
    g.failCounter += 1
    room_run("arc6_18")

def arc6_19():
    g.failCounter += 1
    room_run("arc6_19")
    choices = ["Continue..."]
    paths = makeTears()
    create_choices(choices, paths)

def arc6_20(): #liname
    room_run("arc6_20")

def arc6_21(): #aname
    room_run("arc6_21")

def arc6_22(): #bardname
    room_run("arc6_22")

def arc6_23(): #chef
    room_run("arc6_23")

def arc6_24(): #mname
    room_run("arc6_24")

def arc6_25():
    room_run("arc6_25")
    choices = ["Continue..."]
    paths = ["arc6_26"]
    create_choices(choices, paths)

def arc6_26():
    room_run("arc6_26")
    choices = ["Continue..."]
    paths = ["arc6_27"]
    create_choices(choices, paths)

def arc6_27():
    room_run("arc6_27")
    getInput("How many fingers is Maud holding up?")
    string = g.inputResponse
    global maudAnswers
    if string.lower() in maudAnswers:
        choices = ["Continue..."]
        paths = ["arc6_29"]
    else:
        choices = ["Continue..."]
        paths = ["arc6_28"]
    create_choices(choices, paths)

def arc6_28(): #mname
    room_run("arc6_28")

def arc6_29():
    room_run("arc6_29")
    choices = ["Continue..."]
    paths = ["arc6_30"]
    create_choices(choices, paths)

def arc6_30():
    room_run("arc6_30")
    choices = ["Continue..."]
    paths = ["arc7_0"]
    create_choices(choices, paths)


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
#arc 3
for i in range(0, 9):
    num = i
    story_sections.append("arc3_" + f"{num}")
#arc 4
for i in range(0, 31):
    num = i
    story_sections.append("arc4_" + f"{num}")
#arc 5
for i in range(0, 16):
    num = i
    story_sections.append("arc5_" + f"{num}")
#arc 6
for i in range(0, 31):
    num = i
    story_sections.append("arc6_" + f"{num}")
#arc 7
for i in range(0, 45):
    num = i
    story_sections.append("arc7_" + f"{num}")

story_content = {}
i=0
for section in story_sections:
    #your new arc length plus all the other arc lengths plus one
    if i<9:
        file_path = "script/arc1/" + section + ".txt"
    elif i<72:
        file_path = "script/arc2/" + section + ".txt"
    elif i<81:
        file_path = "script/arc3/" + section + ".txt"
    elif i<112:
        file_path = "script/arc4/" + section + ".txt"
    elif i<128:
        file_path = "script/arc5/" + section + ".txt"
    elif i<159:
        file_path = "script/arc6/" + section + ".txt"
    elif i<204:
        file_path = "script/arc7/" + section + ".txt"
    #203 + arc8 length including 0 then + 1
    with open(file_path, encoding="utf8") as file_reader:
        story_content[section] = file_reader.read()
    i=i+1


#-----------------------------------------------------MAIN-------------------------------------------------------------

#createTxtFiles(45)

win.mainloop()
