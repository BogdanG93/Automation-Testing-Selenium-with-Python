import random
from math import ceil

""" MANDATORY
1. Create 3 lists that contain animals:
a. Mamifere
b. Reptile
c. Pasari
"""
mamifere = ['cartita', 'arici', 'veverita', 'soarece']
reptile = ['limax', 'varan', 'lipitoare', 'gecko']
pasari = ['kiwi', 'sabot', 'cucuveaua', 'flamingo']

print('We have these lists:')
print(f'Mamifere: {mamifere}')
print(f'Reptile: {reptile}')
print(f'Pasari: {pasari}\n')

"""1.2. Sort every list alphabetically"""
mamifere, reptile, pasari = sorted(mamifere), sorted(reptile), sorted(pasari)

print('We ordered the lists:')
print(f'Mamifere: {mamifere}')
print(f'Reptile: {reptile}')
print(f'Pasari: {pasari}\n')

""" 1.3 Create 3 other lists in which to save the same elements from the first 3 lists,
but the words should be upside down.  
Example insect_list = [“greiere”, “musca”] 🡪 insect_list_r = [“ereierg”, “acsum”]"""
mamifere_r, reptile_r, pasari_r = [], [], []

for mamifer in mamifere:
    mamifere_r.append(mamifer[::-1])

for reptila in range(len(reptile)):
    reptile_r.append(reptile[reptila][::-1])

i = 0
while i < len(pasari):
    pasari_r.append(pasari[i][::-1])
    i += 1

print('Lists written backwards:')
print(f'mamifere_r: {mamifere_r}')
print(f'reptile_r: {reptile_r}')
print(f'pasari_r: {pasari_r}\n')

""" 1.4 Count the characters in each string element in each list and display the list with the most characters."""


def count_len(lista_vietuitoare):
    len_list = 0
    for x in range(len(lista_vietuitoare)):
        len_list += int(len(lista_vietuitoare[x]))
    return len_list


len_mamifere = count_len(mamifere)
len_reptile = count_len(reptile)
len_pasari = count_len(pasari)

if len_mamifere > len_reptile and len_mamifere > len_pasari:
    print(f"List with the most characters is: {mamifere}\n")
elif len_reptile > len_mamifere and len_reptile > len_pasari:
    print(f"List with the most characters is: {reptile}\n")
else:
    print(f"List with the most characters is: {pasari}\n")

"""1.5 Replace every second element in each list with "I am an intruder"""
mamifere[1] = reptile[1] = pasari[1] = "I am an intruder"

"""1.6 Shuffle all random elements from the first list. You can use .shuffle()"""
random.shuffle(mamifere), random.shuffle(reptile), random.shuffle(pasari)
print('Lists with shuffled elements + intruder:')
print(mamifere)
print(reptile)
print(pasari)

"""Go through the list and if you find the elementary "I have an intruder",
to return his position, to delete him from the list and to return the message "The intruder was kicked out"""


def find_intruder(lista_vietuitoare):
    for element in lista_vietuitoare:
        if element == "I am an intruder":
            elem_index = lista_vietuitoare.index(element)
            return elem_index


def del_intruder(lista_vietuitoare, elem_index):
    lista_vietuitoare.remove(lista_vietuitoare[elem_index])
    print("The intruder was kicked out.")
    print('New list:', lista_vietuitoare)


def find_and_del_intruder(lista_vietuitoare):
    index_intruder = find_intruder(lista_vietuitoare)
    del_intruder(lista_vietuitoare, index_intruder)


find_and_del_intruder(mamifere)
find_and_del_intruder(reptile)
find_and_del_intruder(pasari)

"""2.1 Create the animal class with 4 attributes and 2 methods
2.2 Create 3 other classes that inherit the animal class and add another method"""


class Animal:
    def __init__(self, name_of_animal, habitat, age, weight):
        self.name = name_of_animal
        self.habitat = habitat
        self.age = age
        self.weight = weight

    def __str__(self):
        return f"{self.name} lives in the {self.habitat}, is {self.age} years old and weights {self.weight}kg."

    def escape(self):
        print(f"The {self.name} walks through the {self.habitat}.")
        bullets = int(input('How many bullets do we have? '))
        if bullets > 0:
            print("Poc!")
            print(f"We missed, the {self.name} escaped.")
        else:
            print("Looks like we're eating salad.")


urs = Animal("bear", "forest", 3, 60)
Animal.escape(urs)


class Mammal(Animal):
    def __init__(self, name_of_mammal, habitat, age, weight):
        Animal.__init__(self, name_of_mammal, habitat, age, weight)

    def define_mammal(self):
        print('Mammals have warm blood. They give birth to live young and nurse them with milk.')


