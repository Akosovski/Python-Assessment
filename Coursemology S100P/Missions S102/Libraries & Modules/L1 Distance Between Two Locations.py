import math

def distance(a, b):
    distance_to_b = math.sqrt((b[0] - a[0])**2 + (b[1] - a[1])**2)
    distance_to_a = math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)
    result = distance_to_b + distance_to_a
    return result

print(distance((2,2), (2,0)))