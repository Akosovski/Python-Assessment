def specialPythagorean():
    # Iterate through possible values of a
    for a in range(1, 1000):
        # Iterate through possible values of b
        for b in range(a, 1000 - a):
            c = 1000 - a - b
            # Check if it's a Pythagorean triplet
            if a**2 + b**2 == c**2:
                # Return the product of a, b, and c
                return a * b * c

result = specialPythagorean()
print("Product of a, b, c:", result)