# Christian M. Dating | BSCPE 1-5 | MINI CALCULATOR

# Create a Simple App Calculator
# 1. The application will ask the user to choose one of the four math operations (Addition, Subtraction, Multiplication, Division)
# 2. The application will ask the user for two numbers.
# 3. Display the result.
# 4. The application will ask the user wants to try again or not.
# 5. If yes, repeat step 1
# 6. If no, Display "Thank you!" and the program will exit.
# 7. Use Python Function and appropriate Exeptions to capture errors during runtime.

# PSEUDOCODE

#Intro
import pyfiglet

greet = "GOOD DAY!"
print("\033[92m" + pyfiglet.figlet_format(greet, font = "puffy"))
input("\033[94mPress Any Key to Start...")
print("\n")

print("\033[90m=" *100)
print("\033[93m SIMPLE CALCULATOR \033[0m".center(105))
print("\033[90m=" *100) 

# Ask the user to choose one of the four math operations (Addition, Subtraction, Multiplication, Division)
# Ask the user for two inputs / define the operations
def ADDITION():
    input_number1 = int(input("\nEnter the first number: "))
    input_number2 = int(input("\nEnter the second number: "))
    print(input_number1,"+",input_number2,"=", input_number1 + input_number2)

def SUBTRACTION():
    input_number1 = int(input("\nEnter the first number: "))
    input_number2 = int(input("\nEnter the second number: "))
    print(input_number1,"-",input_number2,"=", input_number1 - input_number2)

def MULTIPLICATION():
    input_number1 = int(input("\nEnter first number: "))
    input_number2 = int(input("\nEnter second number: "))
    print(input_number1,"x",input_number2,"=", input_number2 * input_number2)

def DIVISION():
    try:
        input_number1 = int(input("\nEnter first number: "))
        input_number2 = int(input("\nEnter second number: "))
        print(input_number1,"÷",input_number2,"=", input_number1 // input_number2)
    
    except ZeroDivisionError:
        while True:
            print("Division by zero.")
            break
# Display the result
# Ask the user to try again
# if yes
# if no
