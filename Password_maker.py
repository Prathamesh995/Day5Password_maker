# Password generator

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to you very own password maker.")
num_letters = int(input("How many letters: "))
num_number = int(input("How many numbers: "))
num_symbol = int(input("How many symbols: "))

letter_list= []
number_list = []
symbol_list = []

for i in range(num_letters):
    letter_list.append(random.choice(letters))

for i in range(num_number):
    number_list.append(random.choice(numbers))

for i in range(num_symbol):
    symbol_list.append(random.choice(symbols))

password = letter_list + number_list + symbol_list
random.shuffle(password)

password_str = ""
for i in password:
    password_str += i

print(f"Your password is '{password_str}'")