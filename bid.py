student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆
# TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

# TODO-2: Write your code below to add the grades to student_grades.👇
for students in student_scores:
    scores =  student_scores[students]
    if scores > 90:
        student_grades[students] = "outstanding"
    elif scores > 80:
        student_grades[students] = "welldone"
    elif scores > 70:
        student_grades[students] = "very good"
    elif scores > 60:
        student_grades[students]  = "good"  
        

# 🚨 Don't change the code below 👇
print(student_grades)