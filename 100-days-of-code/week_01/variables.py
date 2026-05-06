# The goal of this exercise is to practice using variables and string concatenation in Python. It also helps to understand how to switch values between variables using a temporary variable.

# We have 2 variables glass1 and glass2. glass1 contains milk and glass2 contains juice. 
# Write 3 lines of code to switch the contents of the variables. 
# You are not allowed to type the words "milk" or "juice". 
# You are only allowed to use variables to solve this exercise. 

# Hint: You can use a temporary variable to hold the value of one of the glasses while you switch them.

glass1 = "milk"
glass2 = "juice"

# Print the initial contents of the glasses using string concatenation to show the values before switching.
print("We start with Glass #1 containing " + glass1 + " and Glass #2 containing " + glass2)

# glass3 is a temporary variable to hold the value of glass1 while we switch them
glass3 = glass1

# Now we can switch the values of glass1 and glass2
glass1 = glass2

# Finally, we can assign the value of glass3 (which holds the original value of glass1) to glass2
glass2 = glass3

print("Glass #1 is now " + glass1)
print("Glass #2 is now " + glass2)