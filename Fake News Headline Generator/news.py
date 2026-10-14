import random

subjects=["Salman Khan", "Rammi", "Shah Rukh Khan", "Shanna", "A blue cat"]
actions=["is playing cards", "had chronic diarohea", "is riding buffalo", "is being gay"]
places=["in Goa", "in Nepal", "in dessert", "while sleeping"]

print("-----Fake News Headline Generator-----")
while True:
    
    user_choice=input("Do you want to generate the news headline? ").strip()
    if user_choice.lower()=="no":
        print("Goodbye!")
        break
    elif user_choice.lower()!="yes":
        print("Invalid choice.Enter either Yes or No.")
        continue
    else:
        subject=random.choice(subjects)
        action=random.choice(actions)
        place=random.choice(places)
        print("Generating...")
        print(f"Breaking News: {subject} {action} {place}.")