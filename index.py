def calculator():
   
    print("Welcome to a Simple Calculator!")

    while True:
        try:
            # Get the first number from the user
            num1 = float(input("Enter the first number: "))
            break # Exit loop if input is valid
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    while True:
        try:
            # Get the second number from the user
            num2 = float(input("Enter the second number: "))
            break # Exit loop if input is valid
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    while True:
        # Get the desired operation from the user
        operation = input("Enter the operation (add, subtract, multiply, divide): ").lower()

        # Check if the operation is one of the valid options
        if operation in ("add", "subtract", "multiply", "divide"):
            break # Exit loop if operation is valid
        else:
            print("Please choose from 'add', 'subtract', 'multiply', or 'divide'.")

    result = None # Initialize result variable

    # Perform the calculation based on the chosen operation
    if operation == "add":
        result = num1 + num2
    elif operation == "subtract":
        result = num1 - num2
    elif operation == "multiply":
        result = num1 * num2
    elif operation == "divide":
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
            return # Exit function if division by zero occurs
        else:
            result = num1 / num2

    # Print the result
    print(f"The result of {num1} {operation} {num2} is: {result}")

# Call the calculator function to run the program
calculator()
