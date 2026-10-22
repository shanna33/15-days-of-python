import random
easy=["bird" , "table" , "tiger" , "book"]
medium=["tablet" , "happy" , "blanket", "switch"]
hard=["computer" , "airplane" , "octopus" , "laptop"]
name=input("Enter your name: ")


print(f"Hello {name}, Welcome to Password Guesser")

while True:
    playing_choice=input("Do you want to play(y/n)? ")
    if playing_choice.lower()=="n":
        print("Exiting.......")    
        break
   
    elif playing_choice.lower()=="y":
        guess=0
        user_choice=input("Enter your choice : easy , medium , hard: ").strip().lower()
        if user_choice=="easy":
            secret=random.choice(easy)
        elif user_choice=="medium":
            secret=random.choice(medium)
        elif user_choice=="hard":
            secret=random.choice(hard)
        else:
            print("Invalid choice. Default level: Easy")
            secret=random.choice(easy)

        while True:
            user_guess=input("Enter your guess: ")
            guess+=1
            if guess>=10:
                print(f"Many attempts occured.\nWord:{secret}")
                break
                
            if user_guess==secret:
                print("Correct!")
                print(f"Total attempt: {guess}")
                break
            else:
                for i in range(len(secret)):
                    if i<len(user_guess) and user_guess[i]==secret[i]:
                        hint=secret[i]
                    else:
                        hint="_ "
                    print(hint,end="")
                print()
            print(f"Total attempt: {guess}")
            
    else:
        print("Enter either y/n.")
        continue

    