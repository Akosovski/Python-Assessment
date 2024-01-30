def luckyDraw(nameList):
    # Split the input string into a list of participant names
    participants = nameList.split()

    # Create a dictionary to keep track of winners based on surname
    winners_dict = {}

    # Iterate through the participants
    for participant in participants:
        # Split each participant's name into surname and name
        surname, name = participant.split(',')

        # Check if the surname is already a winner
        if surname not in winners_dict:
            # If not, add the participant to the winners and mark the surname as a winner
            winners_dict[surname] = f"{surname},{name}"

            # If we have found 5 winners, break out of the loop
            if len(winners_dict) == 5:
                break

    # Convert the values of the dictionary to a list of winners
    winners_list = list(winners_dict.values())

    # Join the list of winners into a string with space-separated names
    winners_string = '.'.join(winners_list) +  "."

    return winners_string