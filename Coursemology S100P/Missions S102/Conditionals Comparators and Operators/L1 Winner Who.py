def winnerWho(x,y):
    name = ""
    if x > y:
        name = "Braddy"
        power = x ** y
        return f"{name} {power}"
    if x < y:
        name = "Besse"
        power = y ** x
        return f"{name} {power}"
    
winnerWho(3,4)