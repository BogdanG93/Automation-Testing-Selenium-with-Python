import random

# MANDATORY
# Ex:1 Explain in your own words in a comment how an if-else statement works
"""
if condition (== True):
    execute this block of code
else:
    execute this block of code
"""

# Ex.2 Check and print if x is a natural number or not.
a = 5
if a >= 0 and type(a) == int:
    print('You have entered a natural number', a)
else:
    print('You have not entered a natural number. Please try again.')

# Ex.3 Check and print if x is positive, negative or neutral.
x = 12
if x > 0:
    print('The number is positive.')
elif x < 0:
    print('The number is negative.')
else:
    print('The number is neutral.')

# Ex.4 Check and print if x is between -2 and 13.
x = 7
if -2 <= x <= 13:
    print('x is between "-2" and "13".')
else:
    print('x is not between "-2" and "13".')

# Ex.5 Check and print if the difference between x and y is less than 5.
x = 7
y = 4
if x - y < 5:
    print('The difference between x and y is less than 5.')
else:
    print('The difference between x and y is not less than 5.')

# Ex.6 Check if x is NOT between 5 and 27 - (use 'not')
x = 3
if not (5 < x < 27):
    print(x, "is not between 5 and 27.")

# Ex.7 Declare a new variable y of type int and then check and print if x and y are equal,
# if not, print which one is greater.
x = int(input('Choose the value for x. '))
y = int(input('Choose the value for y. '))
if x == y:
    print("x and y are equal.")
elif x > y:
    print("x is greater than y.")
else:
    print('x is less than y.')

# Ex.8 Assuming that x, y, z (all type int) - represent the sides of a triangle, print if the triangle is
# isosceles (two sides are equal), equilateral (all sides are equal) or scalene (no side is equal).
x = int(input('Choose the value for x. '))
y = int(input('Choose the value for y. '))
z = int(input('Choose the value for z. '))
if (x, y, z > 0) and not (x > y + z) and not (y > x + z) and not (z > x + y):
    if x == y == z:
        print('The triangle is equilateral.')
    elif (x == y) or (x == z) or (y == z):
        print('The triangle is isosceles.')
    else:
        print('The triangle is scalene.')
else:
    print('We cannot construct a triangle using these values of the sides.')

# Ex.9 Read a letter from the keyboard and then check and print if it is a vowel or not.
letter = input('Enter a letter. ')
if (letter.isalpha()) and (letter[0] == letter):
    if letter[0].lower() in ['a', 'ă', 'â', 'e', 'i', 'î', 'o', 'u']:
        print('The entered letter is a vowel.')
    else:
        print('The entered letter is a consonant.')

# Ex.10 Transform and print grades from Romanian to American system as follows:
# Over 9 => A
# Over 8 => B
# Over 7 => C
# Over 6 => D
# Over 4 => E
# 4 or below => F
grade = float(input('What is your grade? '))
if 10 >= grade > 9:
    print('My grade is A.')
elif grade > 8:
    print('My grade is B.')
elif grade > 7:
    print('My grade is C.')
elif grade > 6:
    print('My grade is D.')
elif grade > 4:
    print('My grade is E.')
elif grade <= 4:
    print('My grade is F.')
else:
    print("You didn't introduce a number between 0 and 10.")

# OPTIONALS
# Ex.1 Verify if x has at least 4 digits (ex: 7895 has 4 digits, 10 does not have at least 4 digits)
x = input('Choose the value of x. ')
if x.isdigit():
    if len(x) <= 3:
        print('The entered number does not have 4 digits.')
    else:
        print('The entered number has at least 4 digits.')
else:
    print('You did not enter a number.')

# Ex.2 Check if x has exactly 6 digits.
x = 542176
if len(str(x)) == 6:
    print('Has 6 digits.')
else:
    print('Does not have 6 digits.')

# Ex.3 Check if x is even or odd
x = 23
if x % 2 == 0:
    print('The number is even.')
else:
    print('The number is odd.')

# Ex.4 Given three variables x, y, z (all int), display in the console which one is the largest
x = int(input('Choose the value of x. '))
y = int(input('Choose the value of y. '))
z = int(input('Choose the value of z. '))
if x >= y and x >= z:
    print(f'{x} is the largest number.')
elif y >= x and y >= z:
    print(f'{y} is the largest number.')
else:
    print(f'{z} is the largest number.')

# # Ex.5 - Assuming that x, y, z represent the angles of a triangle,
# check and display whether the triangle is valid or not
# (a triangle is valid if the sum of all angles is 180 degrees
# or if the sum of the lengths of any two sides is greater than the length of the third side)
x = int(input('Choose the value of the first angle. '))
y = int(input('Choose the value of the second angle. '))
z = int(input('Choose the value of the third angle. '))
if x + y + z == 180 and x > 0 and y > 0 and z > 0:
    print('The triangle is valid.')
