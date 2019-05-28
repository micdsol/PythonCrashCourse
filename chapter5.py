#chapter 5 - dictionaries

## commit test # 3

# chapter 5 - if statements

# 5-11 try it yourself

# 5-11. Ordinal Numbers:

# numbers = ['1','2','3','4','5','6','7','8','9']
#
# for number in numbers:
#     if number == '1':
#         print(numbers[0] + "st")
#     elif number == '2':
#         print(numbers[1] + "st")
#     elif number == '3':
#         print(numbers[2] + "rd")
#     else:
#         print(number + "th")

# 5-10. Checking usernames

# current_users = ['admin', 'micdsol', 'bkenobi', 'lskywalker', 'jblanco']
# new_users = ['mdiesel','vtran','rnguyen','lskywalker', 'jblanco']
#
# for new_user in new_users:
#     if new_user in current_users:
#         print(new_user.title() + ", you will need to enter a new username " )
#     else:
#         print(new_user.title() + ", this username is available")

# 5-9. No Users:

# usernames = ['admin', 'micdsol', 'bkenobi', 'lskywalker', 'jblanco']
# usernames.append('john')
#
# if usernames:
#     print("Here are the list of users: " + str(usernames))
#
# else:
#     print("We need more users ")


# 5-8. hello admin

# usernames = ['admin', 'micdsol', 'bkenobi', 'lskywalker', 'jblanco']
#
# for username in usernames:
#     if username == 'admin':
#         print("Hello, " + username.title() + " would you like a status report?")
#     else:
#         print("Hello, " + username.title() + " thank you for logging in ")


#  using multiple lists
#
# available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
# requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

# for requested_topping in requested_toppings:
#     if requested_topping in available_toppings:
#         print("Adding " + requested_topping + ".")
#     else:
#         print("Sorry, we dont have " + requested_topping + ".")
# print("\nFinished making your pizza")

# checking that a list is not empty

# requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
#
# if requested_toppings:
#     for requested_topping in requested_toppings:
#         print("adding " + requested_topping + ".")
#     print("\nFinished making your pizzs!")
# else:
#     print("are you sure you want a plain pizza?")


# checking for special items

# requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

# for requested_topping in requested_toppings:
#     if requested_topping == 'green peppers':
#         print("Sorry, we are out of green peppers right now.")
#     print("Adding " + requested_topping + ".")


# 5-7.FavoriteFruit - try it yourself

# favorite_fruits = ['avocados', 'mangos', 'blueberries']
#
# fruit = 'mangos'

# if fruit in favorite_fruits:
#     fruit == 'avocado'
#     print("you really like " + fruit)
# elif fruit == 'mangos':
#     print("you really like " + fruit)
# elif fruit == 'blueberries':
#     print("you really like " + fruit)

# if fruit in favorite_fruits:
#     print("you really like " + str(fruit).title())




# 5-6.Stages of life - try it yourself

# age = "34"
# if int(age) < 2:
#     print("you are a baby")
# elif int(age) < 4:
#     print("you are a toddler")
# elif int(age) < 13:
#     print("you are a kid")
# elif int(age) < 20:
#     print("teenager")
# elif int(age) < 65:
#     print("adult")
# elif int(age) > 65:
#     print("elder")

# 5-7 Alien Colors - try it yourself

# 5-5. Alien Colors #3

# color = "red"
#
# if color == "green":
#     points = 5
# elif color == "yellow":
#     points = 10
# elif color == "red":
#     points = 15
# else:
#     points = 0
# print("You earned " + str(points) + " points.")

# alien_color = ['green', 'yellow', 'red']
#
# color = 'brown'
#
# if color in alien_color:
#     print("you get 5 points")
# else:
#     print('you get 10 points')

# 5-4.5-3 alien_colors #2:


# The if-elif-else Chain only one shall pass

#toppings.py - this example checks for one block of code due to elif
# note: using regular if statement will run all blocks of code

# requested_toppings = ['mushrooms', 'extra cheese']
# if 'mushrooms' in requested_toppings:
#     print("Adding mushrooms.")
# elif 'pepperoni' in requested_toppings:
#     print("adding pepperonis.")
# elif 'extra cheese' in requested_toppings:
#     print("adding extra cheese.")
# print("\nFinished making your pizza")
# Testing multiple conditions

# this ifelif statement is more concise than the previous example

# age = 11
# #
# if age < 4:
#     price = 0
#
# elif age < 18:
#     price = 5
#
# else:
#     price = 10
# print("your ticket admission cost $" + str(price) + ".")

# age = 22
#
# if age < 4:
#     print("your admission cost is $0, ")
# elif age < 18:
#     print("your admission cost is $5, ")
# else:
#     print("your admission cost is $10, ")


# try it yourself

# 5-1.Conditional Tests:“

# Test whether an item is in a list”

# guests = ['justin', 'rachel', 'dylan']
#
# user = "justin"
#
# if user in guests:
#     print(user.title() + " is  on list")
# else:
#     print(user.title() + " is not on list")

# car = "Tesla"
# print("is car == 'tesla'? I predict true ")
# print(car.lower()=='tesla')
# print(car.lower()=='honda')


# checking whether a value is on a list

# banned_users = ['andrew', 'carolina', 'david']
# user = 'david '
#
# if user not in banned_users:
#     print(user.title() + ", you can post a response if you wish.")
# else:
#     print(user.title() + ", not today you bitch")

# checking whether a value is in a list #run in console]

# requested_toppings = ['mushrooms', 'onions', 'pineapple']
# mushrooms in requested_toppings

# checking for inequality

# requested_topping = 'mushrooms'
# if requested_topping != 'anchovies':
#     print("hold the anchovies")

# Using and to Check Multiple Conditions

# age_0 = 22
# age_1 = 18
# age_0 >= 21 and age_1 >= 21 #false


# cars = ['audi', 'bmw', 'subaru', 'toyota']
# for car in cars:
#     if car == "bmw":
#         print(car.upper())
#     else:
#         print(car.title())


# Ignoring Case When Checking for Equality
# in the console terminal run this to test for true/false condition


