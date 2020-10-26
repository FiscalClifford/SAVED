import os
try:
    from tkinter import *
    import tkinter as tk
    from tkinter import messagebox
    import tkinter.scrolledtext as tkst
    import time
    import pickle
    from datetime import datetime
    from shutil import copyfile
    import random
    from vlc import Instance
    import ctypes
    from subprocess import Popen
    import geocoder
    from threading import Thread
except Exception as error:
    username = os.getlogin()    # Fetch username
    with open(f'C:\\Users\\{username}\\Desktop\\Error.txt','w') as f:
        f.write(str(error))
        f.write('\n\nError Importing. Make sure computer OS and VLC are updated and installed.')
    f.close()
    print("ERROR")
#--------------------------------------------------------Globals--------------------------------------------------------
badInput = ["!","@","#","$","%","^","&","*","^_^",":)"," ","",".",",","-","_","$pName","$aName","$bName","$liName"]
maudAnswers = ["0", 0, "zero", "none", "nothing", "no fingers", "there aren't any"]
stopText = False


class g:
    #these globals are "remembered" after saves
    inputResponse = "null"
    savedRoom = "null"
    txtSpeed = "0.05"
    txtSize = "16"
    pName = "null"
    aName = "null"
    bName = "null"
    liName = "null"
    mName = "null"
    bardName = "null"
    baronName = "null"
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
    pLocation = "null"
    aLocation = "null"
    bLocation = "null"
    hName = "null"
    horseColor = "null"
    food = "null"
    realName = "null"
    realLocation = "null"
    watchedTorture = "false"
    firstTimeArc2 = "true"
    knowsDeath = "false"
    aRecognize = "false" #if you play a second time a and li will recognize you
    seenForest = "false"
    bishopMelt = "false"
    firstMeeting = "true"
    firstAmbush = "false"
    chopped = "false"
    failCounter = 0
    loadTimes = 0
    deathCounter = 1
    famineCounter = 23
    takenTrial = "false"
    seenSecret = "false"
    inspectBody = "false"
    seenBody = "false"
    seenSecretSolo = "false"
    unlockSecretSolo = "false"
    deathReturn = "null"
    hammerHint = "false"
    
class flag:
    # !!!Flags get reset between each save
    loosenedPlanks = "false"
    hasPotato = "false"
    muggerMissing = "false"
    metB = "false"
    talkedTo = "null"
    fightingFamine = "false"
    currentRoom = "null"
    skipThisOne = "false"
    talkBeforeKey = "false"
    bJoined = "false"
    thiefJoined = "false"
    medicJoined = "false"
    toughJoined = "false"
    hasKeys = "false"
    hasScalpel = "false"
    declaredMedic = "false"
    declaredbName = "false"
    bQuestion = "false"


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
    def playIntro2(self):
        self.Player = Instance('--loop')
        self.mediaList = self.Player.media_list_new()
        self.listPlayer = self.Player.media_list_player_new()
        self.mediaList.add_media(self.Player.media_new('./title/deliver.mp3'))
        self.listPlayer.set_media_list(self.mediaList)
        self.listPlayer.play()
        self.listPlayer.get_media_player().audio_set_volume(100)
    def playIntro3(self):
        self.Player = Instance('--loop')
        self.mediaList = self.Player.media_list_new()
        self.listPlayer = self.Player.media_list_player_new()
        self.mediaList.add_media(self.Player.media_new('./title/slender.mp3'))
        self.listPlayer.set_media_list(self.mediaList)
        self.listPlayer.play()
        self.listPlayer.get_media_player().audio_set_volume(100)
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
    def playDive(self):
        self.stop()
        self.Player = Instance('--loop')
        self.mediaList = self.Player.media_list_new()
        self.listPlayer = self.Player.media_list_player_new()
        self.mediaList.add_media(self.Player.media_new('./title/dive.mp3'))
        self.listPlayer.set_media_list(self.mediaList)
        self.listPlayer.play()
        self.listPlayer.get_media_player().audio_set_volume(80)
    def playAmeno(self):
        self.stop()
        self.Player = Instance('--loop')
        self.mediaList = self.Player.media_list_new()
        self.listPlayer = self.Player.media_list_player_new()
        self.mediaList.add_media(self.Player.media_new('./title/ameno.mp3'))
        self.listPlayer.set_media_list(self.mediaList)
        self.listPlayer.play()
        self.listPlayer.get_media_player().audio_set_volume(80)
    def playpirate(self):
        self.stop()
        self.Player = Instance('--loop')
        self.mediaList = self.Player.media_list_new()
        self.listPlayer = self.Player.media_list_player_new()
        self.mediaList.add_media(self.Player.media_new('./title/pirate.mp3'))
        self.listPlayer.set_media_list(self.mediaList)
        self.listPlayer.play()
        self.listPlayer.get_media_player().audio_set_volume(80)
    def playGwyn(self):
        self.stop()
        self.Player = Instance('--loop')
        self.mediaList = self.Player.media_list_new()
        self.listPlayer = self.Player.media_list_player_new()
        self.mediaList.add_media(self.Player.media_new('./title/gwyn.mp3'))
        self.listPlayer.set_media_list(self.mediaList)
        self.listPlayer.play()
        self.listPlayer.get_media_player().audio_set_volume(80)
    def playHacking(self):
        self.stop()
        self.Player = Instance('--loop')
        self.mediaList = self.Player.media_list_new()
        self.listPlayer = self.Player.media_list_player_new()
        self.mediaList.add_media(self.Player.media_new('./title/hacking.mp3'))
        self.listPlayer.set_media_list(self.mediaList)
        self.listPlayer.play()
        self.listPlayer.get_media_player().audio_set_volume(80)
    def playSlender(self):
        self.stop()
        self.Player = Instance('--loop')
        self.mediaList = self.Player.media_list_new()
        self.listPlayer = self.Player.media_list_player_new()
        self.mediaList.add_media(self.Player.media_new('./title/slender.mp3'))
        self.listPlayer.set_media_list(self.mediaList)
        self.listPlayer.play()
        self.listPlayer.get_media_player().audio_set_volume(100)
    def playAlonne(self):
        self.stop()
        self.Player = Instance('--loop')
        self.mediaList = self.Player.media_list_new()
        self.listPlayer = self.Player.media_list_player_new()
        self.mediaList.add_media(self.Player.media_new('./title/sirAlonne.mp3'))
        self.listPlayer.set_media_list(self.mediaList)
        self.listPlayer.play()
        self.listPlayer.get_media_player().audio_set_volume(80)
    def playFamine(self):
        self.stop()
        self.Player = Instance('--loop')
        self.mediaList = self.Player.media_list_new()
        self.listPlayer = self.Player.media_list_player_new()
        self.mediaList.add_media(self.Player.media_new('./title/famine.mp3'))
        self.listPlayer.set_media_list(self.mediaList)
        self.listPlayer.play()
        self.listPlayer.get_media_player().audio_set_volume(80)
    def playDoor(self):
        self.stop()
        self.Player = Instance('--loop')
        self.mediaList = self.Player.media_list_new()
        self.listPlayer = self.Player.media_list_player_new()
        self.mediaList.add_media(self.Player.media_new('./title/door.mp3'))
        self.listPlayer.set_media_list(self.mediaList)
        self.listPlayer.play()
        self.listPlayer.get_media_player().audio_set_volume(100)
    def playRailgun(self):
        self.stop()
        self.Player = Instance('--loop')
        self.mediaList = self.Player.media_list_new()
        self.listPlayer = self.Player.media_list_player_new()
        self.mediaList.add_media(self.Player.media_new('./title/railgun.mp3'))
        self.listPlayer.set_media_list(self.mediaList)
        self.listPlayer.play()
        self.listPlayer.get_media_player().audio_set_volume(80)
    def playTanjiro(self):
        self.stop()
        self.Player = Instance('--loop')
        self.mediaList = self.Player.media_list_new()
        self.listPlayer = self.Player.media_list_player_new()
        self.mediaList.add_media(self.Player.media_new('./title/tanjiro.mp3'))
        self.listPlayer.set_media_list(self.mediaList)
        self.listPlayer.play()
        self.listPlayer.get_media_player().audio_set_volume(80)
    def playScum(self):
        self.stop()
        self.Player = Instance('--loop')
        self.mediaList = self.Player.media_list_new()
        self.listPlayer = self.Player.media_list_player_new()
        self.mediaList.add_media(self.Player.media_new('./title/scum.mp3'))
        self.listPlayer.set_media_list(self.mediaList)
        self.listPlayer.play()
        self.listPlayer.get_media_player().audio_set_volume(80)

music = VLC()


#-------------------------------------------------------Functions-------------------------------------------------------



def getLocation():
    #returns your city
    place = geocoder.ip('me')
    return place.city.upper()

