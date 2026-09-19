def age_evaluation(age):
    if age < 0:
        raise ValueError("Error, Enter a valid age")
    elif age < 18:
        return "You are young"
    elif age < 120:
        return "take care of yourself"
    else:
        return "Are you dead?"

print(age_evaluation(130))