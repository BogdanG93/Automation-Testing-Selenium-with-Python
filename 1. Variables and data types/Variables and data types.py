"""1. Within a comment, explain in your own words what a variable is.
A variable is the information that we store in a space allocated by memory, for the purpose of manipulating it.
In practice, we can think of the space as a cabinet, the space allocated for the variable as an object containing
the information (e.g. a box), the variable name as the label on the box, and the information would be inside the box."""

# 2. Declare and initialize one variable of each of the following variable types:
homework = 'Today we are doing our homework.'  # str
exercises = 10  # int
hour = 18.23  # float
finishing_homework = False  # bool
""" 3.Use the type() function to verify if they have the expected data type.
5. Use print() to print in the console four sentences using the four variables."""
print('The variables declared earlier are of the following type:')
print(f'{homework} -->', type(homework))
print(f'Exercises: {exercises} -->', type(exercises))
print(f'Hour: {hour} -->', type(hour))
print(f'Finishing the homework: {finishing_homework} -->', type(finishing_homework))
print(homework + ' We have ' + str(exercises) + ' exercises to solve. Considering it is ' + str(hour) +
      ', do you think we can solve them all in one hour? A: ' + str(finishing_homework))

# 4. Round the float using the round() function and save this modification in the same variable (overwriting):
# Verify its type.
print(f'The variable "ora" has the value of: {hour}')
hour = round(hour)
print(f'After rounding, its value is: {hour} and its type is -->', type(hour))

""" 6. Read from the keyboard:
the name;
the surname.
Display: 'The full name has x characters'. """
name = input('Write your name: ')
surname = input('Write your surname: ')
print(f"The full name has {len(name) + len(surname)} characters.")

""" 7. Read from the keyboard:
the length;
the width.
Display: 'The area of the rectangle is x'. """
print('We are calculating the area of the rectangle.')
length = input('Choose the length of the rectangle: ')
width = input('Choose the width of the rectangle: ')
print('The area of the rectangle is: ', int(length) * int(width))

"""8. Having the string: 'Coral is either the stupidest animal or the smartest rock':
display how many times the word 'the' appears;
print the result. """
sentence = 'Coral is either the stupidest animal or the smartest rock'
print('The string contains the word "the" ', sentence.count(' the '), ' times.')

""" 9. Using the same string:
display how many times the word 'the' appears;
use an assert to check if this string contains only numbers."""
assert sentence.isnumeric() is True, "The sentence does not contain only digits"

""" * Optional Exercises - Difficulty level: Medium to Hard (you may need Google) * """
# 1. Read an odd-length string from the keyboard and display the middle character.
text = str(input('Write a string: '))
print(f'The middle character is: {text[(len(text)//2)]}')

# 2. Using assert, check if a string is a palindrome.
text = 'ana'
assert text == text[::-1], 'The word is not a palindrome'

# 3. Read a string from the keyboard (e.g. 'alabala orange') and do the following:
# save each word in a variable;
# print both variables for verification.
text = input('Write a string: ')
x, y = text.split(' ')
print(f'The first word is: {x}')
print(f'The last word is: {y}')

# 4. Read a string from the keyboard (e.g. 'alabala orange') and do the following:
# save the first character in a variable;
# capitalize this character everywhere except the first and last character => alAbAlA futurAma.
text = str(input('Write a string: '))
first_letter = text[0]
modified_string = text[0]+text[1:len(text)-1].replace(x, x.upper())+text[len(text)-1]
print(modified_string)

# 5. Read a user from the keyboard, read a password. Display: 'The password for user x is ***** and has x characters'
user = str(input('The user is: '))
password = str(input('Type the password: '))
hidden_password = '*' * len(password)
print(f'The password for user {user} is {hidden_password} and has {len(password)} characters')