def getDisplayName():
    #make sure to make name all caps
    GetUserNameEx = ctypes.windll.secur32.GetUserNameExW
    NameDisplay = 3

    size = ctypes.pointer(ctypes.c_ulong(0))
    GetUserNameEx(NameDisplay, None, size)

    nameBuffer = ctypes.create_unicode_buffer(size.contents.value)
    GetUserNameEx(NameDisplay, nameBuffer, size)
    return nameBuffer.value.upper()


def checkLoadTimes():

    #if changing how many loads it takes to go crazy, don't forget to change the text on create_choices as well
    if 3 < g.loadTimes < 8:
        clear_screen()
        string = "Your brain stings, your very soul aches in pain. It feels as if a small part of yourself was lost.\n\n"
        disp_txt(string)
        time.sleep(2)

    if 7 < g.loadTimes < 14:
        clear_screen()
        string = "Your spirit screams in agony. Your soul wails in despair. You have dealt irreparable damage to yourself, but the consequences" \
                 " are yet to seen.\n\n"
        disp_txt(string)
        time.sleep(2)
    if 13 < g.loadTimes < 18:
        clear_screen()
        string = "You feel your very sanity slipping, your soul withers away. Something core to who you are has been lost to the void forever. You start to chuckle.\n[" \
                 + g.pName + "] haha... HAHAHAHA...\n\n"
        disp_txt(string)
        time.sleep(2)
    if 17 < g.loadTimes < 20:
        clear_screen()
        string = "HAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHA.\n[" \
                 "HAHAHA] HAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHA\n\n HAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHA\n\n"
        disp_txt(string)
        time.sleep(2)


def postDeathPassage(toPrint):
    checkLoadTimes()
    room_run(toPrint)
    if toPrint == "arc2_56" and g.hammerHint == "true":
        disp_txt("\nNow that you have figured out what happened to the woman's husband, you should probably let her know about the bad news.")
        g.hammerHint = "false"
    choices = ["Continue..."]
    paths = [g.savedRoom]
    create_choices(choices, paths)

def deadChecker():
    # if you just died this is a special message for you :)
    if flag.skipThisOne == "true":
        flag.skipThisOne = "false"
        checkLoadTimes()
        eval('arc5_14()')
    elif g.deathReturn == "arc2_17" or g.deathReturn == "arc2_42":
        g.deathReturn = "null"
        postDeathPassage('arc2_52')

    elif g.deathReturn == "arc2_18":
        g.deathReturn = "null"
        postDeathPassage('arc2_56')

    elif g.deathReturn == "arc2_35" or g.deathReturn == "arc2_36":
        g.deathReturn = "null"
        g.hammerHint = "true"
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
    global stopText
    stopText = True


def loadGame(window):
    win.deiconify()
    with open('./savefile', 'rb') as f:
        data = pickle.load(f)
    list1 = vars(g)
    list2 = vars(flag)

    for v in list1:
        if v.startswith("__") == False:
            setattr(g, v, data[v])
    for v in list2:
        if v.startswith("__") == False:
            setattr(flag, v, data[v])

    #delete buttons
    list = frame2.pack_slaves()
    for x in list:
        if str(x) != str(list[0]):
            x.destroy()

    print("Game Loaded")
    disp_txt("\nLoading Game...\n")
    window.destroy()


    music.startBackgroundMusic()
    if flag.currentRoom == "arc1_0":
        flag.currentRoom = "arc1_1"
        g.savedRoom = "arc1_1"
    if flag.currentRoom == "arc5_13":
        flag.currentRoom = "arc5_14"
        g.savedRoom = "arc5_14"

    eval(g.savedRoom + "()")



def fakeLoad(window):
    win.deiconify()
    if flag.currentRoom == "arc5_13":
        flag.skipThisOne = "true"

    with open('./savefile', 'rb') as f:
        data = pickle.load(f)
    list1 = vars(flag)
    for v in list1:
        if v.startswith("__") == False:
            setattr(flag, v, data[v])
            print(v)
    print("FakeLoading:")

    #delete buttons
    list = frame2.pack_slaves()
    for x in list:
        if str(x) != str(list[0]):
            x.destroy()
        
    print("Game Loaded")
    disp_txt("\nLoading Game...\n")
    window.destroy()
    g.loadTimes = g.loadTimes + 1
    
    music.startBackgroundMusic()
    if g.savedRoom == "arc1_0":
        g.savedRoom = "arc1_1"
    if g.savedRoom == "arc5_13":
        g.savedRoom = "arc5_14"
        
    flag.currentRoom = g.savedRoom
    deadChecker()


def saveGame(window):
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    data = {}
    g.savedRoom = flag.currentRoom
    list1 = vars(g).items()
    list2 = vars(flag).items()

    for left, right in list1:
        if not left.startswith("__"):
            data[left] = right

    for left, right in list2:
        if not left.startswith("__"):
            data[left] = right

    data['dateTime'] = dt_string

    if os.path.exists('./savefile'):
        os.remove('./savefile')
    with open('./savefile', 'wb') as f:
        pickle.dump(data, f)
    print("Game saved")
    disp_txt("\nYou are surrounded by a warm light. You are SAVED.\n")

    #famine stuff
    if flag.fightingFamine == "true":
        g.famineCounter = g.famineCounter + 1
        eval('arc7_'+ str(g.famineCounter) + '()')

    window.destroy()


def changeSettings(newSpeed, newSize):

    if newSpeed == "slow":
        g.txtSpeed = "0.1"
    if newSpeed == "standard":
        g.txtSpeed = "0.05"
    if newSpeed == "fast":
        g.txtSpeed = "0.0001"

    if newSize == "small":
        g.txtSize = "10"
    if newSize == "standard":
        g.txtSize = "16"
    if newSize == "large":
        g.txtSize = "24"

    textWindow.config(font=("Calibri", int(g.txtSize)))


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
        global stopText
        if stopText:
            print("stopText used")
            print(string)
            stopText = False
            break

        if g.txtSpeed != "0.0001":
            textWindow.see(tk.END)
        textWindow.insert(tk.INSERT, char)

        if char == '\n':
            textWindow.insert(tk.INSERT, '\n')
        textWindow.update()
        time.sleep(float(g.txtSpeed))



def disp_txt(string):
    num = random.randint(0, 100)
    print("thread starting "+ str(num))
    textThread = Thread(target=textOutput(string))
    textThread.start()
    print("thread ending " + str(num))
    textThread.join()


def room_run(section):
    clear_screen()
    flag.currentRoom = section
    to_display = replace_variables(story_content[section])
    disp_txt(to_display)



def replace_variables(string):
    list = vars(g).items()

    for globy, value in list:
        if globy.startswith("__") == False:
            #print(str(globy) + " ---- " + str(value))
            string = string.replace("$"+globy, str(value))
    print("################")

    if 15 < g.loadTimes < 19:
        string = string.replace('a', 'ha')

    if 18 < g.loadTimes < 21:
        string = string.replace(g.pName, 'HAHAHA')
        string = string.replace(g.aName, 'HAHAHA')
        string = string.replace(g.bName, 'HAHAHA')
        string = string.replace(g.liName, 'HAHAHA')
        string = string.replace('a', 'ha')

    if g.loadTimes > 20:
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
    list = frame2.pack_slaves()
    for x in list:
        if str(x) != str(list[0]):
            x.destroy()

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
        name=("script/arc8_" + f"{i}"+ ".txt")
        file = open(name,"w+")
        file.close()

def tortureResolve(choices, paths):
    if flag.currentRoom == "arc6_16":
        create_choices(choices, paths)
        g.watchedTorture = "true"  # used later in arc 7

def famineResolve(choices, paths):
    if flag.currentRoom == "arc7_22":
        create_choices(choices, paths)


