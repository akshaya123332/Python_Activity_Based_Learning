def main():
    password = input("Enter a SAMPLE password to validate: ")
    errors = []

    if len(password) < 8:
        errors.append("Use at least 8 characters.")
    if not any(ch.isupper() for ch in password):
        errors.append("Include at least one uppercase letter.")
    if not any(ch.islower() for ch in password):
        errors.append("Include at least one lowercase letter.")
    if not any(ch.isdigit() for ch in password):
        errors.append("Include at least one digit.")
    if not any(not ch.isalnum() for ch in password):
        errors.append("Include at least one special character.")
    if "password" in password.lower():
        errors.append("Do not include the prohibited substring 'password'.")
    if any(password[i] == password[i + 1] == password[i + 2]
           for i in range(len(password) - 2)):
        errors.append("Do not use three identical consecutive characters.")

    if errors:
        print("INVALID under the sample policy:")
        for error in errors:
            print("-", error)
    else:
        print("VALID under the sample policy.")

if __name__ == "__main__":
    main()
