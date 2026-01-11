def calculate_percentage(total, obtained):
    if total == 0:
        return 0  # Avoid division by zero
    percentage = (obtained / total) * 100
    return percentage


subjects = {
    "Math": 80,
    "Science": 70,
    "English": 75
}

total_marks = 0
max_marks = 100 * len(subjects)  # Assuming each subject is out of 100

for mark in subjects.values():
    total_marks += mark

print("Percentage:", calculate_percentage(max_marks, total_marks))  # Fixed the arguments here

# CodeSentinal: created for you by RuchirAdnaik.