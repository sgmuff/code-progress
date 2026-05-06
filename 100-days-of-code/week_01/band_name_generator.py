# The point of this project is to practice getting user input and concatenating strings. 

#Start with a greeting message. Using. \n will create a new line after the message, so the user input will be on a new line.
print("Welcome to the Band Name Generator!\n")

#Ask the user where they grew up and assign it to a variable called my_city. Use the input() function to get the user's input.
my_city = input("In what city did you grow up?  \n")

#Ask for their first pet's name. Assign it to a variable called my_pet. Use the input() function again to get the user's input.
my_pet = input("What's the name of your first pet?  \n")

#Combine the name of their city and pet and show them their band name. This is called concatenation. Make sure to include a space between the city and pet name, and to capitalize the first letter of each word. 
band_name = my_city + " " + my_pet
print("Your band name is " + band_name)