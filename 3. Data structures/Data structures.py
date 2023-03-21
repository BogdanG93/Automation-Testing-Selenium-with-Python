# 1. Declare a list of musical notes and print it
musical_notes = ['do', 're', 'mi', 'fa', 'sol', 'la', 'si', 'do']
print('a. List of musical notes:\n', musical_notes)

# Reverse the order using slicing and print the new list
musical_notes = musical_notes[::-1]
print('b. Reversed list of musical notes:\n', musical_notes)

# Use the reverse() method to reverse the order again and print the list
musical_notes.reverse()
print('c. Reversed list of musical notes using the reverse function:\n', musical_notes)

# Count the number of times 'do' appears in the list and print it
print('Number of times "do" note appears: ', musical_notes.count("do"))

# 3. Concatenate two lists in two ways and print the result
list1 = [3, 1, 0, 2]
list2 = [6, 5, 4]
new_list = list1 + list2
print(f"New list: {new_list}")
list1.extend(list2)
print("First list extended with the second list using extend function:", list1)

# Sort the list from exercise 3, remove 0, and print the new list
list1.sort()
print(f"Sorted list: {list1}")
list1.remove(0)
print(f"Sorted list after 0 is removed: {list1}")

# Use an if statement to check if the list is empty and print the result
if list1:
    print('List is not empty.')
else:
    print('List is empty.')

# Clear the list and check if it's empty again
list1.clear()
if list1:
    print('List is not empty.')
else:
    print('List is empty.')

# 8. Print the keys of a dictionary
dict1 = {'Ana': 8, 'Gigel': 10, 'Dorel': 5}
print(dict1.keys())

# 9. Print the names and grades of the students in a dictionary
print('Ana\'s grade:', dict1['Ana'])
print('Gigel\'s grade:', dict1['Gigel'])
print('Dorel\'s grade:', dict1['Dorel'])

# 10. Modify a value in the dictionary and print it
dict1.update({'Dorel': 6})
print('Dorel\'s grade:', dict1['Dorel'])

# 11. Remove a key from the dictionary, add a new one, and print the new dictionary
dict1.pop('Gigel')
dict1['Ionica'] = 9
print(dict1)

# 12. Add a new element to a set and print it
romanian_days = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
romanian_weekend = {'sâmbăta', 'duminică'}
romanian_days.add('luni')
print(romanian_days)

# 13. Use an if statement to check whether:
# ● Weekend is a subset of the days of the week.
# ● Weekend is not a subset of the days of the week.
if romanian_weekend.issubset(romanian_days):
    print('Weekend is a subset of the days of the week.')
else:
    print('Weekend is not a subset of the days of the week.')

# 14. Display the differences between these two sets.
print(romanian_days.difference(romanian_weekend))

# 15. Display the intersection of the elements in these two sets.
print(romanian_days.intersection(romanian_weekend))
"""OPTIONAL"""

"""1. Let's imagine a football team for a synthetic field.
Maximum 3 substitutions allowed
● Declare a list with 5 players
● Changes_made = you play with different values
● Max_changes = 3

If player x is on the field and we have substitutions available:

Make the substitution
Remove the substituted player from the list
Add the substituted player to the list of available players
Display "x in, y out, z substitutions remaining"
If the player is not on the field:

Display "Substitution cannot be made because player x is not on the field"
Display "z substitutions remaining"
Test the code with different values
Google search hint: "how to check if item is in list python"""
max_permitted_changes = 3
players_on_field = ['77 Barbu Gabriela Theodora', '12 Barbu Mădălina', '35 Popescu Ionela Diana',
                    '10 Sandu Gabriela Sorina', '27 Șandru Mihaela']
reserves = ['22 Balogh Alexandru', '13 Geagu Bogdan', '33 Pop Octavian Marius']
print('Jucatorii din teren sunt:', players_on_field)
print('Rezervele sunt:', reserves)

while max_permitted_changes > 0:
    changed_player = int(input('Schimba jucatorul din teren folosindu-te de numarul de pe tricou.'))
    if changed_player == 77:
        player_that_is_changed = '77 Barbu Gabriela Theodora'
    elif changed_player == 12:
        player_that_is_changed = '12 Barbu Mădălina'
    elif changed_player == 35:
        player_that_is_changed = '35 Popescu Ionela Diana'
    elif changed_player == 10:
        player_that_is_changed = '10 Sandu Gabriela Sorina'
    elif changed_player == 27:
        player_that_is_changed = '27 Șandru Mihaela'
    else:
        print('We can\'t change this player because he is not on the field.')
        print('You have', max_permitted_changes, 'more changes.')
        changed_player = int(input('Use the number on the T-shirt to change the player.'))
        if changed_player == 77:
            player_that_is_changed = '77 Barbu Gabriela Theodora'
        elif changed_player == 12:
            player_that_is_changed = '12 Barbu Mădălina'
        elif changed_player == 35:
            player_that_is_changed = '35 Popescu Ionela Diana'
        elif changed_player == 10:
            player_that_is_changed = '10 Sandu Gabriela Sorina'
        elif changed_player == 27:
            player_that_is_changed = '27 Șandru Mihaela'

    player_sent_on_the_field = int(input('Use the number on the T-shirt to change the player.'))
    if player_sent_on_the_field == 22:
        player_sent_on_the_field = '22 Balogh Alexandru'
    elif player_sent_on_the_field == 13:
        player_sent_on_the_field = '13 Geagu Bogdan'
    elif player_sent_on_the_field == 33:
        player_sent_on_the_field = '33 Pop Octavian Marius'
    else:
        print('The player you wish to send on the field is not on the reserve bench.')
        player_sent_on_the_field = int(input('Use the number on the T-shirt to change the player.'))
        if player_sent_on_the_field == 22:
            player_sent_on_the_field = '22 Balogh Alexandru'
        elif player_sent_on_the_field == 13:
            player_sent_on_the_field = '13 Geagu Bogdan'
        elif player_sent_on_the_field == 33:
            player_sent_on_the_field = '33 Pop Octavian Marius'

    if player_that_is_changed in players_on_field:
        if player_sent_on_the_field in reserves:
            players_on_field.remove(player_that_is_changed)
            players_on_field.extend([player_sent_on_the_field])
            reserves.remove(player_sent_on_the_field)
            max_permitted_changes -= 1
            print(f'Player that entered on the filed: {player_sent_on_the_field}.\n'
                  f'Player that left the field: {player_that_is_changed}.\n'
                  f'You have {max_permitted_changes} more changes')
            print('Players on the field:', players_on_field)
            print('Reserves:', reserves)

        else:
            print('We could not do the change.')
    else:
        print('Try again.')
