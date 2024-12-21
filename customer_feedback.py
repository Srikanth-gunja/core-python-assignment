ratings = [5, 4, 3, 5, 2, 4, 1, 5]

def percentage(ratings):
    if not ratings:
        return "No ratings Available"

    total_positive=len([i for i in ratings if i in [4,5]])
    return f"Positive Feedback: {round((total_positive/len(ratings)*100),2)}%"

print(percentage(ratings))