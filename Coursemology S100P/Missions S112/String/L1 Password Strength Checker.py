def passwordIsStrong(pw):
    return not pw.isdigit() and not pw.isalpha()

print(passwordIsStrong("asdf"))