def main():
    n = int(input("Number of students: "))
    results = []
    counts = {"High": 0, "Moderate": 0, "Low": 0}

    for i in range(n):
        name = input(f"Student {i + 1} name: ")
        marks = float(input("Academic marks percentage: "))
        attendance = float(input("Attendance percentage: "))
        lab = float(input("Laboratory score percentage: "))
        if not all(0 <= value <= 100 for value in (marks, attendance, lab)):
            print("All values must be between 0 and 100.")
            return

        factors = []
        if marks < 50:
            factors.append("marks below 50")
        if attendance < 75:
            factors.append("attendance below 75")
        if lab < 50:
            factors.append("lab score below 50")
        category = "High" if len(factors) >= 2 else "Moderate" if len(factors) == 1 else "Low"
        counts[category] += 1
        results.append((name, category, factors))

    print("\nACADEMIC RISK REPORT")
    for name, category, factors in results:
        print(f"{name}: {category} risk")
        print("  Risk factors:", ", ".join(factors) if factors else "None")
    print("\nSummary:", counts)

if __name__ == "__main__":
    main()
