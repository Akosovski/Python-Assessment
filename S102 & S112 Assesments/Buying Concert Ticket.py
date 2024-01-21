def tickets(a, b, c, d):
    total_a = 2 * a
    total_b = 5 * b
    total_c = 10 * c
    total_d = 50 * d

    savings = total_a + total_b + total_c + total_d

    cat1 = 328
    cat2 = 288
    cat3 = 228
    cat4 = 148

    merch = 0

    if savings < 148:
        poor = 148 - savings
        return f"Too poor, need to save ${poor} more"

    elif savings - cat1 >= 0:
        merch = savings - cat1
        return f"Category 1 tickets and ${merch} for merchandise"

    elif savings - cat2 >= 0:
        merch = savings - cat2
        return f"Category 2 tickets and ${merch} for merchandise"

    elif savings - cat3 >= 0:
        merch = savings - cat3
        return f"Category 3 tickets and ${merch} for merchandise"

    elif savings - cat4 >= 0:
        merch = savings - cat4
        return f"Category 4 tickets and ${merch} for merchandise"

# a, b, c, d = input("").split()
# a = int(a)
# b = int(b)
# c = int(c)
# d = int(d)
        
print(tickets(1, 4, 6, 1))
print(tickets(5, 2, 18, 3))