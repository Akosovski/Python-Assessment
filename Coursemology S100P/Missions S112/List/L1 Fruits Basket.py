def want_apples(items):
    baskets = []
    # write your codes here
    for i in range(len(items)):
        if 'apple' in items[i]:
            baskets.append(items[i])
    return baskets

print(want_apples([ ['apple','orange'], ['mango','strawberry'], ['apple', 'grapes'] ]))