# Create a Python program that prompts the user to enter two numbers and then performs basic arithmetic operations (addition, subtraction, multiplication, and division) on them. The program should display the results in a clear, user-friendly manner.

# Step 1: Prompt the User for Two Numbers (Using float or int)
first_num = float(input("Enter the first number: "))
second_num = int(input("Enter the second number: "))
# What I am doing: input() is used to collect user input as a string.
# The first prompt asks for a number and converts it to a float. This allows the program to accept both whole numbers and decimal values, giving flexibility in mathematical operations.
# The second prompt asks for another number and converts it to an int. This demonstrates handling integer-specific operations while maintaining compatibility.
# Why convert? Inputs are strings by default, so conversion ensures numerical operations are possible. Using float for the first input allows precise calculations, while int for the second showcases type handling diversity.


# Step 2: Perform Arithmetic Operations
add = first_num + second_num  
# This adds the two inputs together and stores the result in the variable addition.

subtract = first_num - second_num  
# This subtracts the second number from the first and stores the result in the variable subtraction.

multiply = first_num * second_num  
# Multiplies the two inputs and stores the result in the variable multiplication.

if second_num != 0:
        divide = first_num / second_num  
# If the second number is not zero: it performs the division and stores the result.
else:
        divide = "Undefined (cannot divide by zero)" 
# If the second number is zero: assigns a message instead of performing the division, avoiding a crash.
# Division by zero is undefined and would result in a runtime error.

# if Statement: Checks a condition. If the condition is True, the block of code indented under the if is executed.
# else Statement: Executes an alternative block of code if the condition in the if statement is False.
# This logic adds robustness and user-friendliness to the program, ensuring that special cases (like division by zero) are handled without causing errors.

# Step 3: Output the Results

# Display the results
# Printing results to the screen each operation on a new line (\n).
print("\nResults:")

# f strings= An easy way to generate strings that contain interpolated expressions. Any code between curly braces {} will be evaluated and then the result will be turned into a string and inserted into the overall string. 
# f strings are most commonly used when you want to insert variables into a string.       
# Addition: Calculated the combined value of the two input numbers, providing a fundamental arithmetic operation that allows users to see their sum in a simple and clear manner.
print(f"Addition: {add:.2f}") 
        
# Subtraction: Calculated the difference between the first and second numbers, providing users with a clear view of how much one value exceeds or falls short of the other. 
print(f"Subtraction: {subtract:.2f}")  
        
# Multiplication: Calculated the product of the two numbers, demonstrating how one value scales by the other.
print(f"Multiplication: {multiply:.2f}")  
        
# Division: Calculated how many times the second number can fit into the first, which is a key arithmetic operation that helps users understand the relationship between their inputs.
if isinstance(divide, str):
    print(f"Division: {divide}")  
else:
    print(f"Division: {divide:.2f}")  