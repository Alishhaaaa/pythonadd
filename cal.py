#calculate
def addition():
    value1 = float(input("enter the first number:"))
    value2 = float(input("enter the second number:"))
    return value1 + value2

def substraction():
    value1 = float(input("enter the first number:"))
    value2 = float(input("enter the second number:"))
    return value1 - value2

def multiplication():
    value1 = float(input("enter the first number:"))
    value2 = float(input("enter the second number:"))
    return value1 * value2

def division():
    value1 = float(input("enter the first number:"))
    value2 = float(input("enter the second number:"))
    if value2 ==0:
        return "Error:Division by zero is not allowed."
        return value1 / value2

def calculate():
    print("********welcome to the calculator ********")
    print("1. addision")
    print("2. substraction")
    print("3. multiplication")
    print("4. division")
    print("enter 'q' to quit. ")

while True:
    choice = input("\nchoose an operaqtion (1/2/3/4) or 'g' to quit: ").strip()
    if choice == 'q':
        print("Existing the calculator. Goodbye!")
        break

    if choice =='1':
        print(f"The result of addition is: {addition()}")
    elif choice == '2':
        print(f"The result of subtraction is: {subtraction()}")
    elif choice == '3':
        print(f"The result of multipication is: {multiplication()}")
    elif choice == '4':
        print(f"The result of division is: {division()}")
    else:
        print("Invalid choice. Please try again.")