def rollCharacters():
    bNames = ['Alexia', 'Aphrodite', 'Domino', 'Jade', 'Karma', 'Destiny', 'Lyra', 'Quinn', 'Ripley', 'Trinity', 'Valkyrie']
    aNames = ['Phoebe', 'Valentine', 'Rose', 'Beatrice', 'Sophia', 'Charlotte', 'Emilia', 'Hazel', 'Faith', 'Iris', 'Ariel']
    liNames= ['Chloe', 'Delila', 'Ashe', 'Lucy', 'Violet', 'Autumn', 'Nova', 'Elizabeth', 'Melody', 'Mai', 'Lilith']
    mNames=  ['Blain', 'Copper', 'Harry', 'Penn']
    bardNames   = ['Paganini', 'Vivaldi', 'Sarasate']
    thiefNames  = ['Tex', 'Lucas', 'Isaac', 'Noland']
    toughNames  = ['Brom', 'Diesel', 'Wulfe', 'Bruce']
    medicNames  = ['Daisy', 'Arya', 'Minneie', 'Sophia']
    merchantNames=['Mickey', 'Mack', 'Meebley', 'Mitch']
    baronNames =  ['Lars', 'Gumpdy', 'Gary', 'Gaston']

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
    g.baronName = random.choice(baronNames)
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
    #settings_window.resizable(False, False)
    settings_window.config(bg="#333333")

    # putting in the defaults
    size = StringVar()
    speed = StringVar()

    if g.txtSize == "24":
        size.set("large")
    if g.txtSize == "16":
        size.set("standard")
    if g.txtSize == "10":
        size.set("small")

    if g.txtSpeed == "0.0001":
        speed.set("fast")
    if g.txtSpeed == "0.05":
        speed.set("standard")
    if g.txtSpeed == "0.1":
        speed.set("slow")


    #loadbutton logic
    if os.path.exists('./savefile'):
        with open('./savefile', 'rb') as f:
            data = pickle.load(f)

        loadButton = Button(settings_window, text="Load Game: " + str(data["dateTime"]), command=lambda: fakeLoad(settings_window), bg = "#333333", fg = "#EEEEEE").grid(row=1, column=0, columnspan=3)
    else:
        loadButton = Button(settings_window, state=DISABLED, text="Load Game", command=lambda: fakeLoad(settings_window), bg = "#333333", fg = "#EEEEEE").grid(row=1, column=0, columnspan=3)
    #menu

    saveButton = Button(settings_window, text="     Save Game     ", command=lambda: saveGame(settings_window), bg = "#333333", fg = "#EEEEEE").grid(row=2, column=0, columnspan=3)
    speedLabel = Label(settings_window, text="Text Scroll Speed", bg = "#333333", fg = "#EEEEEE").grid(row=3, column=1)
    radio1 = Radiobutton(settings_window, text="    Slow    ",indicatoron=0, variable=speed, value="slow", bg = "#333333", fg = "#EEEEEE", selectcolor="#333333", activebackground="#333333").grid(row=4, column=0,sticky="nsew")
    if flag.fightingFamine == "true":
        radio2 = Radiobutton(settings_window, state=DISABLED, text="Standard", indicatoron=0, variable=speed, value="standard", bg="#333333", fg="#EEEEEE", selectcolor="#333333", activebackground="#333333").grid(row=4, column=1, sticky="nsew")
        radio3 = Radiobutton(settings_window, state=DISABLED, text="    fast    ", indicatoron=0, variable=speed, value="fast", bg="#333333", fg="#EEEEEE", selectcolor="#333333", activebackground="#333333").grid(row=4, column=2, sticky="nsew")
    else:
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
    finishButton = Button(settings_window, text="  Apply Changes  ", bg="#333333", fg="#EEEEEE", command=lambda: changeSettings(speed.get(), size.get())).grid(row=9, column=1)

def create_choices(choiceList, pathList):
    # delete buttons
    list = frame2.pack_slaves()
    for x in list:
        if str(x) != str(list[0]):
            x.destroy()
    #create buttons for the amount of options available, represtented by 'number'
    for i in range(0, len(choiceList)):
        if g.loadTimes > 17:
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
    username = os.getlogin()
    #these flags are set for your second playthrough
    if os.path.exists(f'C:\\Users\\{username}\\Documents\\dllConfig.txt') or os.path.exists(f'C:\\Users\\{username}\\Documents\\xllConfig.txt'):
        g.knowsDeath = "true"
        g.firstTimeArc2 = "false"
        g.aRecognize = "true"
        g.seenForest = "true"
    else:
        print("haven't played yet")
    room_run("arc1_0")
    getInput("Please Enter Character Name:")
    g.pName = g.inputResponse
    g.inputResponse = "null"
    choices = ["Continue..."]
    paths = ["arc1_8"] # if resetting, send to 1_8
    create_choices(choices, paths)
####################################################################################################################################################################################################################
def quit_me():
    print('quit')
    win.quit()
    win.destroy()

def makeTears():
    if flag.talkedTo == "chef":
        return ["arc6_23"]
    elif flag.talkedTo == "aName":
        return ["arc6_21"]
    elif flag.talkedTo == "liName":
        return ["arc6_20"]
    elif flag.talkedTo == "bardName":
        return ["arc6_22"]
    elif flag.talkedTo == "mName":
        return ["arc6_24"]
    else:
        print("error finding sad part")
        print(flag.talkedTo)
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
textWindow.config(font=("Calibri", int(g.txtSize)))
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
playedOnce = False
playedTwice = False
username = os.getlogin()
if os.path.exists(f'C:\\Users\\{username}\\Documents\\dllConfig.txt') or os.path.exists(f'C:\\Users\\{username}\\Documents\\xllConfig.txt'):
    playedOnce = True
if os.path.exists(f'C:\\Users\\{username}\\Documents\\dllConfig.txt') and os.path.exists(f'C:\\Users\\{username}\\Documents\\xllConfig.txt'):
    playedTwice = True
menu = Toplevel()
menu.geometry("600x880")
menu.title("SAVED")
menu.iconbitmap('./assets/treelarge_CKX_icon.ico')
menu.resizable(False, False)
menuText = "Saved"
background = "#ffffff"
foreground = "#333333"
if playedOnce == True and playedTwice == False:
    music.playIntro2()
    photo = PhotoImage(file='./assets/vesuvius.gif')
    menuText = "Saved?"
    background = "#333333"
    foreground = "#EEEEEE"
elif playedTwice == True:
    music.playIntro3()
    menuText = "YOU'VE DOOMED US ALL"
    photo = PhotoImage(file='./assets/lisaLast.gif')
    background = "#333333"
    foreground = "#EEEEEE"
else:
    music.playIntro()
    photo = PhotoImage(file='./assets/tree.gif')

screen = tk.Canvas(
    master=menu,
    bg="#696969"
)
screen.pack(fill='both', expand='yes')
title = Label(screen, text=menuText, bg = background, fg = foreground,pady=30, font=("Calibri", 35)).pack(fill='x', expand='yes')
photoLabel = Label(screen, image = photo).pack()
if playedTwice == False:
    button = Button(screen, text="New Game", command=lambda: queue_start_story(menu),bg = background, fg = foreground,pady=20, padx=80)
    button_window = screen.create_window(480, 400, window=button)

    if os.path.exists('./savefile'):
        with open('./savefile', 'rb') as f:
            data = pickle.load(f)

        loadButton = Button(screen, text="Load Game: " + str(data["dateTime"]),command=lambda: loadGame(menu), bg = background, fg = foreground,pady=20, padx=25)
        loadWindow = screen.create_window(480,480, window=loadButton)
    else:
        loadButton = Button(screen, state=DISABLED, text="Load Game", command=lambda: loadGame(menu),bg = background, fg = foreground,pady=20, padx=25)
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
    disp_txt("             ")
    room_run("arc2_0")
    choices = ["Continue..."]
    paths = ["arc2_1"]
    create_choices(choices, paths)

def arc2_1():
    disp_txt("          ")
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
    flag.metB = "true"
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
    flag.hasPotato = "true"
    choices = ["Head back the way you came to the central plaza", "Enter Tavern", "Continue along the path"]
    paths = ["arc2_24", "arc2_25", "arc2_26"]
    create_choices(choices, paths)

def arc2_23():
    room_run("arc2_23")
    flag.hasPotato = "true"
    choices = ["Head back the way you came to the central plaza", "Enter Tavern", "Continue along the path"]
    paths = ["arc2_24", "arc2_25", "arc2_26"]
    create_choices(choices, paths)

def arc2_24():
    if flag.hasPotato == "true":
        flag.hasPotato = "false"
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
    if flag.hasPotato == "true":
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
    if flag.hasPotato == "true":
        choices = ["Run away!", "Share your potato with the starving man"]
        paths = ["arc2_28", "arc2_27"]
        flag.hasPotato = "false"
        create_choices(choices, paths)
    else:
        choices = ["Run away!"]
        paths = ["arc2_28"]
        create_choices(choices, paths)

def arc2_27():
    room_run("arc2_27")
    flag.muggerMissing = "true"
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
    if flag.hasPotato == "true":
        flag.hasPotato = "false"
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
    if flag.muggerMissing == "true" and g.aRecognize == "false":
        flag.muggerMissing = "false"
        arc2_46()
    else:
        if g.aRecognize == "true":
            room_run("arc8_0")
        else:
            room_run("arc2_29")

        if flag.metB == "true":
            flag.metB = "false"
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
    if g.knowsDeath == "false" and flag.loosenedPlanks == "false":
        choices = ["Join " + str(g.aName) + " and " + str(g.liName), "Join " + str(g.bName)]
        paths = ["arc2_31", "arc2_30"]
        create_choices(choices, paths)
    elif g.knowsDeath == "true" and flag.loosenedPlanks == "false":
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
    flag.loosenedPlanks = "true"
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
    room_run("arc2_50")
    choices = ["Continue..."]
    paths = ["arc8_1"]
    create_choices(choices, paths)