class Bird(Animal):
    def __init__(self, name_of_bird, habitat, age, weight):
        Animal.__init__(self, name_of_bird, habitat, age, weight)

    def define_bird(self):
        print('Birds lay eggs. They have feathers, wings, and beaks.')


class Fish(Animal):
    def __init__(self, name_of_fish, habitat, age, weight):
        Animal.__init__(self, name_of_fish, habitat, age, weight)

    def define_fish(self):
        print('Fish are creatures with cold blood. They swim in water using fins and tails.')


mammal = Mammal("panda", "forest", 2, 85)
mammal.define_mammal()

bird = Bird("phoenix", "mountain", 120, 74)
bird.define_bird()

fish = Fish("fish", "ocean", 1, 20)
fish.define_fish()

"""Ex3. Ask the user to enter a word and display its length, 
number of consonants, number of vowels, and whether it contains any numbers."""
word = input('Enter a word: ')
if word == 'a word':
    print('I see what you did there!')

print("The word has a length of", len(word))
vowels = consonants = num_in_word = 0
for char in word:
    if char.isdigit():
        num_in_word += 1
    if char in ['a', 'e', 'i', 'o', 'u']:
        vowels += 1
    else:
        consonants += 1
print(f'Vowels: {vowels}')
print(f"Consonants: {consonants}")
print(f"Numbers in the word: {num_in_word}")

"""4.1 Create a dictionary with 5 books that contains
the book name, author, number of pages, and a message (whether it is available or not).
4.2 Create a function that allows the librarian to add new books to the library (dictionary).
4.3 Create a function that allows the librarian to delete books from the library.
4.4 Create a function that allows the librarian to enter a book name and check if it is available or not."""
book1 = {'book name': 'Animal farm', 'author': 'George Orwell', 'no_of_pages': 130, 'message': True}
book2 = {'book name': 'The richest man in Babylon', 'author': 'George Clason', 'no_of_pages': 144, 'message': True}
book3 = {'book name': 'Ghost in the wires', 'author': 'Kevin Mitnick', 'no_of_pages': 448, 'message': False}
book4 = {'book name': 'Cuvinte care schimba minti', 'author': 'Shelle Charvet', 'no_of_pages': 324, 'message': False}
book5 = {'book name': 'Winnetou', 'author': 'Karl May', 'no_of_pages': 874, 'message': True}
books_in_the_library = {'Animal farm': book1, 'The richest man in Babylon': book2, 'Ghost in the wires': book3,
                        'Cuvinte care schimba minti': book4, 'Winnetou': book5}


def create_book(list_of_books, name_of_book, author_of_book, no_of_pages_book, message_book=True):
    new_book = {'book name': name_of_book, 'author': author_of_book,
                'no_of_pages': no_of_pages_book, 'message': message_book}
    book = new_book["book name"]
    list_of_books.update({book: new_book})
    return list_of_books


def del_book(list_of_books, book_to_delete):
    list_of_books.pop(book_to_delete)
    return list_of_books


def find_book(list_of_books, book_to_find):
    if book_to_find in list_of_books:
        availability = list_of_books[book_to_find]["message"]
        return availability


while True:
    try:
        answer = int(input("What do you want to do?\n1.Add books\n2.Delete book\n3.Search book\n4. Exit\n"))
        if answer == 1:
            add_books = int(input('How many books do you want to add to the library? '))
            i = 0
            if 1 > add_books:
                print('No books to be added.')
            else:
                while i < add_books:
                    name = input('Name of the book: ')
                    author = input('Name of the author: ')
                    no_of_pages = int(input('Number of pages? '))
                    message = True
                    create_book(books_in_the_library, name, author, no_of_pages, message)
                    i += 1
                print(books_in_the_library, end="\n\n")

        elif answer == 2:
            print('Complete list of books in the library:')
            print(books_in_the_library)
            book_to_be_deleted = input('What book do you want to delete? Use the title of the book.\n')
            if book_to_be_deleted in books_in_the_library:
                del_book(books_in_the_library, book_to_be_deleted)
                print('Complete list of books after the book was deleted:')
                print(books_in_the_library, end="\n\n")
            else:
                print("We don't have this book in the library.")

        elif answer == 3:
            searched_book = input("What book do you want to find? Use the title of the book.\n")
            book_is_available = find_book(books_in_the_library, searched_book)
            if book_is_available:
                print("The book is in the library.")
            else:
                print("The book is not in the library.")

        else:
            # exit(0)   # uncomment if you want the program to exit after you've finished
            break

    except ValueError:
        continue

