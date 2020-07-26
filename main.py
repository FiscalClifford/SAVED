from tkinter import *
import tkinter as tk
import tkinter.scrolledtext as tkst
import time

#--------------------------------------------------------Globals--------------------------------------------------------

#input parsing
badInput = ["fuck", "bitch", "pussy", "", " ", "  ", "_", "cunt", "faggot", "fucker", "dick", "penis", "!", ".", "$"]
inputResponse = "null"
#global values for the speed and size of the text
txtSpeed = 0.01
txtSize = 16

food = "null"
pName = "null"

#!!!Flags!!!
txtdone = 0
#-------------------------------------------------------Functions-------------------------------------------------------
def loadGame():
    return

def saveGame():
    return

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

    print("click choice " + str(choice))
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
    to_display = replace_variables(story_content[section])
    disp_txt(to_display)

def replace_variables(string):
    global food
    global pName
    string = string.replace("$food", food)
    string = string.replace("$pName", pName)
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
    pWindow.iconbitmap('./treelarge_CKX_icon.ico')
    pWindow.geometry("400x80")
    pWindow.resizable(False, False)
    pWindow.config(bg = "#333333")

    entryField = Entry(pWindow, width=300, fg = "#333333", bg = "#EEEEEE", font=("Calibri", 20))
    entryField.pack(fill="x")
    send = Button(pWindow, text="Send", command=lambda: acceptEntry(entryField.get(), pWindow), bg = "#333333", fg = "#EEEEEE")
    send.pack(side=TOP)
    win.wait_window(pWindow)


#--------------------------------------------------------GUI------------------------------------------------------------
def settingsconfig():
    #creating settings window
    settings_window = Toplevel()
    settings_window.title("Settings Configuration")
    settings_window.iconbitmap('./treelarge_CKX_icon.ico')
    settings_window.geometry("360x200")
    settings_window.resizable(False, False)

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
    #menu
    loadButton = Button(settings_window, text="Load Game + load info", command=loadGame).grid(row=1, column=1)
    saveButton = Button(settings_window, text="Save Game", command=saveGame).grid(row=2, column=1)
    speedLabel = Label(settings_window, text="Text Scroll Speed").grid(row=3, column=1)
    radio1 = Radiobutton(settings_window, text="Slow", variable=speed, value="slow").grid(row=4, column=0)
    radio2 = Radiobutton(settings_window, text="Standard", variable=speed, value="standard").grid(row=4, column=1)
    radio3 = Radiobutton(settings_window, text="Fast", variable=speed, value="fast").grid(row=4, column=2)
    sizeLabel = Label(settings_window, text="Text Size (May require you resize Window)").grid(row=5, column=1)
    radio4 = Radiobutton(settings_window, text="Small", variable=textSize, value="small").grid(row=6, column=0)
    radio5 = Radiobutton(settings_window, text="Standard", variable=textSize, value="standard").grid(row=6, column=1)
    radio6 = Radiobutton(settings_window, text="Large", variable=textSize, value="large").grid(row=6, column=2)
    finishButton = Button(settings_window, text="Apply Changes", command=lambda: changeSettings(speed.get(), textSize.get()))
    finishButton.grid(row=8, column=1)

def create_choices(choiceList, pathList):
    #create buttons for the amount of options available, represtented by 'number'
    for i in range(0, len(choiceList)):
        button = Button(frame2, text=choiceList[i], command=lambda i=i: click_choice(pathList[i]), bg="#333333", fg="#EEEEEE")
        button.pack(fill='both', expand='yes')


#build main GUI
win = tk.Tk()
win.geometry("600x800")
win.title("testing")
win.iconbitmap('./treelarge_CKX_icon.ico')
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

#----------------------------------------------Story Sections----------------------------------------------------------
def queue_start_story():
    room_run("arc1_0")
    choices = ["Continue..."]
    paths = ["arc1_1"]
    create_choices(choices, paths)


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

    input("Press Enter to continue...")
    arc1_1()
#-----------------------------------------------Program Start----------------------------------------------------------

story_sections = []
for i in range(0, 8):
    num = i
    story_sections.append("arc1_" + f"{num}")

story_content = {}
for section in story_sections:
    file_path = "script/" + section + ".txt"
    with open(file_path, encoding="utf8") as file_reader:
        story_content[section] = file_reader.read()

#-----------------------------------------------------MAIN-------------------------------------------------------------


queue_start_story()

win.mainloop()