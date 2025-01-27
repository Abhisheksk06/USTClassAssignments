import random

def lucky_number_game():

    random_number = random.randint(1,10)

    while True:
        lucky_number = int(input("Enter your lucky number: (between 1 and 10) "))

        if lucky_number < 1 or lucky_number > 10:
            print("Please enter a valid number between 1 and 10")
            return

        if lucky_number == random_number:
            print("Congratulations!..You are correct")
            print(f"The number was {random_number}")
            break
        else:
            print("Try again! Incorrect match")



lucky_number_game()