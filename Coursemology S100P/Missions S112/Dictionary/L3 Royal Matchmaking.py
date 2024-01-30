def matchMaking(inviteList):
    guests_count = {}
    
    # Count the occurrences of each invite number
    for invite in inviteList:
        guests_count[invite] = guests_count.get(invite, 0) + 1

    # Find guests who are alone
    alone_guests = [guest for guest, count in guests_count.items() if count == 1]

    # Sort the list in ascending order
    alone_guests.sort()

    return alone_guests

print(matchMaking([1,45667,45667,67,89]))
print(matchMaking([45667,45667]))