#calculator

import math

def addition(num_1, num_2):
    return num_1 + num_2

def subtraction(num_1, num_2):
    return num_1 - num_2

def multiplication(num_1, num_2):
    return (num_1 * num_2)

def division(num_1, num_2):
    if num_2 != 0:
        return num_1 / num_2
    else: 
        print("Error: Cannot Divide by Zero")
        return None

print("Calculator: ")
while True:
    print("Select an Operation:")
    print("1.) Addition")
    print("2.) Subtraction")
    print("3.) Multiplication")
    print("4.) Division")
    print("5.) Exit")

    choice = input("Enter a choice from 1-5: ")
    if choice == '5':
         print("Goodbye!")
         break

    num_1 = float(input("Enter the first number: "))
    num_2 = float(input("Enter the second number: "))

    if choice == '1':
        result = addition(num_1, num_2)
        print("Result: ", result)
        break

    elif choice == '2':
        result = subtraction(num_1, num_2)
        print("Result: ", result)
        break

    elif choice == '3':
        result = multiplication(num_1, num_2)
        print("Result: ", result)
        break

    elif choice == '4':
        result = division(num_1, num_2)
        if result is not None:
            print("Result: ", result)
            break
    else:
        print("Invalid choice try again. ")
