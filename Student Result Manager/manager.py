students={}

while True:
    print("\n-----Student Result Manager-----")
    print("""
            1. Add Student
            2. View Students
            3. View Result
            4. Exit    
                """)
    user_choice=input("Enter your choice: ")

    if user_choice=="1":
        name=input("Enter student name: ")
        marks=int(input("Enter the mark: "))

        students[name]=marks
        print(f"{name} added successfully.")

    elif user_choice=="2":
        if not students:
            print("No data found.")
        else:
            for name,marks in students.items():
                print(name.capitalize() , ":" , marks)

    elif user_choice=="3":
        name=input("Enter the name of student: ").strip().lower()

        if name in students:
            marks=students[name]
            if marks<40:
                print("Fail")
            else:
                print("Pass")
        else:
            print("No student found.")

    elif user_choice=="4":
        print("Exiting....")
        break
