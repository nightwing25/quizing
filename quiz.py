import os
import curses

#print all quiz titles in directory in alpha order
full_menu = []
#count = 0
all_files = os.listdir('lessons')
all_files.sort()
for i in all_files:
    if "__init__.py" in i:
        continue
    if ".py" in i:
        if "quiz.py" in i:
            continue
        #print(f"{count}.){i}")
        #count += 1
        full_menu.append(i)
    else:
        pass

#SYSTEM COMPATABILTIY
def clear_sys():
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')


#MENU SETUP
def print_menu(stdscr,selected_row_idx):
    stdscr.clear()#clear the screen each call
    h,w = stdscr.getmaxyx()#get height and width of screen

    for idx, row in enumerate(full_menu):
        x = w//2 - len(row)//2 #pos will be middle of screen
        y = h//2 - len(full_menu)//2 + idx #adds text below eaxh other
        if idx == selected_row_idx:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(y, x, row) #display conetnts of menu going down height in middle
            stdscr.attroff(curses.color_pair(1))
        else:
            stdscr.addstr(y, x, row)

    stdscr.refresh()#refresh screen out of each loop to simulate new contents

x = []
def main(stdscr):
    stdscr.border()
    curses.curs_set(0)#deactivates the blinking cursor
    curses.init_pair(1,curses.COLOR_BLACK, curses.COLOR_WHITE)#create a color pair to use later
    current_row_idx = 0 #create index for the print menu funct
    
    print_menu(stdscr, current_row_idx)
    while 1:#navigation
        key = stdscr.getch()
        stdscr.clear()#clear screen every key press
        if key == curses.KEY_UP and current_row_idx > 0:
            current_row_idx -= 1
        if key == curses.KEY_DOWN and current_row_idx < len(full_menu) -1:
            current_row_idx += 1
        if key == curses.KEY_ENTER or key in [10,13]:
            stdscr.addstr(0,0, f"you pressed {full_menu[current_row_idx]}")
            x.append(f"{full_menu[current_row_idx]}")
            stdscr.refresh()
            stdscr.getch()
            break
            #if current_row_idx == len(full_menu) - 1:
             #   break
        print_menu(stdscr, current_row_idx)
        stdscr.refresh()
curses.wrapper(main)

#START QUIZ SECTION
while True:
    score  = 0
    guesses = []
    ques_num = 0
    wrong = [] 
    count = 2

    if x[0] == "cables_part1.py":
        print("now starting raids lesson")
        from lessons.cables_part1 import *
        clear_sys()
    elif x[0] == "clouds.py":
        from lessons.clouds import *
        clear_sys()
    elif x[0] == "mon_screens.py":
        from lessons.mon_screens import *
        clear_sys()
    elif x[0] == "ports.py":
        from lessons.ports import *
        clear_sys()
    elif x[0] == "printstuff.py":
        from lessons.printstuff import *
        clear_sys()
    elif x[0] == "raids_cpu.py":
        from lessons.raids_cpu import *
        clear_sys()
    elif x[0] == "servings.py":
        from lessons.servings import *
        clear_sys()
    elif x[0] == "trouble.py":
        from lessons.trouble import *
        clear_sys()
    elif x[0] == "virtualization.py":
        from lessons.virtualization import *
        clear_sys()
    elif x[0] == "wireless.py":
        from lessons.wireless import *
        clear_sys()
    elif x[0] == "":
        break
    else:
        pass

    for question in questions:#display one question and 4 answers choices
        #print("---"*10)
        print(f"{count -1}.){question}")
        print("")
        for option in options[ques_num]:
            print(option)
        count+=1

        choice = input("choose answer between a,b,c,or d:").lower()
        guesses.append(choice)
        if choice == answers[ques_num]:#if my choice = to whats in that index
            score += 1
            print("correct")
        else:
            print("incorrect")
            print(f"{answers[ques_num]} is the correct answer")
            wrong.append(question)

        ques_num += 1
        clear_sys()

    print("----"*6)
    print("RESULTS")
    print("----"*6)

    print("answer:",end="")
    for answer in answers:
        print(answer,end="")
    print()
    print("guesses:",end="")
    for guess in guesses:
        print(guess,end="")
    print()

    score = int(score / len(questions) * 100)

    print(f"your score is :{score}%")

    if len(wrong) > 0:
        print("QUESTIONS YOU GOT WRONG!!")
        print("----"*8)
        for i in wrong:
            
            print(f"{count}.){i}")
            count += 1
        print("----"*8)
    new_game = input("would you like to continue?(y/n):")
    if new_game == "y":
        del(guesses)
        del(wrong)
        guesses = []
        wrong = []
        clear_sys()

    else:
        clear_sys()
        print("good bye..")
        #break
        x.pop()
        curses.wrapper(main)
