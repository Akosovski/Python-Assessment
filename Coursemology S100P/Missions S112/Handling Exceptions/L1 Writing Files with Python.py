# Question 1: Write Text to A File
def writeToFile(fname, textToWrite):
    try:
        with open(fname, 'w') as file:
            file.write(textToWrite)
    except Exception as e:
        print(f"Error writing to file '{fname}': {e}")

# Question 2: Write Numbers to File
def writeNumberToFile(fname, number):
    try:
        with open(fname, 'w') as file:
            file.write(str(number))
    except Exception as e:
        print(f"Error writing to file '{fname}': {e}")

# Question 3: Write A List of Items To File
def writeListToFile(fname, items):
    try:
        with open(fname, 'w') as file:
            for item in items:
                file.write(str(item) + '\n')
    except Exception as e:
        print(f"Error writing to file '{fname}': {e}")