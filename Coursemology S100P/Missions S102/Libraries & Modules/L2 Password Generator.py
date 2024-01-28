import random

def generate_password():

    length = int(input("Password Length: "))
    lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
    uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    digits = '0123456789'
    symbols = '!@#$%^&*()-_=+[]{}|;:,.<>?/'

    password = ""
    all_characters = lowercase_letters + uppercase_letters + digits + symbols

    if length == 4:
        password = ''.join(random.choice(all_characters) for x in range(4))
    elif length == 3:
        password = ''.join(random.choice(all_characters) for x in range(3))
    elif length == 2:
        password = ''.join(random.choice(all_characters) for x in range(2))
    elif length == 1:
        password = random.choice(all_characters)
    else:
        password = ''.join(random.choice(all_characters) for x in range(length))

    password_list = list(password)
    random.shuffle(password_list)
    password = ''.join(password_list)

    return password

print(generate_password())