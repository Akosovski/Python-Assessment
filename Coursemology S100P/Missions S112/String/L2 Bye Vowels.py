def byeVowels(toReverse):
    answer = ""
    i = 0
    vowels = ['a', 'i', 'u', 'e', 'o']

    while i < len(toReverse):
        answer += toReverse[i]
        if toReverse[i] in vowels:
            i += 3
        else:
            i += 1
    return answer

print(byeVowels('heeellooo wooorld'))
print(byeVowels('goood daay'))