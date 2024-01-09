import random
import string

# Password generator created by Niraj Gurav

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

print("Password Generator 🔑")

try:
    length = int(input("Enter the desired length of the password: "))
    if length <= 0:
        print("Please enter a positive length for the password.")
    else:
        password = generate_password(length)
        print("Generated Password:", password)
except ValueError:
    print("Invalid input 😓 Please enter a valid number for the length.")