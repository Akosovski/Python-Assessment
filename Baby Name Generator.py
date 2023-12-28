import string
import random

def generate_name(length):
  name = "".join(random.choices(string.ascii_uppercase, k=1))
  name = name + "".join(random.choices(string.ascii_lowercase, k=length-1))
  return name

length = int(input("How many letters should the name have? "))
print(generate_name(length))

