import random
import string
import time

def generate_username(length, include_numbers=False):
    letters = string.ascii_uppercase
    if include_numbers:
        letters += string.digits
    username = ''.join(random.choices(letters, k=length))
    return username

def generate_usernames(length_choice, num_usernames, include_numbers=False):
    usernames = []
    for _ in range(num_usernames):
        username = generate_username(length_choice, include_numbers)
        usernames.append(username)
    return usernames

# Animation d'affichage caractère par caractère
def animate_text(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.1)

# Exemple d'utilisation
length_choice = int(input("Choose the length of pseudonyms (2, 3 or 4): "))
num_usernames = int(input("How many pseudonyms do you want to generate? "))
include_numbers = input("Do you want to include numbers (yes/no) : ").lower() == "yes"

usernames = generate_usernames(length_choice, num_usernames, include_numbers)
print("Pseudonyms generated:")
for username in usernames:
    animate_text(username)
    print()