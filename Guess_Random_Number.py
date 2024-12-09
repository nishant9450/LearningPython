import random

number_to_guess = random.randint(0,100)

while True:
    try:
        number = int(input('Guess a number between 0 and 100 ? '))
        if number < number_to_guess:
            print("Guess a higher Number")
        elif number > number_to_guess:
            print("Guess a smaller number")
        else:
            print("Congratulations you have guess a right number")
            break
    except:
        print("Please enter a valid number")


