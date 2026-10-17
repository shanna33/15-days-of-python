import random
print("***Welcome to Rock Paper Scissor***")

items=["Rock","Paper","Scissor"]
user_won=0
computer_won=0
ties=0

while True:
    
    play=input("Do you want to play rock-paper-scissor?(Yes/No): ")
    if play.lower()=="no":
        print("Bye . See you again!")
        break
    elif play.lower()!="yes":
        print("Enter either yes or no.")
        continue

    user_choice=(input("Enter your choice( Rock , Paper , Scissor): ")).capitalize()

    if user_choice not in items:
        print("Invalid choice.")
        continue

    computer_choice=random.choice(items)

    print(f"User chose:{user_choice} | Computer chose:{computer_choice}")

    if user_choice==computer_choice:
        ties+=1
        print("Its a Tie! Both chose same.")

    elif user_choice=="Rock":
        if computer_choice=="Paper":
            computer_won+=1
            print("Paper hides rock, Computer won.")
        else:
            user_won+=1
            print("Rock smashes scissor, User won.")

    elif user_choice=="Scissor":
        if computer_choice=="Paper":
            user_won+=1
            print("Scissor cuts paper, User won.")
        else:
            computer_won+=1
            print("Rock smashes scissor, Computer won.")

    elif user_choice=="Paper":
        if computer_choice=="Rock":
            user_won+=1
            print("Paper hides rock, User won.")
        else:
            computer_won+=1
            print("Scissor cuts paper, Computer won.")

    print("Total Computer won: ",computer_won , " times.")
    print("Total User won: ", user_won , " times.")
    print("Tie: ", ties)