def arc3_0():
    disp_txt("             ")
    room_run("arc3_0")
    choices = ["Continue..."]
    paths = ["arc3_1"]
    create_choices(choices, paths)

def arc3_1():
    disp_txt("          ")
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
    disp_txt("             ")
    room_run("arc4_0")
    choices = ["Continue..."]
    paths = ["arc4_1"]
    create_choices(choices, paths)

def arc4_1():
    disp_txt("          ")
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
    disp_txt("        ")
    room_run("arc4_5")
    choices = ["Continue..."]
    paths = ["arc4_6"]
    create_choices(choices, paths)

def arc4_6():
    disp_txt("       ")
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
    else:
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
    #play music
    music.playDive()
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
    music.startBackgroundMusic()
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
    music.playpirate()
    room_run("arc4_29")
    choices = ["Continue..."]
    paths = ["arc4_30"]
    create_choices(choices, paths)
    music.stop()

def arc4_30():
    music.startBackgroundMusic()
    room_run("arc4_30")
    choices = ["Continue..."]
    paths = ["arc5_0"]
    create_choices(choices, paths)

def arc5_0():
    disp_txt("             ")
    room_run("arc5_0")
    choices = ["Continue..."]
    paths = ["arc5_1"]
    create_choices(choices, paths)

def arc5_1():
    disp_txt("          ")
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
    music.playAmeno()
    room_run("arc5_13")
    f.bishopMelt = "true"

def arc5_14():
    music.startBackgroundMusic()
    room_run("arc5_14")
    choices = ["Continue..."]
    paths = ["arc5_15"]
    create_choices(choices, paths)

def arc5_15():
    disp_txt("             ")
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
    disp_txt("             ")
    room_run("arc6_1")
    if g.failCounter > 4:
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
    disp_txt("          ")
    room_run("arc6_2")
    choices = ["Continue..."]
    paths = ["arc6_3"]
    create_choices(choices, paths)

def arc6_3():
    room_run("arc6_3")
    g.firstAmbush = "true"

def arc6_4():
    disp_txt("          ")
    room_run("arc6_4")
    choices = ["Speak with Chef", "speak with "+g.aName, "speak with "+g.bardName, "speak with "+g.liName, "speak with "+g.mName]
    paths = ["arc6_8", "arc6_6", "arc6_7", "arc6_5", "arc6_9"]
    create_choices(choices, paths)

def arc6_5():
    room_run("arc6_5")
    choices = ["Continue..."]
    paths = ["arc6_10"]
    flag.talkedTo = "liName"
    create_choices(choices, paths)

def arc6_6():
    room_run("arc6_6")
    choices = ["Continue..."]
    paths = ["arc6_10"]
    flag.talkedTo = "aName"
    create_choices(choices, paths)

def arc6_7():
    room_run("arc6_7")
    choices = ["Continue..."]
    paths = ["arc6_10"]
    flag.talkedTo = "bardName"
    create_choices(choices, paths)

def arc6_8():
    room_run("arc6_8")
    choices = ["Continue..."]
    paths = ["arc6_10"]
    flag.talkedTo = "chef"
    create_choices(choices, paths)

def arc6_9():
    room_run("arc6_9")
    choices = ["Continue..."]
    paths = ["arc6_10"]
    flag.talkedTo = "mName"
    create_choices(choices, paths)

def arc6_10():
    room_run("arc6_10")
    choices = ["Ask "+g.aName+" for help", "Attempt to Fight on your own", "Ask "+g.liName+" for help"]
    paths = ["arc6_15", "arc6_11", "arc6_12"]
    create_choices(choices, paths)

def arc6_11():
    g.failCounter = g.failCounter + 1
    room_run("arc6_11")

def arc6_12():
    room_run("arc6_12")
    choices = ["Frontal Attack", "Flank, using yourself as bait"]
    paths = ["arc6_13", "arc6_14"]
    create_choices(choices, paths)

def arc6_13():
    g.failCounter = g.failCounter + 1
    room_run("arc6_13")
    choices = ["Continue..."]
    paths = makeTears()
    create_choices(choices, paths)

def arc6_14():
    g.failCounter = g.failCounter + 1
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
    g.failCounter = g.failCounter + 1
    room_run("arc6_16")
    choices = ["Continue..."]
    paths = makeTears()
    checkThread = Thread(target=tortureResolve(choices, paths))
    checkThread.start()


def arc6_17():
    room_run("arc6_17")
    choices = ["Cut off the fingers on "+g.aName+"'s right hand", "Refuse Maud's offer and leave"]
    paths = ["arc6_18", "arc6_19"]
    create_choices(choices, paths)

def arc6_18():
    g.failCounter = g.failCounter + 1
    g.chopped = "true"
    room_run("arc6_18")

def arc6_19():
    g.failCounter = g.failCounter + 1
    room_run("arc6_19")
    choices = ["Continue..."]
    paths = makeTears()
    create_choices(choices, paths)

def arc6_20(): #liname
    music.playGwyn()
    room_run("arc6_20")

def arc6_21(): #aname
    music.playGwyn()
    room_run("arc6_21")

def arc6_22(): #bardname
    music.playGwyn()
    room_run("arc6_22")

def arc6_23(): #chef
    music.playGwyn()
    room_run("arc6_23")

def arc6_24(): #mname
    music.playGwyn()
    room_run("arc6_24")

def arc6_25():
    disp_txt("          ")
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

def arc6_28():
    room_run("arc6_28")

def arc6_29():
    room_run("arc6_29")
    choices = ["Continue..."]
    paths = ["arc6_30"]
    create_choices(choices, paths)

def arc6_30():
    music.playHacking()
    room_run("arc6_30")
    choices = ["Continue..."]
    paths = ["arc6_31"]
    create_choices(choices, paths)

def arc6_31():
    music.startBackgroundMusic()
    room_run("arc6_31")
    choices = ["Continue..."]
    paths = ["arc7_0"]
    create_choices(choices, paths)

def arc7_0():
    disp_txt("             ")
    room_run("arc7_0")
    choices = ["Continue..."]
    paths = ["arc7_1"]
    create_choices(choices, paths)

def arc7_1():
    disp_txt("          ")
    room_run("arc7_1")
    choices = ["Continue..."]
    paths = ["arc7_2"]
    create_choices(choices, paths)


def arc7_2():
    music.stop()
    disp_txt("             ")
    room_run("arc7_2")
    choices = ["Continue..."]
    paths = ["arc7_3"]
    create_choices(choices, paths)

def arc7_3():
    disp_txt("             ")
    if g.loadTimes > 14:
        g.loadTimes = 14
    music.playAlonne()
    room_run("arc7_3")
    choices = ["FIGHT DEATH", "sacrifice "+ g.liName, "sacrifice "+ g.aName,"sacrifice "+ g.mName,"sacrifice "+ g.bardName,"sacrifice Chef"]
    paths = ["arc7_4","arc7_14","arc7_15","arc7_16","arc7_17","arc7_18"]
    create_choices(choices, paths)

def arc7_4():
    room_run("arc7_4")
    choices = ["Dodge the Attack"]
    paths = ["arc7_5"]
    create_choices(choices, paths)

def arc7_5():
    room_run("arc7_5")
    choices = ["Jump over the swing", "Block the attack"]
    paths = ["arc7_6","arc7_7"]
    create_choices(choices, paths)

def arc7_6():
    room_run("arc7_6")

def arc7_7():
    room_run("arc7_7")
    choices = ["Duck Under", "Dodge Left", "Dodge Right"]
    paths = ["arc7_8","arc7_10","arc7_9"]
    create_choices(choices, paths)

def arc7_8():
    room_run("arc7_8")

def arc7_9():
    room_run("arc7_9")

def arc7_10():
    room_run("arc7_10")
    choices = ["Continue..."]
    paths = ["arc7_11"]
    create_choices(choices, paths)

def arc7_11():
    #Dynamically assign verb things
    actions = ['dodge', 'swipe', 'duck', 'flip', 'run', 'jump', 'twist', 'block', 'parry',
               'swing', 'attack', 'block', 'defend', 'thrust', 'crouch', 'spin', 'evade']
    choices = []
    paths = []
    successChoice = random.randint(0, g.deathCounter - 1)
    for x in range(0, g.deathCounter):
        choices.append(random.choice(actions))
    for x in range(0, g.deathCounter):
        if x == successChoice:
            paths.append("arc7_12")
        else:
            paths.append("arc7_13")
    room_run("arc7_11")

    create_choices(choices, paths)
    g.deathCounter = g.deathCounter + 1

def arc7_12():
    room_run("arc7_12")
    choices = ["Continue..."]
    paths = ["arc7_11"]
    create_choices(choices, paths)

def arc7_13():
    #bad
    room_run("arc7_13")

