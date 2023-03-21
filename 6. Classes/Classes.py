import math
from datetime import datetime

"""1. Circle Class
Attributes: radius, color
Constructor for both attributes
Methods:
- describe_circle() - will PRINT the color and radius
- area() - will RETURN the area
- diameter()
- circumference()"""


class Circle:
    def __init__(self, radius, color):
        self.radius = radius
        self.color = color

    def describe_circle(self):
        print("Circle color:", self.color + ",", "circle radius:", self.radius)

    def area(self):
        area = math.pi * self.radius ** 2
        print("Circle area is: %.2f" % area)

    def diameter(self):
        diameter = 2 * self.radius
        print("Circle diameter is:", diameter)

    def circumference(self):
        circumference = 2 * math.pi * self.radius
        print("Circle circumference is: %.2f" % circumference)


circle1 = Circle(3, "blue")
circle2 = Circle(5, "yellow")

circle1.describe_circle()
circle1.area()
circle1.diameter()
circle1.circumference()

circle2.describe_circle()
circle2.area()
circle2.diameter()
circle2.circumference()

"""2. Rectangle Class
Attributes: length, width, color
Constructor for all attributes
Methods:
- describe()
- area()
- perimeter()
- change_color(new_color) - this method does not return anything. 
  It takes a new color as a parameter and overwrites the self.color attribute. 
  You can check the color change by calling the describe() method."""


class Rectangle:
    def __init__(self, length, width, color):
        self.length = length
        self.width = width
        self.color = color

    def describe(self):
        print(f"Rectangle description: length = {self.length}, width = {self.width}, color = {self.color}")

    def area(self):
        print("Rectangle area is:", self.length * self.width)

    def perimeter(self):
        print("Rectangle perimeter is:", 2 * (self.length + self.width))

    def change_color(self, new_color):
        self.color = new_color
        print("I changed the rectangle's color, now it is", self.color)


rect1 = Rectangle(15, 10, "blue")
rect1.describe()
rect1.area()
rect1.perimeter()
rect1.change_color("red")
rect1.describe()
print()
rect2 = Rectangle(12, 6, "orange")
rect2.describe()
rect2.area()
rect2.perimeter()
rect2.change_color("green")
rect2.describe()

"""3. Employee Class
Attributes: name, surname, salary
Constructor for all attributes
Methods:
- describe()
- full_name()
- monthly_salary()
- annual_salary()
- increase_salary(percent)"""


class Employee:
    def __init__(self, name, surname, salary):
        self.name = name
        self.surname = surname
        self.salary = salary

    def describe(self):
        print(self.name, "wants to work in IT.")

    def full_name(self):
        print("Full name:", self.name + " " + self.surname)

    def monthly_salary(self):
        return self.salary

    def annual_salary(self):
        return self.salary * 12

    def increase_salary(self, percent):
        self.salary = percent / 100 * self.salary + self.salary
        print("We are starting the year off right. I increased your salary by", percent,
              "% (don't forget to account for inflation).")
        return self.salary


employee1 = Employee("Geagu", "Bogdan", 2700.52)
employee1.describe()
employee1.full_name()
print(f"Monthly salary: {employee1.monthly_salary()}")
print(f"Annual salary: {employee1.annual_salary()}")
employee1.increase_salary(10)
print(f"New monthly salary: {employee1.monthly_salary()}")
print()

employee2 = Employee("Pop", "Octavian", 3500.85)
employee2.describe()
employee2.full_name()
print(f"Monthly salary: {employee2.monthly_salary()}")
print(f"Annual salary: {employee2.annual_salary()}")
employee2.increase_salary(14)
print(f"New monthly salary: {employee2.monthly_salary()}")

"""4. Class Cont
Attributes: iban, holder_account, sold
Constructor for all attributes
Methods:
● see_sold() - The account holder x has in account y the amount of n dollars
● withdraw_account(sum_of_money) - Withdraw the amount of "suma" from the account
● add_sum_to_account(sum_of_money) - Add the amount of "suma" to the account"""


