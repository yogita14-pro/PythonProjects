import random
print("Hello! Lets Play Rock Pappers Scissors!")
li=["Rock","Papers","Scissors"]
while True:
    for _ in range(3):
        compchoice=random.choice(li)
        print(f"Enter your choice from {li}: ",end="")
        userchoice=input()
        if compchoice=="Rock":
            if userchoice=="Papers"or userchoice=="papers":
                print("                           Congratulations....You won! :)")
            elif userchoice=="Scissors" or userchoice=="scissors":
                print("                           Computer Won! Better Luck Next Time :)")
            elif userchoice=="Rock" or userchoice=="rock":
                print("                            Draw! Nice :)")
            else:
                print("Please Enter a valid choice")
        elif compchoice=="Papers":
            if userchoice=="Scissors"or userchoice=="scissors":
                print("                             You won! :) Party Party Yeah!! ")
            elif userchoice=="Rock" or userchoice=="rock":
                print("                             Computer Won! Play once more, You will definately win :)")
            elif userchoice=="Papers" or userchoice=="papers":
                print("                              Draw! Awesome :)")
            else:
                print("Please Enter a valid choice")
        elif compchoice=="Scissors":
            if userchoice=="Rock" or userchoice=="rock":
                print("                               You won! :) Like always a legend!")
                # print()
            elif userchoice=="Papers" or userchoice=="papers":
                print("                               Computer Won! Keep Trying...Will rock it :)")
                
            elif userchoice=="Scissors" or userchoice=="scissors":
                print("                               Draw! Good dude :) ")
            else:
                print("Please Enter a valid choice")
        print("Computer Choose", compchoice)
        print()
    print("Do you wanna play more? Yes/No : ", end="")
    ans=input()
    if ans[0]=='N':
        print("Exiting the game....")
        break

