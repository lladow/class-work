def computegrade (score):
    if score <= 0.6:
        return 'F'
    elif score >= 0.9:
        return 'A'
    elif score >= 0.8:
        return 'B'
    elif score >= 0.7:
        return 'C'
    elif score > 0.6:
        return 'D'

try:
    score = float(input('Enter score:'))
    if score >= 0.0 and score <= 1.0:
        print (computegrade(score))
    else:
        print("Bad score")
except:
    print("Bad score") 
    quit()

