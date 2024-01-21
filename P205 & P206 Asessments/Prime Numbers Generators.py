for i in range(2, 100):
  for j in range(2, 100):
    if i % j == 0:
      break
  if i == j:
    print(i)