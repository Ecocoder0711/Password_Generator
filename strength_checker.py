import re

def strength_checker(password):
    length = len(password)
    score = 0
    if re.search(r'[a-z]',password):
        score += 1
    if re.search(r'[A-Z]',password):
        score +=1
    if re.search(r'\d',password):
        score +=1
    if re.search(r'[!@#$%^&*(),.?":{}|<>]',password):
        score +=1
    
    if length < 8 :
        return "Weak"
    elif score == 3 and length >= 12:
        return "Strong"
    elif score == 2:
        return "Moderate"
    else:
        return "Weak"
    

