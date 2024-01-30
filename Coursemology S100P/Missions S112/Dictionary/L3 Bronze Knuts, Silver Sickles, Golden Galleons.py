def weasleySalary():
    weasleyFamily = [
        {'Name': 'Arthur Weasley', 'Job': 'Head of the Office for the Detection and Confiscation of Counterfeit Defensive Spells and Protective Objects', 'Salary': 1089},
        {'Name': 'Molly Weasley', 'Job': 'Housewife', 'Salary': 0},
        {'Name': 'Bill Weasley', 'Job': 'Curse Breaker for Gringotts Bank', 'Salary': 3009},
        {'Name': 'Charlie Weasley', 'Job': 'Dragonologist', 'Salary': 2050},
        {'Name': 'Percy Weasley', 'Job': 'Head of the Department of Magical Transportation', 'Salary': 5000},
        {'Name': 'Fred Weasley', 'Job': 'Deceased', 'Salary': 0},
        {'Name': 'George Weasley', 'Job': 'Self-employed', 'Salary': 5600},
        {'Name': 'Ron Weasley', 'Job': 'Auror', 'Salary': 4090},
        {'Name': 'Ginny Weasley', 'Job': 'Sports editor for the Daily Prophet', 'Salary': 4000}
    ]

    total_salary = sum(person['Salary'] for person in weasleyFamily)
    return total_salary

print(weasleySalary())