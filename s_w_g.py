import time
import random
list=["s","w","g"]

print("\t\tGame: Snake,Water,Gun")
print("\t\t5 rounds--You vs PC\n")
rounds=1
i=0
pc_point=0
my_point=0
while(i<5):
    pc_choice = random.choice(list)
    print("\ns for snake\nw for water\ng for gun")
    my_choice=input("\nEnter your choice")
    if my_choice=="s":
        if pc_choice=="s":
            print(f"Computer's choice is {pc_choice}\nYour choice is {my_choice}")
            print("Draw!")
            print(f"Your Points: {my_point} & Computer Points: {pc_point}")
        elif pc_choice=="w":
            print(f"Computer's choice is {pc_choice}\nYour choice is {my_choice}")
            print("You Won!")
            my_point+=1
            print(f"Your Points: {my_point} & Computer Points: {pc_point}")
        elif pc_choice=="g":
            print(f"Computer's choice is {pc_choice}\nYour choice is {my_choice}")
            print("Computer Won!")
            pc_point+=1
            print(f"Your Points: {my_point} & Computer Points: {pc_point}")

    elif my_choice=="w":
        if pc_choice=="s":
            print(f"Computer's choice is {pc_choice}\nYour choice is {my_choice}")
            print("Computer Won!")
            pc_point += 1
            print(f"Your Points: {my_point} & Computer Points: {pc_point}")
        elif pc_choice=="w":
            print(f"Computer's choice is {pc_choice}\nYour choice is {my_choice}")
            print("Draw!")
            print(f"Your Points: {my_point} & Computer Points: {pc_point}")
        elif pc_choice=="g":
            print(f"Computer's choice is {pc_choice}\nYour choice is {my_choice}")
            print("You Won!")
            my_point+=1
            print(f"Your Points: {my_point} & Computer Points: {pc_point}")

    elif my_choice=="g":
        if pc_choice=="s":
            print(f"Computer's choice is {pc_choice}\nYour choice is {my_choice}")
            print("You Won!")
            my_point+=1
            print(f"Your Points: {my_point} & Computer Points: {pc_point}")
        elif pc_choice=="w":
            print(f"Computer's choice is {pc_choice}\nYour choice is {my_choice}")
            print("Computer Won!")
            pc_point += 1
            print(f"Your Points: {my_point} & Computer Points: {pc_point}")
        elif pc_choice=="g":
            print(f"Computer's choice is {pc_choice}\nYour choice is {my_choice}")
            print("Draw")
            print(f"Your Points: {my_point} & Computer Points: {pc_point}")
    else:
        print("Invalid Input!!")
        break
    i += 1

    if rounds==5:
        print("\nOkay...Game Over!")
    elif rounds==4:
        print("You have only 1 chance to conquer")
    else:
        print(f"you have {5-rounds} more chances left")
    rounds += 1

if rounds==6:
    print("Lets check the results...")
    time.sleep(3)
    print("Your Points: ",my_point)
    print("Pc's Points: ",pc_point)
    if my_point>pc_point:
        print("You have Won!")
        print("Congratulations")
    elif my_point==pc_point:
        print("Match Tied")
    else:
        print("Pc have won")
        print("Better Luck Next Time")
