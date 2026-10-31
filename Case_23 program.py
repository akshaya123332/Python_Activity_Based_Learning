def to_minutes(time_text):
    hour, minute = map(int, time_text.split(":"))
    if not (0 <= hour < 24 and 0 <= minute < 60):
        raise ValueError("Time must be valid 24-hour HH:MM.")
    return hour * 60 + minute

def main():
    n = int(input("Number of classes: "))
    classes = []
    try:
        for i in range(n):
            subject = input(f"Class {i + 1} subject: ")
            day = input("Day: ").strip().lower()
            start_text = input("Start time (HH:MM): ")
            end_text = input("End time (HH:MM): ")
            start, end = to_minutes(start_text), to_minutes(end_text)
            if start >= end:
                print("End time must be later than start time.")
                return
            classes.append((subject, day, start, end, start_text, end_text))
    except ValueError as error:
        print("Invalid input:", error)
        return

    found = False
    for i in range(len(classes)):
        for j in range(i + 1, len(classes)):
            a, b = classes[i], classes[j]
            if a[1] == b[1] and a[2] < b[3] and b[2] < a[3]:
                print(f"CLASH: {a[0]} ({a[4]}-{a[5]}) and {b[0]} ({b[4]}-{b[5]}) on {a[1].title()}")
                found = True
    if not found:
        print("No timetable clashes detected.")

if __name__ == "__main__":
    main()
