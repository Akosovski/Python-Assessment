numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
oddcubes = [x**3 for x in numbers if x**3 % 2 != 0]

print(oddcubes)