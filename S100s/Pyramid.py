def pyramid(rows):
    pyramid = ""

    i = 0
    while i < rows:
        rowString = ""

        j = 0
        while j < rows - i - 1:
            rowString += " "
            j += 1

        k = 0
        while k < 2 * i + 1:
            rowString += "*"
            k += 1

        pyramid += rowString + "\n"

        i += 1

    return pyramid

print(pyramid(5))