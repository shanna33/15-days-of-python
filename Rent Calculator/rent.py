#room_rent , food , electricity unit , each unit ko cost , divison_person

print("-----RENT CALCULATOR------")

while True:
    choice=input("Do you want to calculate ?(Yes/No): ")
    if choice.lower()=="no":
        break
    if choice.lower()!="yes":
        print("Invalid input. Enter Yes / No. ")
        continue

    try:
        room_rent=int(input("Enter the room rent: "))
        food_cost=int(input("Enter the money spent on food: "))
        electricity_unit=int(input("Enter the electricity unit u consumed: "))
        charge_per_unit=int(input("Enter the each unit price: "))
        number_of_people=int(input("Enter the number of people you want to divide the cost: "))

        total_rent=(room_rent + food_cost + electricity_unit*charge_per_unit )// number_of_people
    except ValueError:
        print("Tnvalid input. Enter a number.")

    except ZeroDivisionError:
        print("Number of people cannot be zero.")

    else:
        print(f"One person should pay {total_rent} this month.")

    