"""Ex5. – Medium
A user can create a restaurant reservation containing name, date, hour, number of people, number of tables.
The number of tables will be calculated automatically depending on the number of people entered by the user.
We know that a table can have 6 seats.
When you run the program, a message like this will appear for the first time:
==== “Welcome to our restaurant restaurant_name” ====.
You can choose the name of the restaurant and the welcome message.
The customer will be asked if he wants to make a reservation
If he answers no, then he will receive the message, "Maybe next time! Have a nice day!"
If he answers yes, then he will be asked the name, date, hour and number of people.
After the user has entered the data, he will be notified that the reservation has been created:
Reservation was created on the name X, on date Y, at Z hour for N persons.
To use functions.
Create a function that will return the list of reservations when called.
"""
reservation_list = {}


def greet_and_reserve():
    while True:
        print("Welcome to The Elusive Tester.")
        make_reservation = input("Do you want to make a reservation?\n1.Yes     2.No\n").lower()
        if make_reservation == "yes" or make_reservation == "1":
            reservation_name = input("On which name should the reservation be? ")
            print("When should we be expecting you?")
            date = input("Date: ")
            hour = input("Hour: ")
            no_of_persons = int(input("How many people? "))
            no_of_tables = ceil(no_of_persons / 6)
            print(f"Reservation was created on the name {reservation_name}, on date {date}, "
                  f"at {hour} hour for {no_of_persons} persons.")
            new_reservation = {"name": reservation_name, "date": date, "hour": hour, "number of persons": no_of_persons,
                               "number of tables": no_of_tables}
            reservation_add = "reservation" + " " + reservation_name
            reservation_list[reservation_add] = new_reservation
        else:
            print("Maybe next time! Have a nice day!")
            return False


def where_my_reservations_at():
    for reservation in reservation_list:
        print(f"{reservation}:{reservation_list[reservation]}")


greet_and_reserve()
where_my_reservations_at()

"""OPTIONAL
1. We have the following classification quiz.
a) We have a list of 20 animals, which goes on: mammals, birds, reptiles, amphibians.
b) A user will be shown an animal from the list and will be asked to classify it
in one of the categories: mammals, birds, reptiles, amphibians.
c) At the end, it will be displayed how many correct answers he had
d) If he answers correctly, he will be shown that he answered correctly
e) If the user answers incorrectly, he will be told that he answered incorrectly and will be given the correct answer.
f) At the end I will be given a rank:
- 20 correct answers: rank S 🡪 Congratulations! You got rank S! You are very knowledgeable about animals!
- between 16 – 19 (inclusive): rank A 🡪 Congratulations! You got rank A!
- 13 – 15 (inclusive): rank B 🡪 Congratulations! You got rank B!
- 10 – 12 (inclusive): rank C 🡪 You got rank C!
- 7 – 9 (inclusive): rank D 🡪 You got rank D!
- under 6 (inclusive): rank F 🡪 Unfortunately you got rank F!
Exercises are in romanian language
"""


def initializeaza_lista():
    lista = ["lama", "koala", "ras", "liliac", "porc",
             "barza", "lebada", "gasca", "cormoran", "vultur",
             "sarpe", "varan", "aligator", "crocodil", "vipera",
             "broasca", "axolotl", "salamandra", "brotacel", "buhai"]
    return lista


vietati = initializeaza_lista()
print("Bine ati venit la \"Animal Quizz\"!\n"
      " Iti voi afisa un animal, tu trebuie sa-mi spui daca este mamifer, pasare, reptila sau amfibian.")


def clasifica_animal(animal):
    if animal == "lama" or animal == "koala" or animal == "ras" \
            or animal == "liliac" or animal == "porc" or animal == 1:
        animal = "mamifer"
    elif animal == "barza" or animal == "lebada" or animal == "gasca" \
            or animal == "cormoran" or animal == "vultur" or animal == 2:
        animal = "pasare"
    elif animal == "sarpe" or animal == "varan" or animal == "aligator" \
            or animal == "crocodil" or animal == "vipera" or animal == 3:
        animal = "reptila"
    else:
        animal = "amfibian"
    return animal


def sa_ne_jucam(lista, score):
    while lista:
        random_vietate = lista[random.randint(0, len(lista) - 1)]
        clasificare_random_vietate = clasifica_animal(random_vietate)
        print("Scotocim prin joben si scoatem din el un/o", random_vietate)
        clasificare_animal = int(input("Alege un numar pentru a-l clasifica:\n"
                                       "1. Mamifer    2. Pasare   3. Reptila  4. Amfibian\n"))
        animal_clasificat_de_player = clasifica_animal(clasificare_animal)
        if clasificare_random_vietate == animal_clasificat_de_player:
            score += 1
        lista.remove(random_vietate)
    return score


