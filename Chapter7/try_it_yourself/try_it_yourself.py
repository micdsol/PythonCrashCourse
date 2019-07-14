# 7-1.Rental Car

# prompt = input("What type of rental car would you like?")
#
# print("Let me see if i can find you a" + prompt.title())


#7-2.Restaurant Seating:

# people = input("How many people in your dinner group?")
# people = int(people)
#
# if people < 8:
#     print("\nYour table is ready")
# else:
#     print("\nYou'll have to wait for another table")


# 7-3. Multiple of Ten: Ask the user for a number, and then report whether the number is a multiple of 10 or not


number = input("Check to see if your number is a multiple of 10")
number = int(number)

if number % 10 == 0:
    print("The number  " + str(number) + " is a multiple of 10")
else:
    print(str(number) +" is not a multiple of 10")