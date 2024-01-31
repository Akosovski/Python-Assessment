import random

def generate_password():
    
    length = int(input("Password Length: "))
    
    password = ""
    for y in range(length):
        password += chr(random.randint(33, 126))

    return password

print(generate_password())