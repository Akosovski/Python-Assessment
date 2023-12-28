def buystorybooks (money):
  ebookPrice = 10
  cbookPrice = 12
  total_ebook = 0
  total_cbook = 0
  budget = 0

  if money <= 0:
        return "Invalid input. Money must be a positive number."

  while money > budget:
    if total_cbook <= (total_ebook / 2):
      total_ebook = total_ebook + 1
      budget += ebookPrice
      total_cbook = total_cbook + 1
      budget += cbookPrice
    else:
      total_ebook = total_ebook + 1
      budget += ebookPrice

  while money < budget:
    total_ebook -= 1
    budget -= 10

  return total_ebook, total_cbook

result_eb, result_cb = buystorybooks(994)
print(f"The number of Chinese books are {result_cb} and the number of English books are {result_eb}.")