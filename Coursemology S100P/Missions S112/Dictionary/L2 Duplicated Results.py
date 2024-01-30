def calculateAverage(scores):
    # Write your code here
    score_dict = {}
    for item in scores:
        name, score = item.split(":")
        score = int(score)
        if name not in score_dict:
            score_dict[name] = [score]
        
    total_sum = sum(sum(scores) for scores in score_dict.values())
    total_count = sum(len(scores) for scores in score_dict.values())
    average = total_sum / total_count

    return average

print(calculateAverage(["Anthony:61","Brad:77","Angela:90","Angela:90"]))