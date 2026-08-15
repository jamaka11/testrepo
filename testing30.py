# Handling ValueError

# create a function that will generate the square root value
# if you provide a positive number
# use import math to use the sqrt() function
import math

def perform_calculation(number1):
    try:
        result = math.sqrt(number1)
        print(f"Result: {result}")
    except ValueError:
        print("Error: Invalid input! Please enter a positive integer or a float value.")
# Test case
number1=float(input("Enter the number:-"))
perform_calculation(number1)


                