else:
    print('The triangle is not valid.')

'''Ex.6 Given the string: 'Coral is either the stupidest animal or the smartest rock' 
read an int x from the keyboard and display the string without the last x characters. 
e.g., if you choose 7, the following string will be displayed: 'Coral is either the stupidest animal or the smarte' '''
original_string = 'Coral is either the stupidest animal or the smartest rock'
cut = int(input('How many characters do you want to remove from the end of the string? '))
print(original_string[0:-cut])

# Ex. 7 Using the same string from exercise 6,
# declare a new string that consists of the first 5 characters + the last 5 characters
string = 'Coral is either the stupidest animal or the smartest rock'
new_string = string[0:5] + string[-5:]
print(f'The new string formed by the first 5 + last 5 characters is: "{new_string}"')

'''Ex:8 Using the same string from exercise 6, save in a variable and display the starting index 
of the word 'rock' - i.e., the position in the string at which the word 'rock' begins 
(hint: there is a function that helps you do this). 
Using this variable + slicing, display the entire string up to this word. 
Expected output: 'Coral is either the stupidest animal or the smartest ' '''
string = 'Coral is either the stupidest animal or the smartest rock'
rock_index = string.index("rock")
print(string[:rock_index])

# Ex.9 Read a string from the keyboard and check if the first and last character are the same.
# Use an assert statement.
# Note: the program should be case-insensitive,
# meaning 'apA' is accepted as a string in which the first and last character are the same
# (hint: you can use a function to make the string case-insensitive)
assert string[0].lower() == string[-1].lower(), 'The first and last character are different.'
print('The first and last character are identical.')

# Ex.10 Having the string '0123456789', display only the even numbers and then only the odd numbers
# (hint: use slicing and control the display in slicing with slicing step)
string_numbers = '0123456789'
print('Even numbers: ', string_numbers[0::2])
print('Odd numbers: ', string_numbers[1::2])

# Ex.1 We want to create an application for buying airplane tickets
# which should receive the following information as inputs:
# Age
# Accompanied by mother
# Accompanied by father
# Passport
# Mother's permission document
# Father's permission document
# Boarding conditions:
# If the person is over 18 years old and has a passport
# If the person is under 18 years old, has a passport, and is accompanied by both parents
# If the person is under 18 years old, has a passport, is accompanied by at least one parent
# and has written permission from the other parent.
# Write the code that implements the boarding conditions above and test
# all the different cases you think should be tested.
# Generate test scenarios with expected results and then run the code to check
# if expected results are equal to actual results.
# Examples:
# Age 19, no passport => Cannot board
# Age 17, valid passport, both parents => Can board
age = int(input("Please enter passenger's age. "))
valid_passport = input("Is the passport valid? Yes/No ").lower()
if age >= 18 and valid_passport == "yes":
    print("You can board.")
elif age < 18 and valid_passport == "yes":
    both_parents = input("Is the child accompanied by both parents? Yes/No ").lower()
    if both_parents == "yes":
        print("You can board.")
    else:
        permission = input("Do you have permission from the other parent? Yes/No ").lower()
        if permission == "yes":
            print("You can board.")
        else:
            print("You cannot board.")
else:
    print("You cannot board.")
""" Test scenarios:
Adult >= 18 years old with valid passport => Can board
Adult >= 18 years old with invalid passport => Cannot board
Child with valid passport and both parents => Can board
Child with valid passport and one parent - missing parent permission => Can board
Child with valid passport and one parent - missing parent permission => Cannot board
Child without valid passport => Cannot board"""

""" Ex.2  Gambling Game
Look up on the internet and see how to generate a random number
Imagine you roll a dice and save the number in a variable called dice_roll.
The saved number will be generated randomly using the method found online
Enter a number from the keyboard that represents the user's chosen number
Check and display if the user has guessed the number
There will be 3 options that need to be handled:
● You lost. You chose a smaller number. You chose x but it was y.
● You lost. You chose a larger number. You chose x but it was y.
● You won. Congratulations! You chose x and the dice was y."""
dice_in_hand = input('Do you want to roll the dice?\n'
                     '1. Yes 2. No\n').lower()

if dice_in_hand == '1' or dice_in_hand == 'yes':
    dice_roll = random.randint(1, 6)
else:
    print('Ok. Bye!')
    exit(0)

guess_dice = int(input('What number do you think came up? '))
if dice_roll == guess_dice:
    print(f"You won. Congratulations! You chose {guess_dice} and the dice was {dice_roll}.")
elif dice_roll > guess_dice:
    print(f"You lost. You chose a smaller number. You chose {guess_dice}, but it was {dice_roll}.")
else:
    print(f"You lost. You chose a larger number. You chose {guess_dice}, but it was {dice_roll}.")
