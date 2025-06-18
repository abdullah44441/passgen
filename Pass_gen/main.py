import random

# Password Generator

print("Welcome to the Password Generator! Enter the length of the password you want to generate: ")
length = int(input())

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+"
if length < 8:
    print("Password length must be at least 8 characters. Please try again.")
    exit()

password = ""
for i in range(length):
    password += random.choice(chars)

print("Your generated password is: " + password)