class Cont:
    def __init__(self, iban, holder_account, sold):
        self.iban = iban
        self.holder_account = holder_account
        self.sold = sold

    def see_sold(self):
        print(f"The account holder, {self.holder_account}, has in account '{self.iban}'"
              f" the amount of {self.sold} dollars.")

    def withdraw_account(self, sum_of_money):
        self.sold -= sum_of_money
        print(f"The account holder {self.holder_account} has withdrawn the amount of {sum_of_money} dollars"
              f" from the account \"{self.iban}\". "
              f"Current balance: {self.sold} dollars.")

    def add_sum_to_account(self, sum_of_money):
        self.sold += sum_of_money
        print(f"The account holder {self.holder_account} has added the amount of {sum_of_money} "
              f"dollars to the account \"{self.iban}\". "
              f"Current balance: {self.sold} dollars.")


account1 = Cont(542855, "Geagu Bogdan", 1500)
account1.see_sold()
account1.withdraw_account(500)
account1.add_sum_to_account(1500)
print()
account2 = Cont(854241, "Pop Octavian Marius", 8200)
account2.see_sold()
account2.withdraw_account(2700)
account2.add_sum_to_account(5000)

# Optional Exercises - difficulty level: Medium to hard: may need Google.
"""1. Class Bill
Attributes: series (constant, no constructor needed, all invoices will have the same series),
number, product name, quantity, unit price
Constructor: all attributes except series
Methods:
● change_quantity(quantity)
● change_price(price)
● change_product_name(name)
● generate_invoice() - will print in a tabular format if you can
Invoice series x number y
Date: automatically generate today's date
Product | quantity | unit price | Total
Phone | 7 | 700 | 49000"""


def i_like_underscores():
    print(" ________________________________________________ ")


class Bill:
    series = '5442'

    def __init__(self, number, product_name, quantity, unit_price):
        self.number = number
        self.product_name = product_name
        self.quantity = quantity
        self.unit_price = unit_price

    def change_quantity(self, quantity):
        self.quantity = quantity
        return self.quantity

    def change_price(self, price):
        self.unit_price = price
        return self.unit_price

    def change_product_name(self, name):
        self.product_name = name
        return self.product_name

    def generate_invoice(self):
        data = datetime.today().strftime('%d.%m.%Y')
        name = self.product_name
        quantity = self.quantity
        price = self.unit_price
        total = self.quantity * self.unit_price
        print("Data:", data)
        print(f"Invoice series {self.series} no. {self.number}")
        i_like_underscores()
        print("{:<20} {:<10} {:<5} {:<5}".format("| Product", "| Quantity", "| Unit Price", "| Total  |"))
        i_like_underscores()
        print("{:<20} {:<11} {:<6} {:<5}".format("| " + str(name), "|    " + str(quantity),
                                                 "| " + str(price), "| " + str(total) + " |"))
        i_like_underscores()


bill1 = Bill(5425, "chocolate", 413, 5)
bill1.change_quantity(350)
bill1.change_price(4.8)
bill1.change_product_name("Chocolate with peanuts")
bill1.generate_invoice()
print()
bill2 = Bill(5426, "ice cream", 2500, 3)
bill2.change_quantity(1875)
bill2.change_price(2.5)
bill2.change_product_name("ITF ice cream")
bill2.generate_invoice()

"""2. Class Car
Attributes: make, model, maximum speed, current speed, color,
available colors (set), registered (bool)
Color = grey - all cars are grey when they leave the factory
Current speed = 0 - all cars stand still when they leave the factory
Available colors = choose 5-7 colors
Make = choose - the factory produces only one make but several models
Registered = False
Constructor: model, maximum speed
Methods:
● describe() - all attributes will be printed, except for available colors
● register() - will change the registered attribute to True
● paint(color) - the car will be painted in the new color ONLY if the new color is in the available color option, 
otherwise display an error
● accelerate(speed) - the car will accelerate to a certain speed, if the speed is negative-an error, 
if the speed is greater than the maximum speed - the car will accelerate to the maximum speed
● brake() - the car will stop and have speed = 0"""


