
def copycat(name):
    duplicates = []
    name = name.split()
    duplicate = False

    for i in name:
        if i.lower() in duplicates:
            duplicate = True
            break
        else:
            duplicates.append(i.lower())

    if duplicate:
        return "Duplicates"
    else:
        return "No Duplicates"

name = "HI HI"
name2 = "Liao Alex Alex"

print(copycat(name))