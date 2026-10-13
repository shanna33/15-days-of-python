print("Welcome to the quiz!")
choice=input("Do you want to play the game?{yes/no}: ")
count=0
if choice.lower()=="no":
    quit()
elif choice.lower() != "yes":
    print("Invalid input.")
else:
    answer=input("What does CPU stands for? ")
    if answer.lower()=="central processing unit":
        count+=1
        print("Correct!")
    else:
        print("Incoorect.")

    answer=input("What does GPU stands for? ")
    if answer.lower()=="graphics processing unit":
        count+=1      
        print("Correct!")
    else:
        print("Incoorect.")

    print(f"You answered {count} questions correctly.")
    print(f"Your result is {(count//2) * 100 }%.")

    