class Car:
    brand = "Dacia"
    color = "grey"
    actual_speed = 0
    colors_in_stock = {"red", "green", "blue", "orange", "yellow"}
    certified = False

    def __init__(self, model, max_speed):
        self.model = model
        self.max_speed = max_speed

    def describe(self):
        print(f"Car:\nbrand:{self.brand}, model: {self.model}, color:{self.color}, "
              f"actual speed: {self.actual_speed},certified: {self.certified},"
              f"max speed: {self.max_speed}")

    def car_is_certified(self):
        self.certified = True
        return self.certified

    def paint(self, color):
        if color in self.colors_in_stock:
            print("You painted the car in the color", color)
            self.color = color
        else:
            print("Sorry, we do not have that color in stock.")

    def accelerate(self, speed):
        if speed <= 0:
            print("ERROR. You can't have a speed below 0.")
        else:
            if speed < self.max_speed:
                print(f"After accelerating, I now have a speed of {speed} km/h.")
                self.actual_speed = speed
            else:
                print(f"After accelerating, I now have a max speed of {speed} km/h..")
                self.actual_speed = self.max_speed

    def breaking(self):
        print("I touched the brake and stopped.")
        self.actual_speed = 0
        print("Actual speed:", self.actual_speed)


car1 = Car("Duster", 220)
car1.describe()
car1.car_is_certified()
car1.paint("white")
car1.accelerate(230)
car1.breaking()

car2 = Car("Logan", 180)
car2.describe()
car2.car_is_certified()
car2.paint("red")
car2.accelerate(-5)
car2.breaking()


# 3. TodoList class
# Attributes: todo (dict, where key is the task name and value is the description)
# Initially, there are no tasks, so the dict is empty and we don't need a constructor.
# Methods:

class TodoList:
    todo = {}

    def add_task(self, name, description):
        self.todo[name] = description
        print("Todo list after adding new task: ", self.todo)

    def complete_task(self, name):
        print(f"Task done: \"{name}\", description: \"{self.todo[name]}\"")
        self.todo.pop(name)
        print("Todo list after deleting task: ", self.todo)

    def display_todo_list(self):
        print("Current todo list:")
        for keys in self.todo.items():
            print(keys)

    def display_additional_details(self, name):
        if name not in self.todo.keys():
            add_new_task = input(f"The task \"{name}\" is not in the todo list. Do you want to add it?\n"
                                 f"1. Yes    2. No\n").lower()
            if add_new_task == "yes" or add_new_task == "1":
                description = input("Add a description of the task: ")
                self.add_task(name, description)
            else:
                print("Ok, bye bye!")
        else:
            print(
                f"The task you are looking for, \"{name}\", is already in the todo list "
                f"with the description: \"{self.todo[name]}\"")


# Example usage of the TodoList class
dict1 = TodoList()
dict1.add_task("write code", "Today, 03/16/2023, you need to solve homework06 from the course.")
dict1.add_task("drink a beer", "After doing your homework, grab a cold one from the fridge.")
dict1.complete_task("drink a beer")
dict1.display_todo_list()
dict1.display_additional_details("exercise")
dict1.display_additional_details("write code")
dict1.display_todo_list()
# We should clear the dictionary when adding a new object,
# so that it doesn't interfere with the tasks from the first object
dict1.todo.clear()

dict2 = TodoList()
dict2.add_task("review OOP", "Review the concept of classes, attributes, methods, and OOP pillars.")
dict2.add_task("make coffee", "Dry your tears in coffee.")
dict2.add_task("watch cute cats", "Take a break and watch videos with cutie-pies cats.")
dict2.complete_task("make coffee")
dict2.display_todo_list()
dict2.display_additional_details("make more coffee")
dict2.display_additional_details("make more coffee")
dict2.display_todo_list()
