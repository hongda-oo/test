print("Welcome to the Simple Calculator!")

# Function to safely get a number from the user
def get_number(prompt):
    while True:
        num = input(prompt)
        # Check if input is a valid number (integer or floating)
        try:
            return float(num)
        except ValueError:
            print("Invalid number. Please try again.")

# Main calculator loop
while True:

    print("\nChoose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Quit")

    choice = input("Enter your choice (1-5): ")

    # Quit
    if choice == "5":
        print("Goodbye!")
        break

    # Check if choice is valid
    if choice not in ["1", "2", "3", "4"]:
        print("Invalid option. Please select 1-5.")
        continue

    # Get two numbers from the user
    num1 = get_number("Enter the first number: ")
    num2 = get_number("Enter the second number: ")

    # Perform the chosen operation
    if choice == "1":
        result = num1 + num2
        symbol = "+"
    elif choice == "2":
        result = num1 - num2
        symbol = "-"
    elif choice == "3":
        result = num1 * num2
        symbol = "*"
    elif choice == "4":
        # Handle division by zero
        if num2 == 0:
            print("Error: Cannot divide by zero.")
            continue
        result = num1 / num2
        symbol = "/"

    # Print the result
    print(f"\nResult: {num1} {symbol} {num2} = {result}")
     # Ask if user wants another calculation
    again = input("Do you want to calculate again? (yes/no): ").lower()

    while again not in ["yes", "no"]:
        again = input("Please type yes or no: ").lower()

    if again == "no":
        print("Goodbye!")
        break