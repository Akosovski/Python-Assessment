def byeVowels(toReverse):
    original_sentence = ""
    vowels = "aeiouAEIOU"

    prev_char = None
    for char in toReverse:
        if char.lower() in vowels:
            if char != prev_char:
                original_sentence += char
        else:
            original_sentence += char
        prev_char = char

    return original_sentence

print(byeVowels('heeellooo wooorld'))
print(byeVowels('goood daay'))