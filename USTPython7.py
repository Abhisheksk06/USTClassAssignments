# 1. use the os and os.path modules to list the contents of your downloads folder
# and indicate for each item whether it's a file or a folder (hint : use os.path.join)

import os

downloads_path = os.path.expanduser("~/Downloads")

if os.path.exists(downloads_path):

    contents = os.listdir(downloads_path)
    

    for item in contents:
        item_path = os.path.join(downloads_path, item)
        if os.path.isfile(item_path):
            print(f"{item} - File")
        elif os.path.isdir(item_path):
            print(f"{item} - Folder")
else:
    print("The Downloads folder does not exist.")

# 2. import  string module and print out all  ASCII letters defined in this module

import string

print("ASCII Letters: ", string.ascii_letters)

# 3. Import the sample() function from the random module and the ascii_letters attribute
# of the string module. use these to randomly sample five letters and assign these
# to a variable called five_letters

from random import sample
import string

five_letters = sample(string.ascii_letters, 5)

print("Five Random Letters:", five_letters)

# 4. Take a input from the user a date for eg: 25/02/2020

#     a.print output Date in format  Tuesday 25 February 2020

#     b.print the day of the week of a given input  date

#     c. Add 15 days and 23 hours to a given input date

#     d. calculate the date 6 months from the current date

from datetime import datetime, timedelta
import calendar

# a. Take input date
input_date = input("Enter a date (DD/MM/YYYY): ")

# Convert the input string to a datetime object
date_obj = datetime.strptime(input_date, "%d/%m/%Y")

# a. Print date in format "Tuesday 25 February 2020"
formatted_date = date_obj.strftime("%A %d %B %Y")
print("Formatted Date:", formatted_date)

# b. Print the day of the week
day_of_week = date_obj.strftime("%A")
print("Day of the week:", day_of_week)

# c. Add 15 days and 23 hours to the given input date
new_date = date_obj + timedelta(days=15, hours=23)
print("New Date (15 days and 23 hours later):", new_date.strftime("%d/%m/%Y %H:%M"))

# d. Calculate the date 6 months from the current date
current_date = datetime.now()
six_months_later = current_date + timedelta(days=183)  # Approximation for 6 months (assuming 30.5 days/month)
print("Date 6 months from today:", six_months_later.strftime("%d/%m/%Y"))

# 5. Create a game of rock paper and scissors where user will input one option
# while second option is chosen by the computer(i.e your python program). Based
# on the options select declare the result
# 1. user wins
# 2. computer wins
# 3. draw
 
# if it is draw continue the game till one of them gets won
import random

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "draw"
    elif ((user_choice == "rock" and computer_choice == "scissors") or 
         (user_choice == "paper" and computer_choice == "rock") or
         (user_choice == "scissors" and computer_choice == "paper")):
         return "user"
    else:
        return "computer"

def play_game():
    choices = ["rock", "paper", "scissors"]

    while True:
        user_choice = input("Enter rock, paper, scissors: ").lower()

        if user_choice not in choices:
            print("Invalid choice! Please choose rock, paper or scissors")
            continue

        computer_choice = random.choice(choices)
        print(f"Computer choice: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)

        if result == "draw":
            print("It's a draw! Let's play again.")
        elif result == "user":
            print("You Win!")
            break
        else:
            print("Computer Wins.")
            break

play_game()



 

