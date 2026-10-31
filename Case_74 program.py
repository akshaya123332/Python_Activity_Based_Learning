def main():
    fee = float(input("Registration fee per participant: "))
    n = int(input("Number of registration records: "))
    if fee < 0 or n < 0:
        print("Fee and record count cannot be negative.")
        return

    seen = []
    duplicates = []
    for i in range(n):
        registration_id = input(f"Registration ID {i + 1}: ").strip().upper()
        if not registration_id:
            print("Blank ID ignored.")
        elif registration_id in seen:
            if registration_id not in duplicates:
                duplicates.append(registration_id)
        else:
            seen.append(registration_id)

    sponsorship_count = int(input("Number of sponsorship contributions: "))
    sponsorships = []
    for i in range(sponsorship_count):
        amount = float(input(f"Sponsorship {i + 1} amount: "))
        if amount < 0:
            print("Negative sponsorship is invalid.")
            return
        sponsorships.append(amount)

    expense_count = int(input("Number of expense entries: "))
    expenses = []
    for i in range(expense_count):
        amount = float(input(f"Expense {i + 1} amount: "))
        if amount < 0:
            print("Negative expense is invalid.")
            return
        expenses.append(amount)

    registration_income = len(seen) * fee
    total_sponsorship = sum(sponsorships)
    total_expenses = sum(expenses)
    total_income = registration_income + total_sponsorship
    balance = total_income - total_expenses

    print("\nFESTIVAL FINANCIAL AUDIT")
    print("Unique registrations:", len(seen))
    print("Duplicate IDs:", ", ".join(duplicates) if duplicates else "None")
    print(f"Registration income: Rs. {registration_income:.2f}")
    print(f"Sponsorships: Rs. {total_sponsorship:.2f}")
    print(f"Total income: Rs. {total_income:.2f}")
    print(f"Total expenses: Rs. {total_expenses:.2f}")
    print(f"Final balance: Rs. {balance:.2f}")
    print("Status:", "Surplus" if balance >= 0 else "Deficit")

if __name__ == "__main__":
    main()
