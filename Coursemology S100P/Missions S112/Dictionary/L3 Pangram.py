def pangram(toCheck):
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    sentence_set = set(toCheck.lower())

    if alphabet.issubset(sentence_set) == True:
        return "pangram"
    else:
        return "not a pangram"

print(pangram("The quick brown fox jumps over the lazy dog"))
print(pangram("The quick brown fox jumps over the lazy do"))