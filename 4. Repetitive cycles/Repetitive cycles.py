import random

# 1. Using a for loop, iterate through a list of cars and print "My favorite car is x" for each car.
cars = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
for car in range(len(cars)):
    print('FOR: My favorite car is', cars[car])

for car in cars:
    print('FOR EACH: My favorite car is', car)

i = 0
while i < len(cars):
    print('WHILE: My favorite car is', cars[i])
    i += 1

# 2. Using a for-else loop, modify the list to capitalize every car name except the first and last, then print the list.
for car in range(1, len(cars)-1):
    cars[car] = cars[car].upper()
else:
    print(cars)

# 3. Iterate through the list until you find a Mercedes, then print
# "I found the car you're looking for" and exit the loop.
# If a Mercedes is not found, print "I found car x. Still searching."
for car in range(len(cars)):
    if 'Mercedes' in cars[car]:
        print("I found the car you're looking for")
        break
    else:
        print('I found car', cars[car], '. Still searching.')

# 4. Iterate through the list and print "You might like car x" for every car except Trabant and Lăstun.
for car in range(len(cars)):
    if cars[car] == 'Trabant' or cars[car] == 'Lăstun':
        continue
    print(f'You might like car {cars[car]}.')

# 5. Create an empty list and iterate through the list of cars. For every Trabant or Lăstun, append the car
# to the empty listand replace the car with 'Tesla'. Print the list of old models and the new list of cars.
old_cars = []
for car in range(len(cars)):
    if cars[car] == 'Trabant' or cars[car] == 'Lăstun':
        old_cars.append(cars[car])
        cars[car] = 'Tesla'
print('Old models:', old_cars)
print('New models:', cars)

# 6. Iterate through a dictionary of car prices and print the cars that are within a budget of 15000 euros.
# Print "For a budget under 15000 euros, you can choose a car..." for each car that fits the budget.
car_prices = {
 'Dacia': 6800,
 'Lăstun': 500,
 'Opel': 1100,
 'Audi': 19000,
 'BMW': 23000
}
budget = 15000
for car, price in car_prices.items():
    if price <= budget:
        print(f"For a budget under {budget} euros, you can choose a {car}.")

# 7. Having this list:
numbers = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# ● Iterate through it.
# ● Print how many times the number 3 appears (don't use the count function).
i = 0
for number in range(len(numbers)):
    if numbers[number] == 3:
        i += 1
print('The number 3 appears', i, 'times in the list.')

# 8. Same list:
# ● Iterate through it
# ● Calculate and display the sum of the numbers (you are not allowed to use the sum function).
sum_of_numbers = 0
for number in numbers:
    sum_of_numbers += number
print('Sum of the numbers:', sum_of_numbers)

# 9. Same list:
# ● Iterate through it.
# ● Display the largest number (you are not allowed to use max).
max_number = 0
for number in numbers:
    if number > max_number:
        max_number = number
print('The largest number in the list is:', max_number)

# 10. The same list:
# ● Iterate through it.
# ● If the number is positive, replace it with its negative value.
# Ex: if it's 3, it should become -3
# ● Print the new list.
for number in range(len(numbers)):
    if numbers[number] > 0:
        numbers[number] -= numbers[number] * 2  # or we can use the abs() function
print(numbers)

# OPTIONAL
# Ex.1
other_numbers = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
even_numbers = []
odd_numbers = []
positive_numbers = []
negative_numbers = []

for number in other_numbers:
    if number % 2 == 0:
        even_numbers.append(number)
    else:
        odd_numbers.append(number)
    if number > 0:
        positive_numbers.append(number)
    else:
        negative_numbers.append(number)

print(f'The list with even numbers is: {even_numbers}')
print(f'The list with odd numbers is: {odd_numbers}')
print(f'The list with positive numbers is: {positive_numbers}')
print(f'The list with negative numbers is: {negative_numbers}')

# Ex.2
other_numbers = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]

print("Unsorted list:", other_numbers)

changed = False
for i in range(len(other_numbers) - 1):
    for j in range(len(other_numbers) - i - 1):
        if other_numbers[j] > other_numbers[j+1]:
            changed = True
            other_numbers[j], other_numbers[j+1] = other_numbers[j+1], other_numbers[j]
    if not changed:
        break

print("Sorted list:", other_numbers)

# Ex.3
secret_number = random.randint(1, 30)
guessed_number = None

while guessed_number is None:
    guess = int(input('Enter a number: '))
    if guess > secret_number:
        print('The secret number is lower.')
    elif guess < secret_number:
        print('The secret number is higher.')
    else:
        print('Congratulations, you found the number!')
        break

# Ex.4
a = 1
b = ''
number = int(input('Choose how many levels the pyramid has.'))

for level in range(1, number + 1):
    b = str(a) * level
    a += 1
    print(b)

# Ex.5
phone_keyboard = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

for i in range(len(phone_keyboard)):
    for j in range(len(phone_keyboard[i])):
        print('The current digit is', phone_keyboard[i][j])
