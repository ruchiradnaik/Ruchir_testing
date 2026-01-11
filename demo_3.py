def calculate_percentage(total, obtained):
    percentage = (obtained / total) * 100
    return percentage


subjects = {
    "Math": 80,
    "Science": 70,
    "English": 75
}

total_marks = 0

for mark in subjects.values():
    total_marks += mark

print("Percentage:", calculate_percentage(0, total_marks))
