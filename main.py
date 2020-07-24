import os

story_sections = []

for i in range(0,8):
    num = i
    story_sections.append("arc1_" + f"{num}")

print(story_sections)

story_content = {}
hint = False
for section in story_sections:
    file_path = "script/" + section + ".txt"
    with open(file_path, encoding="utf8") as file_reader:
        story_content[section] = file_reader.read()


#---------------------Globals and Flags---------------------------------------------
food = "null"
pName = "null"
#---------------------------Chapters------------------------------------------------
def queue_start_story():
    clear_screen()
    # Transfer variables to real names here

    print(story_content["arc1_0"])

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
    # Transfer variables to real names here
    print(story_content["arc1_2"])
    global food
    food = "chocolate"
    input("Press Enter to continue...")
    arc1_5()

def arc1_3():
    clear_screen()
    # Transfer variables to real names here
    print(story_content["arc1_3"])
    global food
    food = "potato chips"
    input("Press Enter to continue...")
    arc1_5()

def arc1_4():
    clear_screen()
    # Transfer variables to real names here
    print(story_content["arc1_4"])
    global food
    food = "chocolate"
    input("Press Enter to continue...")
    arc1_5()

def arc1_5():
    clear_screen()
    # Transfer variables to real names here
    print(story_content["arc1_5"])
    prompt_text = "\nPlease Enter your Name:\n\n"
    user_input = input(prompt_text)
    print(user_input)
    prompt_text = "\nThis is going to be your name for the rest of the game. Are you sure? \n\n Yes / No\n\n"
    sure = input(prompt_text)
    print(sure)
    if sure.lower() == "no":
        arc1_5()
    if sure.lower() == "yes":
        global pName
        pName = user_input
        print("done!")
        print(food)
        print(pName)
        arc1_6()
    else:
        print("I don't understand. Let's try again.")
        arc1_5()

def arc1_6():
    clear_screen()
    # Transfer variables to real names here
    print(story_content["arc1_6"])

    input("Press Enter to continue...")
    arc1_7()

def arc1_7():
    clear_screen()
    # Transfer variables to real names here
    print(story_content["arc1_7"])

    input("Press Enter to continue...")
    arc1_1()


#----------------------Logic----------------------------------------------------

def queue_logic(section, prompt_text,  path_a, path_b, path_c, path_d, path_e):
    clear_screen()
    # Transfer variables to real names here
    print(story_content[section])
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



def clear_screen():
    clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')
    clear()

def main():
    queue_start_story()


if __name__ == '__main__':
    main()