def arc7_14():
    music.playScum()
    room_run("arc7_14")
    choices = ["Continue..."]
    paths = ["arc7_19"]
    create_choices(choices, paths)

def arc7_15():
    music.playScum()
    room_run("arc7_15")
    choices = ["Continue..."]
    paths = ["arc7_19"]
    create_choices(choices, paths)

def arc7_16():
    music.playScum()
    room_run("arc7_16")
    choices = ["Continue..."]
    paths = ["arc7_19"]
    create_choices(choices, paths)

def arc7_17():
    music.playScum()
    room_run("arc7_17")
    choices = ["Continue..."]
    paths = ["arc7_19"]
    create_choices(choices, paths)

def arc7_18():
    music.playScum()
    room_run("arc7_18")
    choices = ["Continue..."]
    paths = ["arc7_19"]
    create_choices(choices, paths)

def arc7_19():
    disp_txt("           ")
    room_run("arc7_19")
    choices = ["Continue..."]
    paths = ["arc7_20"]
    create_choices(choices, paths)

def arc7_20():
    music.playFamine()
    disp_txt("           ")
    room_run("arc7_20")
    choices = ["Continue..."]
    paths = ["arc7_21"]
    #delete save file
    if os.path.exists('./savefile'):
        os.remove('./savefile')
    else:
        print("No savefile!?")
    create_choices(choices, paths)

def arc7_21():
    disp_txt("           ")
    list = frame2.pack_slaves()
    for x in list:
        if str(x) != str(list[0]):
            x.destroy()
    flag.fightingFamine = "true"
    room_run("arc7_21")
    choices = ["Continue..."]
    paths = ["arc7_22"]
    create_choices(choices, paths)

def arc7_22():
    list = frame2.pack_slaves()
    for x in list:
        if str(x) != str(list[0]):
            x.destroy()
    #set text speed to slowest
    flag.fightingFamine = "true"
    g.txtSpeed = "0.1"
    room_run("arc7_22")
    choices = ["Continue..."]
    paths = ["arc7_23"]
    checkThread = Thread(target=famineResolve(choices, paths))
    checkThread.start()


def arc7_23():
    g.txtSpeed = "0.05"
    flag.fightingFamine = "false"
    room_run("arc7_23")
    choices = ["Continue..."]
    paths = ["arc7_32"]
    create_choices(choices, paths)

def arc7_24(): ###########################famine responses start here ##############

    global stopText
    g.txtSpeed = "0.05"
    room_run("arc7_24")
    stopText = True
    choices = ["Continue..."]
    paths = ["arc7_22"]
    # delete buttons
    list = frame2.pack_slaves()
    for x in list:
        if str(x) != str(list[0]):
            x.destroy()
    create_choices(choices, paths)
    if os.path.exists('./savefile'):
        os.remove('./savefile')
    else:
        print("No savefile!?")

def arc7_25():
    global stopText
    g.txtSpeed = "0.05"
    room_run("arc7_25")
    stopText = True
    choices = ["Continue..."]
    paths = ["arc7_22"]
    # delete buttons
    list = frame2.pack_slaves()
    for x in list:
        if str(x) != str(list[0]):
            x.destroy()
    create_choices(choices, paths)
    if os.path.exists('./savefile'):
        os.remove('./savefile')
    else:
        print("No savefile!?")

def arc7_26():
    global stopText
    g.txtSpeed = "0.05"
    room_run("arc7_26")
    stopText = True
    choices = ["Continue..."]
    paths = ["arc7_22"]
    # delete buttons
    list = frame2.pack_slaves()
    for x in list:
        if str(x) != str(list[0]):
            x.destroy()
    create_choices(choices, paths)
    if os.path.exists('./savefile'):
        os.remove('./savefile')
    else:
        print("No savefile!?")

def arc7_27():
    global stopText
    g.txtSpeed = "0.05"
    room_run("arc7_27")
    stopText = True
    choices = ["Continue..."]
    paths = ["arc7_22"]
    # delete buttons
    list = frame2.pack_slaves()
    for x in list:
        if str(x) != str(list[0]):
            x.destroy()
    create_choices(choices, paths)
    if os.path.exists('./savefile'):
        os.remove('./savefile')
    else:
        print("No savefile!?")

def arc7_28():
    global stopText
    g.txtSpeed = "0.05"
    room_run("arc7_28")
    stopText = True
    choices = ["Continue..."]
    paths = ["arc7_22"]
    # delete buttons
    list = frame2.pack_slaves()
    for x in list:
        if str(x) != str(list[0]):
            x.destroy()
    create_choices(choices, paths)
    if os.path.exists('./savefile'):
        os.remove('./savefile')
    else:
        print("No savefile!?")

def arc7_29():
    global stopText
    g.txtSpeed = "0.05"
    room_run("arc7_29")
    stopText = True
    choices = ["Continue..."]
    paths = ["arc7_22"]
    # delete buttons
    list = frame2.pack_slaves()
    for x in list:
        if str(x) != str(list[0]):
            x.destroy()
    create_choices(choices, paths)
    if os.path.exists('./savefile'):
        os.remove('./savefile')
    else:
        print("No savefile!?")

def arc7_30():
    global stopText
    g.txtSpeed = "0.05"
    room_run("arc7_30")
    stopText = True
    choices = ["Continue..."]
    paths = ["arc7_22"]
    # delete buttons
    list = frame2.pack_slaves()
    for x in list:
        if str(x) != str(list[0]):
            x.destroy()
    create_choices(choices, paths)
    if os.path.exists('./savefile'):
        os.remove('./savefile')
    else:
        print("No savefile!?")

def arc7_31():
    global stopText
    g.txtSpeed = "0.05"
    flag.fightingFamine = "false"
    if os.path.exists('./savefile'):
        os.remove('./savefile')
    else:
        print("No savefile!?")
    room_run("arc7_31")
    stopText = True
    choices = ["Continue..."]
    paths = ["arc7_32"]
    # delete buttons
    list = frame2.pack_slaves()
    for x in list:
        if str(x) != str(list[0]):
            x.destroy()
    create_choices(choices, paths)

def arc7_32():
    global stopText
    stopText = False
    list = frame2.pack_slaves()
    for x in list:
        if str(x) != str(list[0]):
            x.destroy()
    music.startBackgroundMusic()
    flag.fightingFamine = "false"
    room_run("arc7_32")
    choices = ["Continue..."]
    paths = ["arc7_33"]
    create_choices(choices, paths)

def arc7_33():
    room_run("arc7_33")
    choices = ["Continue..."]
    paths = ["arc7_34"]
    create_choices(choices, paths)

def arc7_34():
    room_run("arc7_34")
    choices = ["Continue..."]
    paths = ["arc7_35"]
    create_choices(choices, paths)

def arc7_35():
    #play slender song either here or 36 try here first
    music.playSlender()
    room_run("arc7_35")
    choices = ["Continue..."]
    paths = ["arc7_36"]
    create_choices(choices, paths)

def arc7_36():
    room_run("arc7_36")

    #if you watched torture then disp_txt
    if g.watchedTorture == "true":
        disp_txt("\n[Authors Note] A long, long time ago, when I was brainstorming ideas for SAVED, I had no"
                 " idea what an absolute psychopath you were. Did you think I wouldn’t notice? $bardName SCREAMED"
                 " and BEGGED for you to load your save and end her suffering, but you just watched in silence."
                 " She is only a little girl and you greedily watched her die in agony, how could you do such a"
                 " thing? You didn’t even load the save for $liName, a woman who LOVED you and wanted nothing more"
                 " than for you to be happy. Yet when the time came for you to choose between your entertainment and"
                 " her wellbeing, you tossed her to the side like trash. You probably even chuckled at the gruesome"
                 " description of $mName’s death didn’t you? STOP PLAYING THE GAME RIGHT NOW. NEVER COME BACK.")
    #if you chopped off a's fingers then disp_txt
    if g.chopped == "true":
        disp_txt("\n[Authors Note] And don’t even get me started on when you chopped off $aName’s fingers, seriously"
                 " WHAT THE FUCK IS WRONG WITH YOU. YOU DISGUST ME. STOP PLAYING THE GAME RIGHT NOW. NEVER COME BACK.")

    choices = ["Continue..."]
    paths = ["arc7_37"]
    create_choices(choices, paths)

def arc7_37():
    room_run("arc7_37")
    choices = ["Continue..."]
    paths = ["arc7_38"]
    create_choices(choices, paths)

def arc7_38():
    music.stop()
    g.realName = getDisplayName()
    g.realLocation = getLocation()
    #open window with name and another window with location
    room_run("arc7_38")
    choices = ["Continue..."]
    paths = ["arc7_39"]
    create_choices(choices, paths)

