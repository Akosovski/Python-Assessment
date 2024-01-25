def maxBooks(money):
    ebookPrice = 10
    cbookPrice = 12
    total_ebook = 0
    total_cbook = 0
    budget = 0

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
        
    return f"{total_cbook} {total_ebook}"

print(maxBooks(994))
print(maxBooks(1052))
print(maxBooks(2048))