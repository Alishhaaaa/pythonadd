
#A set is a collection of uniqe items.
#unordered
#No duplicate values
#Mutable (Can add/remove items)
fruits = {"apple", "banana", "mango"}

print(fruits)
print(type(fruits))

numbers = {1, 2, 3, 4, 4, 5}

print(numbers)

colors = {"red", "blue", "green"}
 
print(colors)

#to add an item to a set,we can use the add( method)
fruits = {"apple", "banana"}

fruits.add("mango")

#while loop
j = 1
while j < 6:
  print(j)
  j += 1

#break
x = 1
while x < 6:
  print(x)
  if x == 3:
    break
  x += 1

#continue
  k = 0
while k < 6:
  k += 1
  if k == 3:
    continue
  print(k)

#elseif
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

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
    print("1. Addision")
    print("2. Substraction")
    print("3. Multiplication")
    print("4. Division")
    print("enter 'q' to quit. ")

while True:
    choice = input("\nchoose an operaqtion (1/2/3/4) or 'g' to quit: ").strip()
    if choice == 'q':
        print("Existing the calculator. Goodbye!")
        break

    if choice =='1':
        print(f"The result of addition is: {Addition()}")
    elif choice == '2':
        print(f"The result of Subtraction is: {Subtraction()}")
    elif choice == '3':
        print(f"The result of Multipication is: {Multiplication()}")
    elif choice == '4':
        print(f"The result of Division is: {Division()}")
    else:
        print("Invalid choice. Please try again.")
