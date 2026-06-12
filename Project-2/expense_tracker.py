# Expense Tracker - DecodeLabs Project 2

# Variable to store the total expenses
total_expense = 0

print("================================")
print("      EXPENSE TRACKER")
print("================================")
print("Type 'quit' to exit and view the final total.\n")

while True:

    # Get expense amount from user
    user_input = input("Enter expense amount: ")

    # Exit condition
    if user_input.lower() == "quit":
        break

    try:
        expense = float(user_input)

        # Validate negative amounts
        if expense < 0:
            print("Expense amount cannot be negative.\n")
            continue

        # Add expense to total
        total_expense += expense

        # Display updated total
        print(f"Expense Added! Current Total: {total_expense:.2f}\n")

    except ValueError:
        print("Invalid input! Please enter a valid number.\n")

# Final Summary
print("\n================================")
print(f"Total Spent: {total_expense:.2f}")
print("Thank you for using Expense Tracker!")
print("================================")