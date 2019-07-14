prompt = "\nWhat topping would you like? "
prompt += "\n(Enter 'stop' when you are finished)"

while True:
    topping = input(prompt)

    if topping == 'stop':
        break
    else:
        print("adding: " + topping + " to your pizza")