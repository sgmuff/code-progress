# Tip Calculator
print ("Welcome to the tip calculator!")

# Get user input for bill amount, tip percentage, and number of people
bill = float(input("What was the total bill? $"))

# Convert the tip percentage to a decimal and calculate the total tip amount
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))

# Calculate the total bill including tip and then divide by the number of people to get the amount each person should pay. 
people = int(input("How many people to split the bill? "))

# Convert the tip percentage to a decimal by dividing by 100.
tip_as_percent = tip / 100

# Calculate the total tip amount, total bill, and the amount each person should pay.
total_tip_amount = bill * tip_as_percent

# Calculate the total bill including tip and then divide by the number of people to get the amount each person should pay.
total_bill = bill + total_tip_amount

# Calculate the amount each person should pay by dividing the total bill by the number of people.
bill_per_person = total_bill / people

# Round the result to 2 decimal places and format it to always show 2 decimal places, then print the amount each person should pay.
final_amount = round(bill_per_person, 2)

# Format the final amount to always show 2 decimal places, even if it's a whole number, and print the result.
final_amount = "{:.2f}".format(bill_per_person)

# Print the final amount each person should pay
print(f"Each person should pay: ${final_amount}")
