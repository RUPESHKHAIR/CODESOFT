# Task 3- password generator

import random
import string


def generate_password(length):
    if length < 1:
        return "Password length must be at least 1 character."

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ""
    for i in range(length):
        password += random.choice(characters)
    return password


def main():
    print("Welcome to the Password Generator!")
    try:
        length = int(input("Enter the password length: "))
        if length < 1:
            print("Please enter a valid positive number.")
        else:
            password = generate_password(length)
            print(f"Your generated password is: {password}")
    except ValueError:
        print("Invalid input.")


main()
