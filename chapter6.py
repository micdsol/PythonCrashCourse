# chapter 6 dictionaries

# Nesting - a set os dictionaries in a list or a list of items as a value in a dictionary

# A list of dictionaries

# pizza.py

pizza = {
    'crust':'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}

# summarize the order.
print("You ordered a " + pizza['crust'] + "-crust pizza" + " with the following toppings:")


for topping in pizza['toppings']:
    print("\t" + topping)

# aliens.py

# alien_0 = {'color':'green', 'points': 5}
# alien_1 = {'color':'yellow', 'points':10}
# alien_2 = {'color':'red', 'points':15}
#
# aliens = [alien_0, alien_1, alien_2]
#
# for alien in aliens:
#     print(alien)
#
# # make an emoty list for starting aliens.
# aliens = []
#
# # make 30 aliens,
# for alien_number in range(30):
#     new_alien = {'color':'green','points':5, 'speed':'slow'}
#     aliens.append(new_alien)
#
# for alien in aliens[0:3]:
#     if alien['color']=='green':
#         alien['color']= 'yellow'
#         alien['speed']='mediun'
#         alien['points'] = 10
#
# # you can expand on this loop using an elif statement
#     elif alien['color'] == 'yellow':
#         alien['color'] = 'red'
#         alien['color']= 'fast'
#         alien['points']= 15




# show the first 5 aliens

# for alien in aliens[:5]:
#     print(alien)
# print("...")
#
# # show how many aliens have been created
#
# print("total number od aliens " + str(len(aliens)))


# 6-6. try it yourself

# 6-6. Polling - loops through a list of people who should take the poll. person not on list gets a diff msg

# favorite_languages={
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python',
# }
#
# friends = ['phil','sarah']
#
# for name in favorite_languages.keys():
#    print(name.title())
#
#    if name in friends:
#       print(" Hi " + name.title() + " I see your favorite language is " + favorite_languages[name].title() + "!")
# if 'erin' not in favorite_languages.keys():
# 	    print('erin' + " please take our poll")

# goes through the list and sees with people have taken the poll

# .keys() tells python to list all keys in the dict and to sort that list before looping through it
#
# for name in sorted(favorite_languages.keys()):
#     print(name.title() + ", thank you for taking the poll")

# 6-5. Rivers

# runs through dictionary, output 3 major rivers and the country each river runs through.

# rivers = {
#	'nile':'egypt',
#	'mississippi': 'Louisiana',
#	'Amazon': 'manaus',
#	}

# for x,v in rivers.items():
#	print('The {} ' 'runs through {}' .format(x,v))

# 6-4. Glossary 2

# looping through a dictionary. 5 new items/values added using .update. Output will produce words associated with meaning

# glossary = {
#    'ifelse': 'define an action when condtional fails',
#    'boolean':'conditional test',
#    'tuples':'a sequence of immutable Python objects',
#    'if-elif-else': 'runs each conditional test in order until one passes',
# }

# glossary_2 = {
#	'modulus': 'remainder of the dicision of left operand by the right',
#	'keys()': 'method used to work with values of a dict',
#	'.format': 'positonal formatting',
#	'while' : 'executes a target statement as long as a given condtion is true',
#	'float()': 'method return a floating point number from a number or a strong'

#	}

# glossary.update(glossary_2)

# for x,v in glossary.items():
#	print('\n{}: \n{}' .format(x,v))


# .set() to see each item without repitition

# favorite_languages = {
#    'jen': 'python',
#    'sarah': 'c',
#    'edward': 'ruby',
#    'phil': 'python',
# }

# print("The following languages have been mentionted:")
# for language in set(favorite_languages.values()):
#	print(language.title())

# .values() looping through all values in a dictionary

# favorite_languages = {
#    'jen': 'python',
#    'sarah': 'c',
#    'edward': 'ruby',
#    'phil': 'python',}

# the for statement pulls each value from the dicitonary

# print("The following languages have been mentioned: ")
# for language in favorite_languages.values():
# print(language.title())

# sort - one way to return items in a certain order

# favorite_languages = {
#    'jen': 'python',
#    'sarah': 'c',
#    'edward': 'ruby',
#    'phil': 'python',
# }

# .keys() tells python to list all keys in the dict and to sort that list before looping through it

# for name in sorted(favorite_languages.keys()):
#	print(name.title() + ", thank you for taking the poll")

# looping through all the keys in a dictionary

# favorite_languages = {
#    'jen': 'python',
#    'sarah': 'c',
#    'edward': 'ruby',
#    'phil': 'python',
# }
# friends = ['phil','sarah']
# for name in favorite_languages.keys():
#    print(name.title())

#    if name in friends:
#       print(" Hi " + name.title() + " I see your favorite language is " + favorite_languages[name].title() + "!")
# if 'erin' not in favorite_languages.keys():
#	    print('erin' + " please take our poll")

# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python',
#  }

## pulls all the keys in stores one at a time in variable 'name' ##

# for name in favorite_languages: (.keys) can be omitted)
# for name in favorite_languages.keys():
#     print(name.title())


# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python',
# }
# for name,language in favorite_languages.items():
#     print(name.title() + "'s favorite language is ", language.title())

# looping through a dictionary
#
# user_0 = {
#     'username': 'efermi',
#     'first': 'enrico',
#     'last': 'fermi',
# }
#
# for key,value in user_0.items():
#     print("\nKey: " + key)
#     print("Value: " + value)

# 6-3 try it yourself

# 6-2.Favorite numbers:

# glossary = {
#    'ifelse': 'define an action when condtional fails',
#    'boolean':'conditional test',
#    'tuples':'a sequence of immutable Python objects',
#    'if-elif-else': 'runs each conditional test in order until one passes',

# for x,v in glossary.items():
#	print('\n{}:\nDefinition: {}'.format(x,v))


# print("The word , " + programming_words[])

# for x in programming_words.items():
# print(x)


# print(programming_words)

# favorite_numbers = {
#     'jacob':'15',
#     'kent': '33',
#     'justin': '26',
#     'justine': '13',
#     'jack': '7',
# }
# print(favorite_numbers)

# 6-1.Person
#
# person = {'first_name':'Justine', 'last_name':'lu','age':'33','city':'san francisco'}
#
# print(person)


# a dictionary of similar objects

# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python',
# }
# print(favorite_languages)

## looks up corresponding kay-value pair ##
# print("sarah's favorite language is : " + favorite_languages['edward'])

# removing key value pairs

# alien_0 = {'color': 'green', 'points': 5}
# print(alien_0)
#
# del alien_0['points']
# print(alien_0)

# modifying values in a dictionary

# alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
# print("Original x-position: " + str(alien_0['x_position']))

# move the alien to the right
# determine how far to move the alien based on its current speed.

# if alien_0['speed'] == 'slow':
#     x_increment = 1
# elif alien_0['speed'] =='medium':
#     x_increment=2
# else:
# this must be a fast alien
#     x_increment = 3

# the new position is the old position plus the increment.
# alien_0['x_position'] = alien_0['x_position'] + x_increment
# print("new x-position: " + str(alien_0['x_position']))

# alien_0 = {'color': 'green'}
# print("The alien is " + alien_0['color'] + ".")
#
# alien_0['color'] = 'yellow'
# print("The alien is now " + alien_0['color'] + ".")

# starting with an empty dictionary
# alien_0 = {}
# alien_0['color'] = 'green'
# alien_0['points'] = 5
# print(alien_0)

# Adding new key-value pairs

# alien_0 = {'color': 'green', 'points': 5}
# print(alien_0)
#
# alien_0['x_position'] = 0 # additional key value pairs
# alien_0['y_position'] = 25 # additional key value pairs
# print(alien_0)


# accessing values in a dictionary

# alien_0 = {'color': 'green', 'points': 5}
# new_points = alien_0['points']
# print("You just earned " + str(new_points) + " points!")

# alien_0 = {'color': 'green', 'points': 5}
#
# print(alien_0['color'])
# print(alien_0['points'])-