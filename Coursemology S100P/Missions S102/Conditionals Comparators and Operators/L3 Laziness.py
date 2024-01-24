# Question 1: Laziness

def alarm(hour, minutes):
    # write your codes here
    if hour < 1 and minutes < 45:
        minutes = (minutes - 45) + 60
        hour = 23
        return f"{hour} {minutes}"
    elif hour < 1 and minutes >= 45:
        minutes = minutes - 45
        if minutes == 0:
            return "0 0"
        else:
            return f"{hour} {minutes}"
    elif hour >= 1 and minutes >= 45:
        minutes = minutes - 45
        return f"{hour} {minutes}"
    elif hour >= 1 and minutes < 45:
        minutes = (minutes - 45) + 60
        hour -= 1
        return f"{hour} {minutes}"
    
# print(alarm(1,30))
# print(alarm(17,59))
# print(alarm(0,45))

# Question 2: Laziness (Hard)
    
def alarm_improved(hour, minutes, backward):
    total_minutes = (hour * 60) + minutes
    new_total_minutes = total_minutes - backward

    new_total_minutes = (new_total_minutes + 24 * 60) % (24 * 60)
    
    new_hour = new_total_minutes // 60
    new_minutes = new_total_minutes % 60
    
    return f"{new_hour} {new_minutes}"
    
print(alarm_improved(0, 30, 45))
print(alarm_improved(0, 30, 180))
print(alarm_improved(0, 30, 175))