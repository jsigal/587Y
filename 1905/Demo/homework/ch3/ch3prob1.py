#1. Grade Calculator
# Problem: Write a program that calculates the average of a list of exam scores and prints the corresponding letter grade (A, B, C, D, or F). 

scores = [85, 92, 78, 95, 88]
total_score = 0
num_scores = 0

# Calculate the total score and count the number of scores
for score in scores:
    total_score = total_score + score
    num_scores = num_scores + 1

# Calculate the average
average = total_score / num_scores

# Determine the letter grade
if average >= 90:
    grade = 'A'
elif average >= 80:
    grade = 'B'
elif average >= 70:
    grade = 'C'
elif average >= 60:
    grade = 'D'
else:
    grade = 'F'

print("Average Score:", average)
print("Letter Grade:", grade)
