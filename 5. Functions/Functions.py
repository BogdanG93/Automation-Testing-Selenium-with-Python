import math
from datetime import date
from datetime import datetime
import pytz

# MANDATORY
# 1. Function that calculates and returns the sum of two numbers
num1 = int(input("First number: "))
num2 = int(input("Second number: "))


def calculate_sum(first, second):
    sum_result = first + second
    return f'The sum of the two numbers is {sum_result}.'


print(calculate_sum(num1, num2))


# 2. Function that returns TRUE if a number is even, FALSE for odd


def even_odd(number):
    if number % 2 == 0:
        return True
    else:
        return False


print(even_odd(205))
print(even_odd(12))


# 3. Function that returns the total number of characters in your full name.
# (first name, middle name, last name)


def count_full_name_characters(last_name, middle_name, first_name):
    return len(last_name + middle_name + first_name)


print(count_full_name_characters("Smith", "William", "John"))


# 4. Function that returns the area of a rectangle


def rectangle_area(length, width):
    area = length * width
    return area


print(rectangle_area(5, 7))


# 5. Function that returns the area of a circle


def circle_area(radius):
    return math.pi * radius ** 2


print('%.2f' % circle_area(5))


# 6. Function that returns True if a character x is found in a given string and False if it doesn't find it.


def search_char_in_string(char):
    string = input('Write a random string: ')
    if char in string:
        return True
    else:
        return False


print(search_char_in_string('c'))


# 7. Function without return, takes a string and prints on the screen:
# ● Nr of lower case characters is x
# ● Nr of upper case characters is y


def count_lower_upper_chars():
    lower_chars, upper_chars = 0, 0
    string = input('Enter a string: ')
    new_string = ''.join(string.split())
    for char in new_string:
        if char.islower():
            lower_chars += 1
        else:
            upper_chars += 1
    print('Number of lower case characters:', lower_chars)
    print('Number of upper case characters:', upper_chars)


count_lower_upper_chars()


# 8. Function that takes a LIST of numbers and returns a LIST only with positive numbers


def return_positive_numbers():
    random_list = input('Enter the numbers you want. Separate them with a space: ').split()
    new_list = []
    for num in random_list:
        if int(num) > 0:
            new_list.append(num)
    return new_list


print("List of positive numbers:", return_positive_numbers())


# 9. Function that does not return anything. Takes two numbers and PRINTS
# ● The first number x is greater than the second number y
# ● The second number y is greater than the first number x
# ● The numbers are equal.


def compare_two_numbers(x, y):
    if x > y:
        print(f'The first number "{x}" is greater than the second number "{y}".')
    elif x < y:
        print(f'The second number "{y}" is greater than the first number "{x}".')
    else:
        print('The numbers are equal.')


compare_two_numbers(4, 1)
compare_two_numbers(3, 3)

# 10. Function that receives a number and a set of numbers.
# ● Print 'I added the new number to the set' + return True
# ● Print 'I did not add the number to the set. It already exists' + return False


def add_number_to_set(num, num_set):
    if num in num_set:
        print(f"{num} is already in the set.")
        return False
    else:
        num_set.add(num)
        print(f"Added {num} to the set.")
        return True


print(add_number_to_set(33, {54, 42, 712, 33}))
print(add_number_to_set(5, {54, 42, 712, 33}))


# OPTIONAL
# 1. Function that receives a month of the year and returns how many days that month has.


def calendar(month):
    months_in_year = {
        'January': 31,
        'February': 28,
        'March': 31,
        'April': 30,
        'May': 31,
        'June': 30,
        'July': 31,
        'August': 31,
        'September': 30,
        'October': 31,
        'November': 30,
        'December': 31
    }
    if month in months_in_year:
        return months_in_year.get(month)


print(calendar('June'))
print(calendar('January'))
print(calendar('February'))


# 2. A calculator function that returns 4 values: the sum, difference, multiplication and subtraction of two numbers.
# You will use it like this:
# a, b, c, d = calculator(10, 2)
# ● print("Sum: ", a)
# ● print("Difference: ", b)
# ● print("Multiplication: ", c)
# ● print("Subtraction: ", d)


def calculator(numb1, numb2):
    sum_of_num = numb1 + numb2
    subtraction_of_num = numb1 - numb2
    multiplication_of_num = numb1 * numb2
    division_of_num = numb1 / numb2
    return sum_of_num, subtraction_of_num, multiplication_of_num, division_of_num


a, b, c, d = calculator(10, 2)
print("Sum: ", a)
print("Difference: ", b)
print("Multiplication: ", c)
print("Subtraction: ", d)


# 3. Function that receives a list of digits (only 0-9).
# Example: [1, 3, 1, 5, 9, 7, 7, 5, 5]
# It returns a dictionary that tells us how many times each digit appears.


def count_numbers(a_list):
    count_dict = {}
    for numbers in a_list:
        if numbers in count_dict:
            count_dict[numbers] += 1
        else:
            count_dict[numbers] = 1
    print(count_dict)


count_numbers([1, 5, 5, 5, 2, 3, 1])


# 4. Function that receives 3 numbers. Returns the maximum number.


def max_number(number1, number2, number3):
    if number1 > number2 and number1 > number3:
        return number1
    elif number2 > number1 and number2 > number3:
        return number2
    else:
        return number3


print("Max number between 5,3 and 7:", max_number(5, 3, 7))
print("Max number between 12, 4 and 19:", max_number(12, 4, 19))


# 5. A function that receives a number and returns the sum of all numbers from 0 to that number.
# Example: if we give the number 3, the sum will be 6 (0+1+2+3).


def range_sum_no(num):
    sum_all_numbers = 0
    for number in range(num + 1):
        sum_all_numbers += number
    return sum_all_numbers


print("Sum when 5 is introduced:", range_sum_no(5))
print("Sum when 8 is introduced:", range_sum_no(8))


# OPTIONAL
# 1. Function that receives 2 lists of numbers (the numbers may be duplicated). Return the common numbers.
# Example:
# list1 = [1, 1, 2, 3]
# list2 = [2, 2, 3, 4]
# Answer: {2, 3}


def common_numbers_in_lists(list1, list2):
    common_numbers = set(list1) & set(list2)
    return common_numbers


print(common_numbers_in_lists([2, 2, 5, 3], [5, 5, 2, 3, 1]))


# 2. Function that applies a discount to a price.
# If the product costs 100 dollars, and we apply a 10% discount, the price will be 90.
# Handle cases where the discount is invalid. For example, a 110% discount is invalid.


def apply_discount(price, discount):
    if discount <= 0 or discount >= 100:
        print('Discount is invalid.')
    else:
        discounted_price = price * (100 - discount) / 100
        print(f'The product costs {price} dollars. After applying a {discount}% discount, '
              f'it costs {discounted_price} dollars.')


apply_discount(100, 10)
apply_discount(525, 10)


# 3. Function that displays the current date and time in Romania
# (bonus: display the current date and time in China as well)


def current_date_and_time():
    ro_tz = pytz.timezone('Europe/Bucharest')
    ro_date_and_time = datetime.now(ro_tz)
    print('Current date and time in Romania:', ro_date_and_time)

    china_tz = pytz.timezone('Asia/Shanghai')
    china_date_and_time = datetime.now(china_tz)
    print('Current date and time in China:', china_date_and_time)


current_date_and_time()


# 4. Function that displays how many days are left until Christmas


def count_days_until_event(year, month, day):
    event_date = date(year=year, month=month, day=day)
    days_until_event = (event_date - date.today()).days
    return days_until_event


print("Days until Christmas:", count_days_until_event(2023, 12, 25))
