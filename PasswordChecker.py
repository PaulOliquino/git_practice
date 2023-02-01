def check_password_strength(password):
    if len(password) >= 8:
        if any(char.isdigit() for char in password):
            if any(char in "!@#$%^&*()_+-=[]{}|,.<>?/\"\'" for char in password):
                return "password strength = strong"
    elif len(password) >= 6:
        if any(char.isdigit() for char in password):
            if any(char in "!@#$%^&*()_+-=[]{}|,.<>?/\"\'" for char in password):
                return "password strength = medium"
    return "password strength = weak"

password = input("Enter a password: ")
print(check_password_strength(password))