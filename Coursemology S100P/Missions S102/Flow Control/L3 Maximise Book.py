def maxBooks(money):
    max_chinese_book = 0
    max_english_book = 0
    max_total_book = 0
    for chinese_books in range(money // 12 + 1): # chinese book price is 12
        for english_books in range(money // 10 + 1): # english book price is 10
            if chinese_books > english_books / 2 and chinese_books * 12 + english_books * 10 <= money:
                total_books = chinese_books + english_books
                if total_books > max_total_book:
                    max_chinese_book = chinese_books
                    max_english_book = english_books
                    max_total_book = total_books
    return f"{max_chinese_book} {max_english_book}"

print(maxBooks(994))
print(maxBooks(1052))
print(maxBooks(2048))