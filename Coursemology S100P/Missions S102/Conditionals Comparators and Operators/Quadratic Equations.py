def solveQuadraticEqn(a, b, c):
    # Calculate the discriminant
    delta = b**2 - 4*a*c
    
    # Check the nature of the roots
    if delta > 0:
        # Two real and distinct roots
        root1 = (-b + (delta ** 0.5)) / (2 * a)
        root2 = (-b - (delta ** 0.5)) / (2 * a)
        return f"{round(root2, 2)}, {round(root1, 2)}"
    elif delta == 0:
        # Two real and identical roots
        root = -b / (2 * a)
        return str(round(root, 2)) + "0"
    elif delta < 0:
        return 'No real roots'
    
print(solveQuadraticEqn(1, 2, 1))
print(solveQuadraticEqn(1, 2, 5))
print(solveQuadraticEqn(1, 2, -5))