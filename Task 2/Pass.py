# Password Generator
# Aisha Nagah

import random
import string

def generate_password(length):
    
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

while True:
    try:
        length = int(input("Please specify the desired length of the password (at least 6): "))
        if length < 6:
            print("Password length should be at least 6.")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter a number.")

generated_password = generate_password(length)
print("Generated Password:", generated_password)