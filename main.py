from tkinter import *
import tkinter as tk
import tkinter.scrolledtext as tkst
import time

#--------------------------------------------------------Globals--------------------------------------------------------

#global values for the speed and size of the text
txtSpeed = 0.05
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
    disp_txt(str(txtSpeed), txtSpeed)

def disp_txt(string, speed):
    for char in string:
        textWindow.insert(tk.INSERT, char)
        textWindow.update()
        time.sleep(speed)
    global txtdone
    txtdone=1

def queue_logic(section, prompt_text,  path_a, path_b, path_c, path_d, path_e):
    clear_screen()
    to_display = replace_variables(story_content[section])
    print(to_display)
    user_input = input(prompt_text)
    if user_input == '1':
        path_a()
    if user_input == '2':
        path_b()
    if user_input == '3':
        if path_c != "null":
            path_c()
        else:
            print("Please select a valid option \n")
            queue_logic(section, prompt_text, path_a, path_b, path_c, path_d, path_e)
    if user_input == '4':
        if path_d != "null":
            path_d()
        else:
            print("Please select a valid option \n")
            queue_logic(section, prompt_text, path_a, path_b, path_c, path_d, path_e)
    if user_input == '5':
        if path_e != "null":
            path_e()
        else:
            print("Please select a valid option \n")
            queue_logic(section, prompt_text, path_a, path_b, path_c, path_d, path_e)
    else:
        print("Please select a valid option \n")
        queue_logic(section, prompt_text,  path_a, path_b, path_c, path_d, path_e)

def replace_variables(string):
    global food
    global pName
    string = string.replace("$food", food)
    string = string.replace("$pName", pName)
    return string


def clear_screen():
    textWindow.delete(1.0, END)
    textWindow.update()

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
    sizeLabel = Label(settings_window, text="Text Size (My Require you resize Window)").grid(row=5, column=1)
    radio4 = Radiobutton(settings_window, text="Small", variable=textSize, value="small").grid(row=6, column=0)
    radio5 = Radiobutton(settings_window, text="Standard", variable=textSize, value="standard").grid(row=6, column=1)
    radio6 = Radiobutton(settings_window, text="Large", variable=textSize, value="large").grid(row=6, column=2)
    finishButton = Button(settings_window, text="Apply Changes", command=lambda: changeSettings(speed.get(), textSize.get()))
    finishButton.grid(row=8, column=1)

def create_choices(number):
    #create buttons for the amount of options available, represtented by 'number'
    if number == 0:
        option0 = Button(frame2, text="Continue...", command=lambda: click_choice(0),bg = "#333333", fg = "#EEEEEE")
        option0.pack(fill='both', expand='yes')
    if number > 0:
        option1 = Button(frame2, text="fillme", command=lambda: click_choice(1),bg = "#333333", fg = "#EEEEEE")
        option1.pack(fill='both', expand='yes')
    if number > 1:
        option2 = Button(frame2, text="fillme", command=lambda: click_choice(2),bg = "#333333", fg = "#EEEEEE")
        option2.pack(fill='both', expand='yes')
    if number > 2:
        option3 = Button(frame2, text="fillme", command=lambda: click_choice(3),bg = "#333333", fg = "#EEEEEE")
        option3.pack(fill='both', expand='yes')
    if number > 3:
        option4 = Button(frame2, text="fillme", command=lambda: click_choice(4),bg = "#333333", fg = "#EEEEEE")
        option4.pack(fill='both', expand='yes')
    if number > 4:
        option5 = Button(frame2, text="fillme", command=lambda: click_choice(5),bg = "#333333", fg = "#EEEEEE")
        option5.pack(fill='both', expand='yes')

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
    clear_screen()
    to_display = replace_variables(story_content["arc1_0"])
    print(to_display)
    input("Press Enter to continue...")
    arc1_1()

def arc1_1():
    queue_logic(section="arc1_1",

                prompt_text=(
                    "\n"
                    "1: Chocolate\n"
                    "2: Potato Chips\n"
                    "3: Neither\n"
                    "\n\n"),

                path_a=arc1_2,
                path_b=arc1_3,
                path_c=arc1_4,
                path_d="null",
                path_e="null")

def arc1_2():
    clear_screen()
    to_display = replace_variables(story_content["arc1_2"])
    print(to_display)
    global food
    food = "chocolate"
    input("Press Enter to continue...")
    arc1_5()

def arc1_3():
    clear_screen()
    to_display = replace_variables(story_content["arc1_3"])
    print(to_display)
    global food
    food = "potato chips"
    input("Press Enter to continue...")
    arc1_5()

def arc1_4():
    clear_screen()
    to_display = replace_variables(story_content["arc1_4"])
    print(to_display)
    global food
    food = "chocolate"
    input("Press Enter to continue...")
    arc1_5()

def arc1_5():
    clear_screen()
    to_display = replace_variables(story_content["arc1_5"])
    print(to_display)

    prompt_text = "\nPlease Enter your Name:\n\n"
    user_input = input(prompt_text)
    if user_input in ("fuck", "bitch", "pussy","", " ", "_", "cunt", "faggot", "fucker",):
        print("[Debbie] That's a really stupid name, try to be more creative.\n")
        arc1_5()
    prompt_text = "\nThis is going to be your name for the rest of the game. Are you sure? \n\n Yes / No\n\n"
    sure = input(prompt_text)
    print(sure)
    if sure.lower() == "no":
        arc1_5()
    if sure.lower() == "yes":
        global pName
        pName = user_input
        arc1_6()
    else:
        print("I don't understand. Let's try again.")
        arc1_5()

def arc1_6():
    clear_screen()
    to_display = replace_variables(story_content["arc1_6"])
    print(to_display)

    input("Press Enter to continue...")
    arc1_7()

def arc1_7():
    clear_screen()
    to_display = replace_variables(story_content["arc1_7"])
    print(to_display)

    input("Press Enter to continue...")
    arc1_1()
#-----------------------------------------------Program Start----------------------------------------------------------

story_sections = []
for i in range(0,8):
    num = i
    story_sections.append("arc1_" + f"{num}")

story_content = {}
for section in story_sections:
    file_path = "script/" + section + ".txt"
    with open(file_path, encoding="utf8") as file_reader:
        story_content[section] = file_reader.read()

#-----------------------------------------------------MAIN-------------------------------------------------------------


stringy = "this is an example used for testing purposes"
create_choices(0)
disp_txt(stringy, txtSpeed)

win.mainloop()