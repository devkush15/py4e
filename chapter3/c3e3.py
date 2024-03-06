try:
    grade = float(input("Enter score: "))
except:
    print("Bad score")
    quit()

def computegrade(grade):
    if grade < 0 or grade > 1:
        return "Score is out of range..."
    elif grade >= 0.9:
        return "A"
    elif grade >= 0.8:
        return "B"
    elif grade >= 0.7:
        return "C"
    elif grade >= 0.6:
        return "D"
    else:
        return "F"

print(compute grade(grade)) 
