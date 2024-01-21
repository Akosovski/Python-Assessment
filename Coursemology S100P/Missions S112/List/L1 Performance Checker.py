def B_performers(scores):
    count = 0
    # write your codes here
    for i in range(len(scores)):
        if scores[i] >= 60 and scores[i] < 75:
            count += 1
    return count

print(B_performers([ 90,90,85,75, 80,70,60,50, 40,45,47,48, 80,85,83,81, 100,100,100,74, 0,0,0,0 ]))