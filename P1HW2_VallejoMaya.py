# Maya Vallejo
# 09/16/2026
# P1HW2
# The program will be used to calculate and display a users travel expenses

# Displays what the program does
print("This program calculates and displays travel expenses")
print()

# collects user input for expenses to be calculatedand uses integers for price values
budget = int(input("Enter Budget: "))
print()
destination = input("Enter your travel destination: ")
print()
gas = int(input("How much do you think you will spend on gas?: "))
print()
accomodation = int(input("Approximately, how much will you need for accomodation/hotel?: "))
print()
food = int(input("Last, how much do you need for food?: "))
print()

# breaks the page to display input summary and remaining balance after calculations
print("------------Travel Expenses------------")
print()

# displays summary of user input
print("Location:", destination)
print("Initial Budget:", budget)
print()
print("Fuel:", gas)
print("Accommodation:", accomodation)
print("Food:", food)
print()

# calculates the users remaining balance after expenses are calculated from input
remaining_balance = budget - (gas + accomodation + food)
print("Remaining Balance:", remaining_balance)