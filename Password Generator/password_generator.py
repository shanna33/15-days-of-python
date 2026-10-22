import os
import random
import string

PASSWORD_FILE=os.path.join(os.path.dirname(os.path.abspath(__file__)), "password.txt")

def show_password():
    try:
        with open(PASSWORD_FILE,"r") as file:
            data=file.read()                
    except FileNotFoundError:
        print("No such file exists.")
    else:
        if not data:
            print("No data Found.")
        else:
            print(data)

def save_password():
    with open(PASSWORD_FILE,"a") as file:
        file.write(f"{username}:{pwd}\n")

while True:

    print("\n-----Welcome to Password Generator-----")
    print("""
    What do you want to do?
    1. Save password
    2. View passwords
    3. Generate password
    4. Exit
    """)

    user_choice=input("Enter your choice: ")

    if user_choice=="1":
        username=input("Enter the website name: ")
        pwd=input("Enter the password: ")

        save_password()
        print("Password saved.")

    elif user_choice=="2":
        show_password()

    elif user_choice=="3":
        random_pwd= string.ascii_letters + string.digits + string.ascii_uppercase + "!@#$"
        generated_pwd= "".join(random.choice(random_pwd) for _ in range(8))

        print(f"Generated password:{generated_pwd}")

    elif user_choice=="4":
        print("Exiting.....")
        break

    else:
        print("Invalid request.")
        continue

