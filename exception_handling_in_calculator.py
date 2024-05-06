# start: 
#   define a menu function to display the calculator menu
def menu():
#       display "Calculator Menu"- add some astig effect!
    print("Calculator MENU")
#       display "1. Addition"
    print("1. Addition")
#       display "2. Substraction"
    print("2. Substraction")
#       display "3. Multiplication"
    print("3. Multiplication")
#       display "4. Division"
    print("4. Division")
#       display "5. EXIT the program"
    print("Exit")
#   define Addition function to solve for addition
def addition():
#       Test a block of code for errors
    try:
#           input the first number
        first_number = int(input("Enter the First number: "))
#           input the second number
        second_number = int(input("Enter the Second number: "))
#           calculation for addition - add the first and second number
        adding_number = first_number + second_number
#           display the result for addition
        print(adding_number)
#       Handle errors for ValueError
    except ValueError:
#           tell the user that they inputted wrong data type
        print('"VALUE ERROR!" Please use INTEGERS ONLY!')
#   define Subtraction function to solve for substraction
def substraction():
#       Test a block of code for errors
    try:
#           input the first number
        first_number = int(input("Enter the first number"))
#           input the second number
        second_number = int(input("Enter the Second number: "))
#           calculation for substraction - substract the first and second number
        substracting_number = first_number - second_number
#           display the result for substraction
        print(substracting_number)
#       Handle errors for ValueError
    except ValueError:
        print('"VALUE ERROR!" Please use INTEGERS ONLY!')
#   define Multiplication function to solve for multiplication
def multiplication():
#       Test a block of code for errors
    try:
#           input the first number
        first_number = int(input("Enter the first number"))
#           input the second number
        second_number = int(input("Enter the Second number: "))
#           calculation for multiplication - multiply the first and second number
        multiplying_number = first_number * second_number
#           display the result for multiplication
        print(multiplying_number)
#       Handle errors for ValueError
    except ValueError:
        print('"VALUE ERROR!" Please use INTEGERS ONLY!')
#   define Division function to solve for division
def division():
#       Test a block of code for errors
    try:
#           input the first number
        first_number = int(input("Enter the first number"))
#           input the second number
        second_number = int(input("Enter the Second number: "))
#           calculation for division - divide the first and second number
        dividing_number = first_number / second_number
#           display the result for division 
        print(dividing_number)
#       Handle errors for ValueError
    except ValueError:
        print('"VALUE ERROR!" Please use INTEGERS ONLY!')
#       Handle errors for ZeroDivisionError
    except ZeroDivisionError:
        print('"UNDEFINED" You are dividing it to zero')
#   define exit function to stop the calculator
#       display thank you message
#   define main function to run the calculator
#       Test a block of code for errors
#           create an infinite loop to let the user to continue using the calculator
#               call the menu function
#               input the chosen number in the menu function
#               call Addition function if the user chosen number is 1
#               call Substraction function if the user chosen number is 2
#               call Multiplication function if the user chosen number is 3
#               call Division function if the user chosen number is 4
#               call Exit function if the user chosen number is 5
#               Ask user if they want to try again
#               display "Thank you!"
#       Handle errors for ValueError
# end: