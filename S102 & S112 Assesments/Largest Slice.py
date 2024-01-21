import math

def largestSlice(x, r):
    
    x_large_slice = 180 // x
    x_large_slice = (x_large_slice * x) - x

    area = (x_large_slice / 360) * math.pi * r**2
    area = round(area, 1)
    return area

result1 = largestSlice(20, 8)
print(result1)  # Expected Output: 80.0

result1 = largestSlice(15, 7)
print(result1) # Expected Output: 52.5