class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def average(self):
        total = 0
        for m in self.marks:
            total += m
        return total / len(self.marks)


students = [
    Student("Alice", [80, 90, 85]),
    Student("Bob", [70, 75, 72]),
    Student("Charlie", [88, 92, 91])
]

highest_avg = 0
top_student = None

for s in students:
    avg = s.average()
    print(s.name, "average:", avg)

    if avg > highest_avg:
        highest_avg = avg
        top_student = s.name

print("Top student:", top_student)
