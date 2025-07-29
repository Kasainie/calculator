# Get the first number from the user
# input() is used to get text from the user.
# float() converts the text to a floating-point number (allows decimals).

num1_str = input("Enter the first number: ")

num1 = float(num1_str)

# Get the second number from the user

num2_str = input("Enter the second number: ")
num2 = float(num2_str)

# Get the desired operation from the user (e.g., '+', '-', '*', '/')

operation = input("Enter the operation (+, -, *, /): ")

# Construct the expression string.
# This creates a string like "10.0 + 5.0" or "20.0 / 4.0".

expression_string = f"{num1} {operation} {num2}"

# Evaluate the expression string.
# The eval()function takes the string(e.g.,"10.0 + 5.0")and calculatesits value

result = eval(expression_string)

# Print the result in the format specified (e.g., "10 + 5 = 15").
# An f-string is used for easy formatting.

print(f"{num1} {operation} {num2} = {result}")
