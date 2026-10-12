import random

range=int(input("Enter the range you want to guess: "))

random_number=random.randint(0,range)
guess=0
while True:
    user_choice=int(input("Enter your guess: "))
    if user_choice<0 or user_choice>range:
        print("Out of range.")
        continue
    else:
        guess+=1
        if user_choice==random_number:
            print("You got it in " , guess , " guesses!")
            break
        elif user_choice<random_number:
            print("Incorrect!\nYou are below the correct number.")
        elif user_choice>random_number:
            print("Incorrect!\nYou are above the correct number.")

    
        