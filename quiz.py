import os
#from raids_cpu import *
#from mon_screens import *
#from cables_part1 import *
#from printstuff.py import *
#from clouds import *
#from virtualization import *  

"""
OBJECTIVE:
    
    x) list dir and put the lessons from dir in a list 

    x) then get user input to grab index of module anad import 
    by indexing.
    x) put the list in order so when the user pick a number its indexed properly

    x) after display what the user got wrong make a list for the actual letter and problem they got wrong
"""

#print all quiz titles in directory in alpha order
def lessons():
    count = 0
    all_files = os.listdir('lessons')
    all_files.sort()
    for i in all_files:
        if ".py" in i:
            if "quiz.py" in i:
                continue
            print(f"{count}.){i}")
            count += 1
        else:
            pass
    print("----"*8)


while True:
    pos_ans = ["a","b","c","d"]
    score  = 0
    guesses = []
    ques_num = 0
    wrong = []
    count = 2
    lessons()
    x = int(input("choose a number to start lesson:"))
    if x == 0:
        print("now starting raids lesson")
        from lessons.cables_part1 import *
        os.system("clear")
    elif x == 1:
        from lessons.clouds import *
        os.system("clear")
    elif x == 2:
        from lessons.mon_screens import *
        os.system("clear")
    elif x == 3:
        from lessons.ports import *
        os.system("clear")
    elif x == 4:
        from lessons.printstuff import *
        os.system("clear")
    elif x == 5:
        from lessons.raids_cpu import *
        os.system("clear")
    elif x == 6:
        from lessons.trouble import *
        os.system("clear")
    elif x == 7:
        from lessons.virtualization import *
        os.system("clear")
    elif x == "":
        break
    else:
        print("not a real entry")

    
    for question in questions:#display one question and 4 answers choices
        #print("---"*10)
        print(f"{count}.){question}")
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
        os.system("clear")


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
        os.system("clear")
    else:
        os.system("clear")
        print("good bye..")
        break
