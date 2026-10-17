HISTORY_FILE="historyy.txt"

def save_history(equation,result):
    file=open(HISTORY_FILE,"a")
    file.write(f"{equation} ={result}\n")

def show_history():
    file=open(HISTORY_FILE,"r")
    data=file.read()
    if len(data)==0:
        print("No history found.")
        return
    print(data)

def clear_history():
    file=open(HISTORY_FILE,"w")
    file.write("")
    print("History cleared.")
    

def calculate(user_input):
    parts=user_input.split()
    if len(parts)!=3:
        print("You got something wrong. Enter again.")
        return
    num1=float(parts[0])
    op=parts[1]
    num2=float(parts[2])

    if op=="+":
        result=num1 + num2
    if op=="-":
        result=num1-num2
    if op=="*":
        result=num1 * num2 
    if op=="/":
        if num2==0:
            print("Cant divide by zero.")
            return
        result=num1/num2

    num1=int(num1)
    num2=int(num2)
    if int(result)==result:
        result=int(result)
    print(f"{num1} {op} {num2} = {result}")
    save_history(user_input, result)

def main():
    print("*******Calculator*******")
    while True:
        user_input=input("Calculate, history , clear , exit: ")
        if user_input.lower()=="exit":
            print("Exiting.........")
            break

        elif user_input.lower()=="history":
            show_history()

        elif user_input.lower()=="clear":
            clear_history()

        elif user_input.lower()=="calculate":
            equation=input("Enter ur calculation expression(e.g. 5 + 8 ): ")
            calculate(equation)

main()