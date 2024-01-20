## Simple Calculator in Python

### Overview

This Python script allows users to perform basic arithmetic calculations, such as addition, subtraction, multiplication, and division. Users input the desired operation and two numbers, and the calculator displays the result.

### Usage

1. **Run the Script:**
   - Save the code in a file (e.g., `calculator.py`).
   - Open a terminal or command prompt.
   - Navigate to the script's location and run: `python calculator.py`.

2. **Enter Operation and Numbers:**
   - Follow on-screen prompts to enter the desired operation (+, -, *, /).
   - Input the first and second numbers when prompted.

3. **View Result:**
   - The script will display the calculated result.

### Code Breakdown

#### Step 1: Define the Main Calculator Function

```python
def calculator():
    # Function body
```

Defines the main function that encapsulates the entire calculator logic.

#### Step 2: Get User Input for Operation

```python
operation = input("Enter operation (+, -, *, /): ")
```

Prompts the user to input the desired operation.

#### Step 3: Get User Input for Numbers

```python
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
```

Prompts the user to input the first and second numbers as floats.

#### Step 4: Perform Calculation

```python
if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    # Check for division by zero
    if num2 != 0:
        result = num1 / num2
    else:
        print("Error: Division by zero is not allowed.")
        return
else:
    print("Error: Invalid operation.")
    return
```

Uses conditional statements to perform the calculation based on the chosen operation.

#### Step 5: Display Result

```python
print(f"Result: {num1} {operation} {num2} = {result}")
```

Displays the calculated result.

#### Step 6: Call the Calculator Function

```python
calculator()
```

Calls the `calculator` function to run the entire program.

### Notes

- Ensure Python is installed on your system.
- Handle division by zero error gracefully.
- The script can be easily extended for additional functionality.

Feel free to explore and modify the code to suit your needs!
