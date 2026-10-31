def main():
    student_count = int(input("Number of students: "))
    subject_count = int(input("Number of subjects: "))
    students = [input(f"Student {i + 1} name: ") for i in range(student_count)]
    subjects = [input(f"Subject {j + 1} name: ") for j in range(subject_count)]
    marks = []

    for student in students:
        row = []
        for subject in subjects:
            mark = float(input(f"{student} - {subject} mark (0-100): "))
            if not 0 <= mark <= 100:
                print("Marks must be between 0 and 100.")
                return
            row.append(mark)
        marks.append(row)

    print("\nSTUDENT AVERAGES")
    averages = []
    for i, row in enumerate(marks):
        average = sum(row) / subject_count if subject_count else 0
        averages.append(average)
        print(f"{students[i]}: {average:.2f}")

    print("\nSUBJECT AVERAGES")
    subject_averages = []
    for j, subject in enumerate(subjects):
        total = sum(marks[i][j] for i in range(student_count))
        average = total / student_count if student_count else 0
        subject_averages.append(average)
        print(f"{subject}: {average:.2f}")

    if averages:
        top = averages.index(max(averages))
        print(f"Top performer: {students[top]} ({averages[top]:.2f})")
    weak = [subjects[j] for j, avg in enumerate(subject_averages) if avg < 50]
    print("Subjects with average below 50:", ", ".join(weak) if weak else "None")

if __name__ == "__main__":
    main()
