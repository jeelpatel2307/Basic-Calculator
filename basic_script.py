# Step 1: Define the main calculator function
def calculator():
    # Step 2: Get user input for the operation
    operation = input("Enter operation (+, -, *, /): ")

    # Step 3: Get user input for the numbers
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    # Step 4: Perform the calculation based on the chosen operation
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        # Check if the denominator is zero to avoid division by zero error
        if num2 != 0:
            result = num1 / num2
        else:
            print("Error: Division by zero is not allowed.")
            return
    else:
        print("Error: Invalid operation.")
        return

    # Step 5: Display the result
    print(f"Result: {num1} {operation} {num2} = {result}")

# Step 6: Call the calculator function to run the program
calculator()
