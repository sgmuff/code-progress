# First, start with a list of fruits. Then, use a for loop to iterate through the list and print each fruit.
fruits = ["apple", "lime", "cherry"]

# Use a for loop to iterate through the list and print each fruit.
for fruit in fruits:
    print(fruit, "pie")

# Next, this list of numbers is given. Use a for loop to iterate through the list and print the square of each number.


# Use a for loop to iterate through the list and print the square of each number.
# A range of numbers from 1 to 10 is given. Use a for loop to iterate through the range and print the double of each number.
# (1,11) is used because the range function is exclusive of the stop value, so it will iterate from 1 to 10.
for number in range(1, 11):
    print (number * 2)

# This list of student scores is given. Use a for loop to calculate the average score and print it.
student_scores = [90, 85, 78, 92, 88]
# Use a for loop to calculate the average score and print it.
print((sum(student_scores)) / len(student_scores))

# Finally, this list of student scores is given. Use a for loop to find the highest score and print it.
new_student_scores = [90, 85, 78, 92, 88, 95, 80, 82, 91, 87, 89, 94, 86, 90, 93, 88, 91, 89, 92, 90]

# Use a for loop to find the highest score and print it.
max_score = 0

# Iterate through the list of scores and update max_score if a higher score is found.
for score in new_student_scores: # Iterate through each score in the list of new_student_scores.
    if score > max_score: # Check if the current score is greater than the current max_score.
        max_score = score # If the current score is greater than max_score, update max_score to be the current score.
print("The highest score in the class is:", max_score) # Print the highest score found in the list of new_student_scores.

# Use a for loop to calculate the sum of all numbers from 1 to 100 and print the result.
total = 0
# Iterate through the numbers from 1 to 100 and add each number to the total.
for number_total in range(1, 101):
    # Add the current number to the total.
    total += number_total
    # After the loop has finished, print the total sum of numbers from 1 to 100.
print(total)

#For vs While? For loops are typically used when the number of iterations is known beforehand, while while loops are used when the number of iterations is not known and the loop needs to continue until a certain condition is met. For example, if you want to iterate through a list of items, a for loop would be more appropriate. If you want to keep asking a user for input until they provide valid input, a while loop would be more suitable.