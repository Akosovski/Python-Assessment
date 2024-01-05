def nap_time(time, weekend):
    if weekend == True:
        if time <= 120:
            return "Go ahead!"
        else:
            return "That's too long"
    elif weekend == False:
        if time <= 30:
            return "Go ahead!"
        else:
            return "That's too long"
        
nap_time(25, False)
nap_time(60, False)
