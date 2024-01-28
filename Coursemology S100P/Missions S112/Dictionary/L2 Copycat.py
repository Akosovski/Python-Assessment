def copyCat(toCheck):
    words = toCheck.lower().split()  # Convert to lowercase and split into words
    unique_words = set(words)

    if len(words) != len(unique_words):
        return "Duplicates"
    else:
        return "No Duplicates"

copyCat("IT WAS A BRIGHT MORNING")