def acordare_rang(score):
    print("Hope you had some fun. Your score is", score)
    if score == 20:
        print("Congratulations! You got rank S! You are very knowledgeable about animals!")
    elif 19 >= score >= 16:
        print("Congratulations! You got rank A!")
    elif 15 >= score >= 13:
        print("Congratulations! You got rank B!")
    elif 12 >= score >= 10:
        print("You got rank C!")
    elif 9 >= score >= 7:
        print("You got rank D!")
    else:
        print("Unfortunately you got rank F!")


# scor = 0
# scor_player = sa_ne_jucam(vietati, scor)
# acordare_rang(scor_player)

"""The same homework as above, but more difficult.
Two players should be registered with their username and password.
Both players should log in with their username and password.
The first user will start the quiz.
The same rules as in homework 1 apply.
After user1 finishes and is given a rank, user2 will be asked to log in to start the quiz, and question 1 will be given.
Finally, the ranks of the two players will be compared and displayed in order.
The second player will be told how many points behind the first player they are."""


def creaza_cont():
    new_user = input("User-ul dorit: ").lower()
    new_password = input("Parola: ").lower()
    print("Va rugam sa reintroduceti datele.")
    verificare_new_user = input("User: ").lower()
    verificare_new_password = input("Parola: ").lower()
    if new_user == verificare_new_user and new_password == verificare_new_password:
        print("V-ati logat cu succes.")
        return new_user
    else:
        print("User sau parola incorecta.")
        exit(0)


scor = 0
print("Pentru a putea juca in 2, este nevoie de a crea un cont pentru ambii jucatori.")

single_or_double_play = input("Alegeti-va numarul de jucatori.\n"
                              "Apasati \"1\" pentru solo play, \"2\" pentru a juca la dublu. ")

if single_or_double_play == "1":
    creare_cont = input("Doriti sa va creati un cont?\n1. Da    2. Nu\n")
    if creare_cont == "1":
        user = input("User-ul dorit: ").lower()
        parola = input("Parola: ").lower()
        print("Va rugam sa reintroduceti datele.")
        verificare_user = input("User: ").lower()
        verificare_parola = input("Parola: ").lower()
        if user == verificare_user and parola == verificare_parola:
            print("V-ati logat cu succes,", user)
            scor_user = sa_ne_jucam(vietati, scor)
            acordare_rang(scor_user)
        else:
            print("User sau parola incorecta.")
            creare_guest = input("Doriti sa va jucati ca si guest?\n1. Da    2. Nu\n")
            if creare_guest == "1" or creare_guest == "Da":
                guest = "guest" + str(random.randint(1, 1000))
                print("Bun venit", guest)
                scor_guest = sa_ne_jucam(vietati, scor)
                acordare_rang(scor_guest)
            else:
                print("Poate data viitoare.")
                exit(0)
    else:
        creare_guest = input("Doriti sa va jucati ca si guest?\n1. Da    2. Nu\n")
        if creare_guest == "1" or creare_guest == "Da":
            guest = "guest" + str(random.randint(1, 1000))
            print("Bun venit", guest)
            scor_guest = sa_ne_jucam(vietati, scor)
            acordare_rang(scor_guest)
        else:
            print("Poate data viitoare.")
            exit(0)
else:
    if single_or_double_play == "2":
        print("Player 1.")
        user1 = creaza_cont()
        print("Player 2.")
        user2 = creaza_cont()
        scor_user1 = sa_ne_jucam(vietati, scor)
        acordare_rang(scor_user1)
        scor = 0
        vietati = initializeaza_lista()
        scor_user2 = sa_ne_jucam(vietati, scor)
        acordare_rang(scor_user2)
        if scor_user1 > scor_user2:
            print(user1, "a castigat, avand scorul de", scor_user1, "puncte.")
            print("Felicitari si celuilalt player,", user2, "care a fost la diferenta de",
                  scor_user1 - scor_user2, "puncte fata de", user1)
        elif scor_user1 < scor_user2:
            print(user2, "a castigat, avand scorul de", scor_user2, "puncte.")
            print("Felicitari si celuilalt player,", user1, "care a fost la diferenta de",
                  scor_user2 - scor_user1, "puncte fata de", user2)
        else:
            print(f"Felicitari! Atat {user1}, cat si {user2} au acelasi numar de puncte, {scor_user1} = {scor_user2},"
                  f"jocul s-a terminat la egalitate.")
