# Chapter 4 - working with lists #loop

#  4-13.Buffet re-writing tuples

# buffet = ['ocra', 'chicken', 'pot pie', 'steak', 'beef']
#
# print("\noriginal buffet menu: ".title())
# for x in buffet[:]:
#     print(x.title())
#
# buffet = ['corn', 'chicken', 'pot pie', 'steak', 'beef'.title()]
# print("\nnew buffet menu: ".title())
# for x in buffet[:]:
#     print(x.title())

# Tuples

# dimensions = (200, 50)
# print(dimensions[0])
# print(dimensions[1])
#
# dimensions = (400, 100)
# print("\nModified dimensions")
# print(dimensions)

# 4-11.My Pizzas - try it yourself # copying a list


# my_pizzas = ['kansas', 'duke', 'pepperoni', 'veggie']
# friends_pizza = my_pizzas[:]
#
# my_pizzas.append('meats')
# friends_pizza.append("corn")
#
# print("\nMy favortie pizzas are: ")
# for x in my_pizzas[:]:
#     print(x)
#
# print("\nMy friends favorite pizza are: ")
# for x in friends_pizza[:]:
#     print(x)

# 4-10.Slices - try it yourself

# my_foods = ['pizza', 'falafel', 'carrot cake']
# friends_foods = my_foods[:]
#
# my_foods.append("sticky rice")
# friends_foods.append("corn")
#
# print("My favorite foods are: ")
# print(my_foods)
#
# print("\nMy friend's favorite foods are:")
# print(friends_foods)


# Working with part of a list

# slice

# players = ['charles', 'martina', 'michael', 'florence', 'eli']
# print(players[:-2])

# try it yourself

# 4-9 Cube comprehension

# cubes = [n**2 for n in range(1,11)]
# print(cubes)

# 4-8. Cubes

# x = range(1,12)
# for n in x:
#     print(n**2)


# 4-7. Threes

# x = range(3,30,3)
# for n in x:
#     print(n)

# 4-6 Odd Numbers

# x = range(1, 20, 2)
#
# for n in x:
#   print(n)


# 4-5. Odd Numbers
# for value in range(1,1000000):

# 4-4, 4-5
# for value in range(1,1000000):
#     print(value)
# print(min(digits))
# print(max(digits))
# print(sum(digits))

# 4-3
#
# for value in range(1,20):
#  print(value)

# List comprehensions

# squares = [value*82 for value in range(1,11)]
# print(squares)

#“Simple Statistics with a List of Numbers”

# digits = [1,9]
# print(min(digits))
# print(max(digits))
# print(sum(digits))

# squares.py
# squares = []
# for value in range(1,11):
#     square = value**2
#     squares.append(square)
# print(squares)

# Even_numbers

# even_numbers = list(range(2,11,2))
# print(even_numbers)

# “Using the range() Function

# numbers = list(range(1,6))
# print(numbers)


# Using the range() Function #
# for value in range (1,5):
#     print(value)


# try it yourself

# 4.2 animals

# animals = ['cat', 'dog', 'pig']
#
# for animal in range(len(animals)):
#     #print(animal.title() +"\n"
#     print(animals[animal]+ "\n")


# 4.1 pizzas

# pizzas = ['kansas', 'duke', 'veggies', 'meats']
# for pizza in pizzas:
#     print(pizza.title() + ", is my favorite pizza pie\n")
# print("Yes, i love pizza but it is has to be GF")

# magicians = ['david', 'copper', 'roy']
# for magician in magicians:
#     print(magician.title() + ". that was a a great trick!")
#     print("I cant wait to see your next trick, " + magician.title() + ".\n")
# print("Thank you, everyone. That was a great magic show")



# Chapter 2-3 organizing a list

# Try it yourself

#  3-9 dinner guest excercise

# dinner_guests = ['ironman', 'hulk', 'thor', 'captain']
# print("The number of people that I am inviting is: " + str(len(dinner_guests)))

# heroes = ['ironman', 'hulk', 'thor', 'captain']
# print(heroes)
#
# print(sorted(heroes))
# print(heroes)
#
# heroes.reverse()
# print(sorted(heroes))
#
# heroes.sort(reverse=True)
# print(heroes)





# .sort(reverse=True) sorts alphabetically in reverse order

# cars = ['bmw', 'audi', 'toyota', 'subaru']
# cars.sort(reverse=True)
# print(len(cars)) # len returns length of a string
#
# print("\n here is the sorted list")
# print(sorted(cars))
#
# print("\n here is the sorted list again:")
# print(cars)
#
# cars.reverse()
# print(cars)





# 3-4 Guest List #

# names=['dylan', 'jacob', 'justin', 'rachel']
# remove_peep = names.pop()
# print("whats up " + names[1].title() + remove_peep + " will not be coming")



# names.remove('jacob')
# print(names)
#
# names.insert(0, 'Megan')
# print(names)
#
# names.insert(2, 'joe')
# print(names)
#
# remove_justin = names.remove('justin')
# print(names)
# message = "sorry Justin not today"
# print(message.title())
#
# remove_rachel = names.remove('rachel')
# print(names)
# message = "sorry rachel not today"
# print(message.title())
#
# remove_joe = names.remove('joe')
# print(names)
# message = "sorry joe not today"
# print(message.title())
#
# del names[1]
# print(names)
#
# del names[-1]
# print(names)

# “Modifying Elements in a List #

#motorcycles = ['honda', 'yamaha', 'suzuki']
#print(motorcycles)

# .pop removes from the end of the list
#popped_motorcycle = motorcycles.pop()
#print(motorcycles)

#motorcycles[0] = 'ducati'
#print(motorcycles)

# .append adds to end of the list #

# motorcycles.append('Ducati')
# print(motorcycles)

# .insert adds to a list  #
#motorcycles.insert(0, 'ducati')
#print(motorcycles)

# del deletes values #

# del motorcycles[0]
# print(motorcycles)

# last_owned = motorcycles.pop()
#popped_motorcycles = motorcycles
#print(popped_motorcycles)

#motorcycles.remove('honda')
#print(motorcycles)