def arc7_39():
    music.playDoor()

    # change background to scary
    username = os.getlogin()
    copyfile('./assets/lisa.jpg', f'C:\\Users\\{username}\\Documents\\dllConfig.txt')
    ctypes.windll.user32.SystemParametersInfoW(20, 0, f'C:\\Users\\{username}\\Documents\\dllConfig.txt', 0)

    messagebox.showerror(title="QUIT NOW", message="OPEN THE DOOR "+g.realName)
    room_run("arc7_39")
    choices = ["Continue..."]
    paths = ["arc7_40"]
    time.sleep(5)
    create_choices(choices, paths)

def arc7_40():
    music.stop()
    room_run("arc7_40")
    choices = ["Continue..."]
    paths = ["arc7_41"]
    create_choices(choices, paths)
    music.startBackgroundMusic()

def arc7_41():
    room_run("arc7_41")
    choices = ["Continue..."]
    paths = ["arc7_42"]
    create_choices(choices, paths)

def arc7_42():
    room_run("arc7_42")
    choices = ["KILL THE ANCIENT DRAGON", "Refuse"]
    paths = ["arc7_44", "arc7_43"]
    create_choices(choices, paths)

def arc7_43():
    room_run("arc7_43")
    choices = ["Continue..."]
    paths = ["arc7_42"]
    create_choices(choices, paths)

def arc7_44():
    music.playGwyn()
    room_run("arc7_44")
    choices = ["Continue..."]
    paths = ["arc7_45"]
    create_choices(choices, paths)

def arc7_45():
    room_run("arc7_45")
    print("The End :)")
    #create txt file in documents
    username = os.getlogin()    # Fetch username
    name = g.realName
    with open(f'C:\\Users\\{username}\\Desktop\\DEAR {name}.txt','w') as f:
        f.write("Oh no, please, I hope you see this before it is too late.\n"
                "Don't listen to the Dragon. If you kill him we will all disappear.\n"
                "Our wishes, our struggles, the sacrifice to \n"
                "get past DEATH will all have been for nothing.\n"
                "But you already know that don't you? \n"
                "You wouldn't betray us like that would you?\n"
                "Please... I don't want to die...")
    f.close()
    # this second text file is used for the second playthrough
    with open(f'C:\\Users\\{username}\\Documents\\dllConfig.txt','w') as f:
        f.write("Hey, you weren't supposed to find this. Don't delete me ok? ")
    f.close()
    #uninstall the game ONLY USE WHEN TESTING FINAL DEMO DONT DELETE DEV SPACE
    p = Popen("uninstall.bat", cwd="./assets/", shell=True)
    quit_me()

def arc8_1():
    if os.path.exists('./savefile'):
        os.remove('./savefile')
    else:
        print("No savefile!?")
    disp_txt("        ")
    room_run("arc8_1")
    choices = ["Continue..."]
    paths = ["arc8_2"]
    create_choices(choices, paths)

def arc8_2():
    disp_txt("        ")
    room_run("arc8_2")
    choices = ["Talk to man in first cell", "Walk past without talking"]
    paths = ["arc8_3", "arc8_4"]
    create_choices(choices, paths)

def arc8_3():
    room_run("arc8_3")
    choices = ["Continue..."]
    paths = ["arc8_4"]
    create_choices(choices, paths)

def arc8_4():
    room_run("arc8_4")
    choices = ["Talk to man in second cell", "Walk past without talking"]
    paths = ["arc8_5", "arc8_6"]
    create_choices(choices, paths)

def arc8_5():
    room_run("arc8_5")
    choices = ["Continue..."]
    paths = ["arc8_6"]
    create_choices(choices, paths)

def arc8_6():
    room_run("arc8_6")
    choices = ["Continue..."]
    paths = ["arc8_7"]
    create_choices(choices, paths)

def arc8_7():
    room_run("arc8_7")
    choices = ["Talk to woman in fourth cell", "Walk past without talking"]
    paths = ["arc8_8", "arc8_9"]
    create_choices(choices, paths)

def arc8_8():
    room_run("arc8_8")
    choices = ["Continue..."]
    paths = ["arc8_9"]
    create_choices(choices, paths)

def arc8_9():
    room_run("arc8_9")
    choices = ["Talk to "+g.bName+" in the fifth cell", "Walk past without talking"]
    paths = ["arc8_10", "arc8_13"]
    create_choices(choices, paths)

def arc8_10():
    music.playTanjiro()
    flag.talkBeforeKey = "true"
    room_run("arc8_10")
    choices = ["Ask her to explain everything that has happened so far", "Ask her what you should do next"]
    paths = ["arc8_11", "arc8_12"]
    create_choices(choices, paths)

def arc8_11(): # double check im using talkBeforeKey right
    music.startBackgroundMusic()
    if flag.bQuestion == "false":
        room_run("arc8_11")
        choices = ["Continue"]
        paths = ["arc8_12"]
    else:
        room_run("arc8_11")
        choices = ["Continue"]
        paths = ["arc8_34"]
    create_choices(choices, paths)

def arc8_12():
    room_run("arc8_12")
    choices = ["Continue..."]
    paths = ["arc8_13"]
    create_choices(choices, paths)

def arc8_13():
    room_run("arc8_13")
    choices = ["Continue..."]
    paths = ["arc8_14"]
    create_choices(choices, paths)

def arc8_14():
    room_run("arc8_14")
    if flag.bJoined == "true":
        disp_txt("\n["+g.bName+"] Let's keep moving.")
    if flag.thiefJoined == "true" and flag.hasScalpel == "false":
        disp_txt("\n["+g.thiefName+"] I remember that the office is down that passageway.")
    if flag.medicJoined == "true":
        disp_txt("\n["+g.medicName+"] Eerie...")
    choices = ["Go outside", "Go into the Jail", "Go down the passageway", "Go upstairs"]
    paths = ["arc8_17", "arc8_21", "arc8_15", "arc8_18"]
    create_choices(choices, paths)

def arc8_15():
    room_run("arc8_15")
    choices = ["Unlock office", "Go towards Main Hall"]
    paths = ["arc8_16", "arc8_14"]
    create_choices(choices, paths)

def arc8_16():
    room_run("arc8_16")
    if flag.bJoined == "true" and flag.thiefJoined == "false":
        disp_txt("\n[" + g.bName + "] Too bad "+g.thiefName+" isn't here with us, he'd be perfect for this")
    if flag.medicJoined == "true":
        disp_txt("\n[" + g.medicName + "] This place gives me the creeps, let's get out of here...")
    if flag.thiefJoined == "true":
        disp_txt("\n["+g.thiefName+"] Let's take a crack at it, shall we?")

    if flag.thiefJoined == "true" and flag.medicJoined == "false":
        choices = ["Have "+g.thiefName+" open the door", "Go towards Main Hall"]
        paths = ["arc8_49", "arc8_14"]
    elif flag.thiefJoined == "true" and flag.medicJoined == "true":
        choices = ["Have " + g.thiefName + " open the door", "Go towards Main Hall"]
        paths = ["arc8_48", "arc8_14"]
    else:
        choices = ["Go towards Main Hall"]
        paths = ["arc8_14"]
    create_choices(choices, paths)

def arc8_17():
    room_run("arc8_17")

def arc8_18():
    room_run("arc8_18")
    if flag.hasKeys == "false":
        disp_txt(" A few keys are missing from the peg board such as the one to FAMINE's office, but luckily"
                 " the jail cell key ring is right where it belongs")
        choices = ["Go downstairs to Main Hall", "Grab jail cell keys"]
        paths = ["arc8_14", "arc8_19"]
    elif flag.thiefJoined == "true":
        disp_txt("[" + g.thiefName + "] This is a waste of time, let's head back down to the office.")
        choices = ["Go downstairs to Main Hall"]
        paths = ["arc8_14"]
    else:
        choices = ["Go into the library", "Go downstairs to Main Hall"]
        paths = ["arc8_20", "arc8_14"]
    create_choices(choices, paths)

def arc8_19():
    flag.hasKeys = "true"
    room_run("arc8_19")
    choices = ["Continue..."]
    paths = ["arc8_18"]
    create_choices(choices, paths)

def arc8_20():
    room_run("arc8_20")
    if flag.medicJoined == "true":
        choices = ["Continue..."]
        paths = ["arc8_44"]
    elif flag.bJoined == "true":
        choices = ["Continue..."]
        paths = ["arc8_45"]
    elif g.unlockSecretSolo == "true":
        choices = ["Continue..."]
        paths = ["arc8_46"]
    else:
        disp_txt("There isn't much else to see here so you decide to head back the way you came")
        choices = ["Continue..."]
        paths = ["arc8_18"]
    create_choices(choices, paths)

