import random
user_win=0
computer_win=0

options=["rock","paper","scissor"]


while True:
        print("Rock/Paper/Scissor or q to quit")
        choose=input(("Choose one: ")).lower()
        
        if choose=="q":
             print("Your Final points",user_win)    
             print("Computer Final points",computer_win)   
             break
        if choose not in options:
            continue
        
        random_num=random.randint(0,2)
        computer_pick=options[random_num]
        print("computer picked "+computer_pick)
                    
        if choose=="rock" and computer_pick=="scissor":
            print("You won!!")
            user_win+=1
        elif choose=="paper" and computer_pick=="rock":
            print("You won!!")
            user_win+=1
        elif choose=="scissor" and computer_pick=="paper":
            print("You won!!")
            user_win+=1
        elif choose=="rock" and computer_pick=="rock"  :
            print("Both choose same")  
        elif choose=="paper" and computer_pick=="paper"  :
            print("Both choose same")  
        elif choose=="scissor" and computer_pick=="scissor"  :
            print("Both choose same")  
        else:
            print("You Lost")
            computer_win+=1
        print("You won",user_win,"times")    
        print("Computer won",computer_win,"times")    
                
                       