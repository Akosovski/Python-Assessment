def alarm(hour, minutes):
    if hour == 0:
        minutes - 45
        return "0 "+ str(minutes)
    elif hour > 0:
        if minutes - 45 < 0:
            hour -= 1
            minus = minutes - 45
            minutes = 60
            minutes = minutes + minus
            return str(hour) + " " + str(minutes)
        elif minutes - 45 > 0:
            return str(hour) + " " + str(minutes)
        
print(alarm(1,30))
print(alarm(17, 28))