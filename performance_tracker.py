students = {"John": [85, 78, 92], "Alice": [88, 79, 95], "Bob": [88, 79, 95]}


def average_marks(students):
    students_avg_marks = {}
    if len(students) == 0:
        return 0

    students_list = students.keys()
    for student in students_list:
        marks = students.get(student)
        avg_marks = sum(marks) / len(marks)
        students_avg_marks[student] = round(avg_marks, 2)
    print(f"Average Marks: {students_avg_marks}")

    max_avg = max(students_avg_marks.values())

    ## if one or more students got max avg marks
    toppers_list = [student for student, avg in students_avg_marks.items() if avg == max_avg]
    print(f"Top Performer: {', '.join(toppers_list)}")


average_marks(students)