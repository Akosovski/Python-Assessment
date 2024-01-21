def sum (a, b, c):
  if a % 5 == 0:
    a = a * -1
  if b % 5 == 0:
    b = b * -1
  if c % 5 == 0:
    c = c * -1
  result = a + b + c
  return result

a = int(input("a? "))
b = int(input("b? "))
c = int(input("c? "))

print(sum(a, b, c))