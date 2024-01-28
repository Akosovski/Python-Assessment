import random

throwables = int(input("How many coins do you want to throw? "))

head = 0
tail = 0
for i in range(throwables):
    bet = random.randint(1, 2)
    if bet == 1:
        head += 1
    elif bet == 2:
        tail += 1
        
print("The number of times 'heads' appeared: " + str(head))
print("The number of times 'tails' appeared: " + str(tail))