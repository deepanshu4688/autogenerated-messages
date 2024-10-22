# Get input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Check for division by zero
if num2 != 0:
    result = num1 / num2
    print(f"The result of dividing {num1} by {num2} is {result}")
else:
    print("Error! Division by zero is not allowed.")
