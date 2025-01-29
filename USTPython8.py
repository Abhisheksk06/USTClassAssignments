# Exercise 1: Generate 3 random integers between 100 and 999 which is divisible by 5

import random

random_numbers = [random.choice(range(100, 1000, 5)) for _ in range(3)]

print("Random numbers divisible by 5:", random_numbers)

# Exercise 2: Random Lottery Pick. Generate 100 random lottery tickets and pick two lucky tickets from it as a winner.

import random

lottery_tickets = random.sample(range(100000, 999999), 100)

winners = random.sample(lottery_tickets, 2)

print("Lottery Tickets:", lottery_tickets)
print("Winning Tickets:", winners)

# Exercise 3: Generate 6 digit random secure OTP

import random

# Generate a 6-digit OTP
otp = random.randint(100000, 999999)

print("Your OTP is:", otp)

# Exercise 4: Pick a random character from a given String

import random

text = "Hello, Abhishek!"

random_char = random.choice(text)

print("Random Character:", random_char)

# Exercise 5: Generate random String of length 5

import random
import string

random_string = ''.join(random.choices(string.ascii_letters, k=5))

print("Random String:", random_string)

# Exercise 6: Generate a random Password which meets the following conditions Password length must be 10 characters
#  long. It must contain at least 2 upper case letters, 1 digit, and 1 special symbol.

import random
import string

uppercase = string.ascii_uppercase
digits = string.digits
special_chars = string.punctuation

password = [
    random.choice(uppercase),
    random.choice(digits),   
    random.choice(special_chars), 
]

remaining_length = 10 - len(password)
password += random.choices(uppercase + digits + special_chars, k=remaining_length)

random.shuffle(password)

password = ''.join(password)

print("Random Password:", password)

# Exercise 7: Calculate multiplication of two random float numbers

import random

num1 = random.uniform(1.0, 100.0)
num2 = random.uniform(1.0, 100.0)

result = num1 * num2

print(f"Random Numbers: {num1}, {num2}")
print(f"Multiplication Result: {result}")

# Exercise 8: Generate random secure token of 64 bytes and random URL

# random secure token of 64 bytes
import secrets

secure_token = secrets.token_hex(64) 

print("Random Secure Token:", secure_token)

# random URL

import random
import string

base_url = "https://www.example.com/"

random_path = ''.join(random.choices(string.ascii_letters + string.digits, k=8))

random_url = base_url + random_path

print("Random URL:", random_url)

# Exercise 9: Roll dice in such a way that every time you get the same number

import random

random.seed(42)

dice_roll = random.randint(1, 6)

print("Dice Roll (same every time):", dice_roll)

# Exercise 10: Generate a random date between given start and end dates

import random
from datetime import datetime, timedelta

start_date = datetime(2023, 1, 1)
end_date = datetime(2025, 1, 1)

delta = end_date - start_date

random_days = random.randint(0, delta.days)

random_date = start_date + timedelta(days=random_days)

print("Random Date:", random_date.strftime("%Y-%m-%d"))

















