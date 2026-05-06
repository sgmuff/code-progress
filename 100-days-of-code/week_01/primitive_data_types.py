# Subscripting (Indexing)
# In Python, you can access individual characters of a string using subscripting (also known as indexing).
# Strings are immutable, meaning their characters cannot be changed after creation.
# However, you can access individual characters using indexing.
# Indexing starts at 0 for the first character.
# Negative indexing lets you access characters from the end of the string.

print("Hello"[0])   # H (first character)
print("Hello"[4])   # o (fifth character)
print("Hello"[-1])  # o (last character)

# Strings
# You can combine (concatenate) strings using the + operator.
# You can also repeat a string using the * operator.

print("123" + "456")      # "123456"
print("Hello" + "o" * 3)  # "Helloooo"

# Integers
# An integer is a whole number without a decimal point. Python supports both positive and negative integers, as well as zero.
# You can perform basic arithmetic operations on integers:
# + (addition), - (subtraction), * (multiplication), / (division)
# // performs floor division (removes the decimal part)
# % returns the remainder of a division

print(123 + 456)   # 579
print(123 - 456)   # -333
print(123 * 456)   # 56088
print(123 / 456)   # 0.26973684210526316 (float result)
print(123 // 456)  # 0 (floor division)
print(123 % 456)   # 123 (remainder)

# Large Integers
# Python 3 automatically supports arbitrarily large integers.
# There is no separate "long" type—everything is just int.

print(12345678901234567890 + 98765432109876543210)
print(123_456_789_012_345_678_90) # Using underscores for readability  

# Floats
# Floats are used to represent decimal numbers.
# You can perform arithmetic operations on floats as well.
print(3.14 + 2.71)  # 5.85
print(3.14 * 2)     # 6.28

# Booleans
# Booleans represent truth values and can be either True or False.
# They are often used in conditional statements and logical operations.
print(True)   # True
print(False)  # False
print(1 > 0)  # True
print(1 < 0)  # False

# Number manipulation
bmi = 84 / (1.75 * 2)  # BMI calculation
print(bmi)
print(int(bmi))  # Convert to integer (truncates the decimal part
print(round(bmi))  # Round to the nearest integer
print(round(bmi, 2))  # Round to 2 decimal places

# You would not use an f-string to format a number for calculations, but it is useful for displaying results in a readable format.
print(f"Your BMI is {bmi:.2f}")  # Using f-string to format the output to 2 decimal places
