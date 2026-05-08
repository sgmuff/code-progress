# Your program should print each number from 1 to 100 in turn and include number 100.

for number in range(1, 101): # Iterate through the numbers from 1 to 100, inclusive.
    if number % 3 == 0 and number % 5 == 0: # Check if the current number is divisible by both 3 and 5.
        print("FizzBuzz") # If the current number is divisible by both 3 and 5, print "FizzBuzz".
    elif number % 3 == 0: # Check if the current number is divisible by 3.
        print("Fizz") # If the current number is divisible by 3, print "Fizz".
    elif number % 5 == 0: # Check if the current number is divisible by 5.
        print("Buzz") # If the current number is divisible by 5, print "Buzz".
    else: # If the current number is not divisible by either 3 or 5, execute the following block.
        print(number) # Print the current number if it is not divisible by either 3 or 5.