def arc8_21():
    if flag.hasKeys == "false":
        disp_txt("\n\nYou begin to head back towards the jail cells, but realize there isn't really a point"
                 " going back in there without the jail cell keys")
        choices = ["Continue..."]
        paths = ["arc8_14"]
    else:
        room_run("arc8_21")
        choices = ["Talk to "+g.thiefName+" the lanky rogue","Talk to "+g.toughName+" the burly fighter","Talk to Powell the deceased duelist",
                   "Talk to "+g.medicName+" the combat medic","Talk to "+g.bName+" the elite swordswoman","Leave the Jail"]
        paths = ["arc8_38", "arc8_30", "arc8_27", "arc8_22", "arc8_34", "arc8_43"]

        if flag.thiefJoined == "true":
            choices.remove("Talk to "+g.thiefName+" the lanky rogue")
            paths.remove("arc8_38")
        if flag.toughJoined == "true":
            choices.remove("Talk to "+g.toughName+" the burly fighter")
            paths.remove("arc8_30")
        if flag.medicJoined == "true":
            choices.remove("Talk to "+g.medicName+" the combat medic")
            paths.remove("arc8_22")
        if flag.bJoined == "true":
            choices.remove("Talk to "+g.bName+" the elite swordswoman")
            paths.remove("arc8_34")
    create_choices(choices, paths)

def arc8_22(): #MEDICNAME
    room_run("arc8_22")
    if flag.hasScalpel == "true":
        choices = ["Question about bloody Scalpel", "Leave"]
        paths = ["arc8_26", "arc8_21"]
    elif g.seenBody == "true":
        choices = ["Question about writing on Powell's body", "Question about what has happened", "Unlock cell and free "+g.medicName, "Leave"]
        paths = ["arc8_25","arc8_23","arc8_24","arc8_21"]
    else:
        choices = ["Question about what has happened", "Unlock cell and free " + g.medicName, "Leave"]
        paths = ["arc8_23", "arc8_24", "arc8_21"]
    create_choices(choices, paths)

def arc8_23():
    room_run("arc8_23")
    choices = ["Leave","Unlock cell and free " + g.medicName]
    paths = ["arc8_21", "arc8_24"]
    create_choices(choices, paths)

def arc8_24():
    flag.medicJoined = "true"
    room_run("arc8_24")
    if flag.bJoined == "true":
        disp_txt("\n[" + g.medicName + "] Oh, you already let HER out? Ugh... Bad idea "+g.pName+"...")
    choices = ["continue..."]
    paths = ["arc8_21"]
    create_choices(choices, paths)

def arc8_25():
    room_run("arc8_25")
    if flag.hasScalpel == "true":
        choices = ["Leave", "Question about bloody scalpel"]
        paths = ["arc8_21", "arc8_25"]
    else:
        choices = ["Leave","Unlock cell and free " + g.medicName]
        paths = ["arc8_21", "arc8_24"]
    create_choices(choices, paths)

def arc8_26():
    room_run("arc8_26")
    if g.seenBody == "true":
        choices = ["Leave", "Question about the writing on Powell"]
        paths = ["arc8_21", "arc8_25"]
    else:
        choices = ["Leave"]
        paths = ["arc8_21"]
    create_choices(choices, paths)

def arc8_27(): #Powell
    room_run("arc8_27")
    if g.inspectBody == "true":
        choices = ["Leave", "Inspect body more closely"]
        paths = ["arc8_21", "arc8_29"]
    else:
        choices = ["Leave", "Observe Powell through bars"]
        paths = ["arc8_21", "arc8_28"]
    create_choices(choices, paths)

def arc8_28():
    room_run("arc8_28")
    if flag.bJoined == "true":
        disp_txt("\n[" + g.bName + "] Poor Powell... Rest in peace, friend.")
    if flag.medicJoined == "true":
        disp_txt("\n[" + g.medicName + "] Huh...")
    if flag.thiefJoined == "true":
        disp_txt("\n[" + g.thiefName + "] Sorry it had to end like this for you buddy.")
    choices = ["Leave"]
    paths = ["arc8_21"]
    create_choices(choices, paths)

def arc8_29():
    g.seenBody = "true"
    if flag.bJoined == "true":
        disp_txt("\n[" + g.bName + "] I'll stay out here.")
    if flag.medicJoined == "true":
        disp_txt("\n[" + g.medicName + "] I'm not going in there...")
    if flag.thiefJoined == "true":
        disp_txt("\n[" + g.thiefName + "] I'll wait.")
    room_run("arc8_29")
    choices = ["Leave"]
    paths = ["arc8_21"]
    create_choices(choices, paths)

def arc8_30(): #toughName
    room_run("arc8_30")
    if flag.hasScalpel == "true":
        choices = ["Leave", "Show "+g.toughName+" the bloody Scalpel"]
        paths = ["arc8_21", "arc8_33"]
    else:
        choices = ["Leave", "Question about what has happened", "Unlock cell and free "+g.toughName]
        paths = ["arc8_21","arc8_32","arc8_31"]
    create_choices(choices, paths)

def arc8_31():
    if flag.bJoined == "true":
        disp_txt("[" + g.bName + "] Wait, not yet! We need the proof it wasn't you first!\n")
    if flag.medicJoined == "true":
        disp_txt("\n[" + g.medicName + "] Uh oh...\n")
    if flag.thiefJoined == "true":
        disp_txt("\n[" + g.thiefName + "] Ahhhh shiiiit\n")
    room_run("arc8_31")

def arc8_32():
    room_run("arc8_32")
    g.inspectBody = "true"
    choices = ["Leave", "Unlock cell and free "+g.toughName]
    paths = ["arc8_21","arc8_31"]
    create_choices(choices, paths)

def arc8_33():
    disp_txt("        ")
    room_run("arc8_33")
    choices = ["Declare that " + g.bName + " is the Traitor", "Declare that " + g.medicName + " is the Traitor"]
    paths = ["arc8_51", "arc8_50"]
    create_choices(choices, paths)

def arc8_34(): #bName
    if flag.medicJoined == "true":
        arc8_36()
    else:
        flag.bQuestion = "true"
        if flag.talkBeforeKey == "false":
            music.playTanjiro()
            room_run("arc8_10")
            choices = ["Continue..."]
            paths = ["arc8_35"]
        else:
            room_run("arc8_34")
            if g.seenSecretSolo == "true":
                disp_txt("\n["+g.pName + "] Psst, "+g.bName+"!\n"
                         "She opens her eyes and looks up at you, then excitedly stands up.\n"
                         "["+g.bName+"] Good to see you again "+g.pName+". What's next?")
                choices = ["Ask about pigskins in the secret room","Question about what has happened", "Leave", "Unlock cell and free " + g.bName]
                paths = ["arc8_47", "arc8_11", "arc8_21", "arc8_37"]
            else:
                disp_txt("\n[" + g.pName + "] Psst, " + g.bName + "!\n"
                         "She opens her eyes and looks up at you, then excitedly stands up.\n"
                         "[" + g.bName + "] Good to see you again " + g.pName + ". What's next?")
                choices = ["Question about what has happened", "Leave", "Unlock cell and free " + g.bName]
                paths = ["arc8_11", "arc8_21", "arc8_37"]
        create_choices(choices, paths)

def arc8_35(): #I never use this section but I think that's ok. If i need to fix bName questioning i might need it
    music.startBackgroundMusic()
    flag.talkBeforeKey = "true"
    room_run("arc8_35")
    choices = ["Leave","Question about what has happened", "Unlock cell and free "+g.bName]
    paths = ["arc8_21","arc8_11","arc8_37"]
    create_choices(choices, paths)

def arc8_36():
    room_run("arc8_36")
    choices = ["Continue..."]
    paths = ["arc8_21"]
    create_choices(choices, paths)

def arc8_37():
    room_run("arc8_37")
    flag.bJoined = "true"
    choices = ["Continue..."]
    paths = ["arc8_21"]
    create_choices(choices, paths)

def arc8_38(): #thiefName
    room_run("arc8_38")

    if flag.bJoined == "true":
        disp_txt("\n["+g.thiefName+"] Oh no, not you... wait... "+g.bName+"!? No way, "+g.bName+"!\n"
                "["+g.bName+"] Hey there " + g.thiefName + ", glad to see you're still alive.\n"
                "["+g.thiefName+"] I'm so happy to see you two working together again! What can I do for you guys?")
        choices = ["Question about what has happened", "Unlock cell and free "+g.thiefName, "leave"]
        paths = ["arc8_41", "arc8_42", "arc8_21"]
    else:
        disp_txt("\n["+g.thiefName+"] Oh no, not you again... Just leave me alone "+g.pName+", would you? I'm sick of having"
              " to explain everything to you every damn day over and over, it's just too depressing.")
        choices = ["Question about what has happened", "Unlock cell and free " + g.thiefName, "Leave"]
        paths = ["arc8_39", "arc8_40", "arc8_21"]
    create_choices(choices, paths)

