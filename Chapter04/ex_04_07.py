score = input("Enter score: ")
errorMessage = "Bad Score"

def computegrade(score):
    try:
        score = float(score)
        if(score > 1):
            grade = errorMessage
        elif(score >= .9):
            grade = "A"
        elif(score >= .8):
            grade = "B"
        elif(score >= .7):
            grade = "C"
        elif(score >= .6):
            grade = "D"
        elif(score < .6 and score >= 0):
            grade = "F"
        else:
            grade = errorMessage
        print(grade)
    except:
        print(errorMessage)

computegrade(score)