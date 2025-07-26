# Rock Paper Scissor
'''
0 ROCK
-1  PAPAER
1 SCISSOR

'''
import random     #random cant be used without import
computer = random.choice([-1,0,1])   #computer choosing random choice
youStr = input("enter your choice:")
youDict={"R" : 0 , "P" : -1 , "S" : 1}
reverseDict={0 : "Rock" , -1 : "Papar" , 1 : "Scissor"}

you = youDict[youStr]  #important step

print(f"You chose {reverseDict[you]} \nComputer chose {reverseDict[computer]}") #presentable

if(computer == you):
    print("This round DRAW !")
else:
    if(computer==-1 and you==0):  #(computer - you) == -1
        print("You LOSE !")
    elif(computer==-1 and you==1):  #(computer - you) == -2
        print("You WON !")
    elif(computer==0 and you==1):  #(computer - you) == -1
        print("You LOSE !")
    elif(computer==0 and you==-1):  #(computer - you) == 1
        print("You WON !") 
    elif(computer==1 and you==0):  #(computer - you) == 1
        print("You WON !")
    elif(computer==1 and you==-1): #(computer - you) == 2
        print("You LOSE!")
    else:
        print("Something went Wrong...")

    # line 21 to line 34 in 4 lines (short-cut) :
    '''if((computer - you) == -1 or (computer - you) ==2):
        print("Lose !")
    else:
        print("WON !")'''