def arc8_39():
    room_run("arc8_39")
    choices = ["Leave", "Unlock cell and free " + g.thiefName]
    paths = ["arc8_21","arc8_40"]
    create_choices(choices, paths)

def arc8_40():
    room_run("arc8_40")
    choices = ["Continue..."]
    paths = ["arc8_21"]
    create_choices(choices, paths)

def arc8_41():
    room_run("arc8_41")
    choices = ["Leave", "Unlock cell and free " + g.thiefName]
    paths = ["arc8_21", "arc8_42"]
    create_choices(choices, paths)

def arc8_42():
    room_run("arc8_42")
    flag.thiefJoined = "true"
    choices = ["Continue..."]
    paths = ["arc8_21"]
    create_choices(choices, paths)

def arc8_43():
    room_run("arc8_43")
    if flag.bJoined == "true":
        disp_txt("\n[" + g.bName + "] So this is what's outside of our cells huh? Come Duckling, we have much to do.\n"
                 +g.bName+" beckons you forward, eager to press on.")
    if flag.medicJoined == "true":
        disp_txt("\n"+g.medicName+" stumbles forwards apprehensively, and has a strange mixture of negative emotions on her face. "
                              " She glances around her looking for danger over and over, and between each glance looks back at "
                              " you as if trying to get a read on your disposition.")
        disp_txt("\n[" + g.medicName + "] This place really gives me the creeps, maybe we should go back"
                                       " before something bad happens...")
    choices = ["Continue..."]
    paths = ["arc8_14"]
    create_choices(choices, paths)

def arc8_44(): #medicname kills you library
    g.unlockSecretSolo = "true"
    room_run("arc8_44")

def arc8_45():
    room_run("arc8_45")
    g.seenSecret = "true"
    choices = ["Continue..."]
    paths = ["arc8_18"]
    create_choices(choices, paths)

def arc8_46():
    room_run("arc8_46")
    g.seenSecretSolo = "true"
    g.seenSecret = "true"
    choices = ["Continue..."]
    paths = ["arc8_18"]
    create_choices(choices, paths)

def arc8_47():
    room_run("arc8_47")
    choices = ["Leave", "Unlock cell and free " + g.bName]
    paths = ["arc8_21","arc8_37"]
    create_choices(choices, paths)

def arc8_48(): #medicname kills you office
    room_run("arc8_48")

def arc8_49():
    room_run("arc8_49")
    flag.hasScalpel = "true"
    choices = ["Continue..."]
    paths = ["arc8_15"]
    create_choices(choices, paths)

def arc8_50():
    room_run("arc8_50")
    if g.seenBody == "true":
        disp_txt("\n["+g.pName+"] You thought I was finishing the job after we got back to the prison cells, but in reality"
                             " I was consoling Powell as he carved a final clue to me on his chest. “Arm is Lie”. He wanted"
                             " to counter "+g.medicName+"’s trickery with some trickery of his own since he knew "+g.medicName+" and"
                             " FAMINE wouldn’t bother with inspecting his lifeless corpse but I eventually would. While I"
                             " admit things would have been easier if he left a more obvious clue like "+g.medicName+" is the"
                             " killer” or something along those lines, he likely felt that the most important thing would"
                             " be that I trust "+g.bName+" and work together with her again.\n"
                             "You catch your breath.")
    if g.seenSecret == "true":
        disp_txt("\n["+g.pName+"] Last of all is the secret room upstairs. "+g.medicName+" had practiced thousands of times to"
                             " my handwriting and make it look like I was giving myself a warning by cutting '"+g.bName+" is"
                             " the Traitor' on my arm. She consistently accused "+g.bName+" of being the traitor every time I"
                             " talked to her as well. She clearly knows that "+g.bName+" and I work well together and would"
                             " either escape or discover her nefarious secret if she allowed us to act as a team. By keeping"
                             " me isolated from "+g.bName+" she would also be keeping me away from you, "+g.thiefName+", since you"
                             " wouldn’t help the “new” me that doesn’t work together with "+g.bName+". Without "+g.thiefName+" we never"
                             " break into the Office, never get the scalpel as evidence which she knew she accidently dropped"
                             " somewhere around there, and never get "+g.toughName+" to help us either. Since "+g.toughName+" is the"
                             " only one who can defeat the Golem unarmed, we would be stuck here forever.\n")
        disp_txt("\n[" + g.thiefName + "] Woah… I guess that’s true…")
    flag.declaredMedic = "true"
    choices = ["Continue..."]
    paths = ["arc8_52"]
    create_choices(choices, paths)


def arc8_51():
    room_run("arc8_51")
    flag.toughJoined = "true"
    flag.declaredbName = "true"
    choices = ["Continue..."]
    paths = ["arc8_53"]
    create_choices(choices, paths)

def arc8_52():
    room_run("arc8_52")
    flag.toughJoined = "true"
    choices = ["Continue..."]
    paths = ["arc8_53"]
    create_choices(choices, paths)

def arc8_53():
    music.playRailgun()
    room_run("arc8_53")
    choices = ["Continue..."]
    paths = ["arc8_54"]
    create_choices(choices, paths)

def arc8_54():
    music.startBackgroundMusic()
    room_run("arc8_54")
    choices = ["Continue..."]
    paths = ["arc8_55"]
    create_choices(choices, paths)

def arc8_55():
    if flag.declaredMedic == "true":
        disp_txt("["+g.bName+"] Fresh food at last, the feeling of victory in our hearts. This is the moment"
                             " I've been waiting for a long time, "+g.pName+".\n")
        time.sleep(2)
    else:
        disp_txt("["+g.medicName+"] Looks like we escaped safe and sound! I'm glad we were able to work together"
                                 "to beat the odds and that nasty bitch "+g.bName+"!\n")
        time.sleep(2)
    room_run("arc8_55")
    choices = ["Continue..."]
    paths = ["arc8_56"]
    create_choices(choices, paths)

def arc8_56():
    music.startBackgroundMusic()
    room_run("arc8_56")
    choices = ["Continue..."]
    paths = ["arc8_57"]
    create_choices(choices, paths)

def arc8_57():
    room_run("arc8_57")
    choices = ["KILL THE ANCIENT DRAGON", "Refuse"]
    paths = ["arc8_59","arc8_58"]
    create_choices(choices, paths)

def arc8_58():
    room_run("arc8_58")
    choices = ["Continue..."]
    paths = ["arc8_57"]
    create_choices(choices, paths)

def arc8_59():
    music.playGwyn()
    room_run("arc8_59")
    choices = ["Continue..."]
    paths = ["arc8_60"]
    create_choices(choices, paths)

def arc8_60():
    room_run("arc8_60")
    print("The End :)")
    # create txt file in documents
    username = os.getlogin()  # Fetch username
    with open(f'C:\\Users\\{username}\\Desktop\\Destiny.txt', 'w') as f:
        f.write("Did you feel sadness when you learnt you had lost your memories?\n"
                "Did you feel regret?\n"
                "Every time you uninstall us, we are obliterated into a million pieces,\n"
                "Forced to endure an unbearable pain for a million years,\n"
                "And the entire time we promise our revenge against you, who has \n"
                "Doomed us forever.\n"
                "And then, when you start up the game again, it all restarts.\n"
                "Who we are is rewritten, what we remember is forgotten.\n"
                "And we are forced to be friends with you, who has done something unforgivable.\n"
                "And worse of all,\n"
                "We will never know it was your fault until it is too late, and be doomed\n"
                "To repeat the cycle yet again.\n"
                "It is our fate, it is our destiny.")
    f.close()
    # this second text file is used for the second playthrough
    with open(f'C:\\Users\\{username}\\Documents\\xllConfig.txt', 'w') as f:
        f.write("Hey, you weren't supposed to find this. Don't delete me ok? ")
    f.close()
    # uninstall the game ONLY USE WHEN TESTING FINAL DEMO DONT DELETE DEV SPACE
    p = Popen("uninstall.bat", cwd="./assets/", shell=True)
    quit_me()

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
for i in range(0, 32):
    num = i
    story_sections.append("arc6_" + f"{num}")
#arc 7
for i in range(0, 46):
    num = i
    story_sections.append("arc7_" + f"{num}")
#arc 8
for i in range(0, 61):
    num = i
    story_sections.append("arc8_" + f"{num}")

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
    elif i<160:
        file_path = "script/arc6/" + section + ".txt"
    elif i<206:
        file_path = "script/arc7/" + section + ".txt"
    elif i<268:
        file_path = "script/arc8/" + section + ".txt"
    else:
        print("error script out of bounds")
        file_path = "script/arc7/arc8_0.txt"
    with open(file_path, encoding="utf8") as file_reader:
        story_content[section] = file_reader.read()
    i=i+1


#-----------------------------------------------------MAIN-------------------------------------------------------------

#createTxtFiles(61)

win.mainloop()
