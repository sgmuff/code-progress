import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Easy Level - Order not randomised:
# password = ""
# for char in range(1, nr_letters + 1):
#     password += random.choice(letters)
# for char in range(1, nr_symbols + 1):
#     password += random.choice(symbols)
# for char in range(1, nr_numbers + 1):
#     password += random.choice(numbers)
# print(password)

# Hard Level - Order of characters randomised:
password_list = []
for char in range(1, nr_letters + 1): # For every char in the range of 1 to the number of letters + 1, we will add a random letter to the password list.
    password_list.append(random.choice(letters)) # We will use the append method to add the random letter to the password list. The random.choice() method will return a random element from the letters list.
for char in range(1, nr_symbols + 1): # For every char in the range of 1 to the number of symbols + 1, we will add a random symbol to the password list.
    password_list.append(random.choice(symbols)) # We will use the append method to add the random symbol to the password list. The random.choice() method will return a random element from the symbols list.
for char in range(1, nr_numbers + 1): # For every char in the range of 1 to the number of numbers + 1, we will add a random number to the password list.
    password_list.append(random.choice(numbers)) # We will use the append method to add the random number to the password list. The random.choice() method will return a random element from the numbers list.
random.shuffle(password_list) # We will use the shuffle method from the random module to shuffle the password list. This will randomise the order of the characters in the password list.
password = "" # We will create an empty string variable called password to store the final password. We will use a for loop to iterate through the password list and add each character to the password string.
for char in password_list: # For every char in the password list, we will add it to the password string.
    password += char # We will use the += operator to add the char to the password string. This will concatenate the char to the end of the password string.
print(f"Your password is: {password}") # We will use an f-string to print the final password to the user. The f-string will allow us to include the password variable in the string.
