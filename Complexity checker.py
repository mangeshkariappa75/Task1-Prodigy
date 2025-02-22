import re

def check_password_strength(password):
    if len(password) < 8:
        return "Weak: Password is too short."

    if not re.search("[a-z]", password):
        return "Weak: Add lowercase letters."

    if not re.search("[A-Z]", password):
        return "Moderate: Add uppercase letters."

    if not re.search("[0-9]", password):
        return "Moderate: Add numbers."

    if not re.search("[!@#$%^&*(),.?\":{}|<>]", password):
        return "Strong: Consider adding special characters."

    return "Very Strong: Password meets all criteria!"

# Example usage
password = input("Enter your password: ")
print(check_password_strength(password))