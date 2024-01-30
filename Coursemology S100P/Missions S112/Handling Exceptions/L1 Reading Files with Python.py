# Question 1: Read an entire text file
def readFile(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        return f"File '{file_name}' not found."
    
# Question 2: Read First n Lines of A File
def readFileLines(file_name, lines):
    try:
        with open(file_name, 'r') as file:
            content = ''.join(file.readline() for _ in range(lines))
            return content
    except FileNotFoundError:
        return f"File '{file_name}' not found."
    
# Question 3: Read Last n Lines of A File
def readFileLinesFromBottom(file_name, n):
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            content = ''.join(lines[-n:])
            return content
    except FileNotFoundError:
        return f"File '{file_name}' not found."