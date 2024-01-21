def proper(numerator, denominator):
    whole_part = numerator // denominator
    new_numerator = numerator % denominator

    return f"{whole_part} {new_numerator} {denominator}"
    
print(proper(27,12))
print(proper